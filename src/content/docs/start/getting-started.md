---
title: Getting started
description: Invite flanker, learn how commands work, and find your way around.
sidebar:
  order: 1
---

flanker is an all-in-one Discord bot for server security, moderation and
management. This page gets you from zero to a running bot in a couple of
minutes.

## Add flanker

1. Open [flanker.wtf/invite](https://flanker.wtf/invite) and invite the bot to your server. The current server invite requests Administrator; see the permissions guide if you use a narrower configuration.
2. Grant the specific permissions needed by the features you enable. If an
   action needs another permission, flanker names it in its reply. See
   [Invite & setup](/start/setup/) for security and channel permissions.
3. flanker comes online and is ready. No further install is needed.

## Using commands

flanker supports **slash commands**, **prefix commands** and the **dashboard**.

- The default prefix is `,`. For example, `,help` or `,ban @user`.
- You can also mention the bot instead of the prefix.
- Change the prefix with `,prefix set !` (see the [General commands](/commands/general/)).

The command index shows syntax **without** a prefix; copyable examples and setup guides use `,`. Replace it with your server’s prefix when needed. Parameters
in `(round)` brackets are required; `[square]` brackets are optional.

## Finding help in Discord

- `,help` opens a browsable menu of every module.
- `,help <module>` lists one module, for example `,help security`.
- `,help <command>` shows exactly how a command works, its parameters, the
  permission it needs, and where to configure it on the dashboard.

## The dashboard

Most things can also be set up at
[flanker.wtf/dashboard](https://flanker.wtf/dashboard) with a live preview. Sign
in with Discord, pick your server, and configure modules visually. See
[The dashboard](/guides/dashboard/).

## Where to go next

- [Invite & setup](/start/setup/) for permissions and first configuration.
- [Security](/guides/security/) to lock the server down (do this early).
- The [Command reference](/commands/general/) for every command.

## Slash commands

Slash commands use Discord's native fields. For example, `/ban` requires a member picker and offers a reason and Silent switch. Roles and channels use pickers; counts use numeric fields; fixed actions use choices. Flanker replies to the interaction directly, without posting a prefix command first.

Frequently used commands have their own slash names. The rest are grouped by category to fit Discord's command limits. Browse the slash menu for the available actions and options. The generic `/command name arguments` bridge has been removed. Slash and prefix commands keep the same permission, cooldown and security checks.
