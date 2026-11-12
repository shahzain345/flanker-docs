---
title: Bot profile and name style
description: Change flanker's nickname, avatar, banner, bio and name style in your server.
---

The server owner and antinuke admins can change how flanker looks in their
server. Nothing changes in other servers. Everything here is also on the
dashboard's **Bot profile** page.

```
/settings customize name Flanky
/settings customize avatar https://…/avatar.png
/settings customize banner https://…/banner.png
/settings customize bio Moderation for our server
/settings customize reset
```

Discord allows a new avatar, banner or bio once every 6 hours.

## Name style

`/settings customize namestyle` opens menus for flanker's display name:

- **Font**: gg Sans, Tempo, Sakura, Jellybean, Modern, Medieval, 8Bit,
  Vampyre, Monkey Bars, Mainframe, Headbang or Journal.
- **Effect**: Solid, Neon, Toon and Pop use one colour. Gradient, Gummy and
  Prism use up to five.
- **Colours**: pick a preset or **Custom colours…** and type hex codes.

Each pick saves straight away. **Back to default** removes the style.

You can also type it in one go, in any order:

```
/settings customize namestyle sakura gradient #3B82F6 #EF4444
/settings customize namestyle mainframe neon #22D3EE
/settings customize namestyle reset
```

The slash version is `/settings customize namestyle`. Its **font** and
**effect** options are dropdowns, and **colours** takes hex codes separated
by spaces. Leave every option empty to open the menus. When typing, the 8Bit
font is `pixel`.

Discord shows role colours on names in chat and the member list, so the
style shows when someone opens flanker's profile.
