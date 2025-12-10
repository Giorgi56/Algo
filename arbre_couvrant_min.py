"""Algorithme de l'arbre couvrant de poids minimal"""
from DFS_clean import cyclique
from graph import WeightedNonOrientedGraph, NonOrientedGraph

def kruskal(graph:WeightedNonOrientedGraph):
    """Arbre couvrant de poids min avec algo de Kruskal"""
    arcs = graph.arcs()

    T = NonOrientedGraph([[] for _ in range(graph.n)])
    for arc in arcs:
        T.add(arc[1])
        print("adding arc: ", arc)
        print(T.mat)
        if cyclique(T):
            T.remove(arc[1])
            print("removed arc: ", arc)
            print(T.mat)
    
    return T.mat


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
