---
title: Variables
description: Dynamic placeholders you can use in any flanker message or embed.
sidebar:
  order: 2
---

Variables are `{dotted.key}` placeholders that flanker replaces with live data
when a message is sent. Use them anywhere you customise a message: welcome and
leave messages, embeds, autoresponders, tags, boost messages and more.

For example, a welcome message of:

```text
Welcome {user.mention} to {guild.name}! You are member #{guild.count}.
```

is sent as `Welcome @name to My Server! You are member #1234.`

## Member

| Variable | Value |
| --- | --- |
| `{user.mention}` | Mentions the member |
| `{user.name}` | Username |
| `{user.tag}` | Username with discriminator/handle |
| `{user.id}` | User ID |
| `{user.avatar}` | Avatar image URL |
| `{user.color}` | The member's top role colour |
| `{user.boost}` | Whether the member is boosting |
| `{user.bot}` | Whether the member is a bot |
| `{user.badges}` | The member's profile badges |

## Server

| Variable | Value |
| --- | --- |
| `{guild.name}` | Server name |
| `{guild.id}` | Server ID |
| `{guild.count}` | Member count |
| `{guild.icon}` | Server icon URL |
| `{guild.banner}` | Server banner URL |
| `{guild.splash}` | Invite splash URL |
| `{guild.vanity}` | Vanity invite code |
| `{guild.region}` | Voice region |
| `{guild.channels}` | Channel count |
| `{guild.discovery}` | Whether discovery is enabled |
| `{guild.shard}` | The shard the server is on |

## Channel

| Variable | Value |
| --- | --- |
| `{channel.name}` | Channel name |
| `{channel.mention}` | Mentions the channel |
| `{channel.id}` | Channel ID |
| `{channel.topic}` | Channel topic |
| `{channel.type}` | Channel type |
| `{channel.position}` | Channel position |

## Time

| Variable | Value |
| --- | --- |
| `{date.now}` | Current date |
| `{time.now}` | Current time |

:::note
A token with a space or colon, like `{title: ...}`, is a
[script token](/resources/scripting/), not a variable, and is left alone.
Variables are always a single dotted key with no spaces.
:::
