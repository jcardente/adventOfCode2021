# Solution to Day 6 Puzzles

Simulating the exponential population growth of lantern fish
was the task for day 6. The basic rules were:

- Each fish spawns a new fish every 7 days
- New fish require an extra 2 days to reach maturity

An initial population is given with fish at different
number of days until maturity. The following example
starts with 5 fish and demonstrates how the population grows.

```
Initial state: 3,4,3,1,2
After  1 day:  2,3,2,0,1
After  2 days: 1,2,1,6,0,8
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,8
After  5 days: 5,6,5,3,4,5,6,7,7,8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
```

The trick for this puzzle was to track the number of fish at each
day til spawning rather than tracking each individual fish. I represented
the population as a dictionary with,

- Keys as the number of days until spawning
- Values as the number of fish at this lifecycle stage

Simulating a day was then a matter of,

1. Moving the counts to the next lowest day
2. Moving spawning fish to day 6
3. Adding newly spawned fish to day 8

Here's the associated routine,

```python
def populationSimulateDay(pop):
    # Decrement existing fish
    newPop = {d1:pop[d2] for d1,d2 in  zip(range(0,8),range(1,9))}
    
    # Move spawning fish to day 6
    newPop[6] = newPop[6] + pop[0]

    # Spawn new fish
    newPop[8] = pop[0]

    return newPop
```

Getting the final population size was simply a matter of summing
the dictionary values

```python
nfish = sum(pop.values())
```

Final solution can be run from the command line as follows,

```
 python day06_soln.py --help
usage: day06_soln.py [-h] [--input INPUT] [--part {part1,part2}] [--ndays NDAYS]

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT         Input file
  --part {part1,part2}  Puzzle part to solve
  --ndays NDAYS         Number of days to simulate
```
