# Chess Engine Project

This is a chess engine built as part of a group project. It includes an AI that allows you to play against it, along with a GUI that lets you interact with the game board, analyze positions, and more.

## Features

- **AI Gameplay**: Play against the engine, which makes intelligent moves using algorithms like Minimax and Alpha-Beta pruning.
- **Position Analysis**: Analyze any given chess position by manually adding/removing pieces and adjusting castling rights.
- **Castling and Turn Management**: Toggle castling rights and switch turns between players.
- **User Interface**: A graphical interface to display the chessboard, pieces, and manage user interactions.
- **Board Setup**: Easily set up any board position to analyze or study the game.

## Folder Structure and Organization

The project is organized into the following directories:

### `src/`
This directory contains all the source code for the chess engine.

- **`ai/`**: Contains all AI-related logic, including:
  - Move evaluation
  - Minimax algorithm
  - Alpha-Beta pruning
  - Game heuristics and decision-making strategies

- **`game/`**: Core game logic, which handles:
  - Board state management
  - Move validation
  - Game rules (e.g., check, checkmate, castling, etc.)

- **`gui/`**: Code for the graphical user interface (GUI), including:
  - Rendering the chessboard and chess pieces
  - Handling user input (e.g., piece movements, menu interactions)
  - Displaying game status and messages

- **`utils/`**: Contains utility functions and helper code used across the project:
  - Constants (e.g., piece types, board dimensions)
  - Reusable utility functions (e.g., logging, data parsing, helpers)

### `tests/`
This directory holds all the tests for various components of the engine.

- **`ai_tests/`**: Unit and integration tests for the AI logic and algorithms:
  - Ensures correct move evaluation, AI decision-making, and algorithm functionality.

- **`game_tests/`**: Tests for the core game logic, including:
  - Game rules (e.g., castling, en passant, checkmate detection)
  - Board state management and move validation

- **`gui_tests/`**: Tests for the GUI, ensuring proper functionality and user interaction:
  - Verifies that the interface responds correctly to user inputs and displays the correct game state.

- **`utils_tests/`**: Tests for utility functions in the `utils/` directory:
  - Ensures that all helper functions work as expected and produce correct results.

### `assets/`
This directory contains all media files used in the project.

- **`images/`**: Chess piece images/icons for rendering in the GUI:
  - Each piece (king, queen, bishop, knight, rook, pawn) has an image for both white and black pieces.

- **`sounds/`** (optional): Contains sound files for optional game sound effects:
  - E.g., move sounds, check sounds, or other gameplay sounds.

### `docs/`
This directory is for internal documentation that explains the structure and logic of the project.

- Use this folder for:
  - Architecture overviews
  - Detailed explanations of algorithms (e.g., Minimax, Alpha-Beta pruning)
  - Game rules and logic explanations


## Getting Started

To get started with the project, follow these instructions.

### Prerequisites

You need to have **Python** and **Git** installed on your local machine.

- Install Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Install Git: [https://git-scm.com/downloads](https://git-scm.com/downloads)

### Clone the Repository

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/chess-engine.git
   cd chess-engine
(Optional) If you're using a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
Installing Dependencies
Install the necessary dependencies:

```bash
pip install -r requirements.txt
```
Note: If you don’t have a requirements.txt yet, you'll need to create one by listing the Python packages your project needs (e.g., pygame for the GUI, or numpy for any math-heavy operations in AI).

If you're using specific libraries for the GUI or AI, ensure they're installed and available.

Running the Project
After setting up, you can run the chess engine with the following command:

```bash
python src/gui/game_window.py
```
This will launch the graphical interface where you can interact with the chessboard, pieces, and play against the AI.

Alternatively, to just use the AI in a text-based environment (without the GUI):

```bash
python src/ai/play_against_ai.py
```
Testing
To run tests, simply execute:

```bash
pytest
```
This will run all unit and integration tests to ensure the engine and GUI are working as expected.

Contributing
We welcome contributions! If you'd like to contribute to the project, please follow these steps:

Fork the repository to your GitHub account.
Clone your fork to your local machine.
Create a new branch for your feature:
```bash
git checkout -b feature-branch-name
```
Make your changes, commit them, and push the branch to your fork:
```bash
git add .
git commit -m "Brief description of your changes"
git push origin feature-branch-name
```
Create a Pull Request (PR) to merge your changes into the dev branch.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
We would like to acknowledge the chess libraries and resources that helped us build this engine:
python-chess – A popular Python library for handling chess moves, board state, and legal moves.
Pygame – A library used to create the graphical user interface.
