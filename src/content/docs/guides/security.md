---
title: Security
description: Set up antinuke, antiraid and the honeypot to protect your server.
---

flanker's security is its headline feature. Set this up early, before you open
the server to members.

## Antinuke

Antinuke stops server-destroying actions: mass bans and kicks, deleted channels
and roles, dangerous permission grants, webhook and emoji spam, vanity changes
and rogue bot adds. When someone crosses a limit, flanker punishes them and
undoes the damage where possible.

- `,antinuke setup` turns it on. **Beginner** applies the recommended protection
  in one step; **advanced** adds optional hardening as yes/no questions.
- `,antinuke config` shows every module, its limit and punishment, the antinuke
  admins and trusted bots.
- `,antinuke <module> (on/off) [--threshold N] [--do punishment]` tunes one
  module. Modules include ban, kick, channel, role, webhook, emoji, vanity,
  botadd and permissions. Punishments: warn, jail, kick, ban, stripstaff,
  timeout.

:::tip
Add your real, trusted bots as trusted so their normal actions never trip
antinuke. See `,help antinuke` and the [Security commands](/commands/security/).
:::

## Antiraid

Antiraid detects coordinated joins and raid behaviour and reacts in real time.

- `,antiraid` configures raid thresholds and responses.
- `,raid` controls manual raid mode.
- Responses include lockdown, captcha verification for new members, and
  removing raiders.

See [Antiraid commands](/commands/security/) for the full option set.

## Honeypot

A honeypot is a trap channel. Anyone who posts in it is acting like a raider or
spammer, so flanker can catch and punish them automatically.

- `,honeypot` sets up the trap channel and the action taken on anyone who posts.

## Fake permissions and filters

- `,fakepermissions` grants command access that only flanker honours, so staff
  can use flanker without being handed real, abusable Discord permissions.
- `,filter` configures word, link, invite and spam filters that delete or act on
  rule-breaking messages.

## Recovery

When something does get through, flanker helps you recover: deleted channels can
be restored with their settings and recent messages, and removed roles can be
given back. See the backup and channel commands in the
[reference](/commands/security/).
