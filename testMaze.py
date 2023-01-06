from maze import Maze

maze = Maze(4)


print("n:",maze.n)
print("edges:", maze.graph.edges)
print("not edges:", maze.not_edges)

maze.remove_segments(print_b=True)
print("Result:")
print(maze)
