"""
Given infinite amounts of each coin:
    S = (200, 100, 50, 20, 10, 5, 2, 1)
and a value to give back
    ex: 3$57c i.e. 357c
what's the minimal number of coins we can use to give the money back?
"""
from copy import deepcopy

S = (200, 100, 50, 20, 10, 5, 2, 1)
rev_S = {
    200: 0,
    100: 1,
    50: 2,
    20: 3,
    10: 4,
    5: 5,
    2: 6,
    1: 7
}

def recursive(L:list[int], amount_due:int, i:int):
    """
    L is the vector of 8 integers where 
        for all i in {0, ..., 7} L[i] is the number of S[i] coins used.
    It has an exponential complexity!!!
    """
    if i > 7 or amount_due == 0:
        return L

    coin = S[i]

    if amount_due > coin:
        # number of times we could take the coin
        m = amount_due / coin

        L2 = deepcopy(L)
        cases = []  # Each case corresponds to m: the number of times we choose to take the coin
        for j in range(1, m+1):
            L2[i] = j
            case_ = recursive(L2, amount_due-coin, i+1)
            cases.append(sum(case_), case_)
        return min(cases)[1]  # The min is chosen in a lexicographic order

    elif amount_due == coin:
        # Taking the coin is the optimal choice here
        L[i] += 1
        return recursive(L, amount_due-coin, i+1)
    else:
        return recursive(L, amount_due, i+1)

def dynamic(amount_due:int):
    """
    An optimized solution time-wise. It does cost more memory-wise though.
    Recursive formula:
        sum(dynamic(amount_due)) = 1 if there's a coin with the exact value of amount_due
        sum(dynamic(amount_due)) = 1 + min{sum(dynamic(amount_due - S[i])), i in {0, ..., 7} such that S[i] <= amount_due}
    Explanation:
        the non-base calculation is searching for the best coin to take among the candidates, thus the +1. 
        The candidates cannot have a higher value than the amount due.
    """
    solutions = [-1] * (amount_due + 1)
    def aux(due):
        if solutions[due] == -1:
            # solutions[due] has yet to be calculated
            if due in S:
                # Base case
                solutions[due] = 1
            else:
                cases = []
                for i in range(8):
                    if due > S[i]:
                        cases.append(aux(due-S[i]))
                solutions[due] = 1 + min(cases)
        # Now we're sure to have the result
        return solutions[due]
    return aux(amount_due)

print(dynamic(357))
