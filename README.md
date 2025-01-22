# Hangman Game

A simple command-line implementation of the classic Hangman game, written in Python. This is a beginner-level project created to practice Python basics.

## Features

- Randomly selects a word from a predefined list.
- Displays a visual representation of the hangman using ASCII art.
- Tracks correct and incorrect guesses.
- Limits the player to 6 incorrect guesses (lives).
- Displays a victory or defeat message at the end.

## How to Play

1. The program will randomly select a word from a predefined word list.
2. You have 6 lives to guess the word correctly, one letter at a time.
3. Each incorrect guess reduces your lives by 1, and the hangman figure progresses.
4. If you guess all the letters correctly before running out of lives, you win!
5. If you lose all your lives, the game ends, and the correct word is revealed.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/hangman.git
   cd hangman
   ```

2. Ensure you have the following files in your directory:
   - `hangman_word_list.py`: Contains a list of words for the game.
   - `hangman_art.py`: Contains ASCII art for the hangman and game logo.

3. Run the game:
   ```
   python hangman.py
   ```

