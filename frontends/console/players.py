import re
from tic_tac_toe.game.players import Player
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.models import GameState, Move, Mark
from tic_tac_toe.game.players import SabotageComputerPlayer

# class for a human player
class ConsolePlayer(Player):
    def __init__(self, mark: Mark) -> None:
        super().__init__(mark)
        self.sabotage_player = SabotageComputerPlayer(self.mark.other)
    def get_move(self, game_state: GameState) -> Move | None:
        while not game_state.game_over:
            try:
                move = self.sabotage_player.get_move(game_state)
                print(f"Sabotage recommendation: {index_to_grid(move.cell_index)} ")
                index = grid_to_index(input(f"Player 1's move: ").strip())
            except ValueError:
                print("Please provide coordinates in the form of A1 or 1A")
            else:
                try:
                    return game_state.make_move_to(index)
                except InvalidMove:
                    print("That cell is already occupied.")
        return None
    
# to convert user input to grid mapping
def grid_to_index(grid: str) -> int:
    if re.match(r"[abcdABCD][1234]", grid):
        col, row = grid
    elif re.match(r"[1234][abcdABCD]", grid):
        row, col = grid
    else:
        raise ValueError("Invalid grid coordinates")
    return 4 * (int(row) - 1) + (ord(col.upper()) - ord("A"))

    # to convert index to grid mapping


def index_to_grid(index: int) -> str:
    col = chr((index % 4) + ord("A"))
    row = str((index // 4) + 1)
    return col + row
