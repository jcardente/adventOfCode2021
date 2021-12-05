# Solution to Day 3 Puzzles

For day 3, the task was to calculate values from a diagnostic report consisting of
a series of binary numbers. For example,

```
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
```

I decided to represent each value as a tuple of 1's and 0's and wrote routines
to do the initial conversions and perform simply manipulations,

```python
def inputToBits(input):
    return [[int(b) for b in list(i)] for i in input]


def bitsInvert(bits):
    return [1 if b==0 else 0 for b in bits]


def bitsToDecimal(bits):
    ## NB - MSB is first
    return sum([(2**i)*b for i,b in zip(range(len(bits)), bits[::-1])])
```

Part one asked to compute two values from the series based on

- The **most** common bit value in each position
- The **least** common bit value in each position

I wrote a routine to find the most common bit value in each position,

```python
def bitsToMajority(bits, tieValue=0):
    nvalues = len(bits)
    counts  = [sum(x) for x in zip(*bits)]
    return [int(round(x/nvalues)) if (2*x) != nvalues else tieValue for x in counts]
```

And a routine that can invert that value to find the least common bit value
in each position,

```python
def bitsInvert(bits):
    return [1 if b==0 else 0 for b in bits]
```

Computing the answer for part one was then a matter of doing the following,

```python
majority = bitsToMajority(bits)        
gamma = bitsToDecimal(majority)
epsilon = bitsToDecimal(bitsInvert(majority))
ans = gamma * epsilon
```

Part two increased the challenge by adding a recursive filtering process of:

1. Calculating the most/least common bit value at index 0
2. Keeping only those numbers with the value found in step 1 at index 0
3. Recursively doing the same for the remaining index until only one number remains

I implemented a common dynamic programming solution capable of applying either
the most or least common bit value criteria,

```python
def bitsApplyCriteria(bits, idx, mostCommon=True):   
    if len(bits) == 1:
        return bits[0]

    majority = bitsToMajority(bits, tieValue=1)     
    if not mostCommon:
        majority = bitsInvert(majority)
    bits = [b for b in bits if b[idx] == majority[idx]]
    
    return bitsApplyCriteria(bits, idx+1, mostCommon=mostCommon)
```

I used this routine to solve part 2 as follows,

```python
ogr = bitsToDecimal(bitsApplyCriteria(bits, 0, mostCommon=True))
csr = bitsToDecimal(bitsApplyCriteria(bits, 0, mostCommon=False))
ans = ogr * csr
```
