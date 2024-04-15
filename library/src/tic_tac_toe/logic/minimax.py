from functools import partial

from tic_tac_toe.logic.models import GameState, Mark, Move


def minimax(game_state: GameState, maximizer: Mark, is_maximizing: bool, depth: int = 0) -> int:
    if depth >= 4 or game_state.game_over:
        return game_state.evaluate_score(maximizer)

    if is_maximizing:
        best_score = float('-inf')
        for move in game_state.possible_moves:
            score = minimax(move.after_state, maximizer, False, depth + 1)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in game_state.possible_moves:
            score = minimax(move.after_state, maximizer, True, depth + 1)
            best_score = min(best_score, score)
        return best_score


def find_best_move(game_state: GameState) -> Move:
    maximizer = game_state.current_mark
    best_score = float('-inf')
    best_move = None

    for move in game_state.possible_moves:
        score = minimax(move.after_state, maximizer, False)
        if score > best_score:
            best_score = score
            best_move = move

    return best_move
