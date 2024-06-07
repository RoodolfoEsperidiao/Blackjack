# Blackjack Game

This project is a simple console-based Blackjack game implemented in Python. The game allows you to play Blackjack against the computer, including functionalities such as dealing cards, calculating scores, and determining the winner.

## Project Overview

### Files

- **art.py**: Contains the ASCII art for the game logo.
- **main.py**: Contains the main game logic and runs the game loop.

### Main Components

1. **Logo Display**: The game starts by displaying a logo stored in `art.py`.
2. **Game Loop**: The main game loop is controlled by `main.py`, where the game is played repeatedly until the player decides to stop.
3. **Card Dealing**: Cards are dealt randomly using Python's `random` module.
4. **Score Calculation**: The scores for both the player and the computer are calculated based on the dealt cards.
5. **Game Logic**: The game includes logic for hitting (drawing another card) and standing (keeping the current hand). The computer continues to draw cards until its score reaches at least 17.
6. **Result Display**: After each game, the final scores and results are displayed, and the player is asked if they want to play again.
7. **Console Clearing**: The console is cleared between games using the `replit` module to provide a clean slate for each new game.

### How It Works

- **Dealing Cards**: Each player (the user and the computer) starts with two cards. Additional cards are drawn as needed.
- **Blackjack Check**: The game checks for an initial Blackjack (a score of 21 with two cards).
- **Player Turn**: The player can choose to draw additional cards or keep their current hand.
- **Computer Turn**: The computer draws cards until its score reaches 17 or higher.
- **Result Determination**: The game compares the scores of the player and the computer to determine the winner.

### Running the Game

To play the game, run the `main.py` file. Follow the on-screen instructions to draw cards or stand, and see the results after each round. The game will continue to prompt you to play again until you choose to stop.
