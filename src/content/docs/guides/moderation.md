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
