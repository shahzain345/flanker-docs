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

1. Open [flanker.wtf](https://flanker.wtf) and invite the bot to your server.
2. Grant the permissions it asks for. Administrator is the simplest, and the
   security features (antinuke, antiraid, role recovery) need broad permissions
   to undo damage. See [Invite & setup](/start/setup/) for the detail.
3. flanker comes online and is ready. No further install is needed.

## Using commands

flanker is driven by **prefix commands** and the **dashboard**.

- The default prefix is `,`. For example, `,help` or `,ban @user`.
- You can also mention the bot instead of the prefix.
- Change the prefix with `,prefix set !` (see the [General commands](/commands/general/)).

Throughout these docs, commands are written **without** the prefix. Parameters
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
