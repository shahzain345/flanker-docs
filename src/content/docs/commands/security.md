---
title: Security commands
description: flanker security commands, their syntax, permissions and examples.
sidebar:
  order: 2
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## antinuke

Stops nukes: mass bans and kicks, deleted channels and roles, dangerous permission grants, webhook and emoji spam, vanity changes and rogue bots. Whoever trips a limit is punished and the damage is undone where possible.

**Permission:** Server owner or antinuke admin

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Antinuke

- **`antinuke config`**  
  Shows every module, its limit and punishment, admins and trusted bots.
  *Server owner or antinuke admin*
- **`antinuke setup`**  
  Turns antinuke on. Beginner applies the recommended protection in one go; advanced adds optional hardening, asked as yes or no questions.
  *Server owner*
- **`antinuke toggle (on/off)`**  
  Turns antinuke as a whole on or off. Module settings are kept.
  *Server owner*
- **`antinuke (module) (on/off) [--threshold N] [--do punishment] [--command on/off]`**  
  Sets up one module. Modules: ban, kick, channel, role, webhook, emoji, vanity, botadd, permissions. Threshold is how many actions in a short window trip it (1 to 10). Punishments: warn, jail, kick, ban, stripstaff, timeout. --command also counts bans and kicks done through bot commands.
  *Server owner or antinuke admin*  ·  example: `antinuke ban on --threshold 3 --do ban`
- **`antinuke list`**  
  Lists the modules and whether each is on.
  *Server owner or antinuke admin*
- **`antinuke whitelist (member/bots/list)`**  
  Lets a member act without being punished, or whitelists every bot in the server at once. Run it again to remove them.
  *Server owner or antinuke admin*  ·  example: `antinuke whitelist @shahzain`
- **`antinuke admin (member/list)`**  
  Makes a member an antinuke admin: they can change antinuke settings and aren't punished. Run it again to remove them.
  *Server owner*  ·  example: `antinuke admin @shahzain`
- **`antinuke protect (role/user) (punishment)`**  
  Protects a role or member: anyone who removes, deletes or edits it is punished straight away.
  *Server owner or antinuke admin*  ·  example: `antinuke protect @Staff ban`
- **`antinuke protected`**  
  Lists protected roles and members.
  *Server owner or antinuke admin*
- **`antinuke protection`**  
  Shows Flanker Protection: the role that stops anyone below it from banning, kicking or timing out without going through flanker.
  *Server owner or antinuke admin*
- **`antinuke protection allow (role)`**  
  Lets a role sit above Flanker Protection.
  *Server owner or antinuke admin*
- **`antinuke protection off`**  
  Turns Flanker Protection off.
  *Server owner*
- **`antinuke shield (channels/webhooks/admin) (on/off)`**  
  Extra hardening: channel deletes go to a trash you can restore from, webhooks can only be made through flanker, and Administrator can't be handed out.
  *Server owner*
- **`antinuke trusted`**  
  Lists trusted bots, including the built-in list of well-known bots.
  *Server owner or antinuke admin*
- **`antinuke trusted add (bot) (security/utility)`**  
  Trusts a bot. Security bots keep full permissions. Utility bots lose Administrator and Manage Webhooks. The moderator behind either tier still counts.
  *Server owner*  ·  example: `antinuke trusted add @bleed utility`
- **`antinuke trusted remove (bot)`**  
  Stops trusting a bot.
  *Server owner*
- **`antinuke trusted builtin (on/off)`**  
  Turns the built-in trusted bot list on or off.
  *Server owner*
- **`antinuke trusted cap (utility/security) (number)`**  
  How many actions trusted bots of a tier may take before antinuke steps in.
  *Server owner*
- **`antinuke trusted do (utility/security) (strip/kick/ban)`**  
  What happens to a trusted bot that goes over its cap.
  *Server owner*
- **`antinuke backupowner (member/off)`**  
  Sets a backup owner who must approve anything that weakens antinuke, so a hacked owner account can't switch it off.
  *Server owner*  ·  example: `antinuke backupowner @friend`
