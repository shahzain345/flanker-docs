---
title: Moderation commands
description: flanker moderation commands, their syntax, permissions and examples.
sidebar:
  order: 3
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## setup

Creates the jail role, the jail channel and the jail log.

**Permission:** Administrator

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation → Jail

- **`setup`**  
  Creates everything the jail needs and hides other channels from jailed members.
  *Administrator*

## setupmute

Creates the image mute and reaction mute roles.

**Permission:** Manage Server

- **`setupmute`**  
  Creates both roles and denies them in every channel.
  *Manage Server*

## settings

Moderation settings.

**Permission:** Manage Server (real)

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation

- **`settings modlog (channel)`**  
  Where a case is posted for every moderation action.
  *Manage Server (real)*  ·  example: `settings modlog #mod-log`
- **`settings jail (channel)`**  
  The jail channel.
  *Manage Server (real)*
- **`settings jailthreads (on/off)`**  
  Gives each jailed member a private thread with staff.
  *Manage Server (real)*
- **`settings jailmsg (message)`**  
  The message jailed members see.
  *Manage Server (real)*
- **`settings jailmsgchannel (channel)`**  
  Where the jail message is posted.
  *Manage Server (real)*
- **`settings imuted (role/none)`**  
  The image mute role.
  *Manage Server (real)*
- **`settings rmuted (role/none)`**  
  The reaction mute role.
  *Manage Server (real)*
- **`settings appealserver (invite/none)`**  
  An appeal server link added to ban messages.
  *Manage Server (real)*
- **`settings dj (role/off)`**  
  The DJ role for music.
  *Manage Server*
- **`settings autoplay (on/off)`**  
  Plays similar tracks when the music queue runs out.
  *Manage Server*

## invoke

Custom messages for moderation actions: what the member gets in DMs and what's posted in the channel.

**Permission:** Manage Server

- **`invoke (action) (dm/message) (message)`**  
  Sets the message for ban, softban, tempban, hardban, unban, kick, timeout (also `mute`, `to`), untimeout, warn, jail, unjail, imute, iunmute, rmute or runmute. Also on the dashboard under Moderation, Command replies.
  *Manage Server*  ·  example: `invoke ban dm You were banned from \{guild.name}: \{reason}`
- **`invoke (action) (dm/message) view`**  
  Shows the current message.
  *Manage Server*
- **`invoke (action) (dm/message) clear`**  
  Goes back to the default.
  *Manage Server*
- **`invoke test (action) (dm/message) [member]`**  
  Sends a preview.
  *Manage Server*
- **`invoke list`**  
  Shows which actions have custom messages.
  *Manage Server*

## access

Chooses who can use each moderation command: extra roles that may use it, roles it's limited to, or turning it off.

**Permission:** Server owner or Flanker Admin

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation

- **`access`**  
  Shows every customised command.
  *Server owner or Flanker Admin*
- **`access list [page]`**  
  Pages through moderation command access rules.
  *Server owner or Flanker Admin*
- **`access allow (command) (role)`**  
  Lets a role use a command without the Discord permission. Commands that hand out roles are owner-only.
  *Server owner or Flanker Admin*  ·  example: `access allow ban @Mods`
- **`access only (command) (role)`**  
  Members also need one of these roles. Admins are never limited.
  *Server owner or Flanker Admin*  ·  example: `access only kick @Seniors`
- **`access disable (command)`**  
  Turns a command off for everyone but admins.
  *Server owner or Flanker Admin*
- **`access enable (command)`**  
  Turns it back on.
  *Server owner or Flanker Admin*
- **`access reset (command/all)`**  
  Goes back to Discord permissions.
  *Server owner or Flanker Admin*

## ban

Bans a member and deletes their recent messages.

**Permission:** Ban Members

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation

- **`ban (member) [reason] [--silent]`**  
  Bans a member. Already-banned users are left unchanged, without another DM or case. Use --silent to skip the punishment DM.
  *Ban Members*  ·  example: `ban @spammer posting scam links`

## softban

Bans and unbans right away to clear someone's recent messages.

**Permission:** Ban Members

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation

- **`softban (member) [reason] [--silent]`**  
  Removes the member and their last day of messages, then lifts the new ban so they can rejoin. Never lifts an existing ban. Reports if the release fails.
  *Ban Members*  ·  example: `softban @spammer`

## tempban

Bans a member for a set time.

**Permission:** Ban Members

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation

- **`tempban (member) (duration) [reason] [--silent]`**  
  Bans them until the duration ends. An existing ban and its expiry are left unchanged.
  *Ban Members*  ·  example: `tempban @member 7d toxicity`

## hardban

A ban that sticks: if anyone unbans them, flanker bans them again.

**Permission:** Owner, backup owner or antinuke admin

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation

- **`hardban (member) [reason]`**  
  Bans and re-bans on every unban until the hardban is lifted. An existing normal ban gains hardban protection without another ban or DM. Pending tempban expiry is cancelled. Repeating a hardban changes nothing.
  *Owner, backup owner or antinuke admin*

## unban

Lifts a ban.

**Permission:** Ban Members

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation

- **`unban (user, id or username) [reason]`**  
  Unbans a user. A name is looked up in the ban list.
  *Ban Members*  ·  example: `unban baduser`

## kick

Removes a member from the server.

**Permission:** Kick Members

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation

- **`kick (member) [reason] [--silent]`**  
  Kicks a member. They can rejoin with an invite.
  *Kick Members*  ·  example: `kick @member`

## timeout

Stops a member from talking for a while.

**Permission:** Timeout Members

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation

- **`timeout (member) [duration] [reason] [--silent]`**  
  Times a member out. Defaults to 5 minutes, up to 28 days.
  *Timeout Members*  ·  example: `timeout @member 1h spam`

