---
title: Logging, invites, levels commands
description: flanker logging, invites, levels commands, their syntax, permissions and examples.
sidebar:
  order: 7
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## log

Server logs: deleted and edited messages, joins and leaves, role, channel, invite, emoji and voice changes, and moderation done outside flanker.

**Permission:** Manage Server (real)

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Moderation → Logs

- **`log setup`**  
  Creates a private logs category with a channel for each kind of event.
  *Manage Server (real)*
- **`log add (channel) [event]`**  
  Sends an event (or every event) to a channel. Events: messages, members, roles, channels, invites, emojis, voice, moderation.
  *Manage Server (real)*  ·  example: `log add #mod-logs messages`
- **`log remove (channel) [event]`**  
  Stops logging to a channel.
  *Manage Server (real)*
- **`log color (channel) (event) (hex)`**  
  The embed colour for an event.
  *Manage Server (real)*
- **`log ignore (member/channel/category)`**  
  Nothing from them gets logged.
  *Manage Server (real)*
- **`log reset`**  
  Turns every log off.
  *Manage Server (real)*

## invites

Tracks who invited whom, with fake invite checks and rewards for inviters.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Invites

- **`invites enable`**  
  Syncs current invite codes and starts tracking joins.
  *Manage Server*
- **`invites disable`**  
  Stops tracking new joins.
  *Manage Server*
- **`invites [member]`**  
  Shows a member's invites: joins, leaves, fakes and bonus.
- **`invites leaderboard`**  
  The top inviters.
- **`invites leaderboardrename (title)`**  
  Changes the leaderboard title.
  *Manage Server*
- **`invites add (member) [amount]`**  
  Gives bonus invites.
  *Manage Server*
- **`invites remove (member) [amount]`**  
  Takes invites away.
  *Manage Server*
- **`invites roles add (role) (invites)`**  
  A role for reaching an invite count.
  *Manage Server*  ·  example: `invites roles add @Recruiter 10`
- **`invites roles remove (invites)`**  
  Removes a reward.
  *Manage Server*
- **`invites requiredage (days)`**  
  Invites from accounts younger than this count as fake.
  *Manage Server*
- **`invites requiredroles [roles]`**  
  Invites stay fake until the member has every listed role. Run without roles to clear.
  *Manage Server*
- **`invites tracker (channel)`**  
  Posts who invited each new member.
  *Manage Server*
- **`invites tracker remove`**  
  Stops posting join and leave notices.
  *Manage Server*
- **`invites bypass (member)`**  
  Their invites never count as fake.
  *Manage Server*
- **`invites create [channel]`**  
  Creates a new invite in a channel you can access.
- **`invites config`**  
  Shows the current tracker, fake checks and rewards.

## inviter

Shows who invited a member.

**Permission:** Anyone

- **`inviter [member]`**  
  Shows the inviter and the invite used.

## invited

Shows who a member invited.

**Permission:** Anyone

- **`invited [member]`**  
  Lists the members they invited.

## invitecodes

Shows a member's invite links.

**Permission:** Anyone

- **`invitecodes [member]`**  
  Lists their invite codes and uses.

## levels

Chat levels: members earn XP for talking and get roles as they level up.

**Permission:** Anyone

- **`levels [member]`**  
  Shows a member's level and XP.
- **`levels leaderboard`**  
  The highest levels.
- **`levels enable`**  
  Turns leveling on.
  *Manage Server*
- **`levels disable`**  
  Turns it off.
  *Manage Server*
- **`levels add (role) (rank)`**  
  A role for reaching a level.
  *Manage Server*  ·  example: `levels add @Active 10`
- **`levels remove (rank)`**  
  Removes a level role.
  *Manage Server*
- **`levels stackroles (on/off)`**  
  Keep lower level roles when getting a new one.
  *Manage Server*
- **`levels setrate (multiplier > 0)`**  
  Changes how fast XP is earned.
  *Manage Server*
- **`levels message (text)`**  
  The level up message. Design it on the dashboard's Leveling page.
  *Manage Server*
- **`levels message reset`**  
  Back to the default level up message.
  *Manage Server*
- **`levels message view`**  
  Shows the level up message.
  *Manage Server*
- **`levels messages (on/off)`**  
  Turns your own level up messages on or off.
- **`levels messagemode (pm/context/none/channel)`**  
  Where level up messages go.
  *Manage Server*
- **`levels ignore (channel/category/role)`**  
  No XP there or for that role.
  *Manage Server*
- **`levels crownboard (channel or off)`**  
  A live leaderboard channel.
  *Manage Server*
- **`levels reset`**  
  Resets everyone's XP.
  *Manage Server*

## setxp

Sets a member's chat XP.

**Permission:** Manage Server

- **`setxp (member) (amount)`**  
  Sets their XP.
  *Manage Server*  ·  example: `setxp @member 5000`

## removexp

Takes chat XP away.

**Permission:** Manage Server

- **`removexp (member) (amount)`**  
  Removes XP.
  *Manage Server*

## setlevel

Sets a member's chat level.

**Permission:** Manage Server

- **`setlevel (member) (level)`**  
  Sets their level.
  *Manage Server*

## voicelevel

Voice levels: XP for time spent in voice.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Voice

- **`voicelevel [member]`**  
  Shows voice level, time and XP.
- **`voicelevel leaderboard`**  
  The highest voice levels.
- **`voicelevel role (level) (role)`**  
  A role for reaching a voice level.
  *Manage Server*
- **`voicelevel roleremove (role)`**  
  Removes a voice level role.
  *Manage Server*
- **`voicelevel ignore (channel)`**  
  No voice XP in that channel.
  *Manage Server*
