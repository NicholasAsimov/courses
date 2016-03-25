def getSublists(L, n):
    sublists = []

    for i in range(len(L)):
        next_sublist = L[i:i+n]

        if len(next_sublist) == n:
            sublists.append(next_sublist)

    return sublists

# Test Cases
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
print getSublists(L, 4) == [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]

L = [1, 1, 1, 1, 4]
print getSublists(L, 2) == [[1, 1], [1, 1], [1, 1], [1, 4]]
