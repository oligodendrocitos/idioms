#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:03:10 2026

@author: qq20468
"""

#%% set operations ------------------------------------------------------------
A = {1,2,3}
B = {2,3,4}

A | B   # union
A & B   # intersection
A - B   # difference

print(A | B)
print(A & B)
print(A - B)


#%% collections ---------------------------------------------------------------
from collections import Counter, defaultdict
# -----------------------------------------------------
# 1. counter counts how many times each element appears.
# - has an inbuilt method to get most common element
# - Counters can be added / subtracted 
# - Counters can be turned into dicts
arr = [1,2,2,3,3,3]
c = Counter(arr)
print(c)

c[3]  # 3
c[10] # 0 

c.most_common(1) 
# [(3, 3)]

c1 = Counter([1,2,2])
c2 = Counter([2,3])
c1+c2
# Counter({2: 3, 1: 1, 3: 1})
c1-c2 


d = dict(c)


# -----------------------------------------------------
# 2. Defaultdict automatically initializes missing keys 
# - useful in freq counting
# - grouping items
d = defaultdict(list)
d["a"].append(1)

d = defaultdict(int)
for x in arr:
    d[x]+=1

# - grouping items
words = ["bat","tab","eat","tea"]
groups = defaultdict(list)
for w in words:
    key="".join(sorted(w))
    groups[key].append(w)
print(groups)

# - graph adjacency list
edges = [(1,2), (1,3), (2,4)]
graph = defaultdict(list)
for u,v in edges:
    graph[u].append(v)
    
# -----------------------------------------------------    
# 3) deque
# double-ended queue
from collections import deque

q=deque()
q.append(1)
q.append(2)
print(q)
q.popleft()
# q.pop()
print(q)

# -----------------------------------------------------
# 4) named tuple
from collections import namedtuple
Point = namedtuple("Point",["x","y"])
p = Point(3,4)
print(p.x)


#%% itertools -----------------------------------------------------------------
# 1. cartesian product = nested loops
from itertools import product, combinations, permutations
a = [1,3]
b = ['a','b']
# product(a, b) # generator
list(product(a,b))

# with repeat = useful for generating all possibilities
list(product([0,1],repeat=3))
list(product([0,1],repeat=2))
list(product([0,1]))

# 2. combinations = choose k elements, order doesn't matter
nums = [1,2,3]
list(combinations(nums,2))

# 3. permutations = order matters
list(permutations(nums, 2))

# 4. combinations with replacement
# Used when repetition is allowed.
from itertools import combinations_with_replacement
list(combinations_with_replacement([1,2,3], 2))

# 5. chain: flatten iterables
from itertools import chain
lists = [[1,2], [3,4], [5]]
list(chain.from_iterable(lists))
# [1,2,3,4,5]

# 6. accumulate: running totals
from itertools import accumulate
nums = [1,2,3,4]
list(accumulate(nums))
# [1,3,6,10]
# this is prefix sum

# you can also use a custom function
import operator
list(accumulate(nums, operator.mul))
# gives cumulative product

# 7. groupby - group consecutive elements
from itertools import groupby
data = [1,1,2,2,2,3]
for key, group in groupby(data):
    print(key, list(group))
    
    
# 8. zip longest
from itertools import zip_longest
a = [1,2]
b = ['a']
list(zip_longest(a, b, fillvalue=None))
# [(1,'a'), (2,None)]
# Useful when lists are unequal length.


#%% Loading files -------------------------------------------------------------
# CSV
import numpy as np
# 1) loads a numeric numpy array, skips header
npnums = np.loadtxt('file.csv', delimiter=",", skiprows=1)
# 2) structured array
npall =np.genfromtxt('file.csv', delimiter=",", names=True)
npall["a"]
npall["b"]


import pandas as pd
df = pd.read_csv('file.csv')

## TXT
with open("file.txt") as f:
    lines = f.readlines()
    
    
## JSON
import json 
with open("file.json") as f:
    data = json.load(f)
    
#%% Hash ----------------------------------------------------------------------
# An object is hashable if:
# It has a fixed value that does not change during its lifetime
# It has a hash value (an integer)
# It can be compared for equality

# Why Does Hashability Matter?
# Because:
# dict uses hash tables
# set uses hash tables
# So dictionary keys must be hashable.

# What Is a Hash?
# A hash is just a number derived from an object.

hash("hello")
hash(42)
hash((1,2))

# Python uses that number to decide where to store the key internally.
# If two objects are equal (a == b), they must have the same hash.


# These are hashable:
# int
# float
# bool
# str
# tuple (if all elements are hashable)
# frozenset

# Not Hashable (Mutable Types):
# list
# dict
# set

# If you need to use a list as a key:
# key = tuple(my_list)


