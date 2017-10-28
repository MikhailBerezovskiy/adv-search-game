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

    def getMove(self, grid):
        moves = grid.getAvailableMoves()

        best_move = -1
        fn = 0
        for move in moves:
            move_val = self.minmax([move], grid, move==moves[0])
            if move_val > fn:
                best_move = move
                fn = move_val

        ## Return Best Move:
        if best_move not in moves and len(moves) > 0:
            best_move = moves[0]
        return best_move if moves else None
        ## searching implementation below

    def minmax(self, moves, grid, first_child):
        self.depth = 10
        self.alpha = 100
        self.expNodes = 0
        return self.max_func(moves, grid, 0, first_child)

    def max_func(self, moves, grid, depth, first_child):
        # max of moves
        max_val = 0
        for move in moves:
            self.expNodes += 1
            # print('expNodes', self.expNodes)
            newGrid = grid.clone()
            newGrid.move(move)
            hn = self.heuristic_func(newGrid, move)
            if depth >= self.depth:
                if hn > max_val:
                    max_val = hn
            else:
                if hn < self.alpha:
                    self.alpha = hn
                else:
                    if not first_child:
                        return self.alpha
                depth += 1
                return self.min_func(newGrid, depth)
        return max_val

    def min_func(self, grid, depth):
        # min of
        spawns = []
        avail = grid.getAvailableCells()
        for spawn in avail:
            newGrid = grid.clone()
            newGrid.insertTile(spawn, 2)
            newMoves = newGrid.getAvailableMoves()
            first_child = spawn == avail[0]
            spawns.append(self.max_func(newMoves, newGrid, depth, first_child))
        return min(spawns)

    def heuristic_func(self, grid, move):
        # heuristic_func should return value for particular move
        # input: move, grid after move, some current state values
        # return: weight for move
        # 0-up, 1-down, 2-left, 3-right
        # h = 0

        #h = len(grid.getAvailableCells())
        di = {}
        h=0
        for x in range(grid.size-1):
            for y in range(grid.size-1):
                if grid.map[x][y] not in di:
                    di[grid.map[x][y]] = 1
                else:
                    di[grid.map[x][y]] += 1
        for each in di:
            if di[each] == 1:
                h += 10
            elif di[each] == 2:
                h += 5

        return h
