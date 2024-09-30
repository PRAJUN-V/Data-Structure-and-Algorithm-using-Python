# graph using adjacency matrix in python

class Graph:
    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.adj_matrix = [[0 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)]

    def print_graph(self):
        for i in self.adj_matrix:
            print(i)

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.print_graph()
