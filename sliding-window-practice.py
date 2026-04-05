#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 19:16:03 2026
____________________________________________
When Should Your Brain Say "Sliding Window"?
You should suspect sliding window when the problem says things like:
- Longest/shortest subarray…
- Substring with…
- At most K…
- No more than K distinct…
- Sum ≤ / ≥ something…
- Contiguous segment…

If the data is contiguous and you're optimizing something over a range, 
sliding window is likely part of the solution.
______________
Core Intuition
Instead of:
"Try every possible subarray" → O(n²)

You:
Expand right pointer to grow window
Shrink left pointer when constraint breaks
Maintain a valid window in O(n)
Each index moves at most once → total O(n).

@author: qq20468
"""


# Core template:
nums=[1,2,3,4]
l=0
window_invalid=True

for r in range(len(nums)):
    #1. expand window by including nums[r]
    
    while window_invalid:
        # shrink window from left
        l+=1
        
    # 3. updatde answer using current window
    
    
#%% 1.Max sum subarray of size K
# Given array nums and integer K, find the maximum sum of any contiguous
# subarray of length K
# find the maximum sum of K consecutive elements
import math
# 1. maintain sum of current k elements
# 2. when moving r forward by 1, add nums[r]
# and subtract nums[r-k] (the element leaving the window)
# 3. update best once you have a full window

#           |full window  if k=2
# r      0 1 2 3 4
# k      1 2 2 2 2
# n      1 2 3 4 5
# full window: when r>=k-1

foo = "this is where practice starts"

"""
1. init max su  at neg inf
2. init current window sum at 0
3. fixed window: no need to track l
4. add each r element to sum
5. if we've passed  element k-1, window is full: update best and remove previous element """

def max_sum_sub_k(nums,k):
    if k==0 or k>len(nums):
        return None
        
    wsum=0
    best = -math.inf
    
    for r in range(len(nums)):
        wsum+=nums[r]
        
        if r>=k-1:
            best=max(best,wsum)
            wsum-=nums[r-1]
            
    return best





#       0 1 2 3 4
nums = [1,2,3,4,5]; k=2 # 9
nums = [-1,-2,-3]; k=2  # -3
nums=[5]; k=1 # 5

max_sum_sub_k(nums, k)

#%% 2. Longest substring without repeating characters 
# Given string s, find length of longest substring that has 
# no repeated chars. 

# 1. expand r adding characters to frequency map
# 2. if adding s[r] makes window invalid (repeated char count>1),
# move l forward removing characters until the window is valid again. 
# 3. at each valid state, update best 


def longest_sub_unique_char(s):
    n = len(s)
    freq={}  # or collections.Counter / dict of char->count/last index
    l=0
    best=0
    
    for r,ch in enumerate(s):
        #                  key, default
        freq[ch] = freq.get(ch, 0) + 1
        
        # shrink while invalid
        while freq[ch] >1:
            left_ch = s[l]
            freq[left_ch] -=1
            
            if freq[left_ch]==0:
                del freq[left_ch]
                
            l += 1
            
        
        best = max(best, r-l+1)
        
    return best
        




#  01234567
s="abcabcbb" # 3 ( "abc" )
s="bbbbb" # 1 ( "b" )
s="pwwkew" # 3 

longest_sub_unique_char(s)
        
#%% Instead of counts,
# store the last index of each char and jump 
# l directly to last_index+1 when a repeat is seen

# When you see a character ch at index r:
# If you’ve seen ch before at index j
# And j >= l (meaning it's inside the current window)
# Then you must move l to j + 1

# for each ch:
# 1. check if it's seen before, and seen within the current window
# 2. if seen within the current window, move window 1 step forward from this position
# 3. update last seen position for current ch
# 4. update best

def longest_sub_unique_char(s):
    n = len(s)
    last_seen={}  # or collections.Counter / dict of char->count/last index
    l=0
    best=0
    
    for r,ch in enumerate(s):
        if ch in last_seen and last_seen[ch]>= l:
            l = last_seen[ch]+1
            
        last_seen[ch] = r
        best = max(best, r-l+1)
        
    return best


s="abcabcbb" # 3 ( "abc" )
s="bbbbb" # 1 ( "b" )
s="pwwkew" # 3 
#  012345
# s="abba" # 2 

longest_sub_unique_char(s)

#%% 3. Longest repeating character replacement
# Given string s and integer k, return len of longest
# substring you can get by replacing k characters
# so that all characters in the substring are the same.

# 1. maintain counts of chars in window
# 2. track freq of most common char in window
# 3. window is valid if window size - max freq <= k
# i.e. replacements needed <= k
# 4. Expand r, shrink l until valid. 

