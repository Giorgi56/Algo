"""Version propre de DFS.py"""
from graph import OrientedGraph, WeightedNonOrientedGraph, NonOrientedGraph

# fonction de dfs
def dfs(graph: OrientedGraph, start: int):
    """Makes a depth-first search and prints every node as soon as visited"""

    # Construction of the visited nodes' list
    n = graph.n
    visited = [False] * n

    def aux(s:int):
        print(s)
        visited[s] = True
        for neighbor in graph.neighbors(s):
            if not visited[neighbor]:
                aux(neighbor)

    aux(start)

def cyclique(graph:NonOrientedGraph):
    n = graph.n

    def aux(s:int, start:int, parent):
        """Tests if the node s is the starting node of our potential cycle"""

        def aux2(neighbors, start, s):
            """Checks if any of the neighbors lead to the start"""
            if neighbors != []:
                return aux(neighbors[0], start, parent=s) or aux2(neighbors[1:], start, s)
            else:
                return False

        global visited
        neighbors = [] # List of all neighbors we will visit

        visited[s] = True

        for neighbor in graph.neighbors(s):
            if neighbor == start and (parent != start):  # If we arrived back to start (without start being the parent node)
                return True
            elif not visited[neighbor]:
                neighbors.append(neighbor)
        
        # Unless we're at a dead end, repeat aux with all the neighbors
        if  len(neighbors) == 0:  # A dead end is when no more neighbors are unvisited
            return False
        else:
            return aux2(neighbors, start, s)

    b = False  # b = (a cycle has been found)
    for i in range(n):
        # do we come back to i by DFS?
        global visited
        visited = [False] * n
        b = b or aux(i, i, i)
    
    return b

