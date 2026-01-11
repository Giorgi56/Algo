from graph import WeightedOrientedGraph

def has_augmenting_path(graph:WeightedOrientedGraph, s, t) -> tuple[bool, list[int]]:
    """
    Checks if the flow graph (is indeed a flow graph), 
    and that it has an augmenting path from s to t
    """
    assert graph.check_f_is_flow(s, t)
    
    visited_edges = {edge:False for edge in graph.weight.keys()}
    def aux(u, prev=[]):
        """
        Does a DFS of the graph to find t only using edges which have some capacity left.
        Returns None if no path can be found, and a list of vertices otherwise.
        The path resembles [s, ..., t]
        """
        if u == t:
            return prev + [t]
        
        # List of vertices to visit next
        next_visits = []
        for v in graph.adj[u]:
            if self.f[(u, v)] < self.weight[(u, v)] and not visited[(u, v)]:  # graph.weight is the dict of capacities
                next_visits.append(v)
        # Visit said vertices
        for v in next_visits:
            visited_edges[(u, v)] = True
            aux(v, prev+[v])
        # If we're stuck before reaching t then there are no augmenting paths
        if not next_visits:
            return None
    
    ret = aux(s)
    return (ret != None, ret)

def max_capacity_of_path(graph:WeightedOrientedGraph, p:list[int]) -> int:
    """Returns the maximum amount with which the flow can be augmented in graph"""
    capacities = []
    for i in range(len(p) - 1):  # p contains at least s and t so len(p) >= 2
        u, v = p[i], p[i + 1]
        capacities.append(graph.weight[(u, v)] - graph.f[(u, v)])
    return min(capacities)

def augment_path(graph:WeightedOrientedGraph, p:list[int]) -> None:
    """Augmnts the path p in graph by the max possible amount"""
    m = max_capacity_of_path(graph, p)
    for i in range(len(p) - 1):  # p contains at least s and t so len(p) >= 2
        u, v = p[i], p[i + 1]
        graph.f[(u, v)] += m

def ford_fulkerson(graph:WeightedOrientedGraph, s, t):

    while True:
        (b, p) = has_augmenting_path(graph, s, t)
        if not b:
            break
        augment_path(graph, p)
