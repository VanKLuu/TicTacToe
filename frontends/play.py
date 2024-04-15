from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import MinimaxComputerPlayer, RandomComputerPlayer
from tic_tac_toe.logic.models import Mark

from console.renderers import ConsoleRenderer
from console.players import ConsolePlayer

player1 = ConsolePlayer(Mark("X"))
player2= RandomComputerPlayer(Mark("O")) # for testing purposes until implement eval function
# player2= MinimaxComputerPlayer(Mark("O"))

TicTacToe(player1, player2, ConsoleRenderer()).play()