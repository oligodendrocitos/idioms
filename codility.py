#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:03:10 2026

@author: qq20468
"""

#%% 1. Demo problem ------------------------------------------------------------
"""Write a function:
given an array A of N integers, 
returns the smallest positive integer
(greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2],
the function should return 5. 
Given A = [1, 2, 3], 
the function should return 4. 
Given A = [−1, −3], 
the function should return 1. 

Write an efficient algorithm for the following assumptions: 
    N is an integer within the range [1..100,000]; 
    each element of array A is an integer within the range [−1,000,000..1,000,000].

"""

# 1. if array has len M, it can have M slots of integers
# if X = missing integer, 
# The largest possible value X can be is M+1
# Because if you don't have any missing integers, 
# [1,2,3,30,64,] >> 5 slots for ints, 
# [1,2,3,4,6,] >> Best Maximum case scenario of a 5 slot array 
# 5 slots >> max X is 5 (it will never be 999 because with 5 slots it's impossible to have non-missing ints not smaller than 999)

A = [-5,1,2,3,4,7]
A = [1,2,3,4,5,7] 

seen = {}
maxX = len(A)

from collections import Counter
c=Counter(A)
# 1. go through A
# 2. if element is positive, add to seen. 
# 

def solution(A):
    seen={}
    maxX = len(A)+1
    
    for i in A:
        if i>0:
            seen[i] = seen.get(i, 0) + 1
        
    
    # go through dict
    for i in range(1, maxX):
        if i not in seen: # seen[i]:
            return i
        
    
    
solution(A)



#%% 1. Lesson 1 ------------------------------------------------------------
"""
Write fn to return longest sequence of zeros surrounded by 1s
For example, number 9 has binary representation 1001
content_copy
 and contains a binary gap of length 2. The number 529 has binary representation 1000010001
content_copy
 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100
content_copy
 and contains one binary gap of length 1. The number 15 has binary representation 1111
content_copy
 and has no binary gaps. The number 32 has binary representation 100000
content_copy
 and has no binary gaps.
"""
def solution(N):
    # N = 9
    s = bin(N)
    # print(s)
    l=0 #index of left 1
    n=len(s)
    # r = index of right 1

    best = 0
    currgap = (0,0)
    currlen = 0

    # skip initial 1s? l HAS to be 1. 
    while s[l]!='1':
        l+=1

    for r in range(l+1,n):
        assert s[l]=='1'
        ch = s[r]

        # if ch==0, increase currlen
        if ch=='0':
            currlen+=1
        else:
        # elif ch=='1':
            # end of current gap: mark all varuables
            # best = max(best, r-l+1)
            if ch=='1':
                best = max(best, currlen)
            currlen=0
            
            while s[l]!='1':
                l+=1
            r=l+1
        # else:
            # raise ValueError("unexpected")


    # print(best)
    return best




#%% 2. Cyclic array rotation ------------------------------------------------------------

def solution(A, K):
    # Implement your solution here
    # pass

    if not A:
        return []
    if K==0:
        return A

    n=len(A)
    if K==n:
        return A
    
    # idx  = r
    idx = list(i for i in range(n))
    # new index = last K elements + all until K

    if K>n:

        # newK=K//n
        newK=K%n
        newidx = idx[-newK:] + idx[:-newK]
        # newidx = idx[-(n%K):] + idx[:-(n%K)]
        # print(f"theor ix: {}:, [] )
    else:
        newidx = idx[-K:] + idx[:-K]
        # print(f"{-K}:, [] )

    rotA = list(A[i] for i in newidx)

    return rotA



#%% 2. Odd occurences in array ------------------------------------------------------------
def solution(A):
    # return value of unpaired element:
    # option 1: frequency counting
    # option 2: ? 

    counts = {}
    # n = len(A)
    # assert odd? 

    for i in A:
        counts[i] = counts.get(i,0) + 1

    # lookup 
    # val = find_key(counts, 1)
    for key,val in counts.items():
        if val%2==1:
            return key

    # it says I can assume it's always odd
    # return key


#%% 3. Frog jump ------------------------------------------------------------

import math

def solution(X, Y, D):
    if D==0:
        return 0 # wrong, but expects int
        # return None

    ddy = Y-X

    if ddy==0:
        return 0
    # jumps = ddy / D , + 1 if there's a remainder
    jumps = math.ceil(ddy/D)

    return jumps

#%% 3. missing element ------------------------------------------------------------
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(A):
    # Implement your solution here
    # pass
    if not A:
        return 0

    s = sum(A)

    n = len(A)+1
    theorsum = n*(n+1) // 2
    missing = theorsum - s
    
    return missing


#%% 3. tape ------------------------------------------------------------
# failed: 2 elements, 
#         small elements
def solution(A):
    # N integers
    # P splits into two parts
    # difference between parts:
    # |sum(A[:p]) - sum(A[P:])|
    # A = [3,1,2,4,3]
    # 1. init diff sum [0] and sum [1:]
    # 2. loop thru nums, update diff
    # if diff is better, update new splitting point
    
    # print("####")
    if not A:
        return 0
    if len(A)==1:
        return 0

    # P=0
    s1 = 0
    s2 = sum(A)
    best = math.inf #abs(s1-s2)
    bestix = 0

    for i in range(len(A)-1):
        # skip 1st elem? 
        s1+=A[i]
        s2-=A[i]

        newsum = abs(s1-s2)
        # print(newsum)
        if newsum < best:
            best = newsum
            # bestix = i

    return best 

# import 
# A = np.random.rand
A = [2000,2000]
print(solution([3,1,2,4,3]))       # expected 1 (example)
print(solution([1000, -1000]))     # expected 2000 (two elements test)
print(solution([20,0,0,0]))        # expected 20 (small elements style)
print(solution([1, -1, 1, -1, 1])) # expected 1

solution(A)
#%% 1. Demo problem ------------------------------------------------------------

def solution(X, A):
    # pos 0 >> want to get to pos 1 X+1
    # A = [1,3,1,4,2,3,5,4]
    # X = 5
    #    1 2   4 2   5 

    # frog can only cross when 1..X are covered with leaves
    # i.e. we've seen 1,2,3,4,5
    # return index when ints 1..X are satisfied

    if not A:
        return -1

    counts = {}
    need = {x:1 for x in range(1,X+1)} # ??
    req = X
    # print(need)

    for t,x in enumerate(A):
        # if x < X:
        if x in need.keys():
            del need[x]
        # need[x] = need.get(x,0) - 1 # remove element if it's satisifed
        
        if not need:
            return t


    return -1

def solution(X, A):
    # earliest time when positions 1..X all have leaves
    if X <= 0:
        return 0

    needed = set(range(1, X + 1))
    for t, x in enumerate(A):
        if x in needed:
            needed.remove(x)
            if not needed:
                return t
    return -1

#%% 4. Check if permutation ------------------------------------------------------------
def solution(A):
    n = len(A)
    # [1,2,3,4]
    # len 4
    # 
    seen = {k:0 for k in range(1,n+1)} #[False] * 

    for v in A:
        if v>n:
            return 0 # number bigger than n: can't be  a perm

        seen[v] = seen.get(v) + 1
        if seen[v]>1: # freq>1: can't be a perm 
            return 0    

    
    # check if 


#nah

def solution(A):
    N = len(A)
    
    seen = set()
    
    for x in A:
        if x<1 or x>N or x in seen:
            return 0
        seen.add(x)
        
    return 1





