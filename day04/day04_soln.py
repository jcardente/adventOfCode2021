# ------------------------------------------------------------
# Solution to Advent of Code 2021 Day 4
#
# ------------------------------------------------------------

import argparse


def inputRead(fname):
    with open(fname,'r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines


class Board():
    def __init__(self, board):
        self.size=5
        self.board = board
        self.marked = set()
        self.colCounts = {i:0 for i in range(0,5)}
        self.rowCounts = {i:0 for i in range(0,5)}

    def __idxToRowCol(self, idx):
        row = int(idx/self.size)
        col = idx % self.size
        return row, col
        
    def play(self, draw):
        if draw in self.board:
            idx = self.board.index(draw)
            row, col = self.__idxToRowCol(idx)
            self.marked.add(idx)            
            self.rowCounts[row] = self.rowCounts[row] + 1            
            self.colCounts[col] = self.colCounts[col] + 1

    def hasWon(self):
        rowColCounts = (list(self.rowCounts.values()) +
                        list(self.colCounts.values()))
        if any([c == 5 for c in rowColCounts]):
            return True
        return False

    def getUnmarkedValues(self):
        return [self.board[idx] for idx in range(0, len(self.board))
                if not (idx in self.marked)]
            

def inputToDrawsBoards(input):
    draws = [int(d) for d in input[0].split(',')]
    boards = []
    board = []
    for l in input[2:]:
        if len(l) > 0:
            board.extend([int(d) for d in l.split()])
            
        else:
            boards.append(Board(board))
            board=[]
    boards.append(Board(board))
    return draws, boards


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--input',type=str,
                        help='Input file')
    parser.add_argument('--part', type=str,
                        choices=['part1', 'part2'],
                        default='part1',
                        help='Puzzle part to solve')
    args = parser.parse_args()

    input = inputRead(args.input)
    draws, boards = inputToDrawsBoards(input)
   
    allBoards = set(range(0,len(boards)))
    wonBoards = set()
    winLog = []
    for step, draw in enumerate(draws):

        activeBoards = allBoards.difference(wonBoards)
        if len(activeBoards) == 0:
            break
        
        for bid in activeBoards:
            boards[bid].play(draw)

        winningBids = [bid for bid in activeBoards if boards[bid].hasWon()]
        wonBoards.update(winningBids)
        winLog.extend([(step, draw, bid) for bid in winningBids])

        if ((args.part == 'part1') and (len(winningBids) > 0)):
            break
                
    if args.part == 'part1':
        step, draw, bid = winLog[0]
        
    else:
        step, draw, bid = winLog[-1]
        
    unmarkedValues = boards[bid].getUnmarkedValues()
    ans = sum(unmarkedValues) * draw
    print(f'{args.part} winner: Step={step} Draw={draw} Board={bid} Ans={ans}')
    
