from Graph  import Graph
from Queue  import Queue
from Vertex import Vertex

def BFS(G,s):
    color = {}
    distance = {}
    parent = {}
    Q = Queue([])
    for vertex in G.getVertexes():
        color[vertex] = 0
        distance[vertex] = float('inf')
        parent[vertex] = None
    color[s] = 1
    distance[s] = 0
    parent[s] = None
    Q.enqueue(s)
    while Q != []:
        u = Q.dequeue()
        if not u:
            break
        for i in G.getAdjacencyVertexes(u):
            if color[i] == 0:
                color[i] = 1
                distance[i] = distance[u]+1
                parent[i] = u
                Q.enqueue(i)
        color[u] = 2

if __name__=="__main__":
    G = Graph()
    G.addEdge(Vertex("s"),Vertex("w"))
    G.addEdge(Vertex("s"),Vertex("r"))
    G.addEdge(Vertex("r"),Vertex("v"))
    G.addEdge(Vertex("w"),Vertex("x"))
    G.addEdge(Vertex("w"),Vertex("t"))
    G.addEdge(Vertex("x"),Vertex("t"))
    G.addEdge(Vertex("x"),Vertex("u"))
    G.addEdge(Vertex("x"),Vertex("y"))
    G.addEdge(Vertex("t"),Vertex("u"))
    G.addEdge(Vertex("u"),Vertex("t"))
    print G
    BFS(G,Vertex("s"))
