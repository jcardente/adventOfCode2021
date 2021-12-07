# Solution to Day 5 Puzzles

The day 5 puzzles involved plotting lines on a 2D
grid. The lines were given as a pair of endpoints,

```
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
```

The goal in both parts was to determine the number of 
points in the 2D grid in which two or more lines intersect. 
Part 1 only considered horizontal and vertical lines. In this
case, the grid for the above input is,

```
.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
```

And there are 5 intersection points (represented by 2). 

Part 2 added diagonal lines with a 45 degree slope. The resulting
grid for the same input is,

```
1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
```

I decided to represent the grid as a dictionary
with:
- Keys of (x,y) coordinate tuples
- Values of the number of lines that pass through the point

I wrote the following routine to determine the points
that a line passes through. It works for horizontal,
vertical, and diagonal lines.

```python
def gridPlotLine(l):
    points = []
    dx = l[2] - l[0]
    dx = int(dx/abs(dx)) if dx !=0 else dx    
    dy = l[3] - l[1]
    dy = int(dy/abs(dy)) if dy !=0 else dy

    p = [l[0], l[1]]
    while ((p[0] != l[2]) or (p[1] != l[3])):
        points.append([p[0], p[1]])
        p[0] = p[0] + dx
        p[1] = p[1] + dy
    points.append(p)

    return [(p[0], p[1]) for p in points]
```

and simply marked those points in the grid,

```python
def gridMarkPoint(grid, p):
    if not (p in grid):
        grid[p] = 0
    grid[p] = grid[p] + 1
    

def gridAddLines(grid, lines):
    for l in lines:
        for p in  gridPlotLine(l):
            gridMarkPoint(grid, p)
    return grid

```

Finding the points where two or more lines intersected was
then a matter of finding the dictionary keys with values
greater than 1.

```python
def gridFindRiskPoints(grid):
    return [(k,v) for k,v in grid.items() if v > 1]
```

