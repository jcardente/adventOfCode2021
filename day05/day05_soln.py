# ------------------------------------------------------------
# Solution to Advent of Code 2021 Day N

# ------------------------------------------------------------

import argparse
import re

def inputRead(fname):
    with open(fname,'r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines


def inputToLines(data):
    pattern = re.compile(r'([\d]+),([\d]+) -> ([\d]+),([\d]+)')
    lines = []
    for l in data:
        parsed = re.search(pattern, l)
        if parsed:
            coords = tuple([int(i) for i in parsed.groups()])
            lines.append(coords)
    return lines


def linesKeepHorzVert(lines):
    hvlines = []
    for l in lines:
        if ((l[0]==l[2]) or (l[1] == l[3])):
            hvlines.append(l)
    return hvlines


def gridMarkPoint(grid, p):
    if not (p in grid):
        grid[p] = 0
    grid[p] = grid[p] + 1
    

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
    
    
def gridAddLines(grid, lines):
    for l in lines:
        for p in  gridPlotLine(l):
            gridMarkPoint(grid, p)
    return grid


def gridFindRiskPoints(grid):
    return [(k,v) for k,v in grid.items() if v > 1]
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',type=str,
                        help='Input file')
    parser.add_argument('--part', type=str,
                        choices=['part1', 'part2'],
                        default='part1',
                        help='Puzzle part to solve')
    args = parser.parse_args()

    data = inputRead(args.input)
    lines = inputToLines(data)

    if args.part == 'part1':
        lines = linesKeepHorzVert(lines)
    grid = gridAddLines({}, lines)

    risky = gridFindRiskPoints(grid)
    print(f'{args.part}: num risky points {len(risky)}')
    
