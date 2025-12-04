"""Version propre de DFS.py"""
from graph import OrientedGraph

# fonction de dfs
def dfs(graph:OrientedGraph, start:int):
    """Makes a depth-first search and prints every node as soon as visited"""

    # Construction of the visited nodes' list
    n = graph.n
    visited = [False] * n

    def aux(s):
        print(s)
        visited[s] = True
        for neighbor in graph.neighbors(s):
            if not visited[neighbor]:
                aux(neighbor)

    aux(start)

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
