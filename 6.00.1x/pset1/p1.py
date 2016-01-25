# s is predefined string of characters

vowel_counter = 0

for char in s:
    if char in 'aeiou':
        vowel_counter += 1

print "Number of vowels:", vowel_counter
