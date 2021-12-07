# ------------------------------------------------------------
# Solution to Advent of Code 2021 Day 6
# ------------------------------------------------------------

import argparse


def inputRead(fname):
    with open(fname,'r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines


def inputToFishPopulation(data):
    fish = [int(f) for f in data[0].strip().split(',')]
    population = {k:0 for k in range(0,9)}
    for f in fish:
        population[f] = population[f] +1
    return population


def populationSimulateDay(pop):
    # Decrement existing fish
    newPop = {d1:pop[d2] for d1,d2 in  zip(range(0,8),range(1,9))}
    
    # Move spawning fish to day 6
    newPop[6] = newPop[6] + pop[0]

    # Spawn new fish
    newPop[8] = pop[0]

    return newPop
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--input',type=str,
                        help='Input file')
    parser.add_argument('--part', type=str,
                        choices=['part1', 'part2'],
                        default='part1',
                        help='Puzzle part to solve')
    parser.add_argument('--ndays', default=80,
                        type=int,
                        help='Number of days to simulate')
    args = parser.parse_args()

    data = inputRead(args.input)

    pop = inputToFishPopulation(data)
    for i in range(args.ndays):
        pop = populationSimulateDay(pop)

    nfish = sum(pop.values())
    print(f'Simulation Results: Days={args.ndays} Population={nfish}')

