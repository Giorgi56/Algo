# Type Pile
class Pile:
    """LIFO"""
    def __init__(self, lst:list):
        self.pile = lst
    
    def push(self, elt):
        self.pile.append(elt)
    
    def pop(self):
        return self.pile.pop()
    
    def not_empty(self):
        return len(self.pile) > 0
    
# Type OrientedGraph - liste d'adjascence - sommet = entier entre 0 et n-1 où n est le nombre d'arrêtes
class OrientedGraph:
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

def dfs(graph:OrientedGraph, start:int):
    """Makes a depth-first search and prints every node as soon as visited"""
    pile = Pile([start])

    # Construction of the visited nodes' list
    n = len(graph.adj)
    visited = [False] * n

    def aux(s):
        print(s)
        visited[s] = True
        for neighbor in graph.neighbors(s):
            if not visited[neighbor]:
                aux(neighbor)
    
    def aux2():
        """Inutile non?"""
        if pile.not_empty():
            s = pile.pop()
            print(s)
            visited[s] = True
            for neighbor in graph.neighbors(s):
                if not visited[neighbor]:
                    pile.push(neighbor)
                    aux2()
    aux(start)
    visited = [False] * n
    print("--------------------")
    aux2()

# Test
graph = OrientedGraph([
    [1, 2, 7],
    [ 6],
    [3, 5],
    [8],
    [],
    [4],
    [9, 10],
    [],
    [],
    [],
    [],
])

dfs(graph, 0)