- **`antinuke backup [on/off]`**  
  flanker's backup role: Administrator, directly under flanker's role, held only by flanker. Re-inviting flanker with fewer permissions can't disarm it then. Only the owner and backup owner can delete it, take it off flanker or remove its permissions; anyone else who tries is punished. Setup asks before adding it.
  *Server owner*  ·  example: `antinuke backup on`
- **`antinuke event (duration) [--ban N] [--kick N] [--channel N] [--role N] [--webhook N] [--emoji N] [--permissions N]`**  
  Raises limits for a while, for events where staff need to act fast. They go back to normal when it ends.
  *Server owner or antinuke admin*  ·  example: `antinuke event 2h --ban 10`
- **`antinuke event end`**  
  Ends an event early.
  *Server owner or antinuke admin*
- **`antinuke panic`**  
  Shows panic mode. It starts on its own when antinuke fires too often (10 times in 30 minutes by default).
  *Server owner or antinuke admin*
- **`antinuke panic start [reason]`**  
  Turns panic mode on: every antinuke limit drops to 1, dangerous permissions are paused on every role below flanker, and every role, channel and permission change by anyone but the owner is undone.
  *Server owner or antinuke admin*
- **`antinuke panic end`**  
  Ends panic mode and gives the permissions back. Needs the backup owner's approval when one is set. A nuke report goes to the mod log.
  *Server owner*
- **`antinuke panic triggers (count) (minutes)`**  
  How many antinuke triggers start panic mode, and within how long.
  *Server owner or antinuke admin*  ·  example: `antinuke panic triggers 10 30`
- **`antinuke panic notice (channel/off)`**  
  Posts a short public notice there when panic mode starts.
  *Server owner or antinuke admin*

## antiraid

Catches raids: waves of new accounts joining and chat floods. Suspicious joiners are held behind a captcha, kicked or banned, and the server can lock itself down until the raid passes.

**Permission:** Manage Server (real)

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Antiraid

- **`antiraid setup`**  
  Guided setup. Beginner uses recommended limits; advanced asks for each limit and action.
  *Manage Server (real)*
- **`antiraid config`**  
  Shows every antiraid setting.
  *Manage Server (real)*
- **`antiraid tickets (on/off) [--accounts N] [--window 3s]`**  
  Ticket bursts default to six distinct accounts in three seconds. Enabled automatically for existing AntiRaid setups. Flanker stops new tickets during raid mode and removes recent tickets created by flagged raid accounts. Repeated attempts by one account do not fill the limit.
  *Manage Server (real)*  ·  example: `antiraid tickets on --accounts 6 --window 3s`
- **`antiraid voice (on/off) [--accounts N] [--window 3s]`**  
  Join to Create bursts default to six distinct accounts in three seconds. Raid mode locks creator channels, existing voice joins and voice-channel chat. Existing rooms stay, except recent rooms made by flagged raid accounts.
  *Manage Server (real)*  ·  example: `antiraid voice on --accounts 6 --window 3s`
- **`antiraid tickets setup`**  
  Guided setup for another ticket bot. Asks for its bot ID, panel message link and ticket category. Other applications' clicks are private; detection uses channel-creation audit events and one member permission grant. Ambiguous openers are not punished. Use a dedicated panel channel because raid mode hides that channel.
  *Manage Server (real)*
- **`antiraid tickets external (bot ID) (panel message link) (category)`**  
  Adds an external ticket panel in one step. Verifies that the bot owns the panel and is in this server.
  *Manage Server (real)*
- **`antiraid tickets remove (panel message link)`**  
  Removes an external panel from the watch list.
  *Manage Server (real)*
- **`antiraid voice add (#channel)`**  
  Watches another bot's Join to Create voice channel. Flanker's own creators are included automatically.
  *Manage Server (real)*  ·  example: `antiraid voice add #join-to-create`
- **`antiraid voice remove (#channel)`**  
  Stops watching an external creator.
  *Manage Server (real)*  ·  example: `antiraid voice remove #join-to-create`
