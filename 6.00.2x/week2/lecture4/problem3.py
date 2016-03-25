def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if not L:
        return float('NaN')

    mean = sum([len(t) for t in L]) / float(len(L))
    quantities = [(len(t) - mean)**2 for t in L]
    stdDev = (sum(quantities) / len(L))**0.5

    return stdDev


L = ['apples', 'oranges', 'kiwis', 'pineapples']
print stdDevOfLengths(L)
