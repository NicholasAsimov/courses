def getSublists(L, n):
    sublists = []

    for i in range(len(L)):
        next_sublist = L[i:i+n]

        if len(next_sublist) == n:
            sublists.append(next_sublist)

    return sublists


def longestRun(L):
    best = []
    for i in range(len(L), 0, -1):
        for lst in getSublists(L, i):
            if lst == sorted(lst) and len(lst) > len(best):
                best = lst

    return len(best)

# Test Cases
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
# print longestRun(L) == [3, 4, 5, 7, 7]
print longestRun([10, 4, 6, 8, 3, 3, 4, 5, 7, 7, 2, 9])
