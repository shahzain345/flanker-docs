---
title: VoiceMaster
description: Temporary voice channels members create and control themselves.
---

VoiceMaster gives members a "Join to Create" channel. When someone joins it,
flanker makes them a personal temporary voice channel and gives them control of
it. The channel is deleted automatically when it empties.

## Set it up

1. Run `,voicemaster` to create the Join to Create channel and its category.
2. Members join it to get their own room.
3. Owners control their room with the VoiceMaster panel: rename, set a user
   limit, lock or hide it, and allow or reject specific people.

See the [VoiceMaster commands](/commands/voicemaster-tickets-applications/) for
every option.

## On the dashboard

Open the [dashboard](https://flanker.wtf/dashboard), choose your server, and go
to **VoiceMaster**. There you can:

- Pick the Join to Create channel and the category new rooms are made under.
- Set defaults for new rooms (name template, user limit, region).
- Add more than one Join to Create channel, each with its own settings.

Changes on the dashboard apply immediately, the same as the commands.
