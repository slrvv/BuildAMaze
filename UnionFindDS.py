from collections import defaultdict

class Graph :
    def __init__(self, vertices_num):
        self.vertices_num = vertices_num
        #represent graph data structure as array of edges
        self.edges = defaultdict(list)

    def add_edge(self, u, v):
        self.edges[u].append(v)

#structure to represent connected components of the graph
class Component :
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

## find in which component a given node is using path compression normal
## recursion gets too deep
def find_component(components, node):
    while node != components[node].parent:
        components[node].parent = components[components[node].parent].parent
        node = components[node].parent

    return node

# function to do union by rank of two components , identified by cc_u, cc_v
def union_by_rank(components, cc_u, cc_v):

    if components[cc_u].rank > components[cc_v].rank :
        components[cc_v].parent = cc_u

    elif components[cc_v].rank > components[cc_u].rank :
        components[cc_u].parent = cc_v
    #pick one to break the tie, increase the rank of one of them by one.
    else :
        components[cc_v].parent = cc_u
        components[cc_u].rank += 1
