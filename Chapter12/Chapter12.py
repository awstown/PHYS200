# -*- coding: utf-8 -*-

# Chapter 12 Exercises: 12.1, 12.2, 12.3
# Dwight Townsend
# Phys 400 - Spring 2012 - Cal Poly Physics



# imports
import random

# Exerise 12.1
def sumall(*args):
  return sum(args)

print sumall(1, 3, 5, 7, 9)


# Exercise 12.2
def sort_by_length(words):
    t = []
    for word in words:
       t.append((len(word), random.random(), word))

    t.sort(reverse=True)

    res = []
    for length, rand, word in t:
        res.append(word)
    return res

print sort_by_length(['hello','world', 'it', 'is', 'hot', 'in', 'here'])


# Exercise 12.3
english = 'Buddhism can be confusing to begin with, especially if you come from a Christian, Islamitic or Jewish background. You may be unfamiliar with concepts such as karma, rebirth, emptiness and the practice of meditation. On top of that, the presentation of Buddhism in the various traditions can vary quite a bit, so if you read materials from different traditions, it is easy to lose track.'
german  = 'Buddhismus kann verwirrend sein, zu beginnen, besonders wenn Sie aus einer christlichen, jdischen oder islamitischen Hintergrund kommen. Sie drfen nicht vertraut sein mit Begriffen wie Karma, Wiedergeburt, "Leere" und die Praxis der Meditation. Hinzu kommt, dass kann der Prsentation des Buddhismus in den verschiedenen Traditionen variieren ziemlich viel, wenn Sie also Materialien von'
french  = 'Le bouddhisme peut tre source de confusion, pour commencer, surtout si vous venez d\'un chrtien, fond Islamitic ou juive. Vous pouvez ne pas tre familiers avec des concepts tels que le karma, la renaissance, vide et la pratique de la mditation.'


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

def most_frequent(string):
    d = histogram(string)
    t = []
    for key, val in d.items():
        t.append((val, key))

    t.sort(reverse=True)

    res = []
    for occur, letter in t:
        res.append(letter)

    print res

most_frequent(german)

    
    
