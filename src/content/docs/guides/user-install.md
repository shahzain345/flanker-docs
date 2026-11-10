---
title: Add Flanker to your profile
description: Use personal slash commands and understand how profile installation differs from server installation.
---

A profile installation lets you use supported Flanker application commands in Discord contexts that allow external apps. It does not install server protection, grant permissions or give you moderation access.

## Install and find a command

1. Open Flanker’s Discord application profile and choose its profile-install option.
2. Authorize it for your account.
3. Type `/` in a supported channel or direct message, then select Flanker.
4. Choose a command and fill Discord’s typed fields. Required fields must be supplied before Discord sends the command.

Discord and server settings can restrict external application commands. If the command picker is unavailable, check that context’s app permissions and whether you completed profile installation.

## What you can use

Supported personal roots include **afk**, **quote**, **media**, **math**, **convert**, **repost**, **Last.fm**, **family**, **skin**, **games** and **tools**, alongside help and profile lookups. Related actions sit together in feature groups, such as `/family pets list` and `/games chess`. Use the picker’s available subcommands rather than guessing prefix syntax in a slash field.

### AFK across your servers

Run `/afk reason:studying` in a DM or group chat through My Apps. Flanker remembers your AFK status across every server where it is installed, including after a bot restart. People who mention you or reply to your messages there see your reason.

Your next regular message in any Flanker server ends global AFK everywhere, after a five-second grace period. Commands and system messages do not end it. You can also run `/afk clear:true` in a DM or group chat; leave the reason empty when clearing. Flanker does not monitor your ordinary DM conversations to decide when you return.

AFK set directly in a server stays local to that server unless global AFK is already active. While global AFK is active, another AFK command updates its global reason. Starting global AFK replaces older server statuses. Welcome-back replies show only pings from the server you returned in, keeping other servers’ channel links private.

### Quotes and media edits

Use `/quote text:your words` to make a quote in a DM or group chat. The optional author picker changes its attribution; supplied text is not retrieved or verified against a message. Font, layout, colour, light theme, avatar side, bold text and watermark options remain available, with controls that only the person who ran the command can use.

Discord does not give a profile-installed app your private conversation history. Use the text field when Flanker cannot read the source message. Message IDs and links only work in a conversation Flanker can access, and private lookups stay in the conversation where you ran the command. Links to another server or DM do not grant access.

For `/media caption`, fill in text and attach a file, supply an image URL or choose a member's avatar. Other actions use the same source fields. With no source, media tools use your avatar. Captions keep links in their text; select the source image separately. Commands cannot inherit a Discord reply target.

| Effect | My Apps command |
| --- | --- |
| Caption | `/media caption` |
| Liquid distortion | `/media magik` |
| Explode or implode | `/media distort action:bulge` or `action:pinch` |
| Swirl | `/media distort action:swirl` |
| Deep fry, JPEG compression or pixelation | `/media deepfry`, `/media jpeg`, `/media pixelate` |
| Flip or mirror | `/media orientation` |
| Grayscale, invert, blur or reverse | `/media effects` |
| Rotate, widen or sepia | `/media rotate`, `/media wide`, `/media sepia` |
| GIF conversion, spin or playback speed | `/media gif`, `/media spin`, `/media speed` |

Some effects require a still image; reverse and speed require a GIF or video. File limits still apply. Only a small number of edits run at once, and unusually slow files may need to be shortened or reduced.

The [typed slash reference](/guides/slash-commands/) shows actual command paths, required fields and whether each route supports profile installation. A prefix alias is not necessarily a slash-command name.

## What still needs a server installation

Antinuke, antiraid, moderation, tickets, logging and other server configuration need the server context and their normal permissions. Installing Flanker on your profile does not bypass owner checks, hierarchy, command access or security settings.

## Privacy and responses

A profile-installed command is not automatically private. Discord shows whether a particular response is visible only to you; ordinary public replies remain visible in the channel. Interactive features may restrict controls to the person who opened them or the intended participant.

See [Last.fm](/guides/lastfm/), [friendships and gifts](/guides/social/) and the [full command index](/commands/) for the available features.
