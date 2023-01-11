from maze import Maze

maze = Maze(60)


print("n:",maze.n)
print("edges:", maze.graph.edges)
#print("not edges:", maze.not_edges)

maze.remove_segments(print_b=False)
print("Result:")
print(maze)
print("Walls:", maze.not_edges)
