---
title: Moderation
description: Ban, timeout, jail, purge, warnings and the case log.
---

flanker gives you a full moderation toolkit, and every action is recorded in a
searchable case history.

## Core actions

- `,ban`, `,softban`, `,tempban`, `,hardban`, `,unban`
- `,kick`
- `,timeout` and `,untimeout`
- `,jail` and `,unjail` (role-based isolation that survives rejoins)
- `,warn`, `,warnings`, `,clearwarns`
- `,purge` with filters: member, bots, humans, links, images, embeds, mentions,
  or `contains <text>` (1 to 1000 messages)

See the full [Moderation commands](/commands/moderation/) for syntax, limits and
examples.

## Channel control

- `,lock` and `,unlock` a channel
- `,slowmode` to rate-limit a channel

## Mutes

flanker supports several mute styles depending on your setup, including
image mutes and reaction mutes. See `,help imute` and `,help rmute`.

## Case history

Every moderation action creates a case with the moderator, target, reason and
timestamp. Staff can look up and review cases, and add notes. This gives you an
audit trail independent of Discord's own logs.

:::tip
Pair moderation with [Logging](/guides/logging/) so bans, deletions and edits
are mirrored into a channel your staff can review.
:::

## Bulk role updates

Give several safe roles in one batch:

```text
,role all @Member @Events @Updates
,role humans @Member @Events
,role bots @BotRole
,role all @Events @Updates remove
```

A batch accepts up to ten distinct roles. A trailing `remove` removes all listed roles. Mentions, IDs and quoted role names are accepted; separate roles with spaces. Flanker validates every selected role before starting. Dangerous permissions cannot be granted through a mass command.

Only one bulk role job can be running or queued per server, shared by `all`, `humans` and `bots`. Choose all your roles in one command rather than submitting parallel jobs. Other long tools also share limits by task family, with an overall bounded queue and one active bulk worker per server.

Panic pauses pending requests and keeps the job's progress. Jobs recheck permissions before continuing after recovery. Requests already in flight may finish, and jobs do not survive a bot restart.
