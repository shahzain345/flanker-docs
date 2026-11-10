#!/usr/bin/env python3
"""Generate the flanker command reference from the bot's help.txt.

Parses assets/help.txt (the bot's own help source) and writes one Markdown
page per module category into src/content/docs/commands/. Re-run after the
bot's commands change:

    python3 scripts/gen-commands.py ../assets/help.txt

help.txt format (see its own header):
    # --- Category ------                 marks a category section
    @ command ; dashboard-path|- ; perm   a command, then description line(s)
    > syntax ; perm ; description ; ex?    a subcommand/usage row
"""
import os
import json
from pathlib import Path
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "src", "content", "docs", "commands")

CAT_RE = re.compile(r"^#\s*-{2,}\s*(.+?)\s*-{2,}\s*$")

DASH = "https://flanker.wtf/dashboard"

# Dashboard paths (from help.txt) -> the human section name shown to users.
DASH_SECTIONS = {
    "/": "Dashboard home",
    "/antinuke": "Antinuke",
    "/antiraid": "Antiraid",
    "/applications": "Applications",
    "/birthdays": "Birthdays",
    "/community": "Community",
    "/customcommands": "Custom commands",
    "/filter": "Filters",
    "/honeypot": "Honeypot",
    "/invites": "Invites",
    "/moderation": "Moderation",
    "/moderation/channels": "Moderation → Channels",
    "/moderation/jail": "Moderation → Jail",
    "/moderation/logs": "Moderation → Logs",
    "/music": "Music",
    "/notifications": "Notifications",
    "/permissions": "Fake permissions",
    "/reactions": "Reactions",
    "/roles": "Roles",
    "/tags": "Tags",
    "/tickets": "Tickets",
    "/utility": "Utility",
    "/voice": "Voice",
    "/voicemaster": "VoiceMaster",
    "/welcome": "Welcome",
}


def dash_line(path):
    name = DASH_SECTIONS.get(path, path)
    return f"**Configure on the [dashboard]({DASH}):** {name}"


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def md_escape(s):
    # Minimal: keep prose readable; only guard the characters that would
    # otherwise start MDX/Markdown constructs at an awkward spot.
    return s.replace("<", "\\<").replace("{", "\\{")


def parse(path):
    categories = []  # list of (name, [command, ...])
    cur_cat = None
    cur_cmd = None
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            m = CAT_RE.match(line)
            if m:
                cur_cat = {"name": m.group(1).strip(), "cmds": []}
                categories.append(cur_cat)
                cur_cmd = None
                continue
            if line.startswith("#") or not line.strip():
                continue
            if line.startswith("@ "):
                parts = [p.strip() for p in line[2:].split(";")]
                name = parts[0]
                dash = parts[1] if len(parts) > 1 else "-"
                perm = parts[2] if len(parts) > 2 else "-"
                cur_cmd = {"name": name, "dash": dash, "perm": perm,
                           "desc": [], "subs": []}
                if cur_cat is None:
                    cur_cat = {"name": "Other", "cmds": []}
                    categories.append(cur_cat)
                # Internal staff diagnostics stay out of the public reference.
                if name != "pingtrace":
                    cur_cat["cmds"].append(cur_cmd)
                continue
            if line.startswith("> "):
                parts = [p.strip() for p in line[2:].split(";")]
                syntax = parts[0]
                perm = parts[1] if len(parts) > 1 else "-"
                rest = parts[2:]  # desc (may contain ';') + optional example
                base = syntax.split()[0] if syntax.split() else ""
                ex = ""
                # An example is always a command invocation, so it starts with
                # the command's own name. Only then peel it off the tail;
                # otherwise a ';' inside the description would be misread.
                if len(rest) >= 2 and rest[-1].split() and rest[-1].split()[0] == base:
                    ex = rest[-1]
                    rest = rest[:-1]
                cur_cmd["subs"].append({
                    "syntax": syntax,
                    "perm": perm,
                    "desc": "; ".join(r for r in rest if r),
                    "ex": ex,
                })
                continue
            if cur_cmd is not None:  # a plain description line
                cur_cmd["desc"].append(line.strip())
    return [c for c in categories if c["cmds"]]


def perm_label(p):
    return "Anyone" if p in ("", "-") else p


