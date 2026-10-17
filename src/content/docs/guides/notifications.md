---
title: Social notifications
description: Announce new posts and live streams from other platforms.
---

flanker can watch creators on other platforms and post in your server when they
go live or publish something new.

## Supported platforms

- **Twitch** and **Kick** live streams
- **YouTube** uploads
- **Reddit** posts
- **SoundCloud** releases
- **Pinterest** pins
- **Fortnite** data

Set each up with its command (`,twitch`, `,youtube`, `,kickstream`, `,reddit`,
`,soundcloud`, `,pinterest`, `,fortnite`). See the
[Integrations commands](/commands/integrations/).

## On the dashboard

Open the [dashboard](https://flanker.wtf/dashboard), pick your server, and go to
**Notifications**. For each platform you can:

- Add the creators or feeds to watch.
- Choose the channel the announcement is posted in.
- Customise the announcement message with [variables and scripting](/resources/scripting/).

:::note
Some platforms are rate-limited by their own APIs, so there can be a short delay
between a post going live and the announcement appearing.
:::
