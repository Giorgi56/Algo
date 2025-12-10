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
