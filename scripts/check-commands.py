#!/usr/bin/env python3
"""Fail when published command data or equivalent links drift from public commands."""
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
bot = root.parent
help_text = (bot / 'assets/help.txt').read_text()
names = {line[2:].split(';', 1)[0].strip() for line in help_text.splitlines() if line.startswith('@ ')} - {'pingtrace'}
commands = json.loads((root / 'src/data/commands.json').read_text())
assert len(commands) == len(names) == len({c['name'] for c in commands})
assert {c['name'] for c in commands} == names
by_name = {c['name']: c for c in commands}
source = [r for r in json.loads((bot / 'assets/slash.json').read_text())['routes'] if r['command'] in names]
actual = json.loads((root / 'src/data/slash.json').read_text())
assert len(actual) == len(source) + 1
assert len({tuple(r['path']) for r in actual}) == len(actual)
for expected, route in zip(source, actual):
    for key in ('command', 'syntax', 'path', 'description', 'portable', 'options'):
        assert route[key] == expected[key], (key, route['path'])
    assert route['aliases'] == by_name[route['command']]['aliases']
    assert route['details'] == next(form['desc'] for form in by_name[route['command']]['subs'] if form['syntax'] == route['syntax'])
    groups = {}
    for binding in expected['bindings']:
        if binding.get('union') and binding.get('union_required'):
            group = groups.setdefault(binding['union'], {'fields': [], 'multiple': False})
            group['fields'].append(binding['name'])
            group['multiple'] |= binding.get('union_many', False)
    assert route['required_groups'] == list(groups.values()), route['path']
for command in commands:
    page = root / 'src/content/docs/commands' / f"{command['slug']}.mdx"
    assert f"## {command['name']}\n" in page.read_text(), command['name']
    assert command['subs'], command['name']
    for form in command['subs']:
        expected_paths = [r['path'] for r in source if r['command'] == command['name'] and r['syntax'] == form['syntax']]
        assert expected_paths and form['slash'] == expected_paths, (command['name'], form['syntax'])
assert not any(r['command'] == 'pingtrace' for r in actual)
assert actual[-1]['path'] == ['confess'] and not actual[-1]['portable']
assert 'confess schema' in (bot / 'src/slash.rs').read_text()
print(f"PASS: {len(commands)} public names, {sum(len(c['aliases']) for c in commands)} aliases, {sum(len(c['subs']) for c in commands)} prefix forms, {len(actual)} slash paths; exact types/contexts/constraints and every equivalent link; internal pingtrace excluded")
