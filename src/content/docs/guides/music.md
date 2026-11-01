---
title: Music
description: Play music, manage a queue and configure DJs, autoplay and 24/7 mode.
---

Use `,play` with a search or supported track link to start playback in your voice channel. See the [Music command reference](/commands/music/) for the current controls and syntax.

## Player and queue

Use pause, resume, skip, repeat and shuffle from Discord, or open **Music** on your server dashboard for artwork, progress, playback controls, volume and queue management. The dashboard supports removing and moving queued tracks as well as clearing the queue. Control access follows the server's music permissions and DJ configuration.

## Autoplay and 24/7

`,music 247 on` enables staying in empty voice channels and autoplaying similar tracks. `,247 on` and `,settings 247 on` are aliases. Use the corresponding `off` command to disable 24/7 mode. These settings require Manage Server and can also be changed in the dashboard's Music section.

Autoplay uses available recommendations and playable tracks. It cannot guarantee that every recommendation or source remains available. 24/7 mode allows an empty channel; it does not promise uninterrupted playback during outages or bot restarts.

## DJ settings

Configure the DJ role and playback preferences under **Music** on the dashboard. Real server permissions still apply. A public landing-page player preview is separate from your server and cannot control its music.

## Last.fm

Link Last.fm with `,lastfm login` and approve Flanker through its private DM link. Your password stays on Last.fm. `,lastfm set username` supports read-only public stats without authorization. The bot operator must configure Last.fm API credentials before these commands can contact Last.fm.

Use `,fm` for your current or last-played track, or `,fm @member` for someone else's linked profile. `,lastfm recent`, `topartists`, `toptracks`, `topalbums` and `profile` accept a member. Top lists support `7d`, `1m`, `3m`, `6m`, `1y` and `overall`.

`artist`, `track` and `album` show statistics for your current track. Search explicitly with `,lastfm artist find Radiohead`, `,lastfm track find Radiohead | Creep`, or `,lastfm album find Radiohead | OK Computer`. `,lastfm taste @member 1m` compares normalized listening shares among both accounts' top 100 artists. Its overlap percentage is calculated by Flanker and is not Last.fm's compatibility score.

`whoknows`, `whoknowstrack` and `whoknowsalbum` compare live play counts among up to 60 linked server members. Every result states its coverage and unavailable profiles. This is a bounded live comparison, not .fmbot's full-server indexed library or crown system. The `find` variants accept an artist and track/album separated by `|`.

Authorized accounts can use `,lastfm love` and `,lastfm unlove` for their current track, or `love find artist | track` for a specific track. `,lastfm loved` lists loved tracks.

### Voice scrobbling

New authorizations start with voice scrobbling off. Enable it explicitly with `,lastfm scrobble on`; pause it with `,lastfm scrobble off`. Listening outside Flanker is recorded by your own player or Last.fm scrobbler.

Flanker records a voice play only for an eligible track longer than 30 seconds and after enough observed listening: half the track or four minutes, whichever is shorter. Pauses, deafened samples, time before joining, and skipped playback from seeking do not count. Sampling may conservatively miss a few seconds around transitions or connection gaps. Live streams do not scrobble. Track estimates stay in memory until the track ends or the bot restarts.

`,lastfm logout` deletes your linked account/session and cancels pending approval links. Reconnecting through a new approval starts voice scrobbling off again. Existing authorized accounts retain their prior scrobbling behavior until changed. Slash equivalents use typed member pickers, period choices and Boolean switches, with direct interaction replies.
