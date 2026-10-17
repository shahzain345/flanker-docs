---
title: Information commands
description: flanker information commands, their syntax, permissions and examples.
sidebar:
  order: 13
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## userinfo

Shows a member's account: when they joined Discord and the server, their roles, key permissions and join position.

**Permission:** Anyone

- **`userinfo [member]`**  
  Profile card: badges, status and activity, profile colour, banner, account and join dates, join position, boosting, nickname, timeout, roles and key permissions. Nitro shows only when the profile proves it, and Discord never shows connections to bots.
  example: `userinfo @shahzain`

## serverinfo

Shows the server: owner, age, members, channels, boosts, roles, emojis and more.

**Permission:** Anyone

- **`serverinfo`**  
  Owner, members and online count, humans and bots, boost progress, every channel type, emoji and sticker slots, safety settings, key channels, vanity and features.

## roleinfo

Shows a role: members, colour, position, settings and key permissions.

**Permission:** Anyone

- **`roleinfo (role)`**  
  Members and share of the server, position, colour, settings, who manages it, powerful and other permissions, and some members.
  example: `roleinfo Staff`

## inrole

Lists the members who have a role.

**Permission:** Anyone

- **`inrole (role)`**  
  Lists members with the role.
  example: `inrole @Staff`

## membercount

How many members the server has.

**Permission:** Anyone

- **`membercount`**  
  Members, humans, bots, online, boosters and new members today, this week and this month.

## botinfo

About flanker.

**Permission:** Anyone

- **`botinfo`**  
  Servers, members, channels, people who used flanker, commands, uptime and links.

## avatar

Shows someone's avatar in full size.

**Permission:** Anyone

- **`avatar [member]`**  
  Shows a member's avatar, or yours.
  example: `avatar @shahzain`

## serveravatar

Shows someone's server-specific avatar.

**Permission:** Anyone

- **`serveravatar [member]`**  
  Shows the avatar they set for this server.

## banner

Shows someone's profile banner.

**Permission:** Anyone

- **`banner [member]`**  
  Shows a member's banner, or yours.

## guildbanner

Shows the banner a member set for this server.

**Permission:** Anyone

- **`guildbanner [member]`**  
  Shows their server profile banner, or yours. Aliases: gbanner, memberbanner. If none is set, says so instead of showing the global banner.
  example: `guildbanner @shahzain`

## servericon

Shows the server's icon in full size.

**Permission:** Anyone

- **`servericon`**  
  Shows the server icon.

## serverbanner

Shows the server's banner.

**Permission:** Anyone

- **`serverbanner`**  
  Shows the server banner.

## firstmessage

Finds the first message ever sent in a channel.

**Permission:** Anyone

- **`firstmessage [channel]`**  
  Links the channel's first message.

## inviteinfo

Looks up an invite: which server, how many members, who made it.

**Permission:** Anyone

- **`inviteinfo (invite code or link)`**  
  The server behind an invite: members and online, boosts, verification, banner, who made it and when it expires.
  example: `inviteinfo discord.gg/abc`
