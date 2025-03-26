# Graph Implementation in Python

class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to store the graph

    # Method to add an edge to the graph
    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)  # For undirected graph

    # Method to display the graph
    def display(self):
        for node, edges in self.graph.items():
            print(f"{node}: {', '.join(map(str, edges))}")

# Example usage
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

print("Graph:")
g.display()