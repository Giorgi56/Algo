from graph import WeightedOrientedGraph

def has_augmenting_path(graph:WeightedOrientedGraph, s, t) -> bool:
    """
    Checks if the flow graph (is indeed a flow graph), 
    and that it has an augmenting path from s to t
    """
    assert graph.check_weight_is_flow(s, t)

def ford_fulkerson(graph:WeightedOrientedGraph):
    pass