- **`voicelevel crownboard (channel)`**  
  A live voice leaderboard channel.
  *Manage Server*
- **`voicelevel reset (member)`**  
  Resets a member's voice XP.
  *Manage Server*

## stream

Time spent streaming and on camera.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Voice

- **`stream [member]`**  
  Shows stream and camera time.
- **`stream leaderboard`**  
  The top streamers.

## starboard

Reposts messages that collect enough of an emoji to a channel.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Reactions

- **`starboard set (channel)`**  
  The starboard channel.
  *Manage Server*  ·  example: `starboard set #starboard`
- **`starboard threshold (amount)`**  
  How many reactions a message needs.
  *Manage Server*
- **`starboard emoji add (emoji)`**  
  Adds an emoji that counts.
  *Manage Server*
- **`starboard emoji remove (emoji)`**  
  Removes one.
  *Manage Server*
- **`starboard color (hex)`**  
  The embed colour.
  *Manage Server*
- **`starboard (jumpurl/timestamp/attachments/publiconly) (on/off)`**  
  Display options.
  *Manage Server*
- **`starboard ignore (member/role/channel/thread)`**  
  Never stars from there.
  *Manage Server*
- **`starboard enable`**  
  Turns it on.
  *Manage Server*
- **`starboard disable`**  
  Turns it off.
  *Manage Server*

## messages

Message counts, with roles for reaching a count.

**Permission:** Anyone

- **`messages [member]`**  
  Shows how many messages a member has sent.
- **`messages enable`**  
  Starts counting messages (off until turned on).
  *Manage Server*
- **`messages disable`**  
  Stops counting. Totals are kept.
  *Manage Server*
- **`messages leaderboard`**  
  All-time message counts used by message rewards.
- **`messages awards add (role) (messages)`**  
  A role for reaching a count.
  *Manage Server*  ·  example: `messages awards add @Chatter 1000`
- **`messages awards remove (messages)`**  
  Removes a reward.
  *Manage Server*
- **`messages ignore (channel/category/role)`**  
  Not counted there.
  *Manage Server*
- **`messages add (member) (amount)`**  
  Adds messages to a count.
  *Manage Server*
- **`messages remove (member) (amount)`**  
  Takes messages away.
  *Manage Server*

## streak

Daily streaks: claim once a day to keep yours going.

**Permission:** Anyone

- **`streak`**  
  Claims today and shows your streak.
- **`streak leaderboard`**  
  The longest streaks.
- **`streak restore`**  
  Uses a restore to save a broken streak.
- **`streak timezone (zone)`**  
  Sets your timezone so days reset at your midnight.
  example: `streak timezone Europe/London`
- **`streak roles add (role) (days)`**  
  A role for reaching a streak.
  *Manage Server*
- **`streak remove (days)`**  
  Removes a streak role.
  *Manage Server*
- **`streak grantrestore (member) [amount]`**  
  Gives restores.
  *Manage Server*

## suggest

Members post suggestions that others vote on.

**Permission:** Anyone

- **`suggest (idea)`**  
  Posts a suggestion.
  example: `suggest add a music channel`
- **`suggest setup (channel) [review channel]`**  
  Turns suggestions on.
  *Manage Server*
- **`suggest status (status) (suggestion)`**  
  Marks a suggestion approved, denied, considered or in progress.
  *Manage Server*
- **`suggest emoji (upvote) (downvote)`**  
  The vote emojis.
  *Manage Server*
- **`suggest threads (on/off)`**  
  A discussion thread on each suggestion.
  *Manage Server*
- **`suggest ignore (member or role)`**  
  Can't suggest.
  *Manage Server*

## confessions

Anonymous confessions posted with /confess.

**Permission:** Manage Server

- **`confessions add (channel)`**  
  Where confessions are posted.
  *Manage Server*
- **`confessions report (number)`**  
  Sends the author to the private staff report channel.
  *Manage Messages*
- **`confessions reportchannel (channel or none)`**  
  Sets or clears the private staff report channel.
  *Manage Server*
- **`confessions blacklist add (phrase)`**  
  Blocks confessions containing a phrase.
  *Manage Server*
- **`confessions blacklist remove (phrase)`**  
  Removes a blocked phrase.
  *Manage Server*
- **`confessions blacklist list [page]`**  
  Pages through blocked phrases.
  *Manage Server*
- **`confessions (mute/unmute) (member)`**  
  Blocks or restores anonymous posts and replies for this member.
  *Manage Server*
- **`confessions emojis set (upvote or none) (downvote or none)`**  
  Reaction emojis on confessions.
  *Manage Server*
- **`confessions disable`**  
  After confirmation, turns confessions off and wipes stored confession records.
  *Manage Server*

## wordstats

Counts how often words are said.

**Permission:** Anyone

- **`wordstats [member] (word)`**  
  How many times they said a word.
  example: `wordstats @member bro`
- **`wordstats leaderboard (word) [limit]`**  
  Who says a word the most.
- **`wordstats command add (shortcut) (word)`**  
  A shortcut command for a word.
  *Manage Server*
- **`wordstats bots (on/off)`**  
  Count bots too.
  *Manage Server*

## reactstats

Counts reactions members receive, like a sob board.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Reactions

- **`reactstats [member]`**  
  Reactions a member got.
- **`reactstats leaderboard`**  
  Who got the most.
- **`reactstats add (emoji)`**  
  Tracks an emoji (up to 3).
  *Manage Server*
- **`reactstats remove (emoji)`**  
  Stops tracking it.
  *Manage Server*
- **`reactstats command add (shortcut) (emoji)`**  
  A shortcut command for an emoji.
  *Manage Server*
- **`reactstats bots (on/off)`**  
  Count bots too.
  *Manage Server*
