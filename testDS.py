## Testing code
import UnionFindDS as DS
def contains_Cycle(graph):
    components = []

    for u in range(graph.vertices_num):
        components.append(DS.Component(u, 0))

    for u in graph.edges:
        cc_u = DS.find_component(components, u)

        for v in graph.edges[u] :
            cc_v = DS.find_component(components, v)

            if cc_v == cc_u :
                return True
            else:
                DS.union_by_rank(components, cc_u, cc_v)

def answer(g):
    if contains_Cycle(g) :
        print("Graph has cycle")
    else :
        print("Graph has no cycle")

print("Testing if Union Find DS is correct")
g = DS.Graph(5)

g.add_edge(0, 1)

g.add_edge(0, 2)

g.add_edge(0, 3)

g.add_edge(0, 4)
print(g.edges)
answer(g)

g1 = DS.Graph(3)
g1.add_edge(0, 1)

g1.add_edge(1, 2)

g1.add_edge(0, 2)
print(g1.edges)
answer(g1)
