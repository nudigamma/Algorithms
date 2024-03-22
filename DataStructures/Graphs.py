'''This file contains the implementation of undirected Graphs using Adjacency List'''
'''am going to use a dictionary to represent the adjacency list'''
class Graph:
    def __init__(self):
        self.graph = dict()
    
    def add_vertex(self, vertex):
        if self.graph.get(vertex) == None:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if self.graph.get(vertex1) :    #if vertex1 is in the graph
            self.graph[vertex1].append(vertex2)
    def add_list(self, vertex, lst):
        if self.graph.get(vertex):
            self.graph[vertex] = lst
    def print_graph(self):
        for vertex in self.graph.keys():
            print(vertex, '->', self.graph[vertex])
            
            
g = Graph()
g.add_vertex(str(1))
for vertex in g.keys():
    print(vertex)