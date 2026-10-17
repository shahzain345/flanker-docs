---
title: Utility commands
description: flanker utility commands, their syntax, permissions and examples.
sidebar:
  order: 8
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## autopfp

Posts profile pictures, gifs or banners in a channel every few minutes.

**Permission:** Manage Server

- **`autopfp setup (option) (channel)`**  
  Starts posting.
  *Manage Server*  ·  example: `autopfp setup anime #pfps`
- **`autopfp remove (option)`**  
  Stops one.
  *Manage Server*
- **`autopfp list [page]`**  
  Pages through scheduled image feeds and destinations.
  *Manage Server*

## getpfp

A random profile picture.

**Permission:** Anyone

- **`getpfp [female/male]`**  
  Sends a random profile picture.

## getgif

A random animated profile picture.

**Permission:** Anyone

- **`getgif [female/male]`**  
  Sends a random gif avatar.

## getbanner

A random banner.

**Permission:** Anyone

- **`getbanner`**  
  Sends a random banner.

## counter

Channels whose names show live counts, like member count.

**Permission:** Manage Channels

- **`counter add (option) (voice/text/category/announce/stage)`**  
  Creates a counter. Options: members, users_only, bots_only, boosts, booster_count and more.
  *Manage Channels*  ·  example: `counter add members voice`
- **`counter remove (channel)`**  
  Deletes a counter.
  *Manage Channels*
- **`counter list [page]`**  
  Pages through counters, with create and remove controls.
  *Manage Channels*

## giveaways

Giveaways with requirements checked when winners are drawn, bonus entries and rerolls.

**Permission:** Manage Server

- **`giveaways start [channel] (duration) (winners) (prize) [flags]`**  
  Starts a giveaway. Requirement flags include --requiredroles, --messages, --invites, --status, --minlevel, --maxlevel, --voicelevel, --voice, --age and --stay.
  *Manage Server*  ·  example: `giveaways start 1d 1 Nitro --messages 100 --invites 5 --status flanker`
- **`giveaways end (message link)`**  
  Ends one now.
  *Manage Server*
- **`giveaways reroll (message link)`**  
  Picks new winners.
  *Manage Server*
- **`giveaways cancel (message link)`**  
  Cancels one.
  *Manage Server*
- **`giveaways edit (field) [message link] (value)`**  
  Changes prize, winners, duration or one requirement. Use off to clear a status rule.
  *Manage Server*
- **`giveaways list`**  
  Lists running giveaways.
- **`giveaways blacklist (member or role)`**  
  Can't enter giveaways.
  *Manage Server*

## translate

Translates text. Reply with translate or tr for English, or include a language name or code. Use --from if auto-detection gets the source wrong. Unchanged results are not presented as successful translations.

**Permission:** Anyone

- **`translate (language) (text) [--from (source)]`**  
  Translates up to 1,800 characters into the selected language. Put --from last.
  example: `translate spanish good morning`
- **`translate [language] [--from (source)]`**  
  Translates the message you reply to. Defaults to English. --from sets the source, not the destination.; tr en --from ur

## tts

Turns text into speech and sends the audio.

**Permission:** Anyone

- **`tts [--voice (name)] (text)`**  
  Speaks the text, or the message you reply to.
- **`tts voices`**  
  Lists voices.

## repost

Downloads a video from TikTok, Instagram, X, YouTube, Reddit, Twitch clips, Streamable or SoundCloud and posts it here.

**Permission:** Anyone

- **`repost (link)`**  
  Reposts the video.
  example: `repost https://www.tiktok.com/@user/video/123`
- **`repost auto (on/off)`**  
  Reposts supported links automatically.
  *Manage Server*
- **`repost channel (#channel)`**  
  Only auto-repost in some channels.
  *Manage Server*
- **`repost settings`**  
  Shows the settings.
  *Manage Server*

## quote

Turns a message into a PNG with its author's avatar and words. Regular-weight Geist is the default. Font and layout dropdowns edit the same image; buttons change the theme, avatar side, colour, weight and watermark, reset it or remove it. Only the person who ran the command can use these controls, for 15 minutes or until flanker restarts. Older controls may close when the editor is busy; the picture stays.

**Permission:** Anyone

- **`quote [--font geist/noto/serif/mono] [--layout wide/square/portrait]`**  
  Quotes the message you reply to. Choose Geist, Noto Sans, Noto Serif or Geist Mono, with a wide, square or portrait layout.
- **`quote (message link or id) [--color] [--light] [--flip] [--bold] [--no-watermark]`**  
  Quotes a readable message in this server. These optional flags keep the avatar in colour, use a light theme, swap the avatar side, use bold words or hide the flanker mark.

