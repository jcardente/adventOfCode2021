# Solution to Day 4 Puzzles

For day 4, we played bingo! The puzzle input was a:

- List of draws
- Series of 5x5 boards

in the following format,

```
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

```

The game is played by:

- Taking the next draw off the list
- Marking the board postions that contain the drawn value
- Identifying winning boards with a full row or column of marked positions

Both part 1 and 2 used the same game play. The only difference was
that part 1 asked for the first winning board while part asked for the
last. The actual puzzle answers involved summing all of the
**unmarked** values in the desired winning board by the draw that caused it 
to win.

I decided to represent boards as objects that:

- Stored the board values as a flat list
- Tracked the indexes that have been marked
- Kept a count of the number of marked entries in each row and column

Tracking the marked indexes made it easy to find the unmarked board
values. Keeping marked row and column entry counts allowed identifying
winners without having to loop. The final class was,

```python
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
```


I used a common game loop for both parts 1 and 2 that,

- Selected the next draw
- Updated the boards not yet won
- Identifed any new winners and added them a timestamped log

The code for this was,

```python 
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
```

Computing the final puzzle answer was a matter of selecting the right winner, getting its
unmarked values, and multiplying by the draw that caused it to win.

```python
if args.part == 'part1':
    step, draw, bid = winLog[0]

else:
    step, draw, bid = winLog[-1]

unmarkedValues = boards[bid].getUnmarkedValues()
ans = sum(unmarkedValues) * draw
print(f'{args.part} winner: Step={step} Draw={draw} Board={bid} Ans={ans}')
```


