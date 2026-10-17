---
title: Music commands
description: flanker music commands, their syntax, permissions and examples.
sidebar:
  order: 11
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## play

Plays music from YouTube, SoundCloud, Spotify, Apple Music and more in your voice channel.

**Permission:** DJ role if set

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Music

- **`play (song or link)`**  
  Plays or queues a song, album or playlist.
  *DJ role if set*  ·  example: `play never gonna give you up`

## queue

The music queue.

**Permission:** DJ role if set

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Music

- **`queue`**  
  Shows the queue.
- **`queue remove (position)`**  
  Removes a track.
  *DJ role if set*
- **`queue move (position) (new position)`**  
  Moves a track.
  *DJ role if set*
- **`queue clear`**  
  Empties the queue.
  *DJ role if set*

## skip

Skips the current track.

**Permission:** DJ role if set

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Music

- **`skip`**  
  Plays the next track.
  *DJ role if set*

## pause

Pauses the music.

**Permission:** DJ role if set

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Music

- **`pause`**  
  Pauses.
  *DJ role if set*

## resume

Resumes the music.

**Permission:** DJ role if set

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Music

- **`resume`**  
  Resumes.
  *DJ role if set*

## seek

Jumps to a time in the track.

**Permission:** DJ role if set

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Music

- **`seek (mm:ss)`**  
  Jumps to that time.
  *DJ role if set*  ·  example: `seek 1:30`

## volume

Changes the volume.

**Permission:** DJ role if set

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Music

- **`volume (0-200)`**  
  Sets the volume.
  *DJ role if set*  ·  example: `volume 80`

## repeat

Repeats the track or the queue.

**Permission:** DJ role if set

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Music

- **`repeat (off/queue/current)`**  
  Sets repeat.
  *DJ role if set*

## shuffle

Shuffles the queue.

**Permission:** DJ role if set

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Music

- **`shuffle`**  
  Shuffles.
  *DJ role if set*

## stop

Stops the music and leaves the channel.

**Permission:** DJ role if set

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Music

- **`stop`**  
  Stops and clears the queue.
  *DJ role if set*

## nowplaying

What's playing now.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Music

- **`nowplaying`**  
  Shows the track, progress and controls.

## preset

Sound presets like nightcore or bass boost.

**Permission:** DJ role if set

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Music

- **`preset (name/off)`**  
  Applies a preset.
  *DJ role if set*  ·  example: `preset nightcore`
- **`preset list`**  
  Lists presets.

## music

Music settings.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Music

- **`music`**  
  Shows the DJ role and autoplay. Change them with settings dj and settings autoplay.
  *Manage Server*