- **`antiraid setup advanced [--tickets on/off] [--tickets-accounts N] [--tickets-window 3s] [--voice on/off] [--voice-accounts N] [--voice-window 3s]`**  
  Resource-burst flags accompany the other advanced setup flags. Default: six distinct accounts in three seconds. Limits: 2-100 accounts and 1-30 seconds.
  *Manage Server (real)*
- **`antiraid media (on/off) [--messages N] [--window 3s] [--accounts N]`**  
  Requires every participating account to burst image/video messages. Defaults: 6 per account in 3 seconds, at least 2 accounts. Albums count once. Runs while chat detection, raid mode or post-raid watch is active.
  *Manage Server (real)*  ·  example: `antiraid media on --messages 6 --window 3s --accounts 2`
- **`antiraid links (on/off) [--messages N] [--window 10s] [--accounts N]`**  
  Repeated complete link targets, not every link on the same website. Defaults: 3 copies per account in 10 seconds, at least 2 accounts.
  *Manage Server (real)*  ·  example: `antiraid links on --messages 3 --window 10s --accounts 2`
- **`antiraid automod (on/off) [--messages N] [--window 10s] [--accounts N]`**  
  Correlates live Discord mention-spam blocks containing mass pings. Needs an enabled Discord mention-spam rule. Defaults: 3 attempts per account in 10 seconds from at least 2 accounts. One block never qualifies.
  *Manage Server (real)*  ·  example: `antiraid automod on --messages 3 --window 10s --accounts 2`
- **`antiraid setup advanced [--media on/off] [--media-messages N] [--media-window 3s] [--media-accounts N] [--links on/off] [--links-messages N] [--links-window 10s] [--links-accounts N] [--automod on/off] [--automod-messages N] [--automod-window 10s] [--automod-accounts N]`**  
  Optional coordinated-payload settings, alongside the join and text flood flags. Each coordinated rule requires at least two accounts. The dashboard advanced wizard exposes these limits.
  *Manage Server (real)*
- **`antiraid joins (on/off) [--joins N] [--window 10s] [--smart on/off] [--do captcha/kick/ban] [--lock on/off]`**  
  Join raid detection: how many joins in how long count as a raid, and what happens to the joiners.
  *Manage Server (real)*  ·  example: `antiraid joins on --joins 8 --window 10s --do captcha`
- **`antiraid flood (on/off) [--messages N] [--window 3s] [--accounts N] [--repeats N] [--repeat-window 10s] [--repeat-chars N] [--do captcha/jail]`**  
  Detects repeated text, mention floods and bot-like bursts. Requires two accounts by default; choose one for single-sender protection.
  *Manage Server (real)*  ·  example: `antiraid flood on --messages 6 --window 3s --accounts 2 --repeats 3 --repeat-window 10s --repeat-chars 400`
- **`antiraid avatar (on/off) [--do kick/ban]`**  
  Acts on new members with no profile picture during a raid. Strict: some real people never set one.
  *Manage Server (real)*
- **`antiraid newaccounts (on/off) [--threshold days] [--do kick/ban]`**  
  Acts on accounts younger than a number of days.
  *Manage Server (real)*  ·  example: `antiraid newaccounts on --threshold 7 --do kick`
- **`antiraid log (#channel/off)`**  
  Where raid alerts are posted.
  *Manage Server (real)*  ·  example: `antiraid log #antiraid-log`
- **`antiraid whitelist (member)`**  
  Lets a member through raid checks.
  *Manage Server (real)*
- **`antiraid verify (@member/all)`**  
  Lets members waiting on the captcha in.
  *Manage Server (real)*
- **`antiraid unverified`**  
  Lists members still waiting on the captcha.
  *Manage Server (real)*
- **`antiraid end`**  
  Ends raid mode and unlocks the server.
  *Manage Server (real)*
- **`antiraid reset`**  
  Turns everything off and lets every held member in.
  *Manage Server (real)*

## raid

Starts raid mode by hand: locks the server and acts on recent joiners.

**Permission:** Manage Server (real)

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Antiraid

- **`raid (duration) (kick/ban) [reason]`**  
  Acts on everyone who joined in the last duration and turns raid mode on.
  *Manage Server (real)*  ·  example: `raid 10m ban join raid`

## honeypot

