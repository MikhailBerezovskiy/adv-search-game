from random import randint
from BaseAI_3 import BaseAI
from Displayer_3  import Displayer
import time

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
        self.t0 = time.clock()

        # self.vals = []
        moves = grid.getAvailableMoves()
        self.lenmoves = len(moves)
        self.movenum = 0
        self.expNodesLi = []
        fn = 0
        best_move = moves[0]
        for move in moves:
            self.movenum += 1
            self.expNodes = 0
            newGrid = grid.clone()
            newGrid.move(move)
            move_val = self.minmax(newGrid, 4, -100000, 100000, False)
            self.expNodesLi.append(self.expNodes)
            if move_val > fn:
                best_move = move
                fn = move_val
        print ('expNodes:', self.expNodesLi)
        # print ('nodes:', self.expNodes, 'h:', move_val)
        # print(moves, 'val', fn, 'time:', self.t1-self.t0, 'nodes:', self.expNodes, ' movesH:', self.vals)
        return best_move if best_move in moves else None
        ## searching implementation below

    def minmax(self, node, depth, alpha, beta, max_player):
        self.expNodes += 1
        self.t1 = time.clock()
        # print ('time:', t1 - self.t0)
        if depth == 0 or self.t1-self.t0 >= 0.18/self.lenmoves*self.movenum:
        # if depth == 0 or self.t1-self.t0 >= 0.15:
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
                if track > len4:
                    insertVal = 4
                else:
                    insertVal = 2
                childNode.insertTile(spawn, insertVal)

                v = min(v, self.minmax(childNode, depth-1, alpha, beta, True))
                beta = min (v, beta)
                track += 1
                if beta <= alpha:
                    break
            return v


    def heuristic_func(self, grid, depth):
        # heuristic_func should return value for particular move
        # input: move, grid after move, some current state values
        # return: weight for move
        # 0-up, 1-down, 2-left, 3-right

        g = grid
        # w = len(grid.getAvailableCells())/16
        gc = g.getAvailableCells()
        gm = grid.map
        gridSum = 0
        # countBig = 0
        gd = {
            0: 0,
            2: 1,
            4: 2,
            8: 3,
            16: 4,
            32: 5,
            64: 6,
            128: 7,
            256: 8,
            512: 9,
            1024: 10,
            2048: 11,
            4096: 12,
            8192: 13
        }
        h = 0
        h += len(gc)
        for x in range(g.size):
            for y in range(g.size):
                v = gd[gm[x][y]]
                # gridSum += v
                if x<3 and y<3:
                    h += v - gd[gm[x+1][y]]
                    h += v - gd[gm[x][y+1]]
                    h += v - gd[gm[x+1][y+1]]
                
        return h
