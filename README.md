# Build a Tic-Tac-Toe Game Engine With an AI Player in Python

This is a companion project to a Real Python [tutorial](https://realpython.com/tic-tac-toe-ai-python/) about implementing a game engine using the minimax algorithm as rudimentary artificial intelligence. It consists of two elements:

1. Game Engine Library
2. Game Front Ends

---
### Layout of the Code
The codebase is organized into the following files and folders:
```shell
tic-tac-toe/ # This is the root folder of the project
│
├── frontends/ # Contains the user interface components for interacting with the game
│   │
│   └── console/ # The console-based user interface directory
│       ├── __init__.py # Initializes the console frontend package.
│       ├── __main__.py # Entry point for running the console-based game.
│       ├── args.py # Defines command-line arguments and their parsing logic.
│       ├── cli.py # Implements the command-line interface for the game.
│       ├── players.py # Defines player classes for human and AI opponents
│       └── renderers.py # Contains rendering logic for displaying the game state
│
└── library/ # Contains the core logic and components of the Tic-Tac-Toe game
    │
    ├── src/ # Source code directory
    │   │
    │   └── tic_tac_toe/ # Main package for the Tic-Tac-Toe game
    │       │
    │       ├── game/ # Subpackage containing game-related functionality.
    │       │   ├── __init__.py # Initializes the game package
    │       │   ├── engine.py # Implements the game engine for managing game state and turns
    │       │   ├── players.py # Defines player classes and their behavior.
    │       │   └── renderers.py # Contains rendering logic for different user interfaces.
    │       │
    │       ├── logic/ # Subpackage housing the core game logic
    │       │   ├── __init__.py # Initializes the logic package
    │       │   ├── exceptions.py # Defines custom exception classes
    │       │   ├── minimax.py # Implements the minimax algorithm for AI opponents.
    │       │   ├── models.py # Defines data models for representing the game state
    │       │   └── validators.py # Contains functions for validating game state and moves.
    │       │
    │       └── __init__.py # Initializes the main Tic-Tac-Toe package.
    │
    └── pyproject.toml # Configuration file for the project.
```
### Installing through the CMD line
Before proceeding, make sure you've created a virtual environment, activated it, and installed the tic-tac-toe game engine library into it:

```shell
$ cd tic-tac-toe/
$ python -m venv venv/
$ source venv/bin/activate
(venv) $ python -m pip install library/
```

## Installing through VS Code
After downloading and unzipping the GitHub code, open the unzipped folder in VS Code.

In the search bar at the top of VS Code:
1. Ctrl + Shift + P
2. create a virtual environment by typing "Python: Create Environment..."
Note: be sure to use venv for the environment
3. follow the prompts and select the Global interpreter

In the terminal:
1. run "python -m pip install --editable library/"
2. if the editor still shows that there is an issue with some of the paths, run step 1 again. Close and then reopen VS Code.

## Game Front Ends

There are a few game front ends implemented in separate packages for you to try out. Before running them, make sure you've followed the earlier steps just described. Now, change the directory to the game front ends parent folder:

```shell
$ cd tic-tac-toe/frontends/
$ python play.py
```

## Running the Game through VS Code
1. make sure that you are in play.py in the frontends folder
2. click on Run Python File
