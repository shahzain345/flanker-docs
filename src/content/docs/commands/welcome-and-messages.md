---
title: Welcome and messages commands
description: flanker welcome and messages commands, their syntax, permissions and examples.
sidebar:
  order: 5
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## welcome

Messages posted when someone joins. Supports embeds, buttons and layouts.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Welcome

- **`welcome add (channel) (message) [--self_destruct 6-60]`**  
  Sets the welcome message for a channel.
  *Manage Server*  ·  example: `welcome add #welcome Welcome to \{guild.name}, \{user.mention}!`
- **`welcome remove (channel)`**  
  Removes it.
  *Manage Server*
- **`welcome view (channel)`**  
  Shows the message's script.
  *Manage Server*
- **`welcome test (channel)`**  
  Sends a test with you as the new member.
  *Manage Server*
- **`welcome list`**  
  Lists channels with a welcome message.
  *Manage Server*

## leave

Messages posted when someone leaves.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Welcome

- **`leave add (channel) (message) [--self_destruct 6-60]`**  
  Sets the leave message for a channel.
  *Manage Server*  ·  example: `leave add #general \{user.name} left.`
- **`leave remove (channel)`**  
  Removes it.
  *Manage Server*
- **`leave view (channel)`**  
  Shows the message's script.
  *Manage Server*
- **`leave test (channel)`**  
  Sends a test.
  *Manage Server*

## boosts

Messages posted when someone boosts the server.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Welcome

- **`boosts add (channel) (message) [--self_destruct 6-60]`**  
  Sets the boost message for a channel.
  *Manage Server*
- **`boosts remove (channel)`**  
  Removes it.
  *Manage Server*
- **`boosts view (channel)`**  
  Shows the message's script.
  *Manage Server*
- **`boosts test (channel)`**  
  Sends a test.
  *Manage Server*

## greet

Greets members when they join by default. Each channel can instead greet their first message there. Join greets wait for captcha verification and pause during raids.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Welcome

- **`greet add (channel) (message) [--trigger join/message] [--pingable on/off] [--self-destruct seconds]`**  
  Sets the greet for a channel. Defaults to joining.
  *Manage Server*  ·  example: `greet add #chat say hi to \{user.mention}`
- **`greet list`**  
  Shows every greet channel.
  *Manage Server*
- **`greet trigger (join/message) [channel]`**  
  Sets when greets run. Without a channel it changes every greet.
  *Manage Server*  ·  example: `greet trigger message #chat`
- **`greet view (channel)`**  
  Shows a greet's script.
  *Manage Server*
- **`greet message [channel] (message)`**  
  Changes a greet's message.
  *Manage Server*
- **`greet pingable (on/off) [channel]`**  
  Whether greets actually ping. Without a channel it changes all of them.
  *Manage Server*
- **`greet selfdestruct (seconds/off) [channel]`**  
  Deletes greets after a few seconds. Without a channel it changes all of them.
  *Manage Server*
- **`greet test [channel] [member]`**  
  Sends a test.
  *Manage Server*
- **`greet resetuser (member)`**  
  Lets a member be greeted again.
  *Manage Server*
- **`greet remove (channel)`**  
  Removes a channel's greet.
  *Manage Server*

## autorole

Roles given to new members once they're through antiraid's captcha. Roles with dangerous permissions can't be used.

**Permission:** Manage Roles

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Welcome

- **`autorole`**  
  Shows the roles.
  *Manage Roles*
- **`autorole add (roles)`**  
  Roles for everyone who joins.
  *Manage Roles*  ·  example: `autorole add @Member`
- **`autorole remove (roles)`**  
  Stops giving those roles.
  *Manage Roles*
- **`autorole humans add (roles)`**  
  Roles for people only.
  *Manage Roles*
- **`autorole bots add (roles)`**  
  Roles for bots only.
  *Manage Roles*
- **`autorole reset`**  
  Removes every autorole.
  *Manage Roles*

## pingonjoin

Pings new members in channels and deletes the ping right away, so they notice those channels.

**Permission:** Manage Server