def registry():
    source = Path(HERE).parents[1] / "src" / "commands" / "mod.rs"
    text = source.read_text().split("pub const COMMANDS:", 1)[1].split("];", 1)[0]
    return {name: re.findall(r'"([^"\n]+)"', aliases) for name, aliases in re.findall(r'\(\s*"([^"\n]+)"\s*,\s*&\[(.*?)\]\s*,\s*"[^"\n]+"\s*,?\s*\)', text, re.S) if name != "pingtrace"}


def render(cat, order):
    lines = ["---", f"title: {cat['name']} commands", f"description: Flanker {cat['name'].lower()} commands, syntax, permissions and examples.", f"sidebar:\n  order: {order}", "---", "", "import CommandReference from '../../../components/CommandReference.astro';", "import commands from '../../../data/commands.json';", "", "Use your server's prefix (default `,`) or mention Flanker. `(round)` parameters are required; `[square]` parameters are optional. Expand a syntax row for its behavior, permissions and example.", ""]
    for cmd in cat['cmds']:
        lines.extend([f"## {cmd['name']}", "", f"<CommandReference command={{commands.find(command => command.name === {json.dumps(cmd['name'])})}} />", ""])
    return "\n".join(lines)


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "assets", "help.txt")
    cats = parse(src)
    registered = registry()
    names = [cmd['name'] for category in cats for cmd in category['cmds']]
    if len(names) != len(set(names)):
        raise SystemExit("Duplicate command names in help.txt")
    if set(names) != set(registered):
        raise SystemExit(f"Command coverage mismatch. Missing help: {sorted(set(registered)-set(names))}; unregistered: {sorted(set(names)-set(registered))}")
    slash = json.loads((Path(HERE).parents[1] / 'assets' / 'slash.json').read_text())
    public_routes = [route for route in slash['routes'] if route['command'] in registered]
    records = [{**cmd, "aliases": registered[cmd['name']], "category": category['name'], "slug": slug(category['name'])} for category in cats for cmd in category['cmds']]
    for command in records:
        for form in command['subs']:
            form['slash'] = [route['path'] for route in public_routes if route['command'] == command['name'] and route['syntax'] == form['syntax']]
            assert form['slash'], ('No typed equivalent', command['name'], form['syntax'])
    data = Path(HERE).parent / 'src' / 'data'
    data.mkdir(exist_ok=True)
    (data / 'commands.json').write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n")
    forms = {(command['name'], form['syntax']): form['desc'] for command in records for form in command['subs']}
    routes = []
    for route in public_routes:
        groups = {}
        for binding in route['bindings']:
            if binding.get('union') and binding.get('union_required'):
                group = groups.setdefault(binding['union'], {'fields': [], 'multiple': False})
                group['fields'].append(binding['name'])
                group['multiple'] |= binding.get('union_many', False)
        routes.append({**{key: route[key] for key in ('command', 'syntax', 'path', 'description', 'portable', 'options')}, 'details': forms[(route['command'], route['syntax'])], 'aliases': registered[route['command']], 'required_groups': list(groups.values())})
    routes.append({'command': 'confess', 'syntax': '', 'aliases': [], 'required_groups': [], 'path': ['confess'], 'description': 'Submit an anonymous confession through a form.', 'details': 'Submit an anonymous confession through a form.', 'portable': False, 'options': []})
    (data / 'slash.json').write_text(json.dumps(routes, indent=2, ensure_ascii=False) + "\n")

    os.makedirs(OUT, exist_ok=True)
    # Clear old generated pages so removed categories don't linger.
    for f in os.listdir(OUT):
        if f.endswith(".md") or (f.endswith(".mdx") and f != "index.mdx"):
            os.remove(os.path.join(OUT, f))
    for i, cat in enumerate(cats):
        path = os.path.join(OUT, f"{slug(cat['name'])}.mdx")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(render(cat, i + 1))
    total = sum(len(c["cmds"]) for c in cats)
    print(f"wrote {len(cats)} category pages, {total} commands to {os.path.relpath(OUT, HERE)}")
    for c in cats:
        print(f"  - {c['name']}: {len(c['cmds'])} commands")


if __name__ == "__main__":
    main()
