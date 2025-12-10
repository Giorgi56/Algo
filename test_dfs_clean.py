from graph import OrientedGraph, WeightedNonOrientedGraph
from DFS_clean import dfs, cyclique

graph = OrientedGraph([
    [1, 2, 7],
    [6],
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

test_graph = WeightedNonOrientedGraph([
    [(1, 1), (2, 2), (3, 3)],
    [(4, 5), (5, 2)],
    [(4, 3)],
    [(4, 1)],
    [(5, 1)],
    []
])
assert cyclique(test_graph)

test_graph2 = WeightedNonOrientedGraph([
    [(1, 1)],
    [(2, 1)],
    [(3, 1)],
    [(4, 1)],
    [],
    []
])
dfs(test_graph2, start=0)
assert not cyclique(test_graph2)
