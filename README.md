# adv-search-game
2048-puzzle game with adversarial search, minimax, alpha-beta pruning, heuristic functions and weights

PlayerAI_3 - user's implemenation of search algorithms

To run the programm just run GameManager_3:
 $ python3(python) GameManager_3

class PlayerAI(BaseAI):
   -ALGORITHM:
   -getMove
   -minmax of moves
   -  max_func -> min_func -> max_func -> min_func ...
   -  keep track of depth or time (decison should be less than 0.2s)
   -apply alpha-beta pruning inside minmax
   -minimax should use heuristic function for options comparison

   -METHODS:
   -getMove: return best move (I hope) to GameManager
   -max_func: max of heuristic_func(move)
   -min_func: insert new tile, get moves, min of heuristic_func(moves)
   -alpha-beta: keep track of alpha and beta on the class self
   -heuristic_func: should include some best practices adding or removing weight of grid

   -keep track of the time or depth on minmax
