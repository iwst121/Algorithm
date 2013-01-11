from Vertex import Vertex

class Graph:
    
    def __init__(self,directional = False,simple=True,Filename=None):
        self.adjacencyList = {}
        self.directional = directional
        self.simple = simple
        if not Filename:
            self._readFile(Filename)

    def _readFile(self,Filename):
        """
            This is going to be implemented later
        """
        pass

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

if __name__=="__main__":
    P=Graph()
    P.addEdge(Vertex(1),Vertex(2))
    P.addEdge(Vertex(1),Vertex(3))
    print P
