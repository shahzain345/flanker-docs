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


def render(cat, order):
    name = cat["name"]
    lines = [
        "---",
        f"title: {name} commands",
        f"description: flanker {name.lower()} commands, their syntax, permissions and examples.",
        f"sidebar:\n  order: {order}",
        "---",
        "",
        "Commands are shown without a prefix. Use your server's prefix "
        "(default `,`) or mention flanker. `(round)` parameters are required, "
        "`[square]` are optional.",
        "",
    ]
    for cmd in cat["cmds"]:
        lines.append(f"## {cmd['name']}")
        lines.append("")
        if cmd["desc"]:
            lines.append(md_escape(" ".join(cmd["desc"])))
            lines.append("")
        lines.append(f"**Permission:** {perm_label(cmd['perm'])}")
        lines.append("")
        if cmd["dash"] not in ("", "-"):
            lines.append(dash_line(cmd["dash"]))
            lines.append("")
        for s in cmd["subs"]:
            lines.append(f"- **`{md_escape(s['syntax'])}`**  ")
            tail = []
            if s["desc"]:
                tail.append(md_escape(s["desc"]))
            lines.append(("  " + " ".join(tail)) if tail else "  ")
            sub_meta = []
            if perm_label(s["perm"]) != "Anyone":
                sub_meta.append(f"*{s['perm']}*")
            if s["ex"]:
                sub_meta.append(f"example: `{md_escape(s['ex'])}`")
            if sub_meta:
                lines.append("  " + "  ·  ".join(sub_meta))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "assets", "help.txt")
    cats = parse(src)
    os.makedirs(OUT, exist_ok=True)
    # Clear old generated pages so removed categories don't linger.
    for f in os.listdir(OUT):
        if f.endswith(".md"):
            os.remove(os.path.join(OUT, f))
    for i, cat in enumerate(cats):
        path = os.path.join(OUT, f"{slug(cat['name'])}.md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(render(cat, i + 1))
    total = sum(len(c["cmds"]) for c in cats)
    print(f"wrote {len(cats)} category pages, {total} commands to {os.path.relpath(OUT, HERE)}")
    for c in cats:
        print(f"  - {c['name']}: {len(c['cmds'])} commands")


if __name__ == "__main__":
    main()
