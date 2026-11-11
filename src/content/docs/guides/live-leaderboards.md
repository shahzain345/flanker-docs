---
title: Live leaderboards
description: Post the server's top chatters and voice members in a channel, as an image, an embed or a card, updated every minute.
---

A live leaderboard is a message that flanker keeps up to date in a channel.
It shows the top members by messages sent, by time in voice, or both. Each
leaderboard is **daily** (resets at midnight UTC), **weekly** (resets on
Monday) or **monthly** (resets on the 1st), and is redrawn every minute by
default. A server can have up to five.

Every leaderboard has one of three looks:

- **Image**: leaderboard pictures. This is the default.
- **Embed**: a classic embed showing the message you write.
- **Card**: a Components V2 card showing the same message.

## Set it up in Discord

Run `,liveboard` (Manage Server) to open the leaderboard panel. It shows
every leaderboard at a glance: **Messages** and **Voice time**, each daily,
weekly and monthly, with an **Edit** button (or **Set up** when it's not set).
Press it, then change the leaderboard with menus:

- **Channel**: pick a channel and it starts posting right away. Pick
  another to move it.
- **Look**: Image, Embed or Card.
- **Updates**: every minute up to every hour.
- **Members shown**: top 3 to top 15.
- **Edit message**: opens a box with the current message to edit. Clear it
  to go back to the default. Writing a message on an image turns it into an
  embed. **Variables** lists everything a message can show.
- **Stop posting**: removes the leaderboard and deletes its message, after
  you confirm.

Running `,liveboard message` without a message also opens the panel.

## Commands

```
,liveboard add #leaderboard daily embed
,liveboard style 1 card
,liveboard message 1 {embed}$v{title: Top chatters}$v{description: {user.first.emote} {user.first.mention} · {proper(user.first.message_count)}
{user.second.emote} {user.second.mention} · {proper(user.second.message_count)}
{user.third.emote} {user.third.mention} · {proper(user.third.message_count)}

Resets <t:{next_reset}:R>}
,liveboard message 1 reset
,liveboard variables
,liveboard edit 1 weekly 5m top 15
```

The number is the leaderboard's position in `,liveboard list`. The same
commands are under `/stats liveboard`, including `/stats liveboard variables`.

## Variables

Swap `first` for any rank up to `fifteenth`, or use a number, like
`{user.3.name}`. A line about a rank nobody holds yet is left out. Every
`{guild.*}` variable works too.

**Every leaderboard**

| Variable | Shows |
| --- | --- |
| `{user.first.name}` | Username |
| `{user.first.display_name}` | Server nickname or display name |
| `{user.first.id}` | User ID |
| `{user.first.mention}` | Mention (it never pings) |
| `{user.first.avatar}` | Avatar URL |
| `{user.first.emote}` | Rank medal: gold, silver, bronze, then numbers |
| `{user.first.rank}` | Rank number |
| `{user.first.count}`, `{proper(user.first.count)}` | Their count: messages or hours |
| `{user.first.share}` | Their share of the server total, like `12.5%` |
| `{last_reset}`, `{next_reset}`, `{updated}` | UNIX timestamps. Use them like `<t:{next_reset}:R>` |
| `{leaderboard.type}` | `messages` or `voice` |
| `{leaderboard.timeframe}` | `daily`, `weekly` or `monthly` |
| `{leaderboard.period}` | `Today`, `This week` or `This month` |
| `{leaderboard.title}` | Like `Top chatters · This week` |
| `{leaderboard.list}` | The whole ranking, one member per line |
| `{leaderboard.total}`, `{proper(leaderboard.total)}` | The server total |
| `{leaderboard.members}`, `{leaderboard.top}`, `{leaderboard.every}` | Members ranked, members shown, update interval |

**Message leaderboards**

| Variable | Shows |
| --- | --- |
| `{user.first.message_count}` | Messages, like `1234` |
| `{proper(user.first.message_count)}` | Messages, like `1,234` |

**Voice leaderboards**

| Variable | Shows |
| --- | --- |
| `{user.first.hour_count}` | Hours, like `12.5` |
| `{proper(user.first.hour_count)}` | Time, like `12h 30m` |
| `{user.first.minute_count}` | Minutes |

A leaderboard that shows both messages and voice draws the message once for
each. Lines that mention the other kind's counts are left out of each one.

## On the dashboard

Open **Live leaderboards** on the [dashboard](https://flanker.wtf/dashboard).
Each leaderboard has the same settings: channel, period, what it shows,
update interval, members shown and look. Pick **Embed** or **Card** to edit
its message in the message editor. Type `{` to insert a leaderboard variable.
The preview uses your server's real ranking.
