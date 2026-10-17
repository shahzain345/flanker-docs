---
title: Stats commands
description: flanker stats commands, their syntax, permissions and examples.
sidebar:
  order: 9
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## stats

Activity cards: messages, voice time, top members and channels, as images.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Dashboard home

- **`stats`**  
  The server overview card.
- **`stats messages`**  
  Recent message activity, trends, top members and channels.
- **`stats voice`**  
  Voice activity in detail.
- **`stats user (member)`**  
  One member's activity.
- **`stats channel (#channel)`**  
  One channel's activity.
- **`stats lookback (days)`**  
  How far back cards look by default.
  *Manage Server*
- **`stats filter (channel/member/role/onlyrole) (target)`**  
  Leaves channels, members or roles out of stats.
  *Manage Server*

## top

Leaderboards for messages and voice.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Dashboard home

- **`top [members/voice/channels/voicechannels]`**  
  Shows a leaderboard card.

## me

Your own activity card.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Dashboard home

- **`me`**  
  Shows your messages and voice time.

## chart

Activity charts over time.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Dashboard home

- **`chart [messages/voice/members]`**  
  Shows a chart.
  example: `chart voice`
