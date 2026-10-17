---
title: Community commands
description: flanker community commands, their syntax, permissions and examples.
sidebar:
  order: 21
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## tags

The server's own text commands. Any message works: text, embed or card. Once made, `,name` sends it.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Tags

- **`tags add (name) (message)`**  
  Makes a tag.
  *Manage Messages*  ·  example: `tags add rules Read #rules first!`
- **`tags edit (name) (message)`**  
  Changes a tag.
  *Manage Messages*
- **`tags remove (name)`**  
  Deletes a tag.
  *Manage Messages*
- **`tags list`**  
  Lists the tags.
- **`tags info (name)`**  
  Who made it and how often it's used.
- **`tags raw (name)`**  
  Shows the tag's script.
- **`tags (name)`**  
  Sends a tag.

## disablecommand

Turns a command off by default or for one member. Alias: dcmd. Server managers retain access. Member exceptions never grant permissions or bypass module switches or rc restrictions.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Utility

- **`disablecommand [command]`**  
  Turns it off by default. Without arguments, lists defaults and member exceptions.
  *Manage Server*  ·  example: `disablecommand 8ball`
- **`disablecommand all (command)`**  
  Turns it off by default, keeping member exceptions.; dcmd all avatar
  *Manage Server*
- **`disablecommand (member) (command)`**  
  Turns it off for one member, regardless of the server command default.; dcmd @member avatar
  *Manage Server*
- **`disablecommand reset (member) (command)`**  
  Removes that member's exception so the server command default applies.
  *Manage Server*

## enablecommand

Turns a command on by default or for one member. Alias: ecmd. Module switches, rc restrictions and normal command permissions still apply. Explicit user/member selectors accept IDs and quoted names.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Utility

- **`enablecommand (command)`**  
  Turns it on by default, keeping member exceptions.
  *Manage Server*
- **`enablecommand all (command)`**  
  Turns it on by default, keeping member exceptions.; ecmd all avatar
  *Manage Server*
- **`enablecommand (member) (command)`**  
  Allows one member past a server command disable, not other restrictions.; ecmd @member avatar
  *Manage Server*
- **`enablecommand user (member) (command)`**  
  Selects a member explicitly by ID or quoted name.
  *Manage Server*
- **`enablecommand reset (member) (command)`**  
  Removes the member exception and restores the server command default.
  *Manage Server*

## disablemodule

Turns a whole module (like Fun or Roleplay) off for everyone except people with Manage Server.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Utility

- **`disablemodule [module]`**  
  Turns it off. Without a module, lists what's off.
  *Manage Server*  ·  example: `disablemodule roleplay`

## enablemodule

Turns a module back on.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Utility

- **`enablemodule (module)`**  
  Turns it back on.
  *Manage Server*

## stickyrole

Roles given back when a member leaves and rejoins.

**Permission:** Manage Roles

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Roles

- **`stickyrole (add/remove) (role)`**  
  Adds or removes a sticky role.
  *Manage Roles*  ·  example: `stickyrole add @Muted`
- **`stickyrole list`**  
  Lists the sticky roles.
  *Manage Roles*

## temprole

Gives a role for a while, then takes it back.

**Permission:** Manage Roles

- **`temprole (member) (role) (duration)`**  
  Gives it until the time runs out.
  *Manage Roles*  ·  example: `temprole @someone @Event 2d`
- **`temprole list`**  
  Lists running temporary roles.

## swearjar

Counts the words you choose, per member.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Community

- **`swearjar (on/off)`**  
  Turns counting on or off.
  *Manage Server*
- **`swearjar (add/remove) (words)`**  
  Words to count, separated by commas.
  *Manage Server*  ·  example: `swearjar add heck, darn`
- **`swearjar top`**  
  The leaderboard.
- **`swearjar [member]`**  
  How many times someone swore.

## randomnick

New members get a random nickname.

**Permission:** Manage Nicknames

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Community

- **`randomnick (on/off)`**  
  Turns it on or off.
  *Manage Nicknames*
- **`randomnick (add/remove) (words)`**  
  Your own nickname words, separated by commas.
  *Manage Nicknames*

## noselfreact

Removes reactions people add to their own messages.

**Permission:** Manage Messages

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Community

- **`noselfreact (on/off)`**  
  Turns it on or off.
  *Manage Messages*
- **`noselfreact bypass (role)`**  
  Lets a role react to their own messages.
  *Manage Messages*

## highlight

DMs you when someone says one of your words in a channel you can see (at most once a minute).

**Permission:** Anyone

- **`highlight add (word)`**  
  Adds a word (up to 20).
  example: `highlight add flanker`
- **`highlight remove (word)`**  
  Removes a word.
- **`highlight clear`**  
  Removes all your words.
- **`highlight list`**  
  Lists your words.

## pins

A pins archive: moves pinned messages to another channel, so you never hit the 50 pin limit.

**Permission:** Manage Messages

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Community

- **`pins set (channel)`**  
  Where archived pins go.
  *Manage Messages*
- **`pins archive [channel]`**  
  Moves a channel's pins to the archive and unpins them.
  *Manage Messages*
