# Build a Tic-Tac-Toe Game Engine With an AI Player in Python

This is a companion project to a Real Python [tutorial](https://realpython.com/tic-tac-toe-ai-python/) about implementing a game engine using the minimax algorithm as rudimentary artificial intelligence. It consists of two elements:

1. Game Engine Library
2. Game Front Ends

---
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

## Running the Game through VS Code
1. make sure that you are in play.py in the frontends folder
2. click on Run Python File
