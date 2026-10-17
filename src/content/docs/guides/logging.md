---
title: Logging
description: Mirror server events into log channels, grouped by type.
---

flanker's logging mirrors server events into channels you choose, grouped by
event type so you can route each kind where it belongs.

## Event groups

Logging covers these groups, each routable to its own channel:

- **messages** (deletes, edits, bulk purges)
- **members** (joins, leaves, nickname and role changes)
- **roles**, **channels**, **invites**, **emojis**
- **voice** (joins, moves, leaves)
- **moderation** (actions taken through flanker)

## Setup

Configure logging with `,help logging`, or visually on the
[dashboard](https://flanker.wtf/dashboard). You pick a channel per event group,
and you can set a colour per channel and ignore specific users or channels.

## Bulk deletes

When more than five messages are purged at once, flanker attaches a full
`purged-messages.txt` transcript to the log, with each message's author (display
name and username), a timestamp and the content, so nothing is lost to a short
preview.

:::note
Only cached messages have their content; the count in the log is Discord's
reported total, which can be higher than the lines written.
:::