## untimeout

Ends a timeout early.

**Permission:** Timeout Members

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation

- **`untimeout (member) [reason]`**  
  Lets a member talk again.
  *Timeout Members*

## warn

Gives a member a formal warning, saved as a case.

**Permission:** Timeout Members

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation

- **`warn (member) (reason) [--silent]`**  
  Warns a member and DMs them.
  *Timeout Members*  ·  example: `warn @member keep it civil`

## warnings

Lists a member's warnings.

**Permission:** Timeout Members

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation

- **`warnings [member]`**  
  Shows warnings, newest first.
  *Timeout Members*

## clearwarns

Removes a member's warnings.

**Permission:** Timeout Members

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation

- **`clearwarns (member)`**  
  Deletes every warning for the member.
  *Timeout Members*

## jail

Locks a member in the jail channel, away from the rest of the server.

**Permission:** Timeout Members

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation → Jail

- **`jail (member) [duration] [reason] [--silent]`**  
  Jails a member. Their roles are saved and given back when they're released.
  *Timeout Members*  ·  example: `jail @member 2h`

## unjail

Releases a jailed member.

**Permission:** Timeout Members

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation → Jail

- **`unjail (member) [reason]`**  
  Gives their roles back.
  *Timeout Members*

## imute

Stops a member posting images and embeds.

**Permission:** Timeout Members

- **`imute (member) [reason]`**  
  Gives the image mute role.
  *Timeout Members*

## iunmute

Lifts an image mute.

**Permission:** Timeout Members

- **`iunmute (member)`**  
  Removes the image mute role.
  *Timeout Members*

## rmute

Stops a member adding reactions.

**Permission:** Timeout Members

- **`rmute (member) [reason]`**  
  Gives the reaction mute role.
  *Timeout Members*

## runmute

Lifts a reaction mute.

**Permission:** Timeout Members

- **`runmute (member)`**  
  Removes the reaction mute role.
  *Timeout Members*

## purge

Bulk deletes messages.

**Permission:** Manage Messages

- **`purge (1-1000)`**  
  Deletes the last messages in the channel.
  *Manage Messages*  ·  example: `purge 50`
- **`purge (member) (1-1000)`**  
  Only that member's messages.
  *Manage Messages*  ·  example: `purge @spammer 100`
- **`purge (bots/humans/links/images/embeds/mentions/stickers) (1-1000)`**  
  Only one kind of message.
  *Manage Messages*  ·  example: `purge bots 30`
- **`purge contains (text) (1-1000)`**  
  Only messages containing some text.
  *Manage Messages*

## lock

Stops everyone except staff from typing in a channel.

**Permission:** Manage Channels

- **`lock [channel] [reason]`**  
  Locks a channel.
  *Manage Channels*

## unlock

Unlocks a locked channel.

**Permission:** Manage Channels

- **`unlock [channel]`**  
  Lets everyone type again.
  *Manage Channels*

## slowmode

Sets a channel's slowmode.

**Permission:** Manage Channels

- **`slowmode [channel] (duration/off)`**  
  Members wait this long between messages.
  *Manage Channels*  ·  example: `slowmode 10s`

## nickname

Changes a member's nickname.

**Permission:** Manage Nicknames

- **`nickname (member) [nickname/reset]`**  
  Sets or clears a nickname.
  *Manage Nicknames*  ·  example: `nickname @member Bob`

## role

Gives or takes roles, and creates, edits and deletes them.

**Permission:** Manage Roles

- **`role (member) (roles)`**  
  Toggles each role on the member. You can only hand out roles below yours that have no permissions you lack.
  *Manage Roles*  ·  example: `role @member Verified, Member`
- **`role restore (member)`**  
  Restores the latest saved roles after a member leaves, is kicked or is banned, once they rejoin. Respects current hierarchy, actor permissions and antinuke limits. Does not bypass jail, captcha or protected roles. Member settings remain keyed to their user ID.
  *Manage Roles*  ·  example: `role restore @member`
- **`role create (name) [--color hex] [--hoist]`**  
  Creates a role with no permissions.
  *Manage Roles*  ·  example: `role create Events --color #a3b6ff`
- **`role delete (role)`**  
  Deletes a role. Counts toward antinuke's role limit.
  *Manage Roles*
- **`role color (role) (hex)`**  
  Changes a role's colour.
  *Manage Roles*
- **`role rename (role) (new name)`**  
  Renames a role.
  *Manage Roles*
- **`role icon (role) (image URL, emoji or attachment)`**  
  Sets a role icon (boost level 2).
  *Manage Roles*
- **`role hoist (role) (on/off)`**  
  Shows the role separately in the member list.
  *Manage Roles*
- **`role mentionable (role) (on/off)`**  
  Lets anyone mention the role.
  *Manage Roles*
- **`role all (role) [remove]`**  
  Gives a role to (or takes it from) every member. Dangerous roles can't be mass given.
  *Manage Roles*
- **`role humans (role) [remove]`**  
  Every member who isn't a bot.
  *Manage Roles*
- **`role bots (role) [remove]`**  
  Every bot.
  *Manage Roles*

## history

A member's moderation history.

**Permission:** Timeout Members

- **`history [member]`**  
  Lists every case for the member.
  *Timeout Members*

## case

Looks up one moderation case.

**Permission:** Timeout Members

- **`case (number)`**  
  Shows the case.
  *Timeout Members*  ·  example: `case 42`

## reason

Changes the reason on a case.

**Permission:** Timeout Members

- **`reason (case) (new reason)`**  
  Updates the case and its modlog post.
  *Timeout Members*  ·  example: `reason 42 alt account`
