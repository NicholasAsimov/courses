# s is predefined string of characters
s = 'azcbobobegghakl'
bob_counter = 0
idx = 0

while True:
    bob_idx = s.find('bob', idx)

    if bob_idx != -1:
        bob_counter += 1
        idx = bob_idx + 1
    else:
        break

print "Number of times bob occurs is:", bob_counter
