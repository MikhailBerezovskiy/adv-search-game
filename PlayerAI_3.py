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
        d = {
            0: 0,
            2: 0,
            4: 0,
            8: 0,
            16: 0,
            32: 0,
            64: 0,
            128: 0,
            256: 0,
            512: 0,
            1024: 0,
            2048: 0,
            4096: 0,
            8192: 0
        }
        h = 0
        
        # cornering
        s = 0
        cr = 0
        sLi = []
        for x in range (g.size):
            for y in range (g.size):
                v = m[x][y]
                # sLi.append(v)
                # d[v] += 1
                s += v
                if x<3 and y<3:
                    cr += v - m[x+1][y]
                    cr += v - m[x][y+1]
                    # cr += v - m[x+1][y+1]
        
        aver = s / (16 - len(gc))
        for x in range (g.size):
            for y in range (g.size):
                v = m[x][y]
                h += abs(v - aver)
                if x<3 and v<m[x+1][y]:
                    h -= v
                
        # cornering = h / (s * 3)
        # h = h * (len(gc))/16
        # h += len(gc)
        # avcells  = len(gc)/16
        # 
        # 
        # # greed
        # greedLi = []
        # gs = 0
        # for i in d:
        #     if i != 0 and i != 8192:
        #         # print (d[i], d[i*2])
        #         d[i*2] += math.trunc(d[i]*i/(i*2))
        #         d[i] = d[i]%2
        #         if d[i] != 0:
        #             for j in range(d[i]):
        #                 greedLi = [i] + greedLi
        # for i in range(16 - len(greedLi)):
        #     greedLi.append(0)
        # # sLi.sort()
        # gdiff = 0
        # for i in range(16):
        #     if greedLi[i] != 0:
        #         gdiff += sLi[i]
        # greed = gdiff / s
        h += len(gc) * aver
        h += cr
        # print ('corn_greed', cornering, greed)
        return (h)
