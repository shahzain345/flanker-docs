---
title: Emojis and stickers commands
description: flanker emojis and stickers commands, their syntax, permissions and examples.
sidebar:
  order: 14
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## emoji

Adds, steals, removes and renames server emojis, or shows one big.

**Permission:** Anyone

- **`emoji (emoji, name or ID)`**  
  Shows a custom or Unicode emoji and its image. Names and bare IDs are resolved in this server.
- **`emoji information (emoji, name or ID)`**  
  Image, format and custom emoji details.
- **`emoji add (emojis, or image URL/attachment) [name]`**  
  Adds emojis: paste custom emojis from other servers (up to 10 at once), reply to a message with them, or give an image or image link. Without a name, the file's name is used. `steal` works the same way.
  *Manage Expressions*  ·  example: `emoji add \<:pog:123456789012345678>`
- **`emoji steal`**  
  Reply to a message to add every custom emoji in it.
  *Manage Expressions*
- **`emoji remove (emojis)`**  
  Deletes emojis. Counts toward antinuke's emoji limit.
  *Manage Expressions*
- **`emoji rename (emoji) (new name)`**  
  Renames an emoji.
  *Manage Expressions*
- **`emoji enlarge (emoji)`**  
  Shows an emoji full size. Works with normal emojis too.
- **`emoji list [page]`**  
  Pages through the server's emojis.

## sticker

Adds, steals, removes and renames server stickers.

**Permission:** Anyone

- **`sticker add [name]`**  
  Reply to a sticker (or attach an image) to add it here.
  *Manage Expressions*  ·  example: `sticker add cool cat`
- **`sticker remove (name)`**  
  Deletes a sticker.
  *Manage Expressions*
- **`sticker rename (name) (new name)`**  
  Renames a sticker.
  *Manage Expressions*
- **`sticker list [page]`**  
  Pages through the server's stickers. Use quotes around names with spaces in rename and remove commands.
