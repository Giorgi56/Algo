"""Definition of graph objects and properties"""

# Type OrientedGraph - liste d'adjascence - sommet = entier entre 0 et n-1 où n est le nombre d'arrêtes
class OrientedGraph:
    def __init__(self, adj:list[list[int]]):
        self.adj = adj
        self.n = len(adj)
    
    def neighbors(self, s:int):
        return self.adj[s]  # adjascence list of the node with index of s
    
    def add(self, node:int, neighbors:list):
        if node == len(self.adj) + 1:
            # i.e. if we're creating a new node
            self.adj.append(neighbors)
        else:
            self.adj[node] = self.adj[node] + neighbors
    
    def adj_matrix(self):
        mat = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i, line in enumerate(self.adj):
            for j in range(len(line)):
                mat[i][j] = line[j]

        return mat

class NonOrientedGraph(OrientedGraph):
    def __init__(self, adj:list[list[int]]):
        self.adj = adj

        # Creating a symmetrical adjascence list
        for node in range(len(adj)):
            neighbors = adj[node]
            for neighbor in neighbors:
                self.adj[neighbor].append(node)
        
        self.mat = self.adj_matrix()