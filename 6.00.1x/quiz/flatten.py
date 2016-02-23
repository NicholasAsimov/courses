def flatten(aList):
    global flat
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    if aList == []:
        return aList

    if type(aList[0]) == list:
        return flatten(aList[0]) + flatten(aList[1:])

    return aList[:1] + flatten(aList[1:])

aList = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

print flatten(aList)

testCase = [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
print flatten(aList) == testCase
