# Type File
class File:
    """FIFO"""
    def __init__(self, lst):
        self.file = lst
    
    def enqueue(self, elt):
        self.file = [elt] + self.file
    
    def dequeue(self):
        return self.file.pop()
    
    def not_empty(self):
        return len(self.file) > 0
    
# Type NonOrientedGraphe - liste d'adjascence - sommet = entier entre 0 et n-1 où n est le nombre d'arrêtes
class NonOrientedGraph:
    def __init__(self, adj:list[list[int]]):
        self.adj = adj
    
    def neighbors(self, s:int):
        return self.adj[s]  # adjascence list of the node with index of s
    
    def add(self, node:int, neighbors:list):
        if node == len(self.adj) + 1:
            # i.e. if we're creating a new node
            self.adj.append(neighbors)
        else:
            self.adj[node] = self.adj[node] + neighbors

# fonction de dfs

def bfs(graph:NonOrientedGraph, start:int):
    """Makes a depth-first search and prints every node as soon as visited"""
    file = File([start])

    # Construction of the visited nodes' list
    n = len(graph.adj)
    visited = [False] * n

    print(start)
    while file.not_empty():
        a = file.dequeue()
        visited[a] = True
        for neighbor in graph.neighbors(a):
            if not visited[neighbor]:
                print(neighbor)
                file.enqueue(neighbor)

# Test
graph = NonOrientedGraph([
    [1, 2],
    [3, 5],
    [],
    [],
    [],
    [4],
])

bfs(graph, 0)
