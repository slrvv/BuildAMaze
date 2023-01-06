import UnionFindDS as DS
from random import sample

class Maze :
    def __init__(self, n):
        self.n = n
        # Create Graph representing Matrix
        self.graph = DS.Graph(n**2)

        self.components = []
        for u in range(self.graph.vertices_num):
            self.components.append(DS.Component(u, u))

        # edges, that are available for deletion
        self.not_edges = set([
            (i,i+1) for i in range(self.graph.vertices_num) if i % 4 != 3
        ] + [
            (i,i+n) for i in range(self.graph.vertices_num - n)
        ])

    def remove_segments(self):
        """
        Randomly draw edges and remove them until
        upper left und lower right are in one component
        """
        print("--- Remove Segments ---")

        while DS.find_component(self.components, 0) != DS.find_component(self.components, self.graph.vertices_num-1):
            e = sample(self.not_edges, 1)[0]
            print("sampled edge:", e)
            cc_u = DS.find_component(self.components, e[0])
            cc_v = DS.find_component(self.components, e[1])
            DS.union_by_rank(self.components, cc_u, cc_v)
            self.not_edges.remove(e)
            self.graph.add_edge(e[0], e[1])
            print(self)

        return self

    def __str__(self):
        one_h = ("+---",
                 "+   ")
        one_v1 = (["| "," "],
                 ["  "," "])
        one_v2 = (["|"," "],
                  [" ", " "])

        res = one_h[0] * self.n + "+\n"
        for i in range(self.n*2):
            for j in range(self.n):
                idx = (i//2) * self.n + j
                if i % 2 == 1:
                    if idx+self.n in self.graph.edges[idx]:
                        res += one_h[1]
                    else:
                        res += one_h[0]
                else:
                    if idx >= 10: one_v = one_v2
                    else: one_v = one_v1

                    if idx in self.graph.edges[idx-1] and j != 0:
                        res += str(idx).join(one_v[1])
                    else:
                        res += str(idx).join(one_v[0])

            if i % 2 == 1: res += "+\n"
            else: res += "|\n"

        return res

