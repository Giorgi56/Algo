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

def binpacking(B:int, E:list):
    """
    Given 
    B: a weight limit for each pack and 
    E: the set of integers we want to pack

    the function returns the lists of elements of E representing each a pack.
    """
    E.sort(reverse=True)
    print(E)
    n = len(E)

    taken_empty = [False for _ in range(n)]
    def aux(i=0, bin_weight=0):
        """Fills the bin number 'bin_number' """
        global taken

        # print(f"\naux called for bin_number = {bin_number}, bin_weight = {bin_weight}")
        if i >= n:
            return bin_weight
        elif taken[i]:
            return aux(i + 1, bin_weight)
        elif bin_weight + E[i] > B:
            print(f"bin weight: {bin_weight}, E[i] = {E[i]}")
            print("\t\t\tWEIGHT EXCEEDING")
            return aux(i + 1, bin_weight)
        else:
            # weight of the bin if we take i
            print("considering ", E[i])
            print("taken: ", taken)
            w_taken = aux(i + 1, bin_weight + E[i])

            # weight of the bin if we do not take i
            w_not = aux(i + 1, bin_weight)
            
            if w_taken <= B and ((w_not < w_taken) or (B < w_not)):
                # We chose to take E[i] in the new bin
                if w_taken == B:
                    w_taken
                taken[i] = bin_number
                return w_taken
            else:
                return aux(i + 1, bin_weight)
    
    m = 0  # total number of bins
    bin_number = 0
    global taken
    taken = deepcopy(taken_empty)
    for i in range(n):
        if not taken[i]:
            m += 1
            bin_number += 1
            print("creating bin number ", bin_number)
            weight = aux(i)
    
    return partition(E, taken, m)

if __name__ == '__main__':
    print(binpacking(10, [4, 4, 5, 5, 5, 4, 4, 6, 6, 2, 2, 3, 3, 7, 7, 2, 2, 5, 5, 8, 8, 4, 4, 5]))
