---
title: Valorant LFG
description: Set up a Valorant board and find a duo, trio or five-stack.
---

Valorant LFG is available to every server with flanker. There is no early-access grant to request.

## Set up the board

A manager with Manage Server runs `,lfg setup #valorant-lfg`. This posts a panel with Find teammates, Browse and Notifications. `,lfg panel` replaces the panel when needed.

LFG supports Valorant only. Existing Minecraft, Roblox and Fortnite profile commands remain separate. Squad threads, game selection and game-routing commands have been removed.

## Create a party

Click Find teammates or run `,lfg`. The form asks for:

- **Mode:** Competitive, Unrated, Swiftplay, Spike Rush, Deathmatch, Team Deathmatch or Custom.
- **Server:** for example Mumbai, Singapore, Frankfurt, EU or NA.
- **Desired ranks:** Gold, Gold-Platinum, Diamond+ or Any. Rank artwork shows the requested family or range, including all divisions of those families.
- **Party size:** players already together / total party size. `4/5` reserves three places for friends already with the host and leaves one opening; `1/2` finds a duo partner. A plain `2` also means `1/2`.
- **Party code:** your Valorant party code, shown privately after someone joins.
- **Note:** a short message or mic/language preference.

The post shows LF1 or the number of openings, mode, host, party count, server and desired-rank images. Desired ranks are entered manually. There is no Riot login, account linking or automatic rank check.

After a party is posted, flanker replaces the Find teammates panel beneath it so members can reach the form without scrolling up. Join, Leave and Players stay on the party post. Joining displays the submitted party code privately; older posts without a code say that the host has not added one. Only the host can open **Manage**, which shows private controls to start, extend, close or attach their current voice channel. Use my VC keeps the channel's existing permissions. VoiceMaster rooms work as existing voice channels.

Competitive party targets are 2, 3 or 5; other normal modes allow up to 5, and Custom allows up to 10. A party must have an open place when posted. The count includes the host and any manually reserved friends. Players lists Discord members who joined and separately notes reserved friends.

## Limits and expiry

One active party per member per server, 20 active parties per server and one post per host every 10 minutes. Posts expire after 30 minutes. Starting closes new joins and starts a fresh 30-minute timer; the host can extend once. Records survive restarts and are removed after seven days. Unsubmitted forms expire after ten minutes or restart; private Manage menus expire after five minutes.

`lfg browse` shows the newest ten open Valorant parties. Old multi-game panels are refreshed at bot startup, and unsupported game posts are retired. Existing public squad threads are archived when their old group ends; new threads are never created by LFG.

## Notifications

Use `,lfg notify on` or `,lfg notify off`. `,lfg notify valorant on/off` is also accepted. Notifications are opt-in DMs, limited to one per member every 15 minutes with at most 50 eligible subscribers checked per post. Closed DMs may prevent delivery. No roles are granted and no everyone ping is sent.
