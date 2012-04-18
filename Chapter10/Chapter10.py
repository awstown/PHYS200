## Chapter 10 Exercises

# Exercise 10.1
def cum_Sum(numbers):
    csum = [];
    for i in range(len(a)):
        csum.append(sum(a[0:i+1]))
    return csum

a = [12, 3, 4, 5, 6]
print cum_Sum(a)


# Exercise 10.2
def chop(l):
    del l[0]
    del l[-1]
    return None

l = [1, 3, 5, 7]
chop(l)
print l

def middle(l):
    chop(l)
    return l
    
l = [0, 2, 4, 6]
print middle(l)

# Exercise 10.3
def is_sorted(t):
    o = t[:]
    t.sort()
    if o == t:
        return True
    else:
        return False

print is_sorted([1,2,2])
print is_sorted(['b', 'a'])

# Exercise 10.4
def is_anagram(word1, word2):
    list1 = list(word1)
    list2 = list(word2)

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False

print is_anagram('asdf', 'asdfasdf') #False
print is_anagram('asdf', 'fdas')     #True

            
