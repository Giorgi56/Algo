"""Variante de Dijkstra"""

from graph import WeightedNonOrientedGraph

def dijkstra(graph: WeightedNonOrientedGraph, starting_node: int, target_node):
    n = graph.n
    visited = [False] * n

    dists = [float('infinity') for _ in range(n)]
    dists[starting_node] = 0

    def select_c():
        """Selects the node with the minimal distance to s amongst the unvisited set"""
        print(dists)
        if visited != [True] * n:  # (We have not yet reached the target) nor visited every node

            min_dist, indx = float('infinity'), -1
            for i in range(graph.n):
                if not visited[i] and min_dist > dists[i]:
                    min_dist, indx = dists[i], i
            print(f"selected {indx}")
            return indx

        else:
            return None

    c = starting_node  # The current node
    while  c != target_node and c != None:
        for neighbor in graph.neighbors(c):
            if not visited[neighbor]:
                new_dist = dists[c] + graph.mat[c][neighbor]  # Newly calculated distance between starting_node and c
                if new_dist < dists[neighbor]:
                    dists[neighbor] = new_dist
                    print(f" c is {c}. New distance to {neighbor} is {new_dist}")

        visited[c] = True
        b = (target_node == c)
        c = select_c()

    return dists[target_node]
