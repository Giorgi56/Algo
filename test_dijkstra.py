from graph import WeightedNonOrientedGraph
from UCS import dijkstra

test_graph = WeightedNonOrientedGraph([
    [(1, 1), (2, 2), (3, 3)],
    [(4, 5), (5, 2)],
    [(4, 3)],
    [(4, 1)],
    [(5, 1)],
    []
])

print("The shortest distance from 0 to 5 is ", dijkstra(test_graph, 0, 5))

test_graph = WeightedNonOrientedGraph([
    [(1, 0), (2, 1), (3, 1)],
    [(4, 1), (5, 0)],
    [(4, 1)],
    [(4, 0)],
    [(5, 1)],
    []
])

print("The shortest distance from 0 to 5 is ", dijkstra(test_graph, 0, 5))
