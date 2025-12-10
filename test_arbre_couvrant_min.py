from graph import WeightedNonOrientedGraph, NonOrientedGraph
from arbre_couvrant_min import kruskal

test_graph = WeightedNonOrientedGraph([
    [(1, 1)],
    [(2, 1)],
    [(3, 1)],
    [(0, 1)]
])
print(kruskal(test_graph))

test_graph2 = WeightedNonOrientedGraph([
    [(1, 1)],
    [(2, 1)],
    [(3, 1)],
    [(0, 0)]
])
print(kruskal(test_graph2))

test_graph3 = WeightedNonOrientedGraph([
    [(1, 1)],
    [(2, 0), (3, -1)],
    [(3, 1)],
    [(0, 1)]
])
print(kruskal(test_graph3))
