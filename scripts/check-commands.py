#!/usr/bin/env python3
"""Fail when published command data drifts from the bot's public help/catalog."""
import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
bot=root.parent
help_text=(bot/'assets/help.txt').read_text()
expected={line[2:].split(';',1)[0].strip() for line in help_text.splitlines() if line.startswith('@ ')}-{'pingtrace'}
commands=json.loads((root/'src/data/commands.json').read_text())
assert len(commands)==len(expected)==len({c['name'] for c in commands})
assert {c['name'] for c in commands}==expected
assert 'pingtrace' not in expected
for command in commands:
    page=root/'src/content/docs/commands'/f"{command['slug']}.mdx"
    assert f"## {command['name']}\n" in page.read_text(),command['name']
    assert command['subs'],command['name']
actual=json.loads((root/'src/data/slash.json').read_text())
source=json.loads((bot/'assets/slash.json').read_text())['routes']
assert len(actual)==len(source)+1
for expected_route,route in zip(source,actual):
    for key in ('path','description','portable','options'):
        assert route[key]==expected_route[key],(key,route['path'])
assert actual[-1]['path']==['confess'] and not actual[-1]['portable']
assert 'confess schema' in (bot/'src/slash.rs').read_text()
print(f"PASS: {len(commands)} public command names, {sum(len(c['aliases']) for c in commands)} aliases, {sum(len(c['subs']) for c in commands)} prefix forms, {len(actual)} typed slash paths, {len({r['path'][0] for r in actual})} slash roots; exact catalog fields/contexts; internal pingtrace excluded")
