import heapq

class GraphNode:
    def __init__(self, data):
        self.data = data
        self.adjacent = {}  # Dictionary to store adjacent nodes and weights

class Graph:
    def __init__(self):
        self.nodes = {}  # Dictionary to store nodes by their data value

    def add_node(self, data):
        if data not in self.nodes:
            self.nodes[data] = GraphNode(data)
        else:
            print(f"Node {data} already exists.")

    def add_edge(self, from_node, to_node, weight):
        if from_node in self.nodes and to_node in self.nodes:
            self.nodes[from_node].adjacent[self.nodes[to_node]] = weight
            self.nodes[to_node].adjacent[self.nodes[from_node]] = weight
        else:
            print(f"One or both nodes {from_node}, {to_node} not found.")

    # Dijkstra's algorithm is used here.
    def get_shortest_distance_and_path(self, start_node_data, end_node_data):
        if start_node_data not in self.nodes or end_node_data not in self.nodes:
            return "One or both nodes not found."

        start_node = self.nodes[start_node_data]
        end_node = self.nodes[end_node_data]

        distances = {node: float('inf') for node in self.nodes.values()}
        distances[start_node] = 0
        previous_nodes = {node: None for node in self.nodes.values()}

        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in current_node.adjacent.items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        if distances[end_node] == float('inf'):
            return "No path found."

        # Construct the path
        path = []
        current = end_node
        while current:
            path.insert(0, current)
            current = previous_nodes[current]

        return distances[end_node], path

# Example usage
if __name__ == "__main__":
    graph = Graph()
    graph.add_node('Thalassery')
    graph.add_node('Kannur')
    graph.add_node('Calicut')
    graph.add_node('Mumbai')

    graph.add_edge('Thalassery', 'Kannur', 10)
    graph.add_edge('Thalassery', 'Calicut', 20)
    graph.add_edge('Kannur', 'Calicut', 15)
    graph.add_edge("Thalassery", "Mumbai", 89)

    distance, path = graph.get_shortest_distance_and_path('Thalassery', 'Calicut')
    print("Shortest distance:", distance)
    print("Shortest path:", [node.data for node in path])
