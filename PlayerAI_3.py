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
        self.lenmoves = len(moves)
        self.movenum = 0

        fn = 0
        best_move = moves[0]
        for move in moves:
            self.movenum += 1
            newGrid = grid.clone()
            newGrid.move(move)
            move_val = self.minmax(newGrid, 5, -100000, 100000, False)
            # print ('h=', move_val)
            if move_val > fn:
                best_move = move
                fn = move_val

        # print ('nodes:', self.expNodes, 'h:', move_val)
        # print(moves, 'val', fn, 'time:', self.t1-self.t0, 'nodes:', self.expNodes, ' movesH:', self.vals)
        return best_move if best_move in moves else None
        ## searching implementation below

    def minmax(self, node, depth, alpha, beta, max_player):
        self.t1 = time.clock()
        # print ('time:', t1 - self.t0)
        if depth == 0 or self.t1-self.t0 >= 0.15/self.lenmoves*self.movenum:
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

        g = grid
        gc = g.getAvailableCells()
        gm = grid.map
        h = 0
        m = g.getMaxTile()
        for x in range(g.size-1):
            for y in range(g.size-1):
                v = gm[x][y]
                i = x+1
                j = y+1

                h+= v - gm[i][y]/4
                h+= v - gm[x][j]
                h+= v - gm[i][j]/2

        h+= 2*h/(16-len(gc))
        if g.getMaxTile() != gm[0][0]:
            h -= g.getMaxTile()
        # h += len(gc) * h
        return h




    # gd = {
    #     0: 0,
    #     2: 0,
    #     4: 0,
    #     8: 0,
    #     16: 0,
    #     32: 0,
    #     64: 0,
    #     256: 0,
    #     128: 0,
    #     512: 0,
    #     1024: 0,
    #     2048: 0,
    #     4096: 0,
    #     8192: 0
    # }







        # # print ('init d', gd)
        # for i in gd:
        #     if gd[i] != 0 and i not in [0,8192]:
        #         # if i*2 <= gd[i]*i:
        #         #     gd[i*2] += 1
        #         #     gd[i] -= 2
        #         # for j in range(gd[i]):
        #         gd[i*2] += math.trunc(gd[i]*i/(i*2))
        #         gd[i] = gd[i]%2
        #         if gd[i] > 0:
        #             target = [i] + target
        # for i in range(16-len(target)):
        #     # target = [0] + target
        #     target.append(0)
        #
        # # target2 = source[:]
        # # target2.sort()
        # for i in range(len(source)):
        #     h -= abs(target[i] - source[i])
        #         # h += source[i] + target2[i]
        # h += len(gc)
        # print ('d', gd)
        # print ('s', source)
        # print ('t', target)
        # print ('h', h)
