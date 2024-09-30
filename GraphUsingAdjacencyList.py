# Graph using Adjacency list in python.

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertices(self, data):
        if data not in self.graph:
            self.graph[data] = []
        else:
            raise Exception('Vertices already exit...')

    def connectVertices(self, vertex_1, vertex_2):
        if (vertex_1 in self.graph) and (vertex_2 in self.graph):
            self.graph[vertex_1].append(vertex_2)
            self.graph[vertex_2].append(vertex_1)
        else:
            raise Exception("Vertex to connect doesn't exit")

    def print_graph(self):
        print(self.graph)

g = Graph()
g.add_vertices('A')
g.add_vertices('B')
g.add_vertices('C')
g.add_vertices('D')
g.add_vertices('E')
g.connectVertices('A', 'B')
g.connectVertices('A', 'E')
g.print_graph()
