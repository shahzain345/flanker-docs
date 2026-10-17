---
title: Snipe and aliases commands
description: flanker snipe and aliases commands, their syntax, permissions and examples.
sidebar:
  order: 4
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## snipe

Shows the last deleted message in the channel.

**Permission:** Anyone

- **`snipe [number]`**  
  Shows a recently deleted message. 1 is the newest.
  example: `snipe 2`

## editsnipe

Shows the last edited message in the channel, before the edit.

**Permission:** Anyone

- **`editsnipe [number]`**  
  Shows a message as it was before it was edited.

## reactionsnipe

Shows the last removed reaction in the channel.

**Permission:** Anyone

- **`reactionsnipe`**  
  Shows who removed which reaction, and from which message.

## clearsnipe

Clears snipe history for the channel.

**Permission:** Manage Messages

- **`clearsnipe`**  
  Forgets every sniped message in the channel.
  *Manage Messages*

## autosnipe

Automatically reposts deleted messages, message edits and removed reactions to chosen destinations. Use a staff-only channel for deleted content.

**Permission:** Manage Server

- **`autosnipe`**  
  Shows each event type, its destination and setup commands.
  *Manage Server*
- **`autosnipe config`**  
  Shows the current routing settings.
  *Manage Server*
- **`autosnipe list`**  
  Shows the current routing settings.
  *Manage Server*
- **`autosnipe (delete/edit/reaction/all) [channel] [on/off]`**  
  Sets one event destination, or all three. The channel defaults to the current channel and the switch defaults to on.
  *Manage Server*  ·  example: `autosnipe delete #logs on`
- **`autosnipe reset [channel]`**  
  Clears every route pointing to that channel, or the current channel when omitted. Other destinations are kept.
  *Manage Server*

## alias

Your own shortcuts for commands.

**Permission:** Manage Server

- **`alias add (shortcut) (command)`**  
  Makes a shortcut. Anything typed after the shortcut is added to the command.
  *Manage Server*  ·  example: `alias add bk ban --silent`
- **`alias remove (shortcut)`**  
  Deletes a shortcut.
  *Manage Server*
- **`alias view (shortcut)`**  
  Shows what a shortcut runs.
  *Manage Server*
- **`alias list [page]`**  
  Pages through server shortcuts and shows disabled built-in aliases.
  *Manage Server*
- **`alias removeall (command)`**  
  Deletes every shortcut for a command.
  *Manage Server*
- **`alias reset`**  
  Deletes every shortcut.
  *Manage Server*
