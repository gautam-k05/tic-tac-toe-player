# Tic-Tac-Toe Game with AI

This is a Python-based Tic-Tac-Toe game featuring a graphical interface using Pygame and an AI opponent using the minimax algorithm. The game allows a user to play either as 'X' or 'O' against an AI that calculates the optimal move.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Gameplay](#gameplay)

## Features

- User can choose to play as 'X' or 'O'.
- AI opponent using the minimax algorithm for optimal moves.
- Graphical interface created with Pygame.
- Displays the game board and the current state (whose turn it is, winner, or tie).

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/gautam-k05/tic-tac-toe-player.git
    ```

2. **Navigate to the project directory:**

    ```sh
    cd tic-tac-toe
    ```

3. **Install the required libraries:**

    Ensure you have Python installed. You can install the required libraries using pip:

    ```sh
    pip install pygame
    ```
## Usage

1. **Run the game:**

    ```sh
    python runner.py
    ```

2. **Gameplay:**
    - When the game starts, you will be prompted to choose to play as 'X' or 'O'.
    - Click on the respective button to make your choice.
    - The game board will be displayed, and you can click on an empty cell to make your move.
    - The AI will make its move after you.
    - The game will display messages for whose turn it is, or if the game is over and the result.

## Files

- `runner.py`: The main file to run the Tic-Tac-Toe game.
- `tictactoe.py`: Contains the logic for the Tic-Tac-Toe game, including the minimax algorithm.
- `OpenSans-Regular.ttf`: Font file used for rendering text in the game.

## Gameplay

- The game starts with a prompt to choose your player ('X' or 'O').
- The game board is a 3x3 grid, and the player and AI take turns to place their marks.
- The goal is to align three of your marks vertically, horizontally, or diagonally.
- The game ends when a player wins or if the board is full (a tie).
- A "Play Again" button is displayed at the end of the game to start a new game.