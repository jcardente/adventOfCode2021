# Solution to Day 2 Puzzles

The day 2 puzzles involved applying a sequence
of navigation commands to determine a submarine's
final position. For example, the following commands,

```
forward 5
down 5
forward 8
up 3
down 8
forward 2
```

Would put the submarine at the horizontal position 15 and
depth 10.

I converted the puzzle input into a sequence of `(command, value)` 
tuples and implemented a routine to update the submarine's
position,

```python
def doCommandPart1(pos, cmd):
    action, dist = cmd
    if action == 'forward':
        pos['horz'] = pos['horz'] + dist
    elif action == 'down':
        pos['vert'] = pos['vert'] + dist
    elif action=='up':
        pos['vert'] = pos['vert'] - dist
    else:
        raise Exception(f'Unknown command: {cmd}')

    return pos
```

To determine the submarine's final position, used
a reduce operation to apply the sequence of commands,

```python
def applyCommands(cmds, cmdFn, startPos):
    return reduce(cmdFn, commands, startPos)
```

The following examples shows how I used these routines to solve
part 1.

```python
startPos = {'horz': 0, 'vert': 0}
finalPos = applyCommands(commands, doCommandPart1, startPos)
```

Part 2 was essentially the same except for the addition of 
a third position variable called `aim`. I implemented
a new routine to update `aim`,

```python
def doCommandPart2(pos, cmd):
    action, dist = cmd
    if action == 'forward':
        pos['horz'] = pos['horz'] + dist
        pos['vert'] = pos['vert'] + dist*pos['aim']
        
    elif action == 'down':
        pos['aim'] = pos['aim'] + dist
    elif action=='up':
        pos['aim'] = pos['aim'] - dist
    else:
        raise Exception(f'Unknown command: {cmd}')

    return pos
```

And used the same reduce operation to determine the submarine's
final position,

```python
startPos = {'horz': 0, 'vert': 0, 'aim': 0}
finalPos = applyCommands(commands, doCommandPart2, startPos)
```
