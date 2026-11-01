---
title: Security overview
description: Choose the protection that matches the problem, then follow a complete setup guide.
---

Flanker separates destructive server actions, coordinated raids and trap-channel detection. Configure each feature for its purpose. Discord permissions and role hierarchy still limit what any bot can do.

## Choose a setup guide

| Feature | What it handles | Start here |
| --- | --- | --- |
| Antinuke | Destructive moderation, role, channel and permission actions. | [Set up antinuke](/guides/antinuke/) |
| Antiraid | Join waves, coordinated chat activity and resource bursts. | [Set up antiraid](/guides/antiraid/) |
| Honeypot | Accounts that post in a clearly marked trap channel. | [Set up honeypot](/guides/honeypot/) |
| Filters | Content rules, words, links and configured spam checks. | [Security commands](/commands/security/#filter) |

## Access matters

Initial antinuke setup is owner-only. Supported security settings use actual owner, antinuke-admin or real Discord permission checks. Fake permissions never unlock security settings, and ordinary Flanker Admin status does not grant antinuke configuration access.

Keep Flanker’s role above roles and members it must manage. Give it access to its alert and log channels. Read specific missing-permission errors rather than repeatedly retrying an action that Discord is rejecting.

## Understand recovery before an incident

**Panic mode** belongs to antinuke. It pauses dangerous role permissions and bulk work. The owner ends it, with backup-owner approval when configured. Failed role restoration is reported and saved for a later retry; it does not keep panic active indefinitely. See [panic recovery](/guides/antinuke/#5-understand-panic-mode).

**Raid mode** belongs to antiraid. It can restrict channel access and hold suspicious members for verification. Staff review held members and use antiraid recovery to reopen access. See [raid recovery](/guides/antiraid/#4-review-members-and-end-raid-mode).

**Reset** is different from recovery. Antinuke and antiraid resets clear settings and are owner-only commands. Team site admins have a separate dashboard exception. Do not reset protection merely to dismiss an unexplained error.

## Role-grant safety

Autoroles, button and reaction roles, custom commands and bulk role tools cannot grant dangerous permissions. The direct single-member role-command exception is restricted to the owner, backup owner and antinuke admins, subject to hierarchy and other checks. Ordinary staff and fake permissions do not unlock it.

For individual options, see the [complete security reference](/commands/security/) and [moderation guide](/guides/moderation/).
