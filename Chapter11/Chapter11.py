## Chapter 11 Exercises: 11.1, 11.2, 11.3, 11.4, 11.5

# Exercise 11.1
##def fileToDict(f):
##    fin = open(f)
##    d = dict()
##    for line in fin:
##        word = line.strip()
##        print word
##        d[word] = ' '
##        print d
##
##fileToDict('words.txt')


# Exercise 11.2
def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

h = histogram('brontosaurus')
print h

# Exercise 11.3
def print_hist(h):
    lh = h.keys()
    lh.sort()
    for c in lh:
        print c, h[c]

h = histogram('parrot')
print_hist(h)

# Exercise 11.4
def reverse_lookup(d, v):
    l = []
    for k in d:
        if d[k] == v:
            l.append(k)
    return l

h = histogram('parrot')

print reverse_lookup(h, 2)
print reverse_lookup(h, 1)
print reverse_lookup(h, 5)

# Exercise 11.5
## Original
def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    return inv

hist = histogram('parrot')
print hist
inv = invert_dict(hist)
print inv

## Modified
def invert_dict2(d):
    inv = dict()
    for key in d:
        val = d[key]
        inv.setdefault(val,[]).append(key)
    return inv

inv = invert_dict2(hist)
print inv











