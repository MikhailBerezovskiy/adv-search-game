from random import randint
from BaseAI_3 import BaseAI

class PlayerAI(BaseAI):
    
# ALGORITHM:
# getMove
# minmax of moves
#   max_func -> min_func -> max_func -> min_func ...
#   keep track of depth or time (decison should be less than 0.2s)
# apply alpha-beta pruning inside minmax
# minimax should use heuristic function for options comparison

# METHODS:
# getMove: return best move (I hope) to GameManager
# minmax: run search and control depth and time
# max_func: max of heuristic_func(move)
# min_func: insert new tile, get moves, min of heuristic_func(moves)
# alpha-beta: keep track of alpha and beta on the class self
# heuristic_func: should include some best practices adding or removing weight of grid
# min_heuristic: for min
# max_heuristic: for max
    
# keep track of the time or depth on minmax
    def __init__(self):
        self.depth = 2
        
    def getMove(self, grid):
        moves = grid.getAvailableMoves()
        
        if (self.minmax):
            # if search is implemented run search
            best_move = self.minmax(moves, grid, 0)
        else: 
            # if Not use random move
            best_move = moves[randint(0, len(moves)-1)]
        
        ## Return Best Move:
        return best_move if moves else None
        ## searching implementation below
        
        
        
    def minmax(self, moves, grid, depth):
        return self.max_func(moves, grid, depth, 5)[1]
        
    def max_func(self, moves, grid, depth, pmove):
        # max_func search best value move
        # input move, grid
        # return move
        depth += 1
        max_val = 0
        best_move = 0
        for move in moves:
            newGrid = grid.clone()
            newGrid.move(move)
            if depth == 1:
                pmove = move
            # print ('depth', depth, 'h=', self.heuristic_func(newGrid), 'pmove', pmove)
            h = self.heuristic_func(newGrid, move)
            if h > max_val:
                best_move = move
                max_val = h
                 
        if depth > self.depth:
            return [max_val, pmove]
        else:
            return self.min_func(newGrid, depth, pmove)
        
    
    def min_func(self, grid, depth, pmove):
        # min_func search worst case board
        # input board
        # return new grid
        min_val = 6
        spawns = []
        computer_moves = grid.getAvailableCells()
        for spawn in computer_moves:
            newGrid = grid.clone()
            newGrid.insertTile(spawn, 2)
            moves = newGrid.getAvailableMoves()
            sp_val = self.max_func(moves, newGrid, depth, pmove)
            if sp_val[0] < min_val:
                min_val = sp_val[0]
        return [min_val, pmove]
        
    def heuristic_func(self, grid, move):
        # heuristic_func should return value for particular move
        # input: move, grid after move, some current state values
        # return: weight for move
        # 0-up, 1-down, 2-left, 3-right
        h = 0
        h += [0,3,0,3][move]
        h += len(grid.getAvailableCells()) + grid.getMaxTile()
        # print ('h=', h)
        return h
