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

    def get_edge_weight(self, from_node, to_node):
        if from_node in self.nodes and to_node in self.nodes:
            from_node_obj = self.nodes[from_node]
            to_node_obj = self.nodes[to_node]
            if to_node_obj in from_node_obj.adjacent:
                return from_node_obj.adjacent[to_node_obj]
            else:
                return f"No edge exists between {from_node} and {to_node}"
        else:
            return f"One or both nodes {from_node}, {to_node} not found."

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

    print(graph.get_edge_weight('Thalassery', 'Kannur'))  # Output: 10
    print(graph.get_edge_weight('Kannur', 'Thalassery'))  # Output: 10
    print(graph.get_edge_weight('Thalassery', 'Calicut')) # Output: 20
    print(graph.get_edge_weight('Calicut', 'Kannur'))     # Output: 15
    print(graph.get_edge_weight('Thalassery', 'Mumbai'))  # Output: One or both nodes Thalassery, Mumbai not found
    print(graph.get_edge_weight('Mumbai', 'Thalassery'))      # Output: One or both nodes Mumbai, Kannur not found
    print(graph.get_edge_weight('Kannur', 'Kannur'))      # Output: No edge exists between Kannur and Kannur
