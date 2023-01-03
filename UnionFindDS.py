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

## find in which component a given node is
def find_component(components, node):

    if components[node].parent == node :
        return node
    else :
        return find_component(components, components[node].parent)

# function to do union by rank of two components , identified by cc_u, cc_v
def union_by_rank(components, cc_u, cc_v):

    if components[cc_u].rank > components[cc_v].rank :
        components[cc_u].parent = cc_v

    elif components[cc_v].rank > components[cc_u].rank :
        components[cc_v].parent = cc_u
    #pick one to break the tie, increase the rank of one of them by one.
    else :
        components[cc_v].parent = cc_u
        components[cc_v].rank += 1
