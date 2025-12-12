from bin_backing import partition, binpacking

assert partition([9, 5, 2, 3, 1], [1, 0, 1, 1, 0], 2) == [
    [5, 1],
    [9, 2, 3]
]
