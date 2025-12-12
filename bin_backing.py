"""Algorithm of optimal packing"""
from copy import deepcopy

def partition(lst:list, partitioning:list, m:int):
    """
    m :                the number of different bins we're filling
    partitioning :     a list of integers from 0 to m - 1, each corresponding to
                       a bin in which we put elements of lst in.
                       (Both lst and partitioning are the same size)
    lst:               the list of elements we want to partition
    -----------------------------------------------------------------------------
    ex:
    partitioning = [1, 0, 1, 1, 0]
             lst = [9, 5, 2, 3, 1]
    
    then we have two bins : 0 -> [5, 1]
                            1 -> [9, 2, 3]
    
    so we return [
        [5, 1],
        [9, 2, 3]
    ]
    """
    n = len(lst)
    parts = []
    for i in range(m):
        part = []  # part (or bin) number i
        print(f"bin number {i} if being filled")
        for j in range(n):
            if partitioning[j] == i:
                print("\tadding ", lst[j])
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
    bins = []

    taken_empty = [False for _ in range(n)]
    def aux(i=0, bin_weight=0, taken=taken_empty):
        print(f"\naux has been called for i = {i}, bin_weight = {bin_weight}")
        if i >= n:
            return (bin_weight, taken)
        elif taken[i]:
            return aux(i + 1, bin_weight, taken)
        elif bin_weight + E[i] <= B:
            # weight of the bin if we take i
            taken[i] = bin_number
            print(f"added {E[i]} to {bin_weight}")
            take_result = aux(i + 1, bin_weight + E[i], taken)

            # weight of the bin if we do not take i
            taken[i] = False
            not_take_result = aux(i + 1, bin_weight, taken)                
            
            (w_taken, w_not) = take_result[0], not_take_result[0]
            print(f"B is {B}\t\tw_taken is {w_taken}")
            if w_taken <= B and ((w_not < w_taken) or (B < w_not)):
                taken[i] = bin_number
                return (bin_weight + E[i], taken)
            else:
                taken[i] = False
                return (bin_weight, taken)
        else:
            return (bin_weight, taken)
    
    m = 0  # total number of bins
    taken = deepcopy(taken_empty)
    for i in range(n):
        if not taken[i]:
            m += 1
            bin_number = i
            (new_bin_weight, new_bin_list) = aux(i)
            bins.append(new_bin_list)
            taken = new_bin_list
    
    return bins

print(binpacking(10, [4, 4, 5, 5, 5, 4, 4, 6, 6, 2, 2, 3, 3, 7, 7, 2, 2, 5, 5, 8, 8, 4, 4, 5]))
