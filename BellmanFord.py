from graph import OrientedGraph

def bellman_ford(graph:OrientedGraph, s:int):
    """
    s: starting vertice
    Returns:
        dist: the minimal distance from s to every other vertice in graph;
        pred: the predecessor of every vertice in the closest path from s to it.
    """
    n, weight = graph.n, graph.weight

    dist = [float('inf')] * n
    pred = [None] * n
    dist[s] = 0

    for k in range(n):
        # Solving the subproblem consisting in finding dist[u] for every u
        # using at most k edges
        for arc, w in weight.items():
            (u, v) = arc
            # Recalculate distance to v using the (u, v) arc
            new_dist = dist[v] + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                pred[v] = u
    
    # Check for negative-weight cycles:
    for arc, w in weight.items():
        (u, v) = arc
        new_dist = dist[v] + w
        if new_dist < dist[v]:
            raise Exception("graph has negative cycle")
    
    # Otherwise we solved the problem
    print("The graph doesn't have negative-weight cycles")
    return dist, pred
