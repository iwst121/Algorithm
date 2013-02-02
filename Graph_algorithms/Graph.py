from Vertex import Vertex
import json

class Graph:
    
    def __init__(self,directional = False,simple=True,Filename=None):
        self.adjacencyList = {}
        self.directional = directional
        self.simple = simple
        if Filename:
            self._readFile(Filename)

    def _readFile(self,Filename):
        from GraphParser import GraphParser
        parser = GraphParser(Filename)
        self.simple = parser.isSimple()
        self.directional = parser.isDirectional()
        self.adjacencyList = parser.getAdjacencyList()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        simple = "Simple: "+ str(self.simple)+"\n"
        directional = "Directional: " + str(self.directional)+"\n"
        items = "{\n"
        for vertex in self.adjacencyList.keys():
            items = items +"\t"+str(vertex)+"==>"+str(self.adjacencyList[vertex])+"\n"
        items += "}"
        string = simple + directional + items
        return string
    
    def addVetex(self,key,value):
        if Vertex(key,value) not in self.adjacencyList:
            self.adjacencyList[Vertex(key,value)] = []

    def addEdge(self,vertex_a,vertex_b):
        self.addVetex(vertex_a.key,vertex_a.value)
        self.addVetex(vertex_b.key,vertex_b.value)
        if self.simple:
            if vertex_a == vertex_b:
                return
            if vertex_a in self.adjacencyList[vertex_b]:
                return
        self.adjacencyList[vertex_a].append(vertex_b)
        if not self.directional:
            self.adjacencyList[vertex_b].append(vertex_a)

    def getVertexes(self):
        return self.adjacencyList.keys();
    
    def getAdjacencyVertexes(self,vertex):
        return self.adjacencyList[vertex]
    
if __name__=="__main__":
    P=Graph(Filename="graph.xml")
    print P.__repr__() 
