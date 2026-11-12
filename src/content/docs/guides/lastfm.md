---
title: Last.fm
description: Connect an account, browse listening cards and control voice scrobbling.
---

Last.fm commands use your linked Last.fm account. Link a public username for read-only statistics, or authorize your account for actions that change it.

## Connect your account

```text
/lastfm set your-lastfm-name
```

This links public statistics only. For love actions or voice scrobbling, use:

```text
/lastfm login
```

Open the private approval link and authorize Flanker on Last.fm. Never send your Last.fm password to the bot or another member. A public username link is not the same as authorization.

## Choose a listening view

| Command | What it shows |
| --- | --- |
| `/lastfm np` | Current or most recent track. |
| `/lastfm recent` | Recent plays and their times. |
| `/lastfm topartists` | Top artists in the selected period. |
| `/lastfm toptracks` | Top tracks. |
| `/lastfm topalbums` | Top albums. |
| `/lastfm profile` | Account details and totals. |

Recent and top-list commands use Flanker’s information-image design when rendering is available. Other commands stay compact. Top-list periods include `7d`, `1m`, `3m`, `6m`, `1y` and `overall`; see the [full syntax](/commands/integrations/#lastfm) for argument order and member lookups.

## Voice scrobbling

```text
/lastfm scrobble on
/lastfm scrobble off
```

Scrobbling requires account authorization and an explicit opt-in. Seeking, paused playback and deafened periods do not count as listening. Turning it off stops this integration’s voice scrobbling; it does not delete tracks already recorded on Last.fm.

## Rankings and comparisons

Whoknows views compare linked members and report coverage, including unavailable accounts. They inspect up to 60 linked members, so the result is not a guaranteed ranking of everyone in the server. Taste compares normalized artist listening shares, not Last.fm’s own compatibility score.

## Disconnect

`/lastfm logout` deletes your linked account and session from Flanker and cancels pending approval links. See [all Last.fm commands](/commands/integrations/#lastfm) for love, artist, album, track and comparison actions.
