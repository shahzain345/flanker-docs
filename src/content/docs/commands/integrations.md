---
title: Integrations commands
description: flanker integrations commands, their syntax, permissions and examples.
sidebar:
  order: 10
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## lastfm

Last.fm: now playing, top artists and who knows an artist in this server.

**Permission:** Anyone

- **`lastfm login`**  
  Links your Last.fm account.
- **`lastfm set (username)`**  
  Links a username without logging in.
- **`lastfm np`**  
  What you're playing.
- **`lastfm recent`**  
  Your recent plays.
- **`lastfm topartists [period]`**  
  Your top artists.
- **`lastfm toptracks [period]`**  
  Your top tracks.
- **`lastfm whoknows (artist)`**  
  Who listens to an artist the most here.
- **`lastfm logout`**  
  Unlinks your account.

## fm

Shortcut for lastfm now playing.

**Permission:** Anyone

- **`fm [member]`**  
  Shows what someone is playing on Last.fm.

## spotify

Control your own Spotify from Discord.

**Permission:** Anyone

- **`spotify login`**  
  Links your Spotify account.
- **`spotify`**  
  What you're playing.
- **`spotify play (song)`**  
  Plays a song on your device.
- **`spotify (pause/resume/next/previous)`**  
  Playback controls.
- **`spotify volume (0-100)`**  
  Your device volume.
- **`spotify device (name)`**  
  Switches device.
- **`spotify logout`**  
  Unlinks your account.

## fortnite

Fortnite item shop and cosmetics.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Notifications

- **`fortnite shop`**  
  Today's item shop.
- **`fortnite item (cosmetic)`**  
  Looks up a cosmetic.
- **`fortnite watch (cosmetic)`**  
  DMs you when it's in the shop.
- **`fortnite shop channel (channel)`**  
  Posts the shop every day.
  *Manage Server*
- **`fortnite shop ping (role/off)`**  
  Pings a role with the shop.
  *Manage Server*
- **`fortnite shop voting (on/off)`**  
  Vote reactions on shop posts.
  *Manage Server*

## youtube

Posts new videos from YouTube channels.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Notifications

- **`youtube add (channel) (youtube channel)`**  
  Starts posting.
  *Manage Server*  ·  example: `youtube add #videos @MrBeast`
- **`youtube remove (channel) (youtube channel)`**  
  Stops.
  *Manage Server*
- **`youtube message (youtube channel) (message/clear) [--pingable on/off]`**  
  The announcement message.
  *Manage Server*
- **`youtube list [page]`**  
  Pages through subscriptions and delivery channels.
  *Manage Server*

## twitch

Announces when Twitch streamers go live.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Notifications

- **`twitch add (channel) (streamer)`**  
  Starts announcing.
  *Manage Server*
- **`twitch remove (channel) (streamer)`**  
  Stops.
  *Manage Server*
- **`twitch message (streamer) (message/clear) [--pingable on/off]`**  
  The announcement message.
  *Manage Server*
- **`twitch list [page]`**  
  Pages through subscriptions and delivery channels.
  *Manage Server*

## kickstream

Announces when Kick streamers go live.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Notifications

- **`kickstream add (channel) (streamer)`**  
  Starts announcing.
  *Manage Server*
- **`kickstream remove (channel) (streamer)`**  
  Stops.
  *Manage Server*
- **`kickstream message (streamer) (message/clear) [--pingable on/off]`**  
  The announcement message.
  *Manage Server*
- **`kickstream list [page]`**  
  Pages through subscriptions and delivery channels.
  *Manage Server*

## reddit

Posts new posts from subreddits.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Notifications

- **`reddit add (channel) (subreddit)`**  
  Starts posting. NSFW posts only go to age-restricted channels.
  *Manage Server*
- **`reddit remove (channel) (subreddit)`**  
  Stops.
  *Manage Server*
- **`reddit message (subreddit) (message/clear) [--pingable on/off]`**  
  The announcement message.
  *Manage Server*
- **`reddit list [page]`**  
  Pages through subscriptions and delivery channels.
  *Manage Server*

## soundcloud

Posts new SoundCloud uploads.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Notifications

- **`soundcloud add (channel) (artist)`**  
  Starts posting.
  *Manage Server*
- **`soundcloud remove (channel) (artist)`**  
  Stops.
  *Manage Server*
- **`soundcloud message (artist) (message/clear) [--pingable on/off]`**  
  The announcement message.
  *Manage Server*
- **`soundcloud list [page]`**  
  Pages through subscriptions and delivery channels.
  *Manage Server*

## pinterest

Posts new Pinterest pins.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Notifications

- **`pinterest add (channel) (user or board)`**  
  Starts posting.
  *Manage Server*
- **`pinterest remove (channel) (user or board)`**  
  Stops.
  *Manage Server*
- **`pinterest embeds (channel) (yes/no)`**  
  Post as embeds or plain links.
  *Manage Server*
- **`pinterest list [page]`**  
  Pages through subscriptions and delivery channels.
  *Manage Server*
