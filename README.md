# Chess Engine Project

This is a chess engine built as part of a group project. It includes an AI that allows you to play against it, along with a GUI that lets you interact with the game board, analyze positions, and more.

## Features

- **AI Gameplay**: Play against the engine, which makes intelligent moves using algorithms like Minimax and Alpha-Beta pruning.
- **Position Analysis**: Analyze any given chess position by manually adding/removing pieces and adjusting castling rights.
- **Castling and Turn Management**: Toggle castling rights and switch turns between players.
- **User Interface**: A graphical interface to display the chessboard, pieces, and manage user interactions.
- **Board Setup**: Easily set up any board position to analyze or study the game.

## Project Structure

The project is organized into several directories:

chess-engine/

├── .gitignore

├── README.md

├── LICENSE

├── docs/ # Documentation

├── src/ # Source code for the chess engine

│ ├── ai/ # AI-related code (e.g., Minimax, evaluations)

│ ├── game/ # Core game logic (board state, move validation)

│ ├── gui/ # GUI code (graphics, UI interactions)

│ └── utils/ # Utility functions (e.g., logging, helpers)

├── tests/ # Unit tests and integration tests

│ ├── ai_tests/ # Tests related to the AI logic

│ ├── game_tests/ # Tests for game rules and logic

│ ├── gui_tests/ # Tests for GUI functionality

│ └── utils_tests/ # Tests for utility functions

├── assets/ # Graphics, icons, and other media files

│ ├── images/ # Chess piece images/icons

│ └── sounds/ # Optional sound effects

└── .github/ # GitHub-specific configurations (optional)

└── workflows/ # GitHub Actions for CI/CD, if you decide to use it


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
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Installing Dependencies
Install the necessary dependencies:

bash
Copy code
pip install -r requirements.txt
Note: If you don’t have a requirements.txt yet, you'll need to create one by listing the Python packages your project needs (e.g., pygame for the GUI, or numpy for any math-heavy operations in AI).

If you're using specific libraries for the GUI or AI, ensure they're installed and available.

Running the Project
After setting up, you can run the chess engine with the following command:

bash
Copy code
python src/gui/game_window.py
This will launch the graphical interface where you can interact with the chessboard, pieces, and play against the AI.

Alternatively, to just use the AI in a text-based environment (without the GUI):

bash
Copy code
python src/ai/play_against_ai.py
Testing
To run tests, simply execute:

bash
Copy code
pytest
This will run all unit and integration tests to ensure the engine and GUI are working as expected.

Contributing
We welcome contributions! If you'd like to contribute to the project, please follow these steps:

Fork the repository to your GitHub account.
Clone your fork to your local machine.
Create a new branch for your feature:
bash
Copy code
git checkout -b feature-branch-name
Make your changes, commit them, and push the branch to your fork:
bash
Copy code
git add .
git commit -m "Brief description of your changes"
git push origin feature-branch-name
Create a Pull Request (PR) to merge your changes into the dev branch.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Folder Structure and Organization
src/
ai/: Contains all the AI logic, including move evaluation, Minimax algorithm, and any game heuristics.
game/: Handles game rules, board state, and move validation.
gui/: Code for the graphical user interface, including rendering the chessboard, pieces, and handling user input.
utils/: Contains utility functions, constants, and other reusable code snippets.
tests/
ai_tests/: Tests for the AI logic and algorithms.
game_tests/: Tests for game rules and mechanics (e.g., castling, en passant, checkmate detection).
gui_tests/: Tests for the GUI functionality and interaction.
utils_tests/: Tests for utility functions.
assets/
images/: Chess piece images for rendering on the GUI.
sounds/ (optional): If you’re adding sound effects to the game, store them here.
docs/
Use this folder for any internal documentation, such as architecture overviews, algorithms used (e.g., Minimax), or a detailed explanation of the game rules.

Acknowledgments
We would like to acknowledge the chess libraries and resources that helped us build this engine:
python-chess – A popular Python library for handling chess moves, board state, and legal moves.
Pygame – A library used to create the graphical user interface.