# 1. for each char:
# - update count
# - update max freq if count of char is better (it's the only one that was updated in this iteration, so you only need to compare current)
# - string length  - max_freq  = num chars you need to replace
# - while replacements needed > k, shrink
# - decrease count for every char leaving the window

def char_replacement(s, k):
    counts = {}
    max_freq = 0
    best = 0
    l=0
    
    for r, ch in enumerate(s):
        counts[ch] = counts.get(ch,0) + 1
        max_freq = max(max_freq, counts[ch]) # set max freq if count of char is better
        
        while (r - l + 1) - max_freq > k:
            counts[s[l]] -= 1
            l += 1
        
        best = max(best, (r-l+1))
        
    return best


def char_replacement(s,k):
    cnt = {}
    maxfreq = 0
    mfchar = ''
    l=0
    best = 0
    
    for r,ch in enumerate(s):
        cnt[ch] = cnt.get(ch,0)+1
        
        if maxfreq<cnt[ch]:
            mfchar=ch
            print(f"MAX CHAR: {mfchar}:{cnt[ch]}")
        elif maxfreq>=cnt[ch]:
            print(f"MAX CHAR: {mfchar}:{maxfreq}")
        
        
        maxfreq = max(maxfreq,cnt[ch])
        # if this window is valid, this maxfreq will be used to 
        # calculate best. 
        # in fact, why is this also fine? 
        
        # str_len = r-l
        # replacements_needed = (r-l+1) - maxfreq
        
        while (r - l + 1) - maxfreq > k:
            cnt[s[l]]-=1
            if cnt[s[l]]<0:
                del(cnt[s[l]])
            l+=1
            # why is it not possible for maxfreq to be wrongly bigger
            # if we are not updating it here???
            
        best = max(best, (r-l+1)) # this is a valid window
        
    return best
            
    
# why is it not possible for maxfreq to be wrongly bigger?
# At some point max_freq = 3 for "AABAB".
# Later, after shrinking, the current window may no longer actually contain 3 of the same char.
# But keeping max_freq = 3 is still fine, because the algorithm only needs it as a conservative guide for window size.

# TODO !!!!
# STILL DON'Ŧ UNDERSTAND WHY THIS WORKS
# WHY IS MAXFREQ NOT UPDATING NOT A PROBLEM?

# let k=2 
#    0 1 2 3 4 5 6 7 
# s="a b c a b c b b" 
# s="a b c b b b b b" 

#    0 1 2 3 4 5 6 7 
#      1     4        r-l+1 = 4
# s="a b c a b c b b" 
# s="a b b b b c b b" 
#      -------

#    0 1 2 3 4 5 6 7 
#          3       7   r-l+1 = 5
# s="a b c a b c b b" 
# s="a b c b b b b b" 
#          ---------

#    0 1 2 3 4 5 6 7 
#      1       5       r-l+1 = 5, max_freq=2, 5-2=3, 3>k
#        2     5       r-l+1 = 4, max_freq=2, 4-2=2, 2!>k
#        2       6     r-l+1 = 5, max_freq=2, 5-2=3, 3>k
#          3     6     r-l+1 = 4, max_freq=2, 4-2=2, 2!>k
#          3       7   r-l+1 = 5, max_freq=3, 5-3=2, 2!>k
# s="a b c a b c b b" 

s="AABABBA"; k=1 # 4 (change one char to get "AABA" or "BABB")
# s="AAAA"; k=2 # 4
# s="ABAB"; k=2 # 4
# s="ABCD"; k=1 # 2
s="abcabcbbef"; k=2

char_replacement(s, k)

#%% 4. Minimum size subarray sum
# Given array nums and integer target, 
# return minimal length of cont subarray whose sum >=target

# 1. expand r, accumulate window sum
# 2. while window sum>=target, update best
# and shrink from l subtracting nums[l]
# only works when numbers are non-negative. 
# Reason: when you shrink the left pointer l,
# the window sum monotonically decreases 
# (removing a non-negative element reduces sum). 
# That monotonicity guarantees once window_sum < target
# you can safely expand again and never miss a minimal window.
# If elements can be negative, removing nums[l] 
# can increase the window sum (because you might be removing a negative),
# so the expand/shrink logic no longer guarantees correctness. 
# In that case you must use other techniques (prefix sums + binary search, or prefix sums + a monotonic deque) to find the minimal length in O(n log n) or O(n).

