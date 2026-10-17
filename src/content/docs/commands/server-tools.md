---
title: Server tools commands
description: flanker server tools commands, their syntax, permissions and examples.
sidebar:
  order: 22
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## thread

Manage threads and forum posts. Run it in the thread, or mention one first.

**Permission:** Manage Threads

- **`thread lock [thread]`**  
  Locks a thread so only staff can post.
  *Manage Threads*
- **`thread unlock [thread]`**  
  Unlocks it.
  *Manage Threads*
- **`thread rename [thread] (name)`**  
  Renames it.
  *Manage Threads*
- **`thread add [thread] (member)`**  
  Adds someone to the thread.
  *Manage Threads*
- **`thread remove [thread] (member)`**  
  Removes someone from it.
  *Manage Threads*
- **`thread watch [thread]`**  
  Keeps it open: when Discord archives it, flanker opens it again. Run again to stop.
  *Manage Threads*
- **`thread watch list`**  
  Threads being kept open.

## uwulock

Everything the member says comes back uwuified, posted as them.

**Permission:** Manage Messages

- **`uwulock (member)`**  
  Turns it on or off for someone below you.
  *Manage Messages*  ·  example: `uwulock @someone`
- **`uwulock add (member)`**  
  Turns it on.
  *Manage Messages*
- **`uwulock remove (member)`**  
  Turns it off.
  *Manage Messages*
- **`uwulock list`**  
  Who is uwulocked.
- **`uwulock clear`**  
  Lifts it for everyone.
  *Manage Messages*
- **`uwulock protect [add/remove] (member)`**  
  Nobody can uwulock a protected member.
  *Manage Server*
- **`uwulock protected`**  
  Who is protected.

## proof

Proof on a case: text and images. Images are kept by flanker, so the links never expire.

**Permission:** Timeout Members

- **`proof add (case) [text]`**  
  Adds text or attached images (up to 8 MB each).
  *Timeout Members*  ·  example: `proof add 12 spammed invites`
- **`proof set (case) [text]`**  
  Replaces the proof.
  *Timeout Members*
- **`proof remove (case) (number)`**  
  Removes one piece.
  *Timeout Members*
- **`proof view (case)`**  
  Shows the proof.
  *Timeout Members*

## revokefiles

Stops everyone but staff sending files and embeds in a channel.

**Permission:** Manage Channels

- **`revokefiles [channel]`**  
  Takes file and embed permissions away.
  *Manage Channels*

## unrevokefiles

Gives files and embeds back to everyone in a channel.

**Permission:** Manage Channels

- **`unrevokefiles [channel]`**  
  Restores them.
  *Manage Channels*

## picperms

Lets one member send files and embeds in a channel. Run again to take it back.

**Permission:** Manage Channels

- **`picperms (member) [channel]`**  
  Gives or removes their file permission.
  *Manage Channels*

## deafen

Server deafens someone in voice.

**Permission:** Deafen Members

- **`deafen (member)`**  
  Server deafens someone in voice.
  *Deafen Members*

## undeafen

Removes a server deafen.

**Permission:** Deafen Members

- **`undeafen (member)`**  
  Removes a server deafen.
  *Deafen Members*

## drag

Moves people to a voice channel, or to yours.

**Permission:** Move Members

- **`drag (members) [voice channel]`**  
  Moves people to a voice channel, or to yours.
  *Move Members*  ·  example: `drag @a @b #Gaming`

## moveall

Moves everyone from one voice channel (or yours) to another.

**Permission:** Move Members

- **`moveall [from] (to)`**  
  Moves everyone from one voice channel (or yours) to another.
  *Move Members*

## voicemove

Moves everyone in your voice channel. Name a channel, or let flanker join you and drag it where everyone should go.

**Permission:** Move Members

- **`voicemove`**  
  flanker joins your voice channel. Drag it to another channel within 60 seconds and everyone in yours follows, then flanker leaves.
  *Move Members*
- **`voicemove (voice channel)`**  
  Moves everyone in your voice channel to that one.
  *Move Members*  ·  example: `voicemove #gaming`

## selfpurge

Deletes your own last messages here (15 by default, up to 100).

**Permission:** Anyone

