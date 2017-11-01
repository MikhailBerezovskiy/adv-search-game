from random import randint
from BaseAI_3 import BaseAI
from Displayer_3  import Displayer
import time
import math

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

    def getMove(self, grid):

        moves = grid.getAvailableMoves()
        self.t0 = time.clock()
        self.movenum = 0
        self.lenmoves = len(moves)

        fn = 0
        best_move = moves[0]
        for move in moves:
            self.movenum += 1
            newGrid = grid.clone()
            newGrid.move(move)
            move_val = self.minmax(newGrid, 10, -100000, 100000, False)
            if move_val > fn:
                best_move = move
                fn = move_val
        return best_move if best_move in moves else None
        ## searching implementation below

    def minmax(self, node, depth, alpha, beta, max_player):
        self.t1 = time.clock()
        if depth == 0 or self.t1-self.t0 >= 0.15/self.lenmoves*self.movenum:
            return self.heuristic_func(node, depth)

        if max_player:
            v = -100000
            moves = node.getAvailableMoves()
            for move in moves:
                childNode = node.clone()
                childNode.move(move)
                v = max(v, self.minmax(childNode, depth-1, alpha, beta, False))
                alpha = max(v, alpha)
                if beta <= alpha:
                    break
            return v

        else:
            v = 100000
            av_cells = node.getAvailableCells()
            spawns = av_cells + av_cells
            len4 = len(av_cells)
            track = 0
            for spawn in spawns:
                childNode = node.clone()
                # if track > len4:
                #     insertVal = 4
                # else:
                insertVal = 2
                childNode.insertTile(spawn, insertVal)
                # track += 1

                v = min(v, self.minmax(childNode, depth-1, alpha, beta, True))
                beta = min (v, beta)
                if beta <= alpha:
                    break
            return v


    def heuristic_func(self, grid, depth):
        g = grid
        gc = g.getAvailableCells()
        m = grid.map
        h = 0
        gsum = 0
        frow = 0
        srow = 0
        diff = 0
        for x in range(g.size):
            for y in range(g.size):
                v = m[x][y]
                gsum += v
                if x==0:
                    frow += v
                if x==1:
                    srow += v
        for y in range(g.size-1):
            if m[0][y] > m[0][y+1]:
                diff += frow/4
        h += (diff/gsum) * 40

        h += frow / gsum * 40

        h += srow / gsum * 20
        # h += diff / gsum * 20
        h += len(gc) / 12 * 40

        # h += gsum/(16-len(gc))/g.getMaxTile()
        return h