A trap channel only spam bots and hacked accounts post in. Anyone who sends a message there is punished.

**Permission:** Manage Server (real)

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Honeypot

- **`honeypot setup`**  
  Creates the trap channel with a warning message.
  *Manage Server (real)*
- **`honeypot punishment (kick/ban/softban/timeout)`**  
  What happens to accounts caught in the trap.
  *Manage Server (real)*  ·  example: `honeypot punishment softban`
- **`honeypot message (message/view/reset)`**  
  The warning posted in the trap channel.
  *Manage Server (real)*
- **`honeypot alerts (channel)`**  
  Where catches are reported.
  *Manage Server (real)*
- **`honeypot disable`**  
  Removes the trap.
  *Manage Server (real)*

## fakepermissions

Lets staff use flanker's commands as if they had a permission, without giving them the real Discord permission. Never unlocks security settings.

**Permission:** Server owner or Flanker Admin

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Fake permissions

- **`fakepermissions list`**  
  Shows every role with fake permissions.
  *Server owner or Flanker Admin*
- **`fakepermissions add (role) (permissions)`**  
  Gives a role fake permissions. Administrator, Manage Server and Manage Roles can only be given by the owner.
  *Server owner or Flanker Admin*  ·  example: `fakepermissions add @Mods ban_members, kick_members`
- **`fakepermissions remove (role) (permissions)`**  
  Takes fake permissions away from a role.
  *Server owner or Flanker Admin*
- **`fakepermissions reset`**  
  Removes every fake permission.
  *Server owner*

## filter

Deletes blocked words, links, invites, spam, caps, mass mentions, emoji spam and more. Strict: it sees through spacing, look-alike letters and other tricks.

**Permission:** Manage Server (real)

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Filters

- **`filter config`**  
  Shows every filter and where it applies.
  *Manage Server (real)*
- **`filter add (word, word, ...) [strict]`**  
  Blocks one or more words, separated by commas. Normally a word is only blocked when typed on its own. Add strict to block it anywhere, even inside other words.
  *Manage Server (real)*  ·  example: `filter add badword, scam link strict`
- **`filter remove (word, word, ...)`**  
  Unblocks one or more words, separated by commas. Removes the strict version too.
  *Manage Server (real)*  ·  example: `filter remove badword, scam link`
- **`filter list`**  
  Lists blocked words and regex patterns.
  *Manage Server (real)*
- **`filter regex (pattern)`**  
  Blocks anything matching a regex pattern. Test patterns on the dashboard first.
  *Manage Server (real)*  ·  example: `filter regex disc(o|0)rd\.gift`
- **`filter whitelist (word)`**  
  Allows a word that would otherwise match.
  *Manage Server (real)*
- **`filter links [channel/all] (on/off) [--do timeout (duration)]`**  
  Deletes links, including bare domains.
  *Manage Server (real)*  ·  example: `filter links all on`
- **`filter invites [channel/all] (on/off) [--do timeout (duration)]`**  
  Deletes Discord invites.
  *Manage Server (real)*
- **`filter links whitelist (domain)`**  
  Allows a domain through the link filter.
  *Manage Server (real)*  ·  example: `filter links whitelist youtube.com`
- **`filter (filter) exempt (role)`**  
  Lets a role skip one specific filter: links, invites, spam, caps, massmention, emoji, spoilers or musicfiles. Run it again to remove.
  *Manage Server (real)*  ·  example: `filter links exempt @gif`
- **`filter (filter) exempt list`**  
  Shows the roles that skip that filter.
  *Manage Server (real)*  ·  example: `filter links exempt list`
- **`filter spam [channel/all] (on/off) [--threshold N] [--window Ns]`**  
  Too many messages too fast.
  *Manage Server (real)*  ·  example: `filter spam all on --threshold 6 --window 5s`
- **`filter caps [channel/all] (on/off) [--threshold N]`**  
  Messages that are mostly capital letters.
  *Manage Server (real)*
- **`filter massmention [channel/all] (on/off) [--threshold N]`**  
  Messages that mention too many people.
  *Manage Server (real)*
