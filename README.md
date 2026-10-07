# chess_walkthrough

Replays chess games on their own in a Pygame window. Each game is read from a PGN file and turned into simulated mouse drags, so the pieces move across the board as if someone were playing them. A card on the right shows the event, players, Elo ratings and date. When a game ends, win/lose/draw icons appear on the kings for about 10 seconds. Then the board switches to a random theme and the next game starts.

Built on top of [AlejoG10/python-chess-ai-yt](https://github.com/AlejoG10/python-chess-ai-yt).

## Requirements

- Python 3.8+
- `pip install pygame chess mutagen` (pygame 2.x; `chess` is the current name of python-chess)

## Setup

The individual game files are not tracked by git (`games/games/` is in `.gitignore`). Unzip them first:

```bash
cd games
unzip games.zip   # creates games/games/game2.pgn ... game752.pgn (751 games)
```

## Run

Run it from `src/`, because the asset and game paths are relative to that folder:

```bash
cd python-chess-ai-yt/src
python main.py    # opens a 1200x800 window
```

> **Don't touch the mouse while it plays.** The replay moves your real cursor. Moving the mouse over the right-hand card, clicking an empty square, or pressing `r` mid-game will crash it.

Press `t` to switch to a random board theme.

## How it works

1. `moves_to_coordinates.py` reads a PGN with python-chess and converts each move to pixel positions.
2. `mouse_events.py` turns those into a queue of mouse down / move / up events.
3. `main.py` posts one event every 15 ms, so the normal drag-and-drop code moves the pieces.
4. When the queue is empty, it waits 10 s, resets the board and loads the next game.

## Project layout

```
games/
  master_games*.pgn   # raw multi-game PGN downloads
  createGames.py      # run inside games/ to split them into games/game<N>.pgn
  migrateFiles.py     # moves a hard-coded list of games into PASSED/
  FAILED/             # games that don't replay correctly
python-chess-ai-yt/
  src/main.py         # entry point and event loop
  src/card.py         # game details card
  src/sound.py        # move sounds and background music
  assets/             # piece images, sounds, music
chess_walkthrough.py  # early prototype, NOT the app (crashes on missing images)
cards.py, fonts.py    # standalone demos for the card design and font choice
```

## Notes

- The first game is hard-coded in `src/mouse_events.py` (`game554.pgn`). After that, games play in alphabetical filename order (`game10`, `game100`, … `game2`, …).
- Pawns always promote to a queen, so games with an under-promotion go out of sync (e.g. `FAILED/game389.pgn`, which has `e8=N`).
- The red/green numbers in the top-left corner are a debug overlay showing mouse coordinates.
- Any `.mp3`/`.wav`/`.ogg` in `assets/music` can be picked. One random track plays once at startup; auto-advance is commented out in `main.py`.
- Background music: "Summer" by [Bensound](https://www.bensound.com).