def min_subarray_len(nums, target):
    n = len(nums)
    l=0
    wsum=0
    best = math.inf
    
    for r in range(len(nums)):
        wsum+=nums[r]
        
        while wsum>=target:
            best = min(best, (r-l+1))
            wsum -= nums[l]
            l+=1
          
    if best==math.inf:
        return 0
    else:
        return best
            


            

nums=[2,3,1,2,4,3]; target=7 # 2 (subarray [4,3])
nums=[1,1,1,1]; target=5 # 0 (none)
nums=[5]; target=5 # 1
nums=[2,1,6,5,4]; target=9 # 2 ( [6,5] )

min_subarray_len(nums, target)



#%% 5. Subarray product less than K
# given array nums of positive integers and integer k, 
# return number of cont subarrays where product of 
# all elements is < k

# 1. init prod, count and l (not fixed window) 
# 2. expand r, update prod by multiplying nums[r] 
# 3. while prod>=k (target), and l/r indices do not cross,
# - shrink prod by dividing with value leaving window (nums[l])
# - and increment l 
# 4. Once a valid window is reached, all subarrays ending at r with starts
# in [l..r] are valid 
# i.e. every contiguous subarray that ends at r 
# and starts at any index i with l ≤ i ≤ r 
# will have product < k

def num_subarray_product(nums, k):
    prod = 1
    l = 0
    count = 0
    
    for r, val in enumerate(nums):
        prod *= val
        
        while prod >= k and l<=r:
            prod = prod//nums[l]
            l += 1
        
        count += (r-l+1)
        
    return count


nums = [1,3,6,2,4,1,3,5,2]
k = 10

# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# [1, 3, 6, 2, 4, 1, 3, 5, 2]
#  1  3  18                     r-l+1=3
#     3  18                     r-l+1=2
#        6                      r-l+1=1
#        6 12
#           2
#           2  8  8  24 
#              4  4  12 
#                 1  3 
#                 1  3  15
#                    3  15
#                        5
#                        5 10
# [ ,  ,  , 2, 4, 1,  ,  ,  ]
# [ ,  ,  , 2, 4, 1,  ,  ,  ]
# [0, 1, 2, 3, 4, 5, 6, 7, 8]


nums=[10,5,2,6]; k=100 # 8
# nums=[1,2,3]; k=0 # 0 (anything ≤1 or k ≤1 boundary)
# nums=[1,1,1]; k=2 # 6 (all subarrays)
# nums=[3,2,5]; k=5 # 3 ( [3], [2], [5] )
# nums=[3,2,5]; k=10 # 


# nums=[10,5,2,6]; k=100
# nums=[10,5,2,6,10]; k=100
#    [10]
#    [10,5]
#    [   5]
#    [   5,2  ]
#    [     2  ]
#    [   5,2,6]
#    [     2,6]
#    [       6]

#      0 1 2 3 4  5  6  7 8 9 10
# nums=[10,5,2,6,10,10,10,2,4,2,5]; k=100
#    [10,5,2                   ] 6
#    [   5,2,6                 ] 8
#    [       6,10              ] 10  
#    [               10,2,4    ] 1+2+3=6 # lr: 66,76,86
#    [                  2,4,2,5] 3+4=7 lr: 97, 10-7    [2,4] [2,4,2], [4,2], [2], [4,2,5], [2,5], [5], [2,4,2,5]
# r-l+1
# 

# nums=[10,2,4,2,5]; k=100
# nums=[10,5,2,6,10,104,104,104,10,2,4,2,5]; k=100

num_subarray_product(nums, k)

#%% 6. At most K distinct characters
# given string s and integer k, return len of the
# longest substring with at most k distinct characters.

# 1. init counts and l (not fixed window).  
# 2. expand window by increasing r, increment count for each new char
# - Num distinct chars: distinct=len(counts) 
# 4. while distinct>k, 
# - decrement counts[s[l]]
# - delete chars with zero counts from dict (they contribute to len)
# - increment l
# 4. update best when valid

def longest_k_distinct(s, k):
    if k==0:
        return 0
    
    counts = {}
    l = 0
    best = 0
    
    for r,ch in enumerate(s):
        counts[ch] = counts.get(ch,0) + 1
        
        while len(counts) > k:
            counts[s[l]] -= 1
            if counts[s[l]]==0:
                del counts[s[l]]
            l += 1
        
        best = max(best, r-l+1)
        
    return best


s = "aacvalbcbvvnxablsgeoph"
s = "aacvalbcbvvv"
#   "     lbcbvvv"
#   "  cvalb    "
k=1 # length 3, substring "vvv"
k=2 # length 4, substring "bvvv"
k=3 # length 6, substring "bcbvvv"
k=4 # length 7, substring "lbcbvvv"
        
longest_k_distinct(s, k)
        