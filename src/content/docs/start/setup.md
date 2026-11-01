---
title: Invite & setup
description: Permissions flanker needs, how to set the prefix, and the fastest way to configure a server.
sidebar:
  order: 2
---

## Permissions

flanker's security features act on the whole server, so they need real
permissions to work and to reverse an attack:

Grant the specific permissions needed by the features you enable. For security,
these include Manage Roles, Manage Channels, Manage Webhooks, Ban Members,
Kick Members, Moderate Members, Manage Messages and View Audit Log. Flanker
also needs View Channel, Send Messages and Read Message History in channels it uses.
Other features may need rights such as Attach Files, Embed Links, Connect or Speak.

Flanker reports the exact missing permissions when an action is denied, for example
“I’m missing permissions: `BAN_MEMBERS`”. The server invite currently requests Administrator. Individual commands report the specific missing permission rather than asking you to grant Administrator. If you configure narrower permissions manually, grant the permissions required by each enabled feature.

:::caution
Role hierarchy still applies. flanker can only act on roles and members below
its own highest role, so keep flanker's role near the top.
:::

## Prefix

The default prefix is `,`. Change it per server:

- `,prefix` shows the current prefix.
- `,prefix set !` changes it (up to 5 characters).
- `,prefix reset` restores the default.

You can always mention the bot instead of using the prefix.

## Fastest setup

1. **Lock down security first.** Run `,antinuke setup` (beginner mode applies
   the recommended protection in one step). Then `,antiraid` to tune raid
   thresholds. See [Security](/guides/security/).
2. **Turn on logging** so you have an audit trail: `,help logging` or configure
   it on the dashboard. See [Logging](/guides/logging/).
3. **Set up member flow**: a welcome message and autoroles. See
   [Welcome & messages](/guides/welcome/).
4. **Add staff tools**: tickets and applications. See
   [Tickets & applications](/guides/tickets/).

Everything above can also be done on the
[dashboard](https://flanker.wtf/dashboard) with a live preview.

## Staff and access

flanker separates "who can run a command" from Discord's own permissions where
it makes sense (for example antinuke admins). Use `,help access` and
`,help elevate` to see how to grant staff access to specific commands.
