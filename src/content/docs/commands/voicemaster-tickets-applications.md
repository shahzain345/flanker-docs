---
title: VoiceMaster, tickets, applications commands
description: flanker voicemaster, tickets, applications commands, their syntax, permissions and examples.
sidebar:
  order: 12
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## voicemaster

Join to create voice rooms that members own and control.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** VoiceMaster

- **`voicemaster setup`**  
  Creates the join channel, category and control panel.
  *Manage Server*
- **`voicemaster (lock/unlock)`**  
  Locks or unlocks your room.
  *Room owner*
- **`voicemaster (ghost/unghost)`**  
  Hides or shows your room.
  *Room owner*
- **`voicemaster rename (name)`**  
  Renames your room.
  *Room owner*
- **`voicemaster limit (number)`**  
  Sets a user limit.
  *Room owner*
- **`voicemaster trust (member)`**  
  Lets someone into this and future rooms.
  *Room owner*
- **`voicemaster untrust (member)`**  
  Removes someone from your trusted list.
  *Room owner*
- **`voicemaster block (member)`**  
  Removes someone and blocks them from this and future rooms.
  *Room owner*
- **`voicemaster unblock (member)`**  
  Removes someone from your blocked list.
  *Room owner*
- **`voicemaster invite (member)`**  
  Sends a member a link and lets them into this room.
  *Room owner*
- **`voicemaster kick (member)`**  
  Removes someone from this room.
  *Room owner*
- **`voicemaster transfer (member)`**  
  Gives your room to someone.
  *Room owner*
- **`voicemaster claim`**  
  Takes over a room whose owner left.
- **`voicemaster (chatlock/chatunlock)`**  
  Locks or unlocks the room's text chat.
  *Room owner*
- **`voicemaster roomreset`**  
  Restores your room and saved owner settings to server defaults.
  *Room owner*
- **`voicemaster info`**  
  Shows the room's settings.
- **`voicemaster default (name/limit/bitrate/region/role) (value)`**  
  Defaults for new rooms.
  *Manage Server*
- **`voicemaster limitrange (minimum) (maximum)`**  
  Limits the member counts room owners may choose.
  *Manage Server*
- **`voicemaster maxchannels (0-500)`**  
  Caps active temporary rooms. Zero is unlimited.
  *Manage Server*
- **`voicemaster category [private] (category/none)`**  
  Where rooms are created.
  *Manage Server*
- **`voicemaster interface (text channel)`**  
  Re-sends the control panel.
  *Manage Server*
- **`voicemaster admin (room) (lock/unlock/hide/unhide/limit/transfer/close) [value]`**  
  Controls any room.
  *Manage Server*
- **`voicemaster password (password/none)`**  
  Locks your room behind a password. Your choice is stored hashed.
  *Room owner*
- **`voicemaster enter (room owner) (password)`**  
  Joins a room with its password. Your message is deleted.
- **`voicemaster votekick (member)`**  
  Starts one vote in your room. Members can vote yes or no and change their vote for two minutes. The target and bots cannot vote; owners and staff cannot be voted out.
- **`voicemaster votepercent (1-100)`**  
  Percentage of eligible room members needed to remove someone, rounded up. Default 50. The target and bots do not count as voters.
  *Manage Server*
- **`voicemaster creator add (voice channel) [category] [--private] [--limit 0-99] [--max 0-500] [--name template]`**  
  Adds another Join to Create channel with its own settings. --limit is members per room, --max is how many rooms it can have open. Up to 10.
  *Manage Server*
- **`voicemaster creatorlimit (Join to Create channel) (0-500)`**  
  Caps how many rooms one Join to Create channel can have open at once. 0 removes the cap.
  *Manage Server*
- **`voicemaster creator remove (voice channel)`**  
  Removes an extra Join to Create channel.
  *Manage Server*
- **`voicemaster fallback (add/remove) (category)`**  
  Backup categories for when a category is full.
  *Manage Server*
- **`voicemaster textchannels (on/off)`**  
  A private text channel for each room, for the people in it.
  *Manage Server*
- **`voicemaster waitingrooms (on/off)`**  
  A waiting room next to locked rooms. Owners let people in with a button.
  *Manage Server*
- **`voicemaster votekicks (on/off)`**  
  Lets people vote someone out of their room.
  *Manage Server*
- **`voicemaster log (channel/none)`**  
  Logs rooms created, closed, renamed, claimed, locked and vote kicks.
  *Manage Server*
- **`voicemaster feature [name] [on/off]`**  
  Turns owner controls on or off. Without a name it lists them.
  *Manage Server*
- **`voicemaster reset`**  
  Removes the setup.
  *Manage Server*

## ticket

Private support channels members open from a panel.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Tickets

- **`ticket setup`**  
  Quick setup: asks for support roles, a log channel and where to post the panel.
  *Manage Server*
