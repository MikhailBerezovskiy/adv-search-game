from random import randint
from BaseAI_3 import BaseAI

class PlayerAI(BaseAI):

    def getMove(self, grid):
        moves = grid.getAvailableMoves()
        best_move = self.max_func(moves, grid)
        #print (best_move)
        return best_move if moves else None

    def max_func(self, moves, grid):
        max_val = 0
        best_move = 0
        for move in moves:
            newGrid = grid.clone()
            newGrid.move(move)
            move_val = self.min_func(newGrid)
            if move_val > max_val:
                max_val = move_val
                best_move = move
        return best_move

    def min_func(self,grid):
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

    def heuristic_func(self,grid):
        return grid.getMaxTile()
