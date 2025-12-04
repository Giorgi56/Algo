from graph import OrientedGraph

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

# fonction de dfs

def bfs(graph:OrientedGraph, start:int):
    """Makes a depth-first search and prints every node as soon as visited"""
    file = File([start])

    # Construction of the visited nodes' list
    n = graph.n
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

bfs(graph, 0)
