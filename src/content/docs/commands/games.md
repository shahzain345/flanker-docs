---
title: Games commands
description: flanker games commands, their syntax, permissions and examples.
sidebar:
  order: 23
---

Commands are shown without a prefix. Use your server's prefix (default `,`) or mention flanker. `(round)` parameters are required, `[square]` are optional.

## tictactoe

Tic-tac-toe with buttons, against a member or against flanker.

**Permission:** Anyone

- **`tictactoe [member]`**  
  Challenges someone, or plays flanker without one.
  example: `tictactoe @friend`

## rps

Rock paper scissors. Against a member, neither of you sees the other's pick until both chose.

**Permission:** Anyone

- **`rps [member]`**  
  Plays with buttons.
- **`rps (rock/paper/scissors)`**  
  A quick round against flanker.
  example: `rps rock`

## russianroulette

Up to 10 players take turns with a six-chamber revolver. The last one standing wins.

**Permission:** Anyone

- **`russianroulette`**  
  Opens a game. Others press Join, it starts after 30 seconds or when you press Start.

## guessthenumber

flanker picks a number, everyone guesses. It reacts up for higher and down for lower.

**Permission:** Anyone

- **`guessthenumber [max]`**  
  Starts a game from 1 to max (100 by default).
  example: `guessthenumber 500`

## snake

Classic snake on a 9 by 9 board, moved with buttons. Only you can play your game.

**Permission:** Anyone

- **`snake`**  
  Starts a game.

## blacktea

Players join for 30 seconds, then take turns saying a real word that contains the 3 letters shown, within 10 seconds. Run out of time and you lose a life; everyone starts with 2. A word can only be used once per game. Last one standing wins.

**Permission:** Anyone

- **`blacktea`**  
  Opens a game. Others press Join, the host can press Start early.

## end

Stops the chat game running in this channel: black tea, green tea, red tea, the guessing games or guess the number.

**Permission:** Anyone

- **`end [game]`**  
  Ends the game here. Naming it is optional.
  *Game host or Manage Messages*  ·  example: `end blacktea`

## greentea

The first person to type a real word with the letters shown wins the round.

**Permission:** Anyone

- **`greentea [rounds]`**  
  Starts a game (5 rounds by default, up to 15).

## redtea

Everyone types words with the letters shown. The longest real word after 15 seconds wins the round.

**Permission:** Anyone

- **`redtea [rounds]`**  
  Starts a game (5 rounds by default, up to 15).

## guesstheflag

Shows a country's flag. The first to type the country wins the round.

**Permission:** Anyone

- **`guesstheflag [rounds] [solo]`**  
  Starts a game. With solo, only you can answer.
  example: `guesstheflag 10 solo`

## guessthelogo

Shows a brand's logo. The first to type the brand wins the round.

**Permission:** Anyone

- **`guessthelogo [rounds] [solo]`**  
  Starts a game. With solo, only you can answer.

## guesstheartist

Shows a popular artist's picture from the charts. The first to type their name wins the round.

**Permission:** Anyone

- **`guesstheartist [rounds] [solo]`**  
  Starts a game. With solo, only you can answer.

## guessthealbum

Shows a popular album's cover from the charts. The first to type its title wins the round.

**Permission:** Anyone

- **`guessthealbum [rounds] [solo]`**  
  Starts a game. With solo, only you can answer.