- **`pingonjoin add (channel or category)`**  
  Adds a channel.
  *Manage Server*  ·  example: `pingonjoin add #rules`
- **`pingonjoin remove (channel or category)`**  
  Removes it.
  *Manage Server*
- **`pingonjoin time (seconds)`**  
  How long the ping stays.
  *Manage Server*
- **`pingonjoin reset`**  
  Removes every channel.
  *Manage Server*
- **`pingonjoin list [page]`**  
  Pages through ping channels and shows how long the pings stay.
  *Manage Server*

## bumpreminder

Reminds the server to bump on DISBOARD when the 2 hour cooldown ends, and thanks whoever bumped.

**Permission:** Manage Server

- **`bumpreminder channel (channel)`**  
  Where DISBOARD bumps are watched.
  *Manage Server*  ·  example: `bumpreminder channel #bump`
- **`bumpreminder message (message) [--pingable on/off] [--remind_once on/off]`**  
  The reminder message.
  *Manage Server*
- **`bumpreminder thankyou (message) [--pingable on/off]`**  
  The thank-you message.
  *Manage Server*
- **`bumpreminder set (reminder/thankyou) (message)`**  
  Replaces a message without changing its options. Accepts plain text, embeds and cards.
  *Manage Server*
- **`bumpreminder (mentions/thankmentions) (on/off)`**  
  Allows mentions in the reminder or thank-you message.
  *Manage Server*
- **`bumpreminder once (on/off)`**  
  On sends one reminder per bump. Off repeats every two hours until the next bump.
  *Manage Server*
- **`bumpreminder (autolock/autoclean) (on/off)`**  
  Auto-lock blocks chat between bumps. Auto-clean deletes messages from everyone except DISBOARD and flanker.
  *Manage Server*

## timer

Repeating messages posted every so often.

**Permission:** Manage Server

- **`timer add (channel) (interval) (message)`**  
  Posts the message every interval.
  *Manage Server*  ·  example: `timer add #general 2h Remember to read the rules!`
- **`timer remove (channel)`**  
  Stops the timer.
  *Manage Server*
- **`timer view (channel)`**  
  Shows the timer.
  *Manage Server*
- **`timer activity (on/off)`**  
  Skips a post when the channel has been quiet.
  *Manage Server*

## autoresponder

Replies automatically when a message contains a trigger.

**Permission:** Manage Server

- **`autoresponder add (trigger), (response) [--not_strict] [--self_destruct 6-60] [--delete] [--reply] [--ignore_command_check]`**  
  Adds an autoresponder. Note the comma after the trigger.
  *Manage Server*  ·  example: `autoresponder add hello, Hi \{user.mention}!`
- **`autoresponder remove (trigger)`**  
  Deletes one.
  *Manage Server*
- **`autoresponder view (trigger)`**  
  Shows its settings.
  *Manage Server*
- **`autoresponder list`**  
  Lists every autoresponder.
  *Manage Server*
- **`autoresponder exclusive (role/channel) (trigger)`**  
  Only answers for that role or in that channel.
  *Manage Server*
- **`autoresponder role (add/remove) (role) (trigger)`**  
  Gives or takes a role when it fires.
  *Manage Server*
- **`autoresponder reset`**  
  Deletes every autoresponder.
  *Manage Server*

## reaction

Reacts to messages that contain a word, or to every message in a channel.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Reactions

- **`reaction add (emoji(s)) (trigger word)`**  
  Reacts whenever a message contains the word.
  *Manage Server*  ·  example: `reaction add 😭 crying`
- **`reaction delete (trigger word) (emoji)`**  
  Removes one emoji from a trigger.
  *Manage Server*
- **`reaction deleteall (trigger word)`**  
  Removes a trigger.
  *Manage Server*
- **`reaction list`**  
  Lists every trigger.
  *Manage Server*
- **`reaction owner (trigger word)`**  
  Shows who added each emoji.
  *Manage Server*
- **`reaction messages (channel) [emoji] [emoji] [emoji]`**  
  Reacts to every message in a channel, up to 3 emojis.
  *Manage Server*  ·  example: `reaction messages #selfies 🔥 😍`
