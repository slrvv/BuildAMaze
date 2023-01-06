# Build A Maze

Use Maze by executing 

```python
from maze import Maze

maze = Maze(4)

maze.remove_segments()
print("Result:")
print(maze)
```

Example result: 
```
+---+---+---+---+
| 0 | 1   2 | 3 |
+   +---+---+   +
| 4   5   6 | 7 |
+---+---+   +   +
| 8   9  10 |11 |
+   +   +---+   +
|12  13  14  15 |
+---+---+---+---+
```