'''This file implements the Minimum Cut algorithm using the Karger's algorithm.'''
import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
small_graph = {'1': [2, 3], '2': [1, 3, 4], '3': [1, 2, 4], '4': [2, 3]}


def plot_graph(small_graph : dict, title : str) -> None : 
# Create a new graph
    G = nx.Graph()
# Add nodes and edges
    for node, edges in small_graph.items():
        G.add_node(node)
        for edge in edges:
            G.add_edge(node, str(edge))
# Plot the graph
    plt.figure(figsize=(5, 4))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, edge_color='k', linewidths=1, font_size=15)
    plt.title(title, fontsize=20)
    plt.show()
class Graph:
    '''this class implements a graph data structure using an adjacency list representation'''
    '''the graph is represented by a list of vertices and a list of edges
    where the keys are the vertices and the values are lists of
    the vertices that are adjacent to the key vertex, no parallel edges are allowed'''
    def __init__(self):
        self.vertices = []
        self.edges = []
        
def small_test():
    
    small_graph = {'1':[2,3], '2':[1,3,4], '3':[1,2,4], '4':[2,3]}
    edges = []
    for node, connections in small_graph.items():
        for connection in connections:
            edge = (node, str(connection))
            if edge not in edges and (str(connection), node) not in edges:
                edges.append((node, str(connection)))
            
    print(edges)    
        
    #plot_graph(small_graph, 'Small Graph')
    small_graph_1 = Graph()
    
    
    
def main():
    '''read graph from file and contstruct a graph object'''
    graph = Graph()
    with open('kargerMinCut.txt') as f:
        for line in f:
            line = line.split()
            graph.add_vertex((line[0]))
            for vertex in line[1:]:
                graph.connect((line[0]), int(vertex))
    print('Graph constructed')
    
#if __name__ == "__main__":
#    main()

small_test()    