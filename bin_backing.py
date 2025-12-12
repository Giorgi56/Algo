"""Algorithm of optimal packing"""

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
            taken[i] = True
            print(f"added {E[i]} to {bin_weight}")
            take_result = aux(i + 1, bin_weight + E[i], taken)

            # weight of the bin if we do not take i
            taken[i] = False
            not_take_result = aux(i + 1, bin_weight, taken)                
            
            (w_taken, w_not) = take_result[0], not_take_result[0]
            print(f"B is {B}\t\tw_taken is {w_taken}")
            if w_taken <= B and ((w_not < w_taken) or (B < w_not)):
                taken[i] = True
                return (bin_weight + E[i], taken)
            else:
                taken[i] = False
                return (bin_weight, taken)
        else:
            return (bin_weight, taken)
    
    for i in range(n):
        (new_bin_weight, new_bin_list) = aux(i)
        bins.append(new_bin_list)
        taken = new_bin_list
    
    return bins

print(binpacking(10, [4, 4, 5, 5, 5, 4, 4, 6, 6, 2, 2, 3, 3, 7, 7, 2, 2, 5, 5, 8, 8, 4, 4, 5]))
