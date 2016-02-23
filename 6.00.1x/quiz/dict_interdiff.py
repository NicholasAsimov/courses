def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect = {}
    difference = {}

    for key_1, key_2  in map(None, d1.keys() d2.keys()):
        print key_1, key_2
        if key_1 == key_2:
            # intersect[key_1] = f(d1[key_1], d2[key_2])
            intersect[key_1] = 'future'
        else:
            if key_1 is None:
                difference[key_2] = d2[key_2]
            elif key_2 is None:
                difference[key_1] = d1[key_1]
            else:
                difference[key_1] = d1[key_1]
                difference[key_2] = d2[key_2]



    return (intersect, difference)

d1 = {9: 1, 4: 4, 5: 3, 6: 3}
d2 = {1: 1, 2: 2, 3: 3, 4: 5, 8: 4, 10: 0}

#print dict_interdiff(d1, d2)
# print dict_interdiff(d1, d2) == ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})

print dict_interdiff(d1, d2)
