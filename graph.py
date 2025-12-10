"""Definition of graph objects and properties"""
from copy import deepcopy

# Type OrientedGraph - liste d'adjascence - sommet = entier entre 0 et n-1 où n est le nombre d'arrêtes
class OrientedGraph:
    def __init__(self, adj:list[list[int]]):
        self.adj = adj
        self.n = len(adj)
    
    def neighbors(self, s:int):
        return self.adj[s]  # adjascence list of the node with index of s

    def adj_matrix(self, weighted=False):
        if weighted:
            # The inexistent arcs are marked with an infinite distance=
            mat = [[float('infinity') for _ in range(self.n)] for _ in range(self.n)]
            for i in range(self.n):
                mat[i][i] = 0  # The diagonal is null
            return mat     # mat will be completed in 
        else:
            # Return a matrix with 1 if the (i, j) arc exists and 0 if not
            mat = [[0 for _ in range(self.n)] for _ in range(self.n)]

            for i, line in enumerate(self.adj):
                for j in range(len(line)):
                    mat[i][j] = 1

            return mat

class NonOrientedGraph(OrientedGraph):
    def __init__(self, adj:list[list[int]], weighted=False):
        self.adj = adj
        temp_adj = deepcopy(adj)
        self.n = len(adj)

        # Creating a symmetrical adjascence list
        for node in range(len(temp_adj)):
            neighbors = temp_adj[node]
            for neighbor in neighbors:
                self.adj[neighbor].append(node)
        
        self.mat = self.adj_matrix(weighted = weighted)
    
    def add(self, arc:tuple):
        """adds the (u, v) arc"""
        (u, v) = arc
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.mat[u][v], self.mat[v][u] = 1, 1
    
    def remove(self, arc:tuple):
        """adds the (u, v) arc"""
        (u, v) = arc
        self.adj[u].remove(v)
        self.adj[v].remove(u)
        self.mat[u][v], self.mat[v][u] = 0, 0

class WeightedNonOrientedGraph(NonOrientedGraph):
    def __init__(self, adj:list[list[tuple[int, int]]]):
        """format for weights: (n, w) will be respectively neighbor and weight in an arc"""
        simple_adj = [[arc[0] for arc in line] for line in adj]
        super().__init__(simple_adj, weighted=True)

        for u, line in enumerate(adj):
            for arc in line:
                (v, w) = arc
                self.mat[u][v], self.mat[v][u] = w, w
    
    def arcs(self):
        """
        returns a list of the graph's arcs with no redundancies, and sorted by weight.
        Format:
            list of [...(w, (u, v))...] where:
                (u, v) if an arc
                w is (u, v)'s weight
        """
        arcs = []
        for i in range(self.n):
            for j in range(i + 1, self.n):  # j > i leaves us in the top triangle of the mat
                arcs.append((self.mat[i][j], (i, j)))

        return sorted(arcs)
    

test_graph = WeightedNonOrientedGraph([
    [(1, 1), (2, 2), (3, 3)],
    [(4, 5), (5, 2)],
    [(4, 3)],
    [(4, 1)],
    [(5, 1)],
    []
])

for i in range(test_graph.n):
    print(test_graph.mat[i])