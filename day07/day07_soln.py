# ------------------------------------------------------------
# Solution to Advent of Code 2021 Day 7
# ------------------------------------------------------------

import argparse
from collections import Counter


def inputRead(fname):
    with open(fname,'r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines


def inputToPositions(data):
    return [int(i) for i in data[0].split(',')]


def countsByPosition(positions):
    counts = Counter(positions)
    return [counts[i] for i in range(min(positions), max(positions)+1)] 


def costComputeSolns(posCounts, constCost=True):
    # Forward walk
    solnCosts = [0] * len(posCounts)
    for idx1 in range(0,len(posCounts)):
        count = posCounts[idx1]
        cost = 1
        costDelta = 1
        for idx2 in range(idx1+1, len(posCounts)):
            solnCosts[idx2] += count * cost
            if constCost == False:
                costDelta += 1
            cost += costDelta

    # Backward walk
    for idx1 in range(len(posCounts)-1,-1,-1):
        count = posCounts[idx1]
        cost = 1
        costDelta = 1
        for idx2 in range(idx1-1, -1, -1):
            solnCosts[idx2] += count * cost
            if constCost == False:
                costDelta += 1
            cost += costDelta

    return solnCosts


def costsFindBestIdx(solnCosts):
    return solnCosts.index(min(solnCosts))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',type=str,
                        help='Input file')
    parser.add_argument('--part', type=str,
                        choices=['part1', 'part2'],
                        default='part1',
                        help='Puzzle part to solve')
    args = parser.parse_args()

    data  = inputRead(args.input)

    positions = inputToPositions(data)
    posCounts = countsByPosition(positions)


    if args.part == 'part1':
        constCost = True
    else:
        constCost = False
    
    solnCosts = costComputeSolns(posCounts, constCost = constCost)
    bestPosition =  costsFindBestIdx(solnCosts)
    cost = solnCosts[bestPosition]

    print(f'{args.part}: Target={bestPosition} Cost={cost}')