- **`selfpurge [amount]`**  
  Deletes your own last messages here (15 by default, up to 100).

## syncperms

Sets every channel in a category to the category's permissions. A security command: fake permissions don't unlock it.

**Permission:** Manage Channels

- **`syncperms [category]`**  
  Syncs the category (this channel's by default).
  *Manage Channels*

## permissions

Someone's key permissions in flanker and in a channel.

**Permission:** Anyone

- **`permissions [member] [channel]`**  
  Someone's key permissions in flanker and in a channel.

## seticon

A security command: fake permissions don't unlock it.

**Permission:** Manage Server

- **`seticon (image link or attachment, or none)`**  
  Changes the server icon.
  *Manage Server*

## setbanner

Needs boost level 2. A security command: fake permissions don't unlock it.

**Permission:** Manage Server

- **`setbanner (image link or attachment, or none)`**  
  Changes the server banner.
  *Manage Server*

## setsplashbackground

Needs boost level 1. A security command: fake permissions don't unlock it.

**Permission:** Manage Server

- **`setsplashbackground (image link or attachment, or none)`**  
  Changes the invite background.
  *Manage Server*

## splash

Shows the server's invite background.

**Permission:** Anyone

- **`splash`**  
  Shows the server's invite background.

## extractemotes

Sends every server emoji in a zip file.

**Permission:** Manage Expressions

- **`extractemotes`**  
  Sends every server emoji in a zip file.
  *Manage Expressions*

## extractstickers

Sends every server sticker in a zip file.

**Permission:** Manage Expressions

- **`extractstickers`**  
  Sends every server sticker in a zip file.
  *Manage Expressions*

## gnames

The server's past names, tracked since flanker joined.

**Permission:** Anyone

- **`gnames`**  
  The server's past names, tracked since flanker joined.

## cleargnames

Clears the server name history.

**Permission:** Manage Server

- **`cleargnames`**  
  Clears the server name history.
  *Manage Server*

## serverinvites

Every active invite, most used first.

**Permission:** Manage Server

- **`serverinvites`**  
  Every active invite, most used first.
  *Manage Server*

## topcommands

The most used commands in this server.

**Permission:** Anyone

- **`topcommands`**  
  The most used commands in this server.

## boosterslost

People who recently stopped boosting.

**Permission:** Anyone

- **`boosterslost`**  
  People who recently stopped boosting.

## button

Posts a message with one button that answers privately. The answer is saved, so you can edit it later.

**Permission:** Manage Messages

- **`button (channel) (label) && (private reply) [&& message above it]`**  
  Posts it.
  *Manage Messages*  ·  example: `button #rules Read me && Be nice and have fun`

## dump

Sends everyone with the role as a text file.

**Permission:** Manage Roles

- **`dump (role)`**  
  Sends everyone with the role as a text file.
  *Manage Roles*

## embedaccent

The color of a message's embed or card.

**Permission:** Anyone

- **`embedaccent (message link or reply)`**  
  The color of a message's embed or card.

## timediff

Time between two Discord IDs.

**Permission:** Anyone

- **`timediff (id) (id)`**  
  Time between two Discord IDs.

## password

DMs you a random password (8 to 64 characters, 20 by default).

**Permission:** Anyone

- **`password [length]`**  
  DMs you a random password (8 to 64 characters, 20 by default).

## asciify

Turns text into big ASCII letters.

**Permission:** Anyone

- **`asciify (text)`**  
  Turns text into big ASCII letters.
  example: `asciify flanker`

## disableevent

Turns an automatic feature off in one channel: autoresponder, reactions, leveling, streaks, reposts or community (swear jar and highlights).

**Permission:** Manage Channels

- **`disableevent (event or all) [channel or all]`**  
  Turns it off.
  *Manage Channels*  ·  example: `disableevent leveling #memes`
- **`disableevent list`**  
  What's off where.

## enableevent

Turns it back on.

**Permission:** Manage Channels

- **`enableevent (event or all) [channel or all]`**  
  Turns it back on.
  *Manage Channels*

## copydisabled

Copies a channel's turned off events to another.

**Permission:** Manage Channels

- **`copydisabled (from channel) (to channel)`**  
  Copies a channel's turned off events to another.
  *Manage Channels*
