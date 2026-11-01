---
title: Minecraft bridge
description: Connect Paper SMP chat and announced advancements to Discord without sharing a bot token.
---

FlankerBridge relays Minecraft chat and announced advancements into dedicated Discord channels. This release supports **Paper 1.21.11 and Java 21**. Players install nothing. Vanilla, Bedrock and modded servers are not supported by this release.

## Install and pair

1. Download [FlankerBridge.jar](https://flanker.wtf/minecraft) and put it in your Minecraft server's `plugins` folder using your hosting panel or SFTP. Restart the Minecraft server.
2. With Manage Server permissions, run `,minecraft chat play.example.com:25565 #smp-chat` in Discord. Flanker needs View Channel, Send Messages and Embed Links in that destination.
3. Flanker DMs you a private one-time pairing command. Paste it into the local Minecraft host console, without a leading slash. It expires after ten minutes. Pairing is not accepted from player chat or RCON. Enable DMs if the code cannot arrive.
4. Optionally run `,minecraft achievements play.example.com:25565 #achievements` for a separate advancement channel.

Use your actual address and channels. The address identifies the connection; flanker does not log into the SMP. The plugin makes outbound HTTPS requests, so no extra inbound port is needed. Up to three connections are supported per Discord server.

## Credentials and direction

The plugin never receives flanker's Discord bot token. Pairing creates a separate revocable credential in the plugin's `config.yml`; keep that file private. This release relays Minecraft to Discord only. It does not execute game commands or send Discord messages back into Minecraft. Recipe unlocks and advancements that do not announce to chat are skipped.

## Manage a connection

- `,minecraftlink status` shows connections and selected channels.
- Repeat the chat or achievements command to change a channel.
- `,minecraftlink pair play.example.com:25565` revokes the old credential and DMs a fresh code.
- `,minecraftlink disconnect play.example.com:25565` revokes the connection immediately. Run `flanker unlink` in the local Minecraft console to remove its local credential too.
- `,help minecraftlink` shows the setup instructions in Discord.

If messages are missing, check `flanker status` in the Minecraft console, the Discord connection status, destination permissions and channel filters. Mentions are disabled. Delivery uses bounded queues and may drop messages during downtime or overload; it is a live relay, not a chat backup.
