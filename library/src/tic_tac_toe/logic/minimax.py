from functools import partial
from tic_tac_toe.logic.models import GameState, Mark, Move


def minimax(game_state: GameState, maximizer: Mark, is_maximizing: bool, depth: int = 0, alpha: float = float('-inf'), beta: float = float('inf')) -> int:
    if depth >= 4 or game_state.game_over:
        return game_state.evaluate_score(maximizer)

    if is_maximizing:
        best_score = float('-inf')
        for move in game_state.possible_moves:
            score = minimax(move.after_state, maximizer, False, depth + 1, alpha, beta)
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if alpha >= beta:
                break
        return best_score
    else:
        best_score = float('inf')
        for move in game_state.possible_moves:
            score = minimax(move.after_state, maximizer, True, depth + 1, alpha, beta)
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if alpha >= beta:
                break
        return best_score
    
def reverse_minimax(game_state: GameState, minimizer: Mark, is_minimizing: bool, depth: int = 0, alpha: float = float('-inf'), beta: float = float('inf')) -> int:
    if depth >= 5 or game_state.game_over:
        return game_state.evaluate_score(minimizer)
    
    if is_minimizing:
        worst_score = float('inf')
        for move in game_state.possible_moves:
            current_score = reverse_minimax(move.after_state, minimizer, False, depth + 1, alpha, beta)
            worst_score = min(worst_score, current_score)
            if worst_score >= beta:
                break
            beta = min(worst_score, beta)
        return worst_score
    else:
        best_score = float('-inf')
        for move in game_state.possible_moves:
            current_score = reverse_minimax(move.after_state, minimizer, True, depth + 1, alpha, beta)
            best_score = max(best_score, current_score)
            alpha = max(alpha, best_score)
            if alpha >= beta:
                break
        return best_score

    # if depth >= 4 or game_state.game_over:
    #     return game_state.evaluate_score(minimizer)
    
    # if is_minimizing:
    #     worst_score = float('inf')
    #     for move in game_state.possible_moves:
    #         score = reverse_minimax(move.after_state, minimizer, False, depth + 1, alpha, beta)
    #         worst_score = min(worst_score, score)
    #         beta = min(beta, worst_score)
    #         if alpha >= beta:
    #             break
    #     return worst_score
    # else:
    #     worst_score = float('-inf')
    #     for move in game_state.possible_moves:
    #         score = reverse_minimax(move.after_state, minimizer, True, depth + 1, alpha, beta)
    #         worst_score = max(worst_score, score)
    #         alpha = max(alpha, worst_score)
    #         if alpha >= beta:
    #             break
    #     return worst_score

def find_best_move(game_state: GameState, mark: Mark) -> Move:
    # maximizer = game_state.current_mark
    maximizer = mark
    best_score = float('-inf')
    best_move = None

    for move in game_state.possible_moves:
        score = minimax(move.after_state, maximizer, False)
        if score > best_score:
            best_score = score
            best_move = move

    return best_move

def find_worst_move(game_state: GameState, mark: Mark) -> Move:
    # minimizer = game_state.current_mark
    minimizer = mark
    worst_score = float('inf')
    worst_move = None

    for move in game_state.possible_moves:
        score = reverse_minimax(move.after_state, minimizer, True)
        if score < worst_score:
            worst_score = score
            worst_move = move

    return worst_move