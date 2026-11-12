---
title: Embed and card builder
description: Build embeds and Components V2 cards in Discord with buttons, no code or Studio needed.
---

Run `/embed create (name)` (Manage Messages) and flanker posts the embed with
buttons under it. Every change shows up on the embed straight away and is
saved under its name. For a Components V2 card, run `/server-tools card create (name)`.
Leave the name out and flanker picks one, like `embed1`.

## The buttons

- **Edit basic info**: title, description, colour, a link on the title, and
  plain text above the embed.
- **Edit author**: a small name at the top, with an icon and a link.
- **Edit footer**: small text at the bottom, an icon, and the time it was sent.
- **Edit images**: a big image and a small one in the corner.
- **Add field**: a heading with text, on its own line or side by side.
- **Add link**: a link button under the message, up to five.
- **Remove a field or link**: the menu under the buttons.
- **Make it a card** / **Make it an embed**: switches the look and keeps
  everything you wrote.
- **Code**: shows the script, to paste anywhere flanker takes a message.
- **Send it to a channel**: posts a copy there.
- **Done**: removes the buttons and leaves the finished message.

Variables like `{user.mention}` and `{guild.name}` work in every box. The
builder fills them in with you while you edit.

## Using it

```
/embed create rules
/server-tools card create welcome-card
/embed edit rules
/embed send #rules rules
```

`/embed edit (name)` and `/server-tools card edit (name)` reopen a saved one in the
builder.

## Slash commands

| Slash command | Does |
| --- | --- |
| `/embed create name:` | Opens the embed builder (leave **embed-code** empty) |
| `/server-tools card create` | Opens the card builder. **name** is optional |
| `/server-tools card edit name:` | Reopens a saved embed or card in the builder |
| `/embed send` | Posts a saved one: put its name in **embed-code** |

The builder buttons work the same however you opened it. Saved embeds and cards work on buttons too, with `embed:rules` or
`ephemeral:rules`. Something written as code with menus or role buttons
can't open in the builder. Change it with `/embed create (name) (code)` or in
[Studio](https://flanker.wtf/studio).
