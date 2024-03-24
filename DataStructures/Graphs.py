'''this class implements a graph data structure using an adjacency list representation'''
'''the graph is represented as a dictionary 
where the keys are the vertices and the values are lists of
the vertices that are adjacent to the key vertex, no parallel edges are allowed'''



class Graph:
    def __init__(self):
        self.graph = {}

        
    def add_vertex(self, vertex : int ) -> None:
        if self.graph.get((str(vertex))) == None :
            self.graph[str(vertex)] = []
    def connect(self, vertex1 :int, vertex2:int ) -> None:
        if self.graph.get(str(vertex1)) != None and self.graph.get(str(vertex2)) != None: 
            if vertex2 not in self.graph[str(vertex1)]:
                self.graph[str(vertex1)].append(vertex2)
            if vertex1 not in self.graph[str(vertex2)]:
                self.graph[str(vertex2)].append(vertex1)

