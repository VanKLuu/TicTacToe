# Build a Tic-Tac-Toe Game Engine With an AI Player in Python

This is a companion project to a Real Python [tutorial](https://realpython.com/tic-tac-toe-ai-python/) about implementing a game engine using the minimax algorithm as rudimentary artificial intelligence. It consists of two elements:

1. Game Engine Library
2. Game Front Ends

---

<<<<<<< HEAD
### Installing
=======
## Game Engine Library

The underlying game logic is encapsulated in a common library, which can be reused across multiple [game front ends](#game-front-ends) without duplicating the code.

## Installing with VSCode
After downloading and unzipping the GitHub code, open the unzipped folder in VSCode.
At the top of VSCode perform Ctrl+Shift+P and create an environment by typing Python: Create Environment... be sure to use venv for the environment
Follow the prompts and select the Global interpreter.
In the terminal run: "python -m pip install --editable library/"
Note: the editor may show that there are issue with some of the paths. After running the above command, the program will run
The program is now ready to be run. To run the program, make sure that you click on play.py under the frontend folder and then Run Python file.

### Installing through the CMD line
>>>>>>> Working-branch

Before proceeding, make sure you've created a virtual environment, activated it, and installed the tic-tac-toe game engine library into it:

```shell
$ cd tic-tac-toe/
$ python -m venv venv/
$ source venv/bin/activate
(venv) $ python -m pip install library/
```

## Game Front Ends

There are a few game front ends implemented in separate packages for you to try out. Before running them, make sure you've followed the earlier steps just described. Now, change the directory to the game front ends parent folder:

```shell
$ cd tic-tac-toe/frontends/
$ python play.py


