---
title: The dashboard
description: Configure flanker visually at flanker.wtf/dashboard.
---

Almost everything flanker does can be configured at
[flanker.wtf/dashboard](https://flanker.wtf/dashboard), with a live preview and
without memorising commands.

## Signing in

1. Go to [flanker.wtf/dashboard](https://flanker.wtf/dashboard).
2. Sign in with Discord.
3. Pick a server you manage. You need Manage Server there (or be the owner).

## What you can configure

- **Security**: antinuke modules, antiraid, honeypot.
- **Moderation and logging**: cases, filters, log channels per event group.
- **Welcome and messages**: the visual card builder with buttons and menus,
  autoroles, autoresponders.
- **Community**: tickets, applications, vanity rewards, leveling, giveaways,
  starboard.
- **VoiceMaster**: temporary voice channels and their defaults.

## Every dashboard section

Each area of the dashboard configures a set of features. Open the dashboard,
pick your server, and choose the section:

| Section | Configures |
| --- | --- |
| **Antinuke** | Antinuke modules, thresholds, punishments, admins, trusted bots |
| **Antiraid** | Raid detection thresholds, captcha and raid responses |
| **Honeypot** | The trap channel and the action taken on posters |
| **Filters** | Word, link, invite and spam filters |
| **Fake permissions** | Command access that only flanker honours |
| **Moderation** | Moderation defaults, settings and access |
| **Moderation → Jail** | Jail setup and jailed-member handling |
| **Moderation → Logs** | Log channels per event group |
| **Moderation → Channels** | Auto-publish, ignore, image-only and sticky channels |
| **Welcome** | Welcome, leave, autoroles and boost messages |
| **Roles** | Sticky roles and role settings |
| **Reactions** | Reaction roles, reaction triggers, starboard, reaction stats |
| **Tickets** | Ticket panels and handling |
| **Applications** | Application forms and review |
| **Community** | Swear jar, pins, random nick, no-self-react |
| **Invites** | Invite tracking and settings |
| **Voice** | Voice leveling and stream settings |
| **VoiceMaster** | Join-to-Create channels and room defaults |
| **Notifications** | Twitch, YouTube, Kick, Reddit, SoundCloud, Pinterest, Fortnite |
| **Birthdays** | Birthday channel, message and role |
| **Tags** | Custom tag messages |
| **Custom commands** | Custom command builder |
| **Music** | Music settings and presets |
| **Utility** | Prefix, enabling/disabling commands and modules |

Any command whose reference entry shows a **Configure on the dashboard** line
can be set up in the matching section above instead of by command.

## How settings reach the bot

The dashboard and the bot share one database. When you save a setting, it is
sent to the bot and applied to your server, so dashboard changes and in-Discord
commands stay in sync.

## Privacy

What flanker stores, why, how long, and how to request deletion is explained in
the [privacy policy](https://flanker.wtf/privacy). Production data is encrypted
at rest.
