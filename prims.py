import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def prim_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        total_cost = 0

        for _ in range(self.V):
            u = min((key[i], i) for i in range(self.V) if i not in parent)[1]

            for v in range(self.V):
                if 0 < self.graph[u][v] < key[v] and v not in parent:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        print("Edge \t Weight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i}\t{key[i]}")
            total_cost += key[i]
        print(f"Total Cost of MST: {total_cost}")

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    g.prim_mst()
