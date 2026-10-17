---
title: Lookups commands
description: flanker lookups commands, their syntax, permissions and examples.
sidebar:
  order: 24
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## convert

Converts an amount between currencies using dated reference rates. Estimates exclude exchange fees.

**Permission:** Anyone

- **`convert (amount) (from currency) [to] (to currency)`**  
  Use three-letter codes, in either case. Commas in amounts must group thousands. Alias: conversion.
  example: `convert 10 USD CAD`
- **`convert (amount) (from currency) to (to currency)`**  
  The word to is optional.
  example: `convert 1000 usd to pkr`

## rate

Shows how much of the second currency equals one unit of the first, with the rate date and source.

**Permission:** Anyone

- **`rate (from currency) (to currency)`**  
  Uses the same dated reference rates as convert.
  example: `rate CAD USD`

## crypto

A coin's price, 24 hour change, market cap and volume, from CoinGecko.

**Permission:** Anyone

- **`crypto (coin)`**  
  Looks it up.
  example: `crypto bitcoin`

## gas

Ethereum gas right now, and what common transactions cost.

**Permission:** Anyone

- **`gas`**  
  Shows the gas price.

## transaction

A Bitcoin or Ethereum transaction: status, value and fee.

**Permission:** Anyone

- **`transaction (hash)`**  
  Looks it up. Hashes starting with 0x are Ethereum.

## github

A GitHub profile: bio, repos, followers.

**Permission:** Anyone

- **`github (username)`**  
  Looks it up.
  example: `github torvalds`

## minecraft

A Minecraft account: UUID, head, body and skin.

**Permission:** Anyone

- **`minecraft (username)`**  
  Looks it up.
  example: `minecraft Notch`

## steam

A Steam profile: status, location, member since.

**Permission:** Anyone

- **`steam (profile name, link or ID)`**  
  Looks it up.

## anime

An anime from AniList: score, episodes, status and genres. Adult titles never show.

**Permission:** Anyone

- **`anime (title)`**  
  Looks it up.
  example: `anime frieren`

## manga

A manga from AniList. Adult titles never show.

**Permission:** Anyone

- **`manga (title)`**  
  Looks it up.

## character

An anime or manga character from AniList. Spoilers are left out.

**Permission:** Anyone

- **`character (name)`**  
  Looks it up.

## book

A book from Open Library: author, year, pages and rating.

**Permission:** Anyone

- **`book (title or author)`**  
  Looks it up.
  example: `book dune`

## movie

A movie's summary and poster, from Wikipedia.

**Permission:** Anyone

- **`movie (title)`**  
  Looks it up.
  example: `movie inception`

## tvshow

A TV show from TVmaze: premiere, status, rating and network.

**Permission:** Anyone

- **`tvshow (title)`**  
  Looks it up.
  example: `tvshow breaking bad`

## define

A word's meanings and examples.

**Permission:** Anyone

- **`define (word)`**  
  Looks it up.
  example: `define serendipity`

## itunes

A song from iTunes: album, release date, length and a preview.

**Permission:** Anyone

- **`itunes (song)`**  
  Looks it up.

## lyrics

A song's lyrics, from lrclib.net.

**Permission:** Anyone

- **`lyrics (song, optionally with the artist)`**  
  Looks them up.
  example: `lyrics bohemian rhapsody queen`

## ipinfo

An IP address's country, region, network and type. Never the city.

**Permission:** Anyone

- **`ipinfo (IP address)`**  
  Looks it up.

## duckduckgo

DuckDuckGo's instant answer for a search.

**Permission:** Anyone

- **`duckduckgo (search)`**  
  Searches.
  example: `duckduckgo rust language`

## nba

Today's NBA scoreboard from ESPN.

**Permission:** Anyone

- **`nba [team]`**  
  All games, or one team's.

## nfl

Today's NFL scoreboard from ESPN.

**Permission:** Anyone

- **`nfl [team]`**  
  All games, or one team's.

## nhl

Today's NHL scoreboard from ESPN.

**Permission:** Anyone

- **`nhl [team]`**  
  All games, or one team's.

## mlb

Today's MLB scoreboard from ESPN.

**Permission:** Anyone

- **`mlb [team]`**  
  All games, or one team's.

## soccer

A football league's scoreboard from ESPN. Premier League by default.

**Permission:** Anyone

- **`soccer [league]`**  
  laliga, seriea, bundesliga, ligue1, mls, ucl, uel or worldcup.
  example: `soccer laliga`

## fastforward

Skips ahead in the current song.

**Permission:** Anyone

- **`fastforward [seconds or mm:ss]`**  
  Forward 10 seconds, or the amount given.
  example: `fastforward 30`

## rewind

Goes back in the current song.

**Permission:** Anyone

- **`rewind [seconds or mm:ss]`**  
  Back 10 seconds, or the amount given.

## spotifyalbum

An album from Spotify. No linked account needed.

**Permission:** Anyone

- **`spotifyalbum (album, optionally with the artist)`**  
  Looks it up.
