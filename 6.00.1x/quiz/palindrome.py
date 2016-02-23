def isPalindrome(aString):
    '''
    aString: a string
    '''
    original = aString.lower()
    bad_symbols = '!@#$%^&*()-_=+., '

    for ch in original:
        if ch in bad_symbols:
            original = original.replace(ch, '')

    reverse_word = ''

    for i in range(len(original)-1, -1, -1):
        reverse_word += original[i]

    return original == reverse_word


print isPalindrome("Acrobats stab orca.")
