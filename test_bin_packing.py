from bin_backing import partition, binpacking

assert partition([9, 5, 2, 3, 1], [1, 2, 1, 1, 2], 2) == [
    [9, 2, 3],
    [5, 1]
]

assert partition(['a', 'b', 'v', 'e', 'r', 'q', 'z'], [1, 3, 2, 2, 2, 3, 1], 3) == [
    ['a', 'z'],
    ['v', 'e', 'r'],
    ['b', 'q']
]
