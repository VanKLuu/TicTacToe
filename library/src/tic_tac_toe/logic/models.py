import enum
import re
import random
from dataclasses import dataclass
from functools import cached_property
from tic_tac_toe.logic.exceptions import InvalidMove, UnknownGameScore
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.validators import validate_game_state, validate_grid 

# the winning patterns
WINNING_PATTERNS = (
    "????............",
    "....????........",
    "........????....",
    "............????",
    "?...?...?...?...",
    ".?...?...?...?..",
    "..?...?...?...?.",
    "...?...?...?...?",
    "?....?....?....?",
    "...?..?..?..?...",   
)
# creating the characters for the players
class Mark(str, enum.Enum):
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> "Mark":
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT

# creating the board  
@dataclass(frozen=True)
class Grid:
    # creating the board cells
    cells: str = " " * 16

    # for error checking to make sure valid data
    def __post_init__(self) -> None:
        validate_grid(self)
    
    # determining the number of Xs on the board
    @cached_property
    def x_count(self) -> int:
        return self.cells.count("X")
    
    # determining the number of Os on the board
    @cached_property
    def o_count(self) -> int:
        return self.cells.count("O")
    
    # determining the number of available spaces on the board
    @cached_property
    def empty_count(self) -> int:
        return self.cells.count(" ")
    
# for carrying the information of the game
@dataclass(frozen=True)
class Move:
    mark: Mark
    cell_index: int
    before_state: "GameState"
    after_state: "GameState"

