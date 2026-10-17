---
title: Embed & card scripting
description: Build rich messages, embeds and Components V2 cards with flanker's script format.
sidebar:
  order: 1
---

Everywhere flanker lets you customise a message (welcome and leave, embeds,
tickets, autoresponders, tags, boosts and more) it uses one shared script
format. The easiest way to build one is the visual editor on the
[dashboard](https://flanker.wtf/dashboard), which previews the result live.
This page documents the underlying format for power users.

## How a script is structured

A script is a series of **parts** separated by `$v`. There are two message
styles: a classic **embed**, and a Components V2 **card**.

```text
{embed}$v{title: Welcome}$v{description: Hey {user.mention}!}$v{color: #5c6b8a}
```

```text
{component}$v{container}$v{text: ## Welcome}$v{separator: small}$v{button: https://flanker.wtf && Website}$v{end}
```

Plain text with no `$v` and no leading `{` is sent as a normal message.

## Embed tokens

Start with `{embed}`, then add any of these parts:

| Token | What it does |
| --- | --- |
| `{title: ...}` | Embed title |
| `{description: ...}` | Main body |
| `{color: #5c6b8a}` | Accent colour (hex, or a named colour) |
| `{url: ...}` | Makes the title a link |
| `{author: name}` / `{author.icon: url}` / `{author.url: url}` | Author line |
| `{footer: text}` / `{footer.icon: url}` | Footer |
| `{field: Name && Value && true}` | A field; the third part `true` makes it inline |
| `{image: url}` | Large image |
| `{thumbnail: url}` | Small thumbnail |
| `{content: ...}` | Plain text above the embed |

## Card tokens (Components V2)

Start with `{component}`, open a `{container}`, add parts, and close it with
`{end}`. Buttons and menus placed **before** `{end}` sit inside the card;
placed **after** `{end}` they sit outside it.

| Token | What it does |
| --- | --- |
| `{container}` ... `{end}` | Opens and closes a card container |
| `{text: ...}` | A block of markdown text |
| `{separator: small}` | A divider (`small`, `large`, or `hidden` for spacing only) |
| `{section: text && button ...}` | Text with a button or thumbnail beside it |
| `{media: url}` | An image or media gallery item |
| `{button: ...}` | A button (see below) |
| `{menu: ...}` | A select menu |

## Buttons

Parts are separated by `&&`. The first part decides the kind:

- **Link:** `{button: https://flanker.wtf && Website}` (optionally a third part for an emoji).
- **Channel link:** `{button: channel link && #rules && #rules}`.
- **Styled / role button:** `{button: primary && Label && role:ROLE_ID}`.
  Styles are `primary`, `secondary`, `success`, `danger`, `link`. For role
  buttons the target can be `role:ID` (toggle), `give:ID` (add only) or
  `take:ID` (remove only).
- Add `disabled` as any part to disable a button.

## Variables

Any `{dotted.key}` token is replaced with live data when the message is sent,
for example `{user.mention}` or `{guild.name}`. See
[Variables](/resources/variables/) for the full list.

:::tip
You rarely need to write this by hand. The dashboard's message editor builds
the same script visually, with a live preview and buttons you can drag inside or
outside the card.
:::
