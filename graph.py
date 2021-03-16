from vertex import Vertex

class Graph:
    def __init__(self):
        self.V = []
        self.adj = {}
    
    def setAdjacent(self, adj):
        self.adj.clear()
        self.adj = adj
    
    def setVertices(self, v):
        self.V.clear()
        self.V = v

    def addEdge(self, u, v, w):
        if u in self.adj:
            self.adj[u].append((Vertex(v), w))
        else:
            self.V.append(Vertex(u))
            self.adj[u] = [(Vertex(v), w)]

        if not self.vertexExists(v):
            self.V.append(Vertex(v))
        if v not in self.adj:
            self.adj[v] = []

    def vertexExists(self, v):
        for vertex in self.V:
            if vertex.value == v:
                return True
        return False