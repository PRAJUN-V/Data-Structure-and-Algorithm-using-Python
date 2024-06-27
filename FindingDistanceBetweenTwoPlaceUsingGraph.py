from Graph import Graph

map_graph = Graph()
map_graph.add_node("Thalassery")
map_graph.add_node("Kannur")
map_graph.add_node("Goa")
map_graph.add_node("Karnadaka")

map_graph.add_edge("Thalassery", "Goa", 300)
map_graph.add_edge("Kannur", "Thalassery", 40)
map_graph.add_edge("Kannur", "Goa", 20)
map_graph.add_edge("Goa", "Thalassery", 10)

distance, path = map_graph.get_shortest_distance_and_path( "Goa", "Thalassery")

print(distance)
print("Shortest path:", [node.data for node in path])
