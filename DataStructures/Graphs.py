class Graph:
    def __init__(self):
        self.graph = dict()

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, bidirectional=False):
        # Ensure both vertices exist
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Add edge from vertex1 to vertex2
        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)

        # For undirected graphs, add edge from vertex2 to vertex1 as well
        if bidirectional and vertex1 not in self.graph[vertex2]:
            self.graph[vertex2].append(vertex1)

    def add_list(self, vertex, lst):
        # Ensure the vertex exists
        self.add_vertex(vertex)

        # Optionally: Validate vertices in lst exist or add them
        for v in lst:
            self.add_vertex(v)

        self.graph[vertex] = lst

    def print_graph(self):
        for vertex in sorted(self.graph.keys()):  # Sorting vertices for a more organized output
            print(f"{vertex} -> {self.graph[vertex]}")
