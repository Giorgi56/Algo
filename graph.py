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
    

class WeightedOrientedGraph:
    def __init__(self, n:int, weight:dict):
        """
        n: the vertice set is {0, ..., n-1}
        weight: edge (u, v) -> weight(u, v) of the edge if the edge exists
        """
        self.n = n
        self.weight = weight

        # f is the flow. It has the same structure as self.weight
        # It is automatically made symmetric by a method below!
        # In the Ford-Fulkerson algorithm the initial flow is null
        self.f = {edge:0 for edge in weight.keys()}
        self.make_f_symmetric()
        
        # Adjascence list
        self.make_adj_list()

    def make_adj_list(self) -> None:
        """Make an adjascence list out of the weight function"""
        self.adj = [[] for _ in range(self.n)]
        for arc in self.weight.keys():
            (u, v) = arc
            self.adj[u].append(v)
    
    def make_f_symmetric(self):
        """Makes f symmetric, letting us create the flow more easily"""
        for edge, w in self.f.keys():
            (u, v) = edge
            self.f[(v, u)] = -w
    
    def check_f_is_flow(self, s, t) -> bool:
        """Checks that the weight function is indeed a flow verifying Ford-Fulkerson method hypotheses"""
        b = True

        # Skew symmetry (testing make_f_symmetric)
        for edge, w in self.f.items():
            (u, v) = edge
            b == (w == -self.f[(v, u)])

        # Check that the flow doesn't exceed the capacity
        for edge, w in self.weight.items():
            b = b and (self.f[edge] <= weight)
        
        # Check that the flow only goes out of s and in t
        for v in range(self.n):
            if (v, s) in self.f.keys() or (t, v) in self.f.keys():
                b = False
        
        # Check the flow conservation;
        # Also check that the flow going out of s is the flow going in t
        going_out_s, going_in_t = 0, 0
        for v in range(self.n):
            if v not in (s, t):
                # Then the flow going in should equal the flow coming out
                going_in, going_out = 0, 0
                for edge, w in self.f.items():
                    (a, b) = edge
                    if a == v:
                        going_out += w
                    elif b == v:
                        going_in += w
                b = b and (going_in == going_out)
            
            # Check that the flow going out of s is the flow going in t
            elif v == s:
                for edge, w in self.weight.items():
                    (a, b) = edge
                    if a == s:
                        going_out_s += w
                    elif b == t:
                        going_in_t += w
        
        b = b and (going_out_s == going_in_t)

        return b

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