import textwrap
from typing import Iterable

from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.models import GameState, Mark

# to render the game screen
class ConsoleRenderer(Renderer):
    def render(self, game_state: GameState) -> None:
        clear_screen() # clear out the last state
        if game_state.winner:
            print_blinking(game_state.grid.cells, game_state.winning_cells)
            if game_state.winner == Mark.CROSS:
                print(f"Player 1 wins \N{party popper}")
            elif game_state.winner == Mark.NAUGHT:
                print(f"Player 2 wins \N{party popper}")
        else:
            print_solid(game_state.grid.cells) # print the new state
            if game_state.tie:
                print("No one wins this time \N{neutral face}")

# to clear the screen
def clear_screen() -> None:
    print("\033c", end="")

# to make the winning marks blink
def blink(text: str) -> str:
    return f"\033[5m{text}\033[0m"

# to print the blinking marks
def print_blinking(cells: Iterable[str], positions: Iterable[int]) -> None:
    mutable_cells = list(cells)
    for position in positions:
        mutable_cells[position] = blink(mutable_cells[position])
    print_solid(mutable_cells)

# to print the solid board
def print_solid(cells: Iterable[str]) -> None:
    print(
        textwrap.dedent(
            """\
             A   B   C   D
           -----------------
        1 ┆  {0} │ {1} │ {2} │ {3}
          ┆ ───┼───┼───┼───
        2 ┆  {4} │ {5} │ {6} │ {7}
          ┆ ───┼───┼───┼───
        3 ┆  {8} │ {9} │ {10} │ {11}
          ┆ ───┼───┼───┼───
        4 ┆  {12} │ {13} │ {14} │ {15}
    """
        ).format(*cells)
    )