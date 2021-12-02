# Solution to Day 1 Puzzles

Both puzzles on Day 1 required examining a sequence of integers and
counting the number of times a value is larger than the last. 

The core of my solution was a function that tests adjacent values
and creates a sequence of booleans with `True` indicating increases.

```python
def depthsFindIncreased(depths):
    return [depths[i-1]<depths[i] for i in range(1, len(depths))]
```

Counting the number of sequences was then a matter of summing
the boolean sequence,

```python
incFlags = depthsFindIncreased(depths)
incCount = sum(incFlags)
print(f'Number of depth increases: {incCount}')
```

For part two, the task was the same but this time over a sequence
of sliding window sums of the original sequence. For this I wrote
a routine to calculate the sliding window sums,

```python
def depthsSumWindow(depths, window=3):
    return [sum(depths[i:i+window]) for i in range(0, len(depths)-window+1)]
```

And then used the solution for part 1 on this new sequence,

```python
windowDepths = depthsSumWindow(depths, window=3)
incFlags = depthsFindIncreased(windowDepths)
incCount = sum(incFlags)
print(f'Number of sliding window depth increases: {incCount}')
```