- **`filter emoji [channel/all] (on/off) [--threshold N]`**  
  Messages with too many emojis.
  *Manage Server (real)*
- **`filter spoilers [channel/all] (on/off) [--threshold N]`**  
  Messages with too many spoilers.
  *Manage Server (real)*
- **`filter musicfiles [channel/all] (on/off)`**  
  Audio file uploads.
  *Manage Server (real)*
- **`filter edit (channel/all) (on/off)`**  
  Also checks edited messages.
  *Manage Server (real)*
- **`filter exempt (role)`**  
  Lets a role skip the word filter. Use "filter (filter) exempt (role)" for links, invites, spam and the others.
  *Manage Server (real)*
- **`filter strikes (on/off) [--count 2-20] [--window 1m-24h] [--timeout 1m-28d]`**  
  Times out members who keep hitting the filter.
  *Manage Server (real)*  ·  example: `filter strikes on --count 3 --window 10m --timeout 1h`
- **`filter reset`**  
  Turns every filter off.
  *Manage Server (real)*

## channel

Channel tools with antinuke's trash: deleted channels can be restored for a few days.

**Permission:** Manage Channels (real)

- **`channel create (name) [text/voice] [category]`**  
  Creates a channel.
  *Manage Channels (real)*  ·  example: `channel create announcements text`
- **`channel rename [channel] (name)`**  
  Renames a channel.
  *Manage Channels (real)*
- **`channel delete (channel)`**  
  Moves a channel to the trash instead of deleting it for good.
  *Manage Channels (real)*
- **`channel trash`**  
  Lists trashed channels.
  *Manage Channels (real)*
- **`channel restore (channel or name)`**  
  Brings a trashed channel back with its permissions.
  *Manage Channels (real)*

## webhook

Webhooks made through flanker, so antinuke can tell them apart from rogue ones.

**Permission:** Manage Webhooks (real)

- **`webhook create (channel) (name)`**  
  Creates a webhook and DMs you its URL.
  *Manage Webhooks (real)*
- **`webhook list [page]`**  
  Pages through webhooks and their identifiers.
  *Manage Webhooks (real)*
- **`webhook send (identifier or channel) [--name (name)] [--avatar (link)] [--thread (forum post title)] --message (message)`**  
  Posts through flanker's webhook. With a channel, flanker makes its webhook there the first time. Buttons and menus work. --name and --avatar change who it appears as.
  *Manage Webhooks (real)*  ·  example: `webhook send #news --name News --message \{embed}$v\{title: Update}`
- **`webhook url (webhook link) [--name (name)] [--avatar (link)] [--thread (forum post title)] --message (message)`**  
  Posts through your own webhook from this server. Only link buttons work there; others are left out.
  *Manage Webhooks (real)*  ·  example: `webhook url https://discord.com/api/webhooks/1/abc --message Hello`
- **`webhook edit (message link) --message (new message)`**  
  Replaces a message sent through flanker's webhook.
  *Manage Webhooks (real)*  ·  example: `webhook edit https://discord.com/channels/1/2/3 --message Updated`
- **`webhook delete (identifier)`**  
  Deletes a webhook.
  *Manage Webhooks (real)*

## elevate

Temporary permissions: staff ask for a permission for a while and the owner approves it.

**Permission:** Server owner approval

- **`elevate (permission[,permission]) (duration) [reason]`**  
  Asks the owner for permissions for 1 minute to 24 hours. They approve or deny it in DMs.
  example: `elevate ban_members 30m cleaning up spam`
- **`elevate list [page]`**  
  Pages through active and pending elevations.
- **`elevate revoke (member)`**  
  Ends someone's elevation early.
  *Server owner*

## backup

Keeps a copy of channels, roles and emojis so they can be restored after a nuke.

**Permission:** Server owner

- **`backup enable`**  
  Turns backups on and saves a first snapshot.
  *Server owner*
- **`backup now`**  
  Saves a snapshot right now.
  *Server owner*
- **`backup restore`**  
  Recreates missing channels, roles and emojis from the latest snapshot.
  *Server owner*
- **`backup disable`**  
  Turns backups off.
  *Server owner*
