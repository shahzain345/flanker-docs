---
title: Custom commands commands
description: flanker custom commands commands, their syntax, permissions and examples.
sidebar:
  order: 25
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## customcommand

Custom commands built on the dashboard by wiring blocks together: typed options, if / else if / else, variables, buttons and dropdowns with their own paths, repeats, and events (joins, leaves, words, reactions). They can't moderate, edit channels or ping everyone. Only the owner, the backup owner and antinuke admins can make them, and they only run while antinuke is armed.

**Permission:** Server owner

**Configure on the [dashboard](https://flanker.wtf/dashboard):** Custom commands

- **`customcommand list [page]`**  
  Pages through the server's custom commands and event workflows.
- **`customcommand info (name)`**  
  What one does and how often it's used.
- **`customcommand enable (name)`**  
  Turns one on.
  *Server owner*
- **`customcommand disable (name)`**  
  Turns one off.
  *Server owner*
- **`customcommand delete (name)`**  
  Deletes one.
  *Server owner*
