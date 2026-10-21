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

## active

A live image of the five busiest voice channels and the five busiest text channels, posted in a channel and updated by itself every minute. Voice channels show who is in them (their avatars and how many). Text channels show messages per minute over the last 10 minutes. Members and channels hidden with `stats filter` are left out, and bots don't count. One per server. Also `activenow` and `busiest`.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** /liveboards

- **`active`**  
  Shows where the card is posted.
  *Manage Server*
- **`active set (#channel)`**  
  Posts the card there and keeps it updated every minute. Running it again with another channel moves it.
  *Manage Server*  ·  example: `active set #activity`
- **`active remove`**  
  Stops it and deletes the post.
  *Manage Server*
- **`active refresh`**  
  Updates it now.
  *Manage Server*

## chart

Activity charts over time.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Dashboard home

- **`chart [messages/voice/members]`**  
  Shows a chart.
  example: `chart voice`

## servercopy

flanker admins only, and only in a server a flanker admin owns: wipes this server and copies another server's roles, channels, permissions and flanker settings into it, for test servers. Members and bots stay.

**Permission:** flanker staff

- **`servercopy (source server id)`**  
  Asks to confirm, then copies. The report comes by DM.
  *flanker staff*  ·  example: `servercopy 1550802110260580503`
- **`servercopy cleanup`**  
  Clears the backup owner, antinuke admins, whitelist, approved bots and protected users here (people are never copied, this tidies up older copies).
  *flanker staff*

## liveboard

Live leaderboards: images of the top members by messages and by voice time, posted together in a channel and updated by itself every minute (or every few minutes). Server managers choose the period for each board: daily (resets at midnight UTC), weekly (resets on Monday) or monthly (resets on the 1st). Run one board per period to show all three. Also `liveleaderboard`.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** /liveboards

- **`liveboard add (#channel) [daily/weekly/monthly] [both/messages/voice] [1m/5m/10m/15m/30m/60m] [top N]`**  
  Posts a live leaderboard (up to 5 per server). Pick daily, weekly or monthly. Defaults: weekly, both messages and voice, every minute, top 10.
  *Manage Server*  ·  example: `liveboard add #leaderboard daily 1m top 10`
- **`liveboard edit (number) [daily/weekly/monthly] [both/messages/voice] [1m-60m] [top N] [#channel]`**  
  Changes a board in place, including its period (daily, weekly or monthly). A new channel moves it there.
  *Manage Server*  ·  example: `liveboard edit 1 monthly`
- **`liveboard list`**  
  Lists this server's live leaderboards.
  *Manage Server*
- **`liveboard remove (number or #channel)`**  
  Removes one and deletes its message.
  *Manage Server*
- **`liveboard refresh`**  
  Updates every live leaderboard now.
  *Manage Server*

## stafftasks

Staff tasks: message, voice and invite targets for each staff role, worth points. A live progress board updates in place, a final report is posted at every reset and finished periods are kept. Set it up on the dashboard. Also `quota`, `staffpoints`.

**Permission:** Anyone

- **`stafftasks [@member]`**  
  Your progress this period, or a member's.
- **`stafftasks points`**  
  All-time staff points from finished periods.
- **`stafftasks history`**  
  The last 10 periods with links to their reports.
- **`stafftasks refresh`**  
  Updates the requirements post and the progress board now.
  *Manage Server*
- **`stafftasks end`**  
  Ends the period now: posts the report and starts again from zero.
  *Manage Server*
- **`stafftasks on/off`**  
  Turns tracking on or off. Turning it on starts a new period.
  *Manage Server*