## embed

Saved messages you can send, edit and use on buttons. A button is \{button: colour && label && action}. Colours: blurple, grey, green, red. Actions: embed:name (show a saved message), ephemeral:name (show it privately), role:@Role (give or take), give:@Role, take:@Role, ticket:panel/option (open a ticket) and apply:form (start an application). The message editor's Custom response action designs a separate text, embed or card reply inside the button. It is private by default, with public replies and a 6-3,600 second auto-delete option. The editor generates its reply: target. Link buttons are \{button: https://... && label} and are always grey.

**Permission:** Manage Messages

- **`embed create (name) (embed code)`**  
  Saves an embed.
  *Manage Messages*  ·  example: `embed create rules \{embed}$v\{title: Rules}`
- **`embed send [channel] (embed code)`**  
  Sends an embed.
  *Manage Messages*
- **`embed dm (embed code)`**  
  Sends a test copy to your DMs.
  *Manage Messages*  ·  example: `embed dm \{embed}$v\{title: Hi}`
- **`embed edit (message link) (embed code)`**  
  Edits one of flanker's messages.
  *Manage Messages*
- **`embed view (name)`**  
  Previews a saved embed.
  *Manage Messages*
- **`embed code (name)`**  
  Shows a saved embed's code.
  *Manage Messages*
- **`embed list`**  
  Lists saved embeds.
  *Manage Messages*
- **`embed delete (name)`**  
  Deletes one.
  *Manage Messages*

## embedcode

Gets the embed code of a message so you can reuse it.

**Permission:** Anyone

- **`embedcode (message link)`**  
  Shows the code, or reply to a message.

## pagination

Messages with pages members can flip through.

**Permission:** Manage Messages

- **`pagination add (message link) (embed code)`**  
  Adds a page.
  *Manage Messages*
- **`pagination update (message link) (page ID) (embed code)`**  
  Edits a page.
  *Manage Messages*
- **`pagination remove (message link) (page ID)`**  
  Removes a page.
  *Manage Messages*
- **`pagination list`**  
  Lists paginated messages.
  *Manage Messages*

## media

Image and video tools: captions, speech bubbles, gifs and effects.

**Permission:** Anyone

- **`media caption [image] (text) [--bottom] [--black]`**  
  Adds a caption.
  example: `media caption when the code works`
- **`media magik [image]`**  
  Applies a strong liquid distortion. Every media tool uses the image you attach, link or reply to (including pictures in embeds and cards), a mentioned member's avatar, or yours.
- **`media speechbubble [image]`**  
  Adds a speech bubble.
- **`media gif [image]`**  
  Turns an image or video into a gif.
- **`media (grayscale/invert/reverse/blur) [media]`**  
  Effects. Each also works on its own, like `invert`.
- **`media deepfry [media]`**  
  Crushes the colours and adds grain. Also `fry`.; deepfry
- **`media jpeg [image]`**  
  Heavy JPEG compression.
- **`media pixelate [media] [size 2-64]`**  
  Big pixels. Also `pixel`.; pixelate 20
- **`media (flip/mirror) [media]`**  
  Flips upside down, or mirrors left to right. `mirror` works on its own.
- **`media rotate [media] [90/180/270]`**  
  Turns it.; rotate 180
- **`media wide [media] [factor 1.2-5]`**  
  Stretches it sideways. Also `stretch`.; wide 3
- **`media sepia [media]`**  
  Old photo colours.
- **`media (bulge/pinch/swirl) [image] [strength]`**  
  Bulges, pinches or swirls the middle. Also `explode` and `implode`.; swirl 4
- **`media spin [image]`**  
  Turns a still image into a spinning gif.
- **`media speed [gif or video] (0.5-4)`**  
  Changes the speed.
- **`media info [media]`**  
  Shows size and format.

## customize

Changes how flanker looks in this server. Also on the dashboard's Bot profile page. Antinuke admins can use it too.

**Permission:** Server owner

- **`customize name [nickname]`**  
  flanker's nickname here. Leave it out to remove it.
  *Server owner*
- **`customize avatar (image URL, attachment or reset)`**  
  flanker's avatar here.
  *Server owner*
- **`customize banner (image URL, attachment or reset)`**  
  flanker's banner here.
  *Server owner*
- **`customize bio (text or reset)`**  
  flanker's bio here. It always ends with Website: https://flanker.wtf.
  *Server owner*
- **`customize reset`**  
  Back to normal.
  *Server owner*
