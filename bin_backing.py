"""Algorithm of optimal packing"""
from copy import deepcopy

def partition(lst:list, partitioning:list, m:int):
    """
    m :                the number of different bins we're filling
    partitioning :     a list of integers from 1 to m, each corresponding to
                       a bin in which we put elements of lst in.
                       (Both lst and partitioning are the same size)
    lst:               the list of elements we want to partition
    -----------------------------------------------------------------------------
    ex:
    partitioning = [1, 0, 1, 1, 0]
             lst = [9, 5, 2, 3, 1]
    
    then we have two bins : 1 -> [5, 1]
                            2 -> [9, 2, 3]
    
    so we return [
        [5, 1],
        [9, 2, 3]
    ]
    """
    n = len(lst)
    parts = []
    for i in range(1, m + 1):
        part = []  # part (or bin) number i
        for j in range(n):
            if partitioning[j] == i:
                part.append(lst[j])
        parts.append(part)
    return parts

def print_indexes(lst, indx):
    ret = []
    for i in indx:
        ret.append(lst[i])
    print(ret)

def binpacking(B:int, E:list):
    """
    Given 
    B: a weight limit for each pack and 
    E: the set of integers we want to pack

    the function returns the lists of elements of E representing each a pack.
    """
    E.sort(reverse=True)
    n = len(E)

    def aux(i=0, bin_weight=0, path=[]):
        """Fills the bin number 'bin_number' """
        global taken

        if path:
            print_indexes(E, path)

        # print(f"\naux called for bin_number = {bin_number}, bin_weight = {bin_weight}")
        if i >= n:
            return bin_weight, path
        elif taken[i]:
            return aux(i + 1, bin_weight, path)
        elif bin_weight + E[i] > B:
            return aux(i + 1, bin_weight, path)
        else:
            # weight of the bin if we take i
            w_taken = aux(i + 1, bin_weight + E[i], path + [i])[0]

            # weight of the bin if we do not take i
            w_not = aux(i + 1, bin_weight)[0]
            
            if (w_not < w_taken) or (B < w_not):
            # Then we chose to take E[i] in the new bin:
                taken[i] = bin_number
                return w_taken, path
            else:
                return aux(i + 1, bin_weight, path)
    
    m = 0           # total number of bins
    bin_number = 0  # current working bin

    # taken list
    taken_empty = [False for _ in range(n)]
    global taken
    taken = deepcopy(taken_empty)

    ret = []
    for i in range(n):
        if not taken[i]:
            print("STARTING A NEW BIN")
            m += 1
            bin_number += 1
            hi = aux(i)
    # return partition(E, taken, m)

binpacking(10, [4, 4, 5, 5, 5, 4, 4, 6, 6, 2, 2, 3, 3, 7, 7, 2, 2, 5, 5, 8, 8, 4, 4, 5])