- **`ticket config [page]`**  
  Shows settings and pages through every panel and option.
  *Manage Server*
- **`ticket panel (name) [channel]`**  
  Sends or resends a panel.
  *Manage Server*  ·  example: `ticket panel Support #support`
- **`ticket panel create (name) [channel]`**  
  Makes a new panel.
  *Manage Server*
- **`ticket panel set (panel) (channel/message/display/max/log/inside) (value)`**  
  Changes a panel. inside on puts the open buttons or menu inside a card instead of under it.
  *Manage Server*
- **`ticket panel delete (name)`**  
  Deletes a panel.
  *Manage Server*
- **`ticket option add (panel) (name) [label]`**  
  Adds an option (a kind of ticket) to a panel.
  *Manage Server*
- **`ticket option set (panel) (option id) (field) (value)`**  
  Changes an option: label, emoji, style, support roles, category, claiming, welcome message, inside (Close and Claim inside the welcome card) and more.
  *Manage Server*
- **`ticket option remove (panel) (option id)`**  
  Removes an option.
  *Manage Server*
- **`ticket forms add (panel) (option id) (question) [--paragraph] [--optional]`**  
  Asks a question before the ticket opens.
  *Manage Server*
- **`ticket settings (log/category/cooldown/autoclose/closeonleave/dmlog/autodelete/closedcategory/closedname) (value)`**  
  Server-wide ticket settings.
  *Manage Server*
- **`ticket claim`**  
  Claims the ticket you're in.
  *Support roles*
- **`ticket unclaim`**  
  Gives up the claim.
  *Support roles*
- **`ticket add (member or role)`**  
  Gives someone access to the ticket.
  *Support roles*
- **`ticket remove (member or role)`**  
  Takes access away.
  *Support roles*
- **`ticket close [reason]`**  
  Closes the ticket and saves a transcript.
  *Support roles*
- **`ticket closerequest [timeout] [reason]`**  
  Asks to close, with an optional auto-close timer.
  *Support roles or opener*  ·  example: `ticket closerequest 10m resolved`
- **`ticket autoclose [hours]`**  
  Closes the ticket after some quiet hours.
  *Support roles*
- **`ticket move (category)`**  
  Moves the ticket to another category.
  *Support roles*
- **`ticket info`**  
  Number, panel, opener, claimer and open time.
  *Support roles*
- **`ticket reopen [ticket id] [reason]`**  
  Reopens a closed ticket.
  *Manage Server*
- **`ticket delete [ticket id] [reason]`**  
  Deletes a ticket's channel.
  *Manage Server*
- **`ticket list [status] [member]`**  
  Lists tickets.
  *Manage Server*
- **`ticket stats [member]`**  
  Ticket counts.
  *Manage Server*
- **`ticket blacklist (member or role)`**  
  Can't open tickets.
  *Manage Server*
- **`ticket force (member) [panel]`**  
  Opens a ticket for someone.
  *Manage Server*
- **`ticket reason (ticket id) (reason)`**  
  Changes a ticket's close reason.
  *Manage Server*

## application

Applications: forms members fill in to apply for staff and other roles, reviewed by staff with Accept and Deny buttons.

**Permission:** Manage Server

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Applications

- **`application`**  
  Lists every application.
- **`application list [page]`**  
  Pages through forms, review destinations and pending counts.
- **`application create (name) [review channel]`**  
  Makes a new application.
  *Manage Server*  ·  example: `application create staff #applications`
- **`application question add (form) (question) [--paragraph] [--optional]`**  
  Adds a question (up to 25, 45 characters each).
  *Manage Server*  ·  example: `application question add staff Why do you want to join?`
- **`application question remove (form) (number)`**  
  Removes a question.
  *Manage Server*
- **`application question move (form) (from) (to)`**  
  Reorders questions.
  *Manage Server*
- **`application set (form) (setting) (value)`**  
  Settings: review, reviewers, ping, thread, roles, removeroles, required, accountage, serverage, cooldown, accepted, denied, message, button, emoji, style.
  *Manage Server*  ·  example: `application set staff roles @Trial Mod`
- **`application panel (form) (channel)`**  
  Posts the Apply button.
  *Manage Server*
- **`application (open/close) (form)`**  
  Opens or closes applications.
  *Manage Server*
- **`application accept (number) [reason]`**  
  Accepts: gives the roles and DMs them.
  *Reviewers*
- **`application deny (number) [reason]`**  
  Denies and DMs them the reason.
  *Reviewers*
- **`application pending [form]`**  
  Lists applications waiting for review.
  *Reviewers*
- **`application view (number)`**  
  Shows an application's answers.
  *Reviewers*
- **`application delete (form)`**  
  Deletes an application.
  *Manage Server*

## apply

Starts an application.

**Permission:** Anyone

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Applications

- **`apply [form]`**  
  Opens the application form.
  example: `apply staff`
