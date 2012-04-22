# Exercise 8.1
def printBackwards(str):
    """Exercise 8.1 prints the input word backwards"""
    index = len(str)
    while index > 0:
        print str[index-1]
        index = index - 1
    
## printBackwards('hello')

# Exercise 8.2
##prefixes = 'JKLMNOPQ'
##suffix = 'ack'
##
##for letter in prefixes:
##    if (letter == 'O') or (letter == 'Q'):
##        print letter + 'u' + suffix
##    else:
##        print letter + suffix

# Exercise 8.4
def find(word, letter, index=0):
    """ This function searches the given word for the given letter. """
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print find('hello','l')

# Exercise 8.5
def count(word, letter):
    """ Counts the number of times 'letter' appears in 'word'. """
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    return count

print count('hello', 'l')

# Exercise 8.6
##def count(word, letter):
##    count = 0
    
# Exercise 8.9
def is_palindrome(word):
    """ This function checks to see if 'word' is a palindrome. """
    if word == word[::-1]:
        return True
    else:
        return False

print is_palindrome('asdfdsa')

# Exercise 8.10
## Done and Done



    
    
