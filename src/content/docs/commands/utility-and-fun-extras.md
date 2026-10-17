---
title: Utility and fun extras commands
description: flanker utility and fun extras commands, their syntax, permissions and examples.
sidebar:
  order: 20
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## base64

Encodes or decodes base64.

**Permission:** Anyone

- **`base64 (encode/decode) (text)`**  
  Encodes or decodes base64.
  example: `base64 encode hello`

## binary

Turns text into binary and back.

**Permission:** Anyone

- **`binary (encode/decode) (text)`**  
  Turns text into binary and back.
  example: `binary encode hi`

## rot13

Shifts letters by 13 (ROT13).

**Permission:** Anyone

- **`rot13 (text)`**  
  Shifts letters by 13 (ROT13).
  example: `rot13 hello`

## urlencode

Makes text safe for a link.

**Permission:** Anyone

- **`urlencode (text)`**  
  Makes text safe for a link.
  example: `urlencode a b`

## urldecode

Turns %20-style text back.

**Permission:** Anyone

- **`urldecode (text)`**  
  Turns %20-style text back.
  example: `urldecode a%20b`

## md5

The MD5 hash of some text.

**Permission:** Anyone

- **`md5 (text)`**  
  The MD5 hash of some text.
  example: `md5 hello`

## uuid

A random UUID.

**Permission:** Anyone

- **`uuid`**  
  A random UUID.

## randomnumber

A random number. Also `rng`.

**Permission:** Anyone

- **`randomnumber [min] [max]`**  
  A random number. Also `rng`.
  example: `randomnumber 1 6`

## randomhex

A random colour with a swatch.

**Permission:** Anyone

- **`randomhex`**  
  A random colour with a swatch.

## color

A colour's swatch and values, or a member's role colour. Also `hex`.

**Permission:** Anyone

- **`color (hex or member)`**  
  A colour's swatch and values, or a member's role colour. Also `hex`.
  example: `color #a3b6ff`

## charinfo

Code points of characters.

**Permission:** Anyone

- **`charinfo (characters)`**  
  Code points of characters.
  example: `charinfo é`

## calculate

Does a sum: + - * / % ^, brackets, sqrt, round. Also `calc`.

**Permission:** Anyone

- **`calculate (sum)`**  
  Does a sum: + - * / % ^, brackets, sqrt, round. Also `calc`.; calc 2 * (3 + 4)

## poll

Posts a Discord poll.

**Permission:** Anyone

- **`poll (question) | (answer) | (answer) [--hours 1-768] [--multi]`**  
  Posts a Discord poll.
  example: `poll Pizza? | Yes | No --hours 2`

## quickpoll

A yes or no poll with reactions. Also `qp`.

**Permission:** Anyone

- **`quickpoll (question)`**  
  A yes or no poll with reactions. Also `qp`.
  example: `quickpoll Movie night?`

## variables

Lists the variables you can use in messages.

**Permission:** Anyone

- **`variables`**  
  Lists the variables you can use in messages.

## uwuify

Uwuifies text. Also `uwu`.

**Permission:** Anyone

- **`uwuify (text)`**  
  Uwuifies text. Also `uwu`.; uwu hello friend

## iq

Someone's (made up) IQ.

**Permission:** Anyone

- **`iq [member]`**  
  Someone's (made up) IQ.

## pp

Someone's pp size.

**Permission:** Anyone

- **`pp [member]`**  
  Someone's pp size.

## gayrate

How gay someone is.

**Permission:** Anyone

- **`gayrate [member]`**  
  How gay someone is.

## compliment

Compliments someone.

**Permission:** Anyone

- **`compliment [member]`**  
  Compliments someone.

## insult

A light-hearted insult.

**Permission:** Anyone

- **`insult [member]`**  
  A light-hearted insult.

## dadjoke

A dad joke.

**Permission:** Anyone

- **`dadjoke`**  
  A dad joke.

## uselessfact

A useless fact. Also `fact`.

**Permission:** Anyone

- **`uselessfact`**  
  A useless fact. Also `fact`.

## truth

A truth question.

**Permission:** Anyone

- **`truth`**  
  A truth question.

## dare

A dare.

**Permission:** Anyone

- **`dare`**  
  A dare.

## wouldyourather

A would-you-rather question. Also `wyr`.

**Permission:** Anyone

- **`wouldyourather`**  
  A would-you-rather question. Also `wyr`.

## truthordare

A random truth or dare. Also `tod`.

**Permission:** Anyone

- **`truthordare`**  
  A random truth or dare. Also `tod`.

## cat

A random cat picture.

**Permission:** Anyone

- **`cat`**  
  A random cat picture.

## dog

A random dog picture.

**Permission:** Anyone

- **`dog`**  
  A random dog picture.

## fox

A random fox picture.

**Permission:** Anyone

- **`fox`**  
  A random fox picture.

## channelinfo

Details about a channel. Also `ci`.

**Permission:** Anyone

- **`channelinfo [channel]`**  
  Type, category, position, who can see it, privacy, overrides and sync, slowmode or voice settings. Also `ci`.

## roles

Lists every role.

**Permission:** Anyone

- **`roles`**  
  Lists every role.

## bots

Lists the bots in the server.

**Permission:** Anyone

- **`bots`**  
  Lists the bots in the server.

## boosters

Lists who's boosting, oldest first.

**Permission:** Anyone

- **`boosters`**  
  Lists who's boosting, oldest first.

## newmembers

The newest members. Also `joins`.

**Permission:** Anyone

- **`newmembers`**  
  The newest members. Also `joins`.

## getbotinvite

An invite link for a bot.

**Permission:** Anyone

- **`getbotinvite (bot)`**  
  An invite link for a bot.

## jaillist

Lists jailed members.

**Permission:** Moderate Members

- **`jaillist [page]`**  
  Pages through jailed members and their automatic release times.
  *Moderate Members*
