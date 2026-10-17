---
title: Moderation extras commands
description: flanker moderation extras commands, their syntax, permissions and examples.
sidebar:
  order: 17
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## hide

Hides a channel from everyone except staff.

**Permission:** Manage Channels

- **`hide [channel]`**  
  Hides the channel.
  *Manage Channels*

## unhide

Shows a hidden channel again.

**Permission:** Manage Channels

- **`unhide [channel]`**  
  Unhides the channel.
  *Manage Channels*

## syncadmin

Brings the Flanker Admin role up to date. It looks like an admin role in Discord, but never holds Administrator, Manage Server, Ban or Kick.

**Permission:** Owner, backup owner or antinuke admin

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Antinuke

- **`syncadmin`**  
  Resets the role's permissions, keeps it below Flanker Protection and gives it access to every channel, private ones included.
  *Owner, backup owner or antinuke admin*

## nuke

Recreates a channel empty: every message is wiped, settings stay. Counts toward antinuke's channel limit.

**Permission:** Owner, backup owner or antinuke admin

- **`nuke [channel]`**  
  Clones the channel and deletes the old one. Settings that used it (welcome, logs, tickets...) move to the new one.
  *Owner, backup owner or antinuke admin*

## topic

Changes a channel's topic.

**Permission:** Manage Channels

- **`topic [channel] (text/clear)`**  
  Sets or clears the topic.
  *Manage Channels*  ·  example: `topic Read the rules before posting`

## pin

Pins a message.

**Permission:** Manage Messages

- **`pin (reply, or message link)`**  
  Pins the message.
  *Manage Messages*

## unpin

Unpins a message.

**Permission:** Manage Messages

- **`unpin (reply, or message link)`**  
  Unpins the message.
  *Manage Messages*

## forcenickname

Keeps a member at a nickname: if they change it, it's set back.

**Permission:** Manage Nicknames

- **`forcenickname (member) (nickname)`**  
  Forces the nickname.
  *Manage Nicknames*  ·  example: `forcenickname @member Behave`
- **`forcenickname (member) reset`**  
  Lets them change it again.
  *Manage Nicknames*
- **`forcenickname list`**  
  Lists forced nicknames.
  *Manage Nicknames*

## stripstaff

Removes every staff role from a member at once.

**Permission:** Manage Roles

- **`stripstaff (member) [reason]`**  
  Takes away roles with moderation or admin permissions and logs a case.
  *Manage Roles*

## restore

Gives a member back the roles they had when they left.

**Permission:** Manage Roles

- **`restore (member)`**  
  Same as role restore. Skips deleted, protected and ungrantable roles. Requires the member to have rejoined and completed any active security hold.
  *Manage Roles*

## rolecommands

Restricts built-in commands for specific members or members holding a role. Server managers and Flanker Admins bypass these restrictions. Restrictions never grant permissions, and built-in aliases share the same rule.

**Permission:** Manage Server

- **`rolecommands add (member or role) (command, command)`**  
  Blocks command roots and their subcommands for that member or role. Alias: rc. Use names without a prefix. Member and role mentions select the target type.; rc add @member ban, timeout
  *Manage Server*
- **`rolecommands add user (member ID or quoted name) (command, command)`**  
  Explicitly selects a member. Restrictions are server-only and stay with their user ID if they leave and rejoin. Use role instead of user to explicitly select a role.; rc add user @member ban
  *Manage Server*
- **`rolecommands remove (member or role) (command, command)`**  
  Removes only those direct member or role rules. Supports the same user/role selectors. Removing a member rule does not bypass an existing role rule.; rc remove @member ban
  *Manage Server*
- **`rolecommands list [page]`**  
  Lists both member and role restrictions. Recovery commands and help cannot be blocked. Server managers and Flanker Admins retain access.; rc list
  *Manage Server*

## bans

Lists banned users.

**Permission:** Ban Members

- **`bans`**  
  Shows bans with their reasons.
  *Ban Members*

## unbanall

Unbans everyone except hardbanned users.

**Permission:** Owner, backup owner or antinuke admin

- **`unbanall`**  
  Lifts every ban in the background.
  *Owner, backup owner or antinuke admin*

## cleanup

Deletes flanker's messages and command messages in the channel.

**Permission:** Manage Messages

- **`cleanup [amount]`**  
  Looks through the last messages (up to 100) and deletes bot replies and commands.
  *Manage Messages*

## notes

Private staff notes about members.

**Permission:** Timeout Members

- **`notes (member)`**  
  Shows notes about a member.
  *Timeout Members*
- **`notes add (member) (note)`**  
  Adds a note.
  *Timeout Members*  ·  example: `notes add @member warned in DMs about spam`
- **`notes remove (number)`**  
  Removes a note.
  *Timeout Members*
- **`notes clear (member)`**  
  Removes every note about a member.
  *Timeout Members*

## modstats

How much moderation someone has done.

**Permission:** Timeout Members

- **`modstats [member]`**  
  Cases by type in the last 7 days, 30 days and all time.
  *Timeout Members*
