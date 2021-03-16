import heapq
import random

def dj(G, w, s):
    init_single_source(G,s)
    S = []
    Q = []
    
    for vertex in G.V:
        heapq.heappush(Q, (vertex.distance, vertex))

    for node in Q:
        print(node[1].value)
    
    print('\n')

    while len(Q) != 0:
        u = heapq.heappop(Q)[1]
        S.append(u)

        for vertex in G.adj[u.value]: #G.adj[u]
            currentVertex = vertex[0]
            originalDistance = currentVertex.distance
            relax(u, currentVertex, w, G)
            if currentVertex.distance != originalDistance:
                for index, vTuple in enumerate(Q):
                    if vTuple[1].value == currentVertex.value:
                        Q[index] = (currentVertex.distance, currentVertex)
                        heapq.heapify(Q)


    for node in S:
        print('node:' + node.value)
        print('node distance:' + str(node.distance))
        if node.predecessor is not None:
            print('node parent:' + node.predecessor.value)
        print('\n')
                
def init_single_source(G, s):
    for vertex in G.V:
        if vertex.value == s:
            vertex.distance = 0
        else:
            vertex.distance = float('inf')
        vertex.predecessor = None
        
    for vertex in G.adj.values():
        for node in vertex:
            currentNode = node[0]
            if currentNode.value == s:
                currentNode.distance = 0
            else:
                currentNode.distance = float('inf')
            currentNode.predecessor = None

def relax(u,v,w, G):
    if v.distance > u.distance + w(u,v,G):
        v.distance = u.distance + w(u,v,G)
        v.predecessor = u

def weight(u,v,G):
    for vertex in G.adj[u.value]:
        currentVertex = vertex[0]
        if currentVertex.value == v.value:
            return vertex[1]
    
    return 0

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
        
class Vertex:
    def __init__(self, val):
        self.predecessor = None
        self.distance = None
        self.value = val

    def __lt__(self, other):
        # Overload the less than operator. This function is called when there needs to be a tie break.
        return random.choice([self,other])

def main():
    graph = Graph()
    # adjList = {'s': [Vertex('t', 10), Vertex('y', 5)], 't': [Vertex('x', 1), Vertex('y', 2)], 'y': [Vertex('t', 3), Vertex('x', 9), Vertex('z', 2)], 'x': [Vertex('z', 4)], 'z': [Vertex('x', 6), Vertex('s', 7)]}
    # adjList = {'s': [Vertex('t', 3), Vertex('y', 5)], 't': [Vertex('x', 6), Vertex('y', 2)], 'y': [Vertex('t', 1), Vertex('x', 4), Vertex('z', 6)], 'x': [Vertex('z', 2)], 'z': [Vertex('x', 7), Vertex('s', 3)]}
    vertexList = [Vertex('s'), Vertex('t'), Vertex('y'), Vertex('x'), Vertex('z'), Vertex('b')]
    adjList = {'s': [(Vertex('t'), 2), (Vertex('y'),4)], 't': [(Vertex('x'),7), (Vertex('y'),1)], 'y': [(Vertex('z'),3)], 'x': [(Vertex('b'),1)], 'z': [(Vertex('x'),2), (Vertex('b'),5)], 'b': []}
    graph.setAdjacent(adjList)
    graph.setVertices(vertexList)
    dj(graph, weight, 's')

if __name__ == "__main__":
    main()