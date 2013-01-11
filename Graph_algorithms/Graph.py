from Vertex import Vertex

class Graph:
    
    def __init__(self):
        self.adjacencyList = {}

    def __str__(self):
        print self.adjacencyList.keys()[0]
        return str(self.adjacencyList)
    
    def addVetex(self,key,value):
        if Vertex(key,value) not in self.adjacencyList:
            self.adjacencyList[Vertex(key,value)] = []

    def addEdge(self,vertex_a,vertex_b):
        self.addVetex(vertex_a.key,vertex_a.value)
        self.addVetex(vertex_b.key,vertex_b.value)
        self.adjacencyList[vertex_a].append(vertex_b)
        self.adjacencyList[vertex_b].append(vertex_a)

