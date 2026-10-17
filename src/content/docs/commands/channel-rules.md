---
title: Channel rules commands
description: flanker channel rules commands, their syntax, permissions and examples.
sidebar:
  order: 18
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## sticky

A message that stays at the bottom of a channel.

**Permission:** Manage Messages

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation → Channels

- **`sticky add (channel) (message)`**  
  Sets a sticky message. Embed scripts work.
  *Manage Messages*  ·  example: `sticky add #general Read the rules in #rules`
- **`sticky remove (channel)`**  
  Removes it.
  *Manage Messages*
- **`sticky list [page]`**  
  Pages through sticky messages and their channels.
  *Manage Messages*

## autopublish

Publishes every message in an announcement channel, so following servers get it.

**Permission:** Manage Channels

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation → Channels

- **`autopublish (channel)`**  
  Turns auto-publish on or off for an announcement channel.
  *Manage Channels*
- **`autopublish`**  
  Lists channels.
  *Manage Channels*
- **`autopublish list [page]`**  
  Pages through channels that auto-publish.
  *Manage Channels*

## imageonly

Channels where only images and videos are allowed. Text-only messages are deleted.

**Permission:** Manage Channels

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation → Channels

- **`imageonly (channel)`**  
  Turns image-only on or off. Staff are exempt.
  *Manage Channels*
- **`imageonly`**  
  Lists channels.
  *Manage Channels*
- **`imageonly list [page]`**  
  Pages through image-only channels.
  *Manage Channels*

## ignore

Makes flanker ignore commands in channels or from members and roles. People with Manage Server are never ignored.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation → Channels

- **`ignore (channel/role/member)`**  
  Toggles ignoring.
  *Manage Server*
- **`ignore list [page]`**  
  Pages through ignored channels, roles and members.
  *Manage Server*
