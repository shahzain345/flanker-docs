---
title: Leveling
description: Reward activity with text and voice levels, roles and rank cards.
---

flanker awards members XP for chatting and for spending time in voice, with
level-up messages, role rewards and rank cards.

## Text leveling

Members earn XP for messages (rate-limited so spam does not help). As they level
up, flanker can announce it and grant role rewards. See the leveling commands in
the [Logging, invites, levels reference](/commands/logging-invites-levels/).

## Voice leveling

Time spent in voice earns XP too, tracked separately from text. Configure it
with the voice commands (`,voicelevel`).

## Rank and leaderboard

- Members can check their rank card to see their level and progress.
- A server leaderboard shows the most active members.

## On the dashboard

- **Voice leveling** lives under the [dashboard](https://flanker.wtf/dashboard)
  **Voice** section: enable it, set the XP rate and role rewards.
- Level role rewards and the level-up message are configured alongside the
  leveling settings. Open the dashboard, pick your server, and look for the
  leveling options.

## Move from another leveling bot

Configure flanker's reward roles with the levels they already represent, for example `,levels add @Level50 50`. Members holding a configured reward role are adopted at that role's level when leveling imports their existing roles. The highest matching configured level is used as a starting floor rather than resetting them to zero; existing higher XP is preserved.

This imports the levels represented by those Discord roles, not another bot's private XP totals or progress within a level. Text leveling and voice leveling remain separate. Check your role-to-level mappings before enabling rewards.
