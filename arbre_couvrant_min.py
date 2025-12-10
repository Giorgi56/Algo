"""Algorithme de l'arbre couvrant de poids minimal"""
from DFS_clean import cyclique
from graph import WeightedNonOrientedGraph, NonOrientedGraph

def kruskal(graph:WeightedNonOrientedGraph):
    """Arbre couvrant de poids min avec algo de Kruskal"""
    arcs = graph.arcs()
    print(arcs)

    T = NonOrientedGraph([[] for _ in range(graph.n)])
    for arc in arcs:
        T.add(arc[1])
        if cyclique(T):
            T.remove(arc[1])
    
    return T


test_graph2 = WeightedNonOrientedGraph([
    [(1, 1)],
    [(2, 1)],
    [(3, 1)],
    [(4, 1)],
    [],
    []
])
kruskal(test_graph2)
