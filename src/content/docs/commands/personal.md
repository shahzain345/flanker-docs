---
title: Personal commands
description: flanker personal commands, their syntax, permissions and examples.
sidebar:
  order: 15
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## afk

Sets you as AFK. Anyone who mentions you or replies to you is told why. It ends when you send a message, and flanker shows you who pinged you while you were away.

**Permission:** Anyone

- **`afk [reason]`**  
  Goes AFK.
  example: `afk sleeping`

## remind

Reminds you about something later, in the channel or by DM.

**Permission:** Anyone

- **`remind (time) (what)`**  
  Sets a reminder, 30 seconds to a year away.
  example: `remind 2h check the oven`
- **`remind list [page]`**  
  Pages through your pending reminders and their numbers.
- **`remind delete (number)`**  
  Cancels a reminder.

## birthday

Birthdays: set yours, see upcoming ones, and announce them with a role for the day.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Birthdays

- **`birthday [member]`**  
  Shows someone's birthday, or yours.
- **`birthday set (date)`**  
  Sets your birthday, like 5 March or 2000-03-05.
  example: `birthday set 5 March`
- **`birthday remove`**  
  Removes your birthday.
- **`birthday list`**  
  Upcoming birthdays in this server.
- **`birthday channel (channel/off)`**  
  Where birthdays are announced.
  *Manage Server*
- **`birthday role (role/off)`**  
  A role members get on their birthday.
  *Manage Server*
- **`birthday message (message/reset)`**  
  The announcement. Embed scripts work.
  *Manage Server*

## timezone

Your time zone, so others can see your local time and birthdays line up.

**Permission:** Anyone

- **`timezone set (zone)`**  
  Sets your time zone.
  example: `timezone set Europe/London`
- **`timezone [member]`**  
  Shows someone's local time.
- **`timezone remove`**  
  Removes yours.

## time

Shows someone's local time.

**Permission:** Anyone

- **`time [member]`**  
  Their local time, if they set a time zone.

## seen

When someone last talked.

**Permission:** Anyone

- **`seen (member)`**  
  Shows when and where they last sent a message.

## namehistory

Past usernames and display names flanker has seen.

**Permission:** Anyone

- **`namehistory [member]`**  
  Lists name changes, newest first.
- **`namehistory clear`**  
  Clears your own history.

## selfprefix

Your own prefix that works in every server, alongside the server's prefix.

**Permission:** Anyone

- **`selfprefix`**  
  Shows yours.
- **`selfprefix set (prefix)`**  
  Sets it, up to 5 characters.
  example: `selfprefix set ?`
- **`selfprefix remove`**  
  Removes it.
