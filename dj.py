import heapq
import random

def dj(G, w, s):
    init_single_source(G,s)
    S = []
    Q = []
    dupeChecker = set()

    for vertex in G.V.values():
        for node in vertex:
            if node.value not in dupeChecker:
                dupeChecker.add(node.value)
                heapq.heappush(Q, (node.distance, node))
    
    for node in Q:
        print(node[1].value)
    
    print('\n')

    while len(Q) != 0:
        u = heapq.heappop(Q)[1]
        S.append(u)

        for vertex in G.V[u.value]: #G.adj[u]
            originalDistance = vertex.distance
            relax(u, vertex, w, G)
            if vertex.distance != originalDistance:
                for index, vTuple in enumerate(Q):
                    if vTuple[1].value == vertex.value:
                        Q[index] = (vertex.distance, vertex)
                        heapq.heapify(Q)


    for node in S:
        print(node.value)
        if node.predecessor is not None:
            print('whut')
            print(node.predecessor.value)
        print('\n')
                
def init_single_source(G, s):
    for vertex in G.V.values():
        for node in vertex:
            if node.value == s:
                node.distance = 0
            else:
                node.distance = float('inf')
            node.predecessor = None

def relax(u,v,w, G):
    if v.distance > u.distance + w(u,v,G):
        v.distance = u.distance + w(u,v,G)
        v.predecessor = u

def weight(u,v,G):
    for vertex in G.V[u.value]:
        if vertex.value == v.value:
            return vertex.weight

class Graph:
    def __init__(self):
        self.V = {}
    
    def adj(self, u):
        #return vertices adjacent to u
        adjacent = []
        temp = u.next
        adjacent.append(temp)
        while temp:
            temp = temp.next
            adjacent.append(temp)
        
        return adjacent
    
    def setEntire(self, V):
        self.V.clear()
        self.V = V

        
class Vertex:
    def __init__(self, val, weight):
        self.predecessor = None
        self.distance = None
        self.value = val
        self.weight = weight

    def __lt__(self, other):
        # Overload the less than operator. This function is called when there needs to be a tie break.
        return random.choice([self,other])

def main():
    graph = Graph()
    # adjList = {'s': [Vertex('t', 10), Vertex('y', 5)], 't': [Vertex('x', 1), Vertex('y', 2)], 'y': [Vertex('t', 3), Vertex('x', 9), Vertex('z', 2)], 'x': [Vertex('z', 4)], 'z': [Vertex('x', 6), Vertex('s', 7)]}
    # adjList = {'s': [Vertex('t', 3), Vertex('y', 5)], 't': [Vertex('x', 6), Vertex('y', 2)], 'y': [Vertex('t', 1), Vertex('x', 4), Vertex('z', 6)], 'x': [Vertex('z', 2)], 'z': [Vertex('x', 7), Vertex('s', 3)]}
    adjList = {'s': [Vertex('t', 2), Vertex('y', 4)], 't': [Vertex('x', 7), Vertex('y', 1)], 'y': [Vertex('z', 3)], 'x': [Vertex('b', 1)], 'z': [Vertex('x', 2), Vertex('b', 5)], 'b': []}
    graph.setEntire(adjList)
    dj(graph, weight, 's')

if __name__ == "__main__":
    main()