# for keeping track of the state of the game
@dataclass(frozen=True)
class GameState:
    grid: Grid
    starting_mark: Mark = Mark("X")

    def __post_init__(self) -> None:
        validate_game_state(self)

    # returns who will make the next move
    @cached_property
    def current_mark(self) -> Mark:
        if self.grid.x_count == self.grid.o_count:
            return self.starting_mark
        else:
            return self.starting_mark.other
        
    # for determining if the game has started
    @cached_property
    def game_not_started(self) -> bool:
        return self.grid.empty_count == 16
    
    # for determining if the game is over
    @cached_property
    def game_over(self) -> bool:
        return self.winner is not None or self.tie
    
    # for determining if there is a tie (see if all squares are full)
    @cached_property
    def tie(self) -> bool:
        return self.winner is None and self.grid.empty_count == 0

    # for determining if either player won
    @cached_property
    def winner(self) -> Mark | None:
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return mark
        return None
    
    # for determining what the winning cells were
    @cached_property
    def winning_cells(self) -> list[int]:
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return [
                        match.start()
                        for match in re.finditer(r"\?", pattern)
                    ]
        return []
    
    # for determining the possible moves
    @cached_property
    def possible_moves(self) -> list[Move]:
        moves = []
        if not self.game_over:
            for match in re.finditer(r"\s", self.grid.cells):
                moves.append(self.make_move_to(match.start()))
        return moves
    
    # to allow for the AI to make a random move (initially)
    def make_random_move(self) -> Move | None:
        try:
            return random.choice(self.possible_moves)
        except IndexError:
            return None
    
    # for making a move
    def make_move_to(self, index: int) -> Move:
        if self.grid.cells[index] != " ":
            raise InvalidMove("Cell is not empty")
        return Move(
            mark=self.current_mark,
            cell_index=index,
            before_state=self,
            after_state=GameState(
                Grid(
                    self.grid.cells[:index]
                    + self.current_mark
                    + self.grid.cells[index + 1:]
                ),
                self.starting_mark,
            ),
        )
    
    # for the minimax algorithm
    def evaluate_score(self, mark: Mark) -> int:
        if self.tie and mark == "X":
            return 2 # tie is the goal
        elif self.tie and mark == "O":
            return -1 # goal is to win
        elif self.winner == mark and mark == "X":
            return 2 # don't really care if win
        elif self.winner == mark and mark == "O":
            return 2 # goal is to win
        elif self.winner == mark.other and mark == "X":
            return -1 # don't want to lose
        elif self.winner == mark.other and mark == "O":
            return -2 # don't want to lose
        else:
            return self.evaluation_function(mark)
        
    def evaluation_function(self, mark: Mark) -> int:
        index = 0
        while index < 16:
            # Check the rows to see who is winning (instance of 3 in a row)
            if self.grid.cells[index] == self.grid.cells[index + 1] and self.grid.cells[index + 1] == self.grid.cells[index + 2] and self.grid.cells[index + 3] == " ":
                if self.grid.cells[index] == mark:
                    return 2
                elif self.grid.cells[index] == mark.other:
                    return -2
            elif self.grid.cells[index + 3] == self.grid.cells[index + 2] and self.grid.cells[index + 2] == self.grid.cells[index + 1] and self.grid.cells[index] == " ":
                if self.grid.cells[index + 3] == mark:
                    return 2
                elif self.grid.cells[index] == mark.other:
                    return -2
            
            # instance of 2 in a row
            if self.grid.cells[index] == self.grid.cells[index + 1] and self.grid.cells[index + 2] == " " and self.grid.cells[index + 3] == " ": # far left
                if self.grid.cells[index] == mark:
                    return 2
                elif self.grid.cells[index] == mark.other:
                    return -2
            elif self.grid.cells[index + 3] == self.grid.cells[index + 2] and self.grid.cells[index + 1] == " " and self.grid.cells[index] == " ": # far right
                if self.grid.cells[index + 3] == mark:
                    return 2
                elif self.grid.cells[index] == mark.other:
                    return -2
            elif self.grid.cells[index] == " " and self.grid.cells[index + 1] == self.grid.cells[index + 2] and self.grid.cells[index + 3] == " ": # in the middle
                if self.grid.cells[index + 1] == mark:
                    return 2
                elif self.grid.cells[index + 1] == mark.other:
                    return -2
            elif self.grid.cells[index] == self.grid.cells[index + 2] and self.grid.cells[index + 1] == " " and self.grid.cells[index + 3] == " ": # split left
                if self.grid.cells[index] == mark:
                    return 1 # more risky so worth less
                elif self.grid.cells[index] == mark.other:
                    return -1
            elif self.grid.cells[index + 3] == self.grid.cells[index + 1] and self.grid.cells[index + 2] == " " and self.grid.cells[index] == " ": # split right
                if self.grid.cells[index + 3] == mark:
                    return 1
                elif self.grid.cells[index + 3] == mark.other:
                    return -1
            index += 4
            
        # check the columns to see whose winning
        index = 0
        while index < 4:
            # instance of 3 in a row
            if self.grid.cells[index] == self.grid.cells[index + 4] and self.grid.cells[index + 4] == self.grid.cells[index + 8] and self.grid.cells[index + 12] == " ":
                if self.grid.cells[index] == mark:
                    return 2
                elif self.grid.cells[index] == mark.other:
                    return -2
            elif self.grid.cells[index + 12] == self.grid.cells[index + 8] and self.grid.cells[index + 8] == self.grid.cells[index + 4] and self.grid.cells[index] == " ":
                if self.grid.cells[index + 12] == mark:
                    return 2
                elif self.grid.cells[index] == mark.other:
                    return -2
                
            # instance of two in a row
            if self.grid.cells[index] == self.grid.cells[index + 4] and self.grid.cells[index + 8] == " " and self.grid.cells[index + 12] == " ": # top
                if self.grid.cells[index] == mark:
                    return 2
                elif self.grid.cells[index] == mark.other:
                    return -2
            elif self.grid.cells[index + 12] == self.grid.cells[index + 8] and self.grid.cells[index + 4] == " " and self.grid.cells[index] == " ": # bottom
                if self.grid.cells[index + 12] == mark:
                    return 2
                elif self.grid.cells[index] == mark.other:
                    return -2
            elif self.grid.cells[index] == " " and self.grid.cells[index + 4] == self.grid.cells[index + 8] and self.grid.cells[index + 12] == " ": # in the middle
                if self.grid.cells[index + 4] == mark:
                    return 2
                elif self.grid.cells[index + 4] == mark.other:
                    return -2
            elif self.grid.cells[index] == self.grid.cells[index == 8] and self.grid.cells[index + 4] == " " and self.grid.cells[index + 12] == " ": # split up
                if self.grid.cells[index] == mark:
                    return 1 # worth less because more risky
                elif self.grid.cells[index] == mark.other:
                    return -1
            elif self.grid.cells[index + 12] == self.grid.cells[index + 4] and self.grid.cells[index + 8] == " " and self.grid.cells[index] == " ": # split down
                if self.grid.cells[index + 12] == mark:
                    return 1
                elif self.grid.cells[index + 12] == mark.other:
                    return -1
            index += 1

        # check the right diagonal to see whose winning
        index = 0
        # instance of 3 in a row
        if self.grid.cells[index] == self.grid.cells[index + 5] and self.grid.cells[index + 5] == self.grid.cells[index + 10] and self.grid.cells[index + 15] == " ":
            if self.grid.cells[index] == mark:
                return 2
            elif self.grid.cells[index] == mark.other:
                return -2
        elif self.grid.cells[index + 15] == self.grid.cells[index + 10] and self.grid.cells[index + 10] == self.grid.cells[index + 5] and self.grid.cells[index] == " ":
            if self.grid.cells[index + 15] == mark:
                return 2
            elif self.grid.cells[index + 15] == mark.other:
                return -2
        
        # instance of 2 in a row
        if self.grid.cells[index] == self.grid.cells[index + 5] and self.grid.cells[index + 10] == " " and self.grid.cells[index + 15] == " ":
            if self.grid.cells[index] == mark:
                return 2
            elif self.grid.cells[index] == mark.other:
                return -2
        elif self.grid.cells[index + 15] == self.grid.cells[index + 10] and self.grid.cells[index + 5] == " " and self.grid.cells[index] == " ":
            if self.grid.cells[index + 15] == mark:
                return 2
            elif self.grid.cells[index + 15] == mark.other:
                return -2 
        elif self.grid.cells[index] == " " and self.grid.cells[index + 5] == self.grid.cells[index + 10] and self.grid.cells[index + 15] == " ":
            if self.grid.cells[index + 5] == mark:
                return 2
            elif self.grid.cells[index + 5] == mark.other:
                return -2

        # check the other diagonal to see whose winning
        # instance of 3 in a row
        if self.grid.cells[index + 3] == self.grid.cells[index + 6] and self.grid.cells[index + 9] == self.grid.cells[index + 9] and self.grid.cells[index + 12] == " ":
            if self.grid.cells[index + 3] == mark:
                return 2
            elif self.grid.cells[index + 3] == mark.other:
                return -2
        elif self.grid.cells[index + 12] == self.grid.cells[index + 9] and self.grid.cells[index + 9] == self.grid.cells[index + 6] and self.grid.cells[index + 3] == " ":
            if self.grid.cells[index + 12] == mark:
                return 2
            elif self.grid.cells[index + 12] == mark.other:
                return -2
        
        # instance of 2 in a row
        if self.grid.cells[index + 3] == self.grid.cells[index + 6] and self.grid.cells[index + 9] == " " and self.grid.cells[index + 12] == " ":
            if self.grid.cells[index + 3] == mark:
                return 2
            elif self.grid.cells[index + 3] == mark.other:
                return -2
        elif self.grid.cells[index + 12] == self.grid.cells[index + 9] and self.grid.cells[index + 6] == " " and self.grid.cells[index + 3] == " ":
            if self.grid.cells[index + 12] == mark:
                return 2
            elif self.grid.cells[index + 12] == mark.other:
                return -2 
        elif self.grid.cells[index + 3] == " " and self.grid.cells[index + 6] == self.grid.cells[index + 9] and self.grid.cells[index + 12] == " ":
            if self.grid.cells[index + 6] == mark:
                return 2
            elif self.grid.cells[index + 6] == mark.other:
                return -2
            
        return 0
