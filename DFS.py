# Type Pile
class Pile:
    """LIFO"""
    def __init__(self, lst:list):
        self.pile = lst
    
    def push(self, elt):
        self.pile.append(elt)
    
    def _pop(self):
        return self.pile.pop()
    
    def not_empty(self):
        return len(self.pile) > 0
    
# Type NonOrientedGraph - liste d'adjascence - sommet = entier entre 0 et n-1 où n est le nombre d'arrêtes
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

def dfs(graph:NonOrientedGraph, start:int):
    """Makes a depth-first search and prints every node as soon as visited"""
    pile = Pile([start])

    # Construction of the visited nodes' list
    n = len(graph.adj)
    visited = [False] * n

    print(start)
    while pile.not_empty():
        a = pile._pop()
        visited[a] = True
        for neighbor in graph.neighbors(a):
            if not visited[neighbor]:
                print(neighbor)
                pile.push(neighbor)

# Test
graph = NonOrientedGraph([
    [1, 2],
    [3, 5],
    [],
    [],
    [],
    [4],
])

dfs(graph, 0)
