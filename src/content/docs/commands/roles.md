---
title: Roles commands
description: flanker roles commands, their syntax, permissions and examples.
sidebar:
  order: 6
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## reactionrole

Members react to a message to get a role.

**Permission:** Manage Roles

- **`reactionrole create (channel) (reaction) (role) [--exclusive] [--message (message or script)]`**  
  Creates a new reaction role panel. Add --message at the end to post your own text, embed or card instead of "Choose your roles".
  *Manage Roles*
- **`reactionrole message (message link) (message)`**  
  Edits the panel message, keeping its reactions and role controls.
  *Manage Roles*
- **`reactionrole add (message link) (reaction) (role) [--exclusive]`**  
  Adds a reaction role. --exclusive allows only one role from that message at a time.
  *Manage Roles*
- **`reactionrole remove (message link) (reaction)`**  
  Removes one.
  *Manage Roles*
- **`reactionrole removeall (message link)`**  
  Removes every reaction role on a message.
  *Manage Roles*
- **`reactionrole list [page]`**  
  Pages through reaction roles and their panels.
  *Manage Roles*

## buttonrole

Members press a button on a message to get a role.

**Permission:** Manage Roles

- **`buttonrole create (channel) (role) [style] [emoji] [label] [--exclusive] [--inside] [--message (message or script)]`**  
  Creates a new button role panel. Styles: blurple, grey, green, red. Add --message at the end to post your own text, embed or card; the buttons go under it.
  *Manage Roles*
- **`buttonrole message (message link) (message)`**  
  Edits the panel message, keeping its role controls.
  *Manage Roles*
- **`buttonrole layout (message link) [inside/under] [1-5] [even/natural]`**  
  Any mix of: buttons inside the card or under it, how many buttons sit on a row, and even widths (shorter labels padded to match the longest) or natural ones.
  *Manage Roles*  ·  example: `buttonrole layout https://discord.com/channels/1/2/3 inside 4 even`
- **`buttonrole add (message link) (role) (style) [emoji] [label] [--exclusive]`**  
  Adds a role button. Styles: blurple, grey, green, red.
  *Manage Roles*
- **`buttonrole remove (message link) (index)`**  
  Removes a button.
  *Manage Roles*
- **`buttonrole removeall (message link)`**  
  Removes every button.
  *Manage Roles*
- **`buttonrole list [page]`**  
  Pages through role buttons and their panels.
  *Manage Roles*

## rolemenu

Dropdown menus members pick roles from.

**Permission:** Manage Roles

- **`rolemenu create (message link) (role) [multiple/exclusive] [placeholder]`**  
  Adds a menu to one of flanker's messages.
  *Manage Roles*
- **`rolemenu panel (channel) (role) [multiple/exclusive] [placeholder] [--message script]`**  
  Creates a new role menu panel.
  *Manage Roles*
- **`rolemenu message (message link) (message)`**  
  Edits the panel message, keeping its role controls.
  *Manage Roles*
- **`rolemenu add (message link) (menu) (role) [label]`**  
  Adds a role to a menu.
  *Manage Roles*
- **`rolemenu remove (message link) (menu) (option)`**  
  Removes a role from a menu.
  *Manage Roles*
- **`rolemenu edit (message link) (menu) (mode/limit/placeholder) (value)`**  
  Changes a menu.
  *Manage Roles*
- **`rolemenu delete (message link) (menu)`**  
  Deletes a menu.
  *Manage Roles*
- **`rolemenu view (message link) [page]`**  
  Pages through the menus and options on a message.
  *Manage Roles*
- **`rolemenu list [page]`**  
  Pages through role menu panels and their selection limits.
  *Manage Roles*

## boosterrole

Boosters make their own custom role with a name, colour and icon.

**Permission:** Server Booster

- **`boosterrole create (name) [color] [second color]`**  
  Makes your booster role. A second colour makes a gradient role.
  *Server Booster*  ·  example: `boosterrole create shahzain #ff7a00`
- **`boosterrole rename (new name)`**  
  Renames it.
  *Server Booster*
- **`boosterrole color (color) [second color] [name]`**  
  Changes its colour.
  *Server Booster*
- **`boosterrole icon (image URL, emoji, or attachment)`**  
  Sets its icon (needs boost level 2).
  *Server Booster*
- **`boosterrole random`**  
  Picks a random colour.
  *Server Booster*
- **`boosterrole dominant`**  
  Uses the main colour of your avatar.
  *Server Booster*
- **`boosterrole share (member)`**  
  Shares your role with someone.
  *Server Booster*
- **`boosterrole remove`**  
  Deletes your role.
  *Server Booster*
- **`boosterrole list [page]`**  
  Pages through custom booster roles, owners and shared access.
- **`boosterrole base (role)`**  
  Booster roles are placed under this role.
  *Manage Roles*
- **`boosterrole limit (1-10)`**  
  How many booster roles one member can have.
  *Manage Roles*
- **`boosterrole award set (role)`**  
  A role every booster gets.
  *Manage Roles*
- **`boosterrole link (member) (role)`**  
  Links an existing role to a booster.
  *Manage Roles*

## badge

Rewards members who wear this server's guild tag.

**Permission:** Manage Roles

- **`badge role add (role)`**  
  Gives the role to members with the tag.
  *Manage Roles*
- **`badge role remove (role)`**  
  Stops giving it.
  *Manage Roles*
- **`badge channel (channel)`**  
  Where new tag wearers are announced.
  *Manage Roles*
- **`badge message (message/view/clear)`**  
  The announcement message.
  *Manage Roles*
- **`badge sync`**  
  Rechecks everyone now.
  *Manage Roles*

## vanity

Rewards visible custom statuses containing a link or keyword, with optional required roles. Does not read bios. Discord privacy settings can hide statuses. Configure everything at flanker.wtf/dashboard, under Community, Vanity rewards. No boost tier or vanity URL is needed. Only roles awarded by this module are removed when eligibility is lost.

**Permission:** Manage Server

- **`vanity (on/off)`**  
  Enable rewards or turn them off and remove recorded awards.
  *Manage Server*
- **`vanity set substring (text)`**  
  The text to look for in statuses, 1 to 128 characters.
  *Manage Server*  ·  example: `vanity set substring /flanker`
- **`vanity role (add/remove) (role)`**  
  The reward role.
  *Manage Roles*
- **`vanity require (add/remove) (role)`**  
  Require a role before someone earns rewards. Required roles cannot also be rewards.
  *Manage Server*  ·  example: `vanity require add @Members`
- **`vanity require clear`**  
  Remove required-role conditions.
  *Manage Server*
- **`vanity requiremode (all/any)`**  
  Match all required roles or at least one. Default: all.
  *Manage Server*
- **`vanity strict (on/off)`**  
  Exact status match instead of contains. Both ignore case.
  *Manage Server*
- **`vanity offline (on/off)`**  
  Remove rewards when offline or invisible. Off by default; known required-role loss is still enforced.
  *Manage Server*
- **`vanity award [channel/clear]`**  
  Where rewards are announced. Clear keeps awards silent.
  *Manage Server*
- **`vanity message [message/clear]`**  
  A message, embed or card for new awards. Variables: member, channel and \{vanity.keyword}. Role repair does not send it again.
  *Manage Server*
- **`vanity configure (settings JSON)`**  
  Atomically save dashboard settings. Reward roles always use automatic-role safety checks.
  *Manage Server and Manage Roles when changing rewards*
