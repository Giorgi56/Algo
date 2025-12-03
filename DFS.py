from graph import OrientedGraph

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
