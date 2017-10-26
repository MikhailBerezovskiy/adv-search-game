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
# max_func: max of heuristic_func(move)
# min_func: insert new tile, get moves, min of heuristic_func(moves)
# alpha-beta: keep track of alpha and beta on the class self
# heuristic_func: should include some best practices adding or removing weight of grid
    
# keep track of the time or depth on minmax
    
        
    def getMove(self, grid):
        moves = grid.getAvailableMoves()
        
        if (self.search):
            # if search is implemented run search
            best_move = self.max_func(moves, grid)
        else: 
            # if Not use random move
            best_move = moves[randint(0, len(moves)-1)]
        
        ## Return Best Move:
        return best_move if moves else None
        ## searching implementation below
        
        
        
    def search(self):
        return True
        
    def max_func(self, moves, grid):
        # max_func search best value move
        # input move, grid
        # return move
        max_val = 0
        best_move = [0]
        for move in moves:
            newGrid = grid.clone()
            newGrid.move(move)
            move_val = self.heuristic_func(newGrid, move, grid.getMaxTile(), grid.getAvailableCells())
            if move_val > max_val:
                max_val = move_val
                best_move = [move]
            elif move_val == max_val:
                best_move.append(move)
        print (best_move)
        return best_move[randint(0, len(best_move)-1)]

    def min_func(self,grid):
        # min_func search worst case board
        # input board
        # return new grid
        min_val = 0
        worst_move = 0
        computer_moves = grid.getAvailableCells()
        for tile_pos in computer_moves:
            newGrid = grid.clone()
            newGrid.insertTile(tile_pos, 2)
            move_val = newGrid.getMaxTile()
            if move_val < min_val:
                min_val = move_val
        return min_val

    def heuristic_func(self, grid, move, cur_max, cur_avail):
        # heuristic_func should return value for particular move
        # input: move, grid after move, some current state values
        # return: weight for move
        h = 0
        if move == 2:
            h  -= 1
        elif move == 1:
            h += 1
        else:
            h += 2
        
        if grid.getMaxTile() > cur_max:
            h += 2
        if grid.getAvailableCells() > cur_avail:
            h += 2

        return h
