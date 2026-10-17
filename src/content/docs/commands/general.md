---
title: General commands
description: flanker general commands, their syntax, permissions and examples.
sidebar:
  order: 1
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## help

Shows every command, or how one command works.

**Permission:** Anyone

- **`help`**  
  Shows every module, with a menu to browse each one.
- **`help (module)`**  
  Lists every command in a module with what it does.
  example: `help security`
- **`help (command) [subcommand]`**  
  Shows how a command works: what it does, its parameters, the permission it needs, and where to set it up on the dashboard. Misspelled names suggest close commands, aliases or modules.
  example: `help antinuke whitelist`

## prefix

Shows or changes the prefix flanker answers to in this server.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Utility

- **`prefix`**  
  Shows the current prefix.
- **`prefix set (symbol)`**  
  Changes the prefix. Up to 5 characters.
  *Manage Server*  ·  example: `prefix set !`
- **`prefix reset`**  
  Goes back to the default prefix.
  *Manage Server*

## dashboard

Links to flanker's dashboard for this server.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Utility

- **`dashboard`**  
  Shows the dashboard link.
- **`dashboard stats (on/off)`**  
  Whether members who can't manage the server see its stats on the dashboard.
  *Manage Server*

## ping

Shows how fast flanker is answering right now.

**Permission:** Anyone

- **`ping`**  
  Shows latest and average websocket heartbeat latency, recent samples, Discord API, MongoDB, reply-send time, shard and uptime. Reply time includes Discord rate-limit waits. Dashboard capture is not a Discord send.
