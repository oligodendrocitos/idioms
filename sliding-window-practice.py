#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 2. Sliding window
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
Instead of trying every possible subarray  O(n^2):
- move r forward to grow it
- move l forward to shrink it when needed
Each index enters once and leaves once, so the whole thing is O(n).

@author: qq20468

# Core template:
# TYPE A — Fixed-size window (k=3)
nums=[1,2,3,4]
l=0
window_invalid=True

for r in range(len(nums)):
    #1. expand window by including nums[r]
    
    while window_invalid:
        # shrink window from left
        l+=1
        
    # 3. updatde answer using current window
    

# Type B — Variable Size, longest valid window, At Most K 
shrink while INVALID, then update
l = 0
k = 3
n = len(nums)
count = {}

for r in range(n):
    add s[r]

    while window invalid:
        remove s[l]
        l += 1

    best = max(best, r-l+1) # update_answer



# Type C — Variable Size, Shortest Valid Window (Harder)
l=0
for r in range(n):
    # expand
    add s[r]

    while window_valid:
        best = min(best, r-l+1) # update_answer
        remove s[l];            # shrink
        l += 1

"""

#%% =============== 1. Max sum subarray of size k ===========================
# ============================================================================
# Given array nums and integer K, find the maximum sum
# of any contiguous subarray of length K.
# find the maximum sum of K consecutive elements

# 1. maintain sum of current k elements
# 2. when moving r forward by 1, add nums[r]
# and subtract nums[r-k] (the element leaving the window)
# 3. update best once you have a full window

#           |full window  if k=2
# r      0 1 2 3 4
# k      1 2 2 2 2
# n      1 2 3 4 5
# full window: when r>=k-1

# 1. init max su  at neg inf
# 2. init current window sum at 0
# 3. fixed window: no need to track l
# 4. add each r element to sum
# 5. if we've passed  element k-1, window is full: update best and remove previous element

import math

def max_sum_sub_k(nums,k):
    s=0
    best=-math.inf
    full_win = k-1

    if k>len(nums) or k==0:
        return None
    
    for r in range(len(nums)):
        s+=nums[r]
        
        if r>=full_win: # check for full window
            best = max(s,best)
            s-=nums[r-(k-1)] # remove leftmost item
            
    print(best)
    return best
            
            
max_sum_sub_k([1,2,3,4,5], 2)==9  # 9
max_sum_sub_k([5,4,3,1,5], 2)==9  # 9
max_sum_sub_k([-1,-2,-3],  2)==-3 # -3
max_sum_sub_k([5], 1)==5          # 5

#%% ====== 2. Longest substring without repeating characters ===============
# ============================================================================
# Given string s, return length of longest substring
# with no repeated chars.  

# 1. expand r adding characters to frequency map
# 2. if adding s[r] makes window invalid (repeated char count>1),
# move l forward removing characters until the window is valid again. 
# 3. at each valid state, update best 

# how do you know it's invalid? : freq[ch] > 1 
# why does this work? because a) previous ch should all be <1 since we keep moving 
# the window until this is true. 

def longest_sub_unique_char(s):
    n = len(s)
    freq={}  # or collections.Counter / dict of char->count/last index
    l=0
    best=0
    
    for r,ch in enumerate(s):
        #                  key, default
        freq[ch] = freq.get(ch, 0) + 1
        print(f"add   : {freq}")
        
        # shrink while invalid
        while freq[ch] >1:
            left_ch = s[l]
            freq[left_ch] -=1
            
            if freq[left_ch]==0:
                del freq[left_ch]
            print(f"remove: {freq}")

            l += 1
            
        
        best = max(best, r-l+1)
        
    return best





#  01234567
# s="abcabcbb" # 3 ( "abc" )

longest_sub_unique_char("abcabcbb")==3 # 3 ( "abc" )
longest_sub_unique_char("bbbbb")==1    # 1 ( "b" )
longest_sub_unique_char("pwwkew")==3   # 3 wke
longest_sub_unique_char("abba")==2     # 2 ab
#%% ---------- 2b. Same problem, jump l with last-seen index -----------------
# --- Idea: ---
# Store the last index of each char. 
# When you see a character ch at index r, 
# if it was seen INSIDE the window (last[ch] >= l),
# jump l straight to last[ch]+1 instead of stepping.
# update last seen position for current ch, and update best.
# The '>= l' check matters: an old index outside the window must not move l
# backwards.
# --- Example: --- "abba"
# r=2 'b'  last[b]=1 >= l=0  -> l=2     window "b"
# r=3 'a'  last[a]=0 <  l=2  -> ignore  window "ba", best 2
#          (without the check, l would go BACK to 1: window "bba", wrong)
# --- Complexity: --- O(n) time, O(alphabet) space


# for each ch:
# 1. check if it's seen before, and seen within the current window
# 2. if seen within the current window, move window 1 step forward from that position
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
            print(f"{ch} in window")
            print(f"move l   : {last_seen[ch]}")
            
        last_seen[ch] = r
        print(f"update   : {last_seen}")
        best = max(best, r-l+1)
        
    return best



longest_sub_unique_char("abcabcbb")==3 # 3 ( "abc" )
longest_sub_unique_char("bbbbb")==1    # 1 ( "b" )
longest_sub_unique_char("pwwkew")==3   # 3 wke
longest_sub_unique_char("abba")==2     # 2 ab
#%% ========= 3. Longest repeating character replacement ====================
# ============================================================================
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

# --- Why is it fine that max_freq is never decreased? ---
# When chars leave on the left, max_freq can become too big (stale), so the
# current window may really be invalid. That never gives a wrong answer:
# 1. The window never gets smaller. Each step adds 1 on the right and the
#    while removes at most 1 on the left (you could write `if`). So the
#    window's size is always the best length found so far.
# 2. The window only GROWS when max_freq grows, and max_freq only grows
#    when ch really has that many copies inside the current window. At that
#    moment the window is truly valid, so the new best is real.
# So a stale max_freq only lets an invalid window slide along at the OLD
# best length. It can never create a new best. To beat best you need a
# window with more copies of one char than ever before, which is exactly
# when max_freq goes up.

# --- Example: --- s="AABCBB", k=1
#          window  max_freq  real max  best
# r=0 A    A         1         1        1
# r=1 A    AA        2         2        2
# r=2 B    AAB       2         2        3    (replace B)
# r=3 C    ABC       2         1        3    4-2>1 -> drop A. ABC needs 2
#                                            replacements: INVALID, but its
#                                            size is 3 = best, so no harm
# r=4 B    BCB       2         2        3    drop A, valid again
# r=5 B    BCBB      3         3        4    max_freq grows -> real new best


# --- Complexity: --- O(n) time, O(alphabet) space

def char_replacement(s, k):
    counts = {}
    max_freq = 0
    best = 0
    l=0
    
    for r, ch in enumerate(s):
        counts[ch] = counts.get(ch,0) + 1
        max_freq = max(max_freq, counts[ch]) # set max freq if count of char is better
        
        # str_len = r-l+1
        # need_to_replace = str_len - max_freq
        # if need_to_replace > k, shrink
        while (r-l+1)-max_freq>k:
            counts[s[l]] -= 1
            # str_len = r-l+1
            # need_to_replace = str_len - max_freq    
            l += 1
            # decrease count for every char leaving the window
        
        best = max(best, (r-l+1))
        
    return best


          
char_replacement("AABABBA",    k=1) # 4  (change one char to get "AABA" or "BABB")
char_replacement("AAAA",       k=2) # 4
char_replacement("ABAB",       k=2) # 4
char_replacement("ABCD",       k=1) # 2
char_replacement("abcabcbbef", k=2) # 5


#%% =============== 4. Minimum size subarray sum ============================
# ============================================================================
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
            


min_subarray_len([2,3,1,2,4,3], 7) # 2 (subarray [4,3])
min_subarray_len([1,1,1,1], 5)     # 0 (none)
min_subarray_len([5], 5)           # 1
min_subarray_len([2,1,6,5,4], 9)   # 2 ( [6,5] )



#%% 5. Subarray product less than K
# ============================================================================
# given array nums of positive integers and integer k, 
# return number of cont subarrays where product of 
# all elements is < k
# a product and sum is well defined for a single number. 

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

# --- Example: ---
#          [10,5,2,6], k=100
# r=0      [10]          10           +1   [10]
# r=1      [10,5]        50           +2   [5] [10,5]
# r=2      [10,5,2]     100 -> drop 10
#             [5,2]      10           +2   [2] [5,2]
# r=3         [5,2,6]    60           +3   [6] [2,6] [5,2,6]
#                               total: 8
# --- Complexity: --- O(n) time, O(1) space

def num_subarray_product(nums, k):
    prod = 1
    l = 0
    count = 0
    
    for r, val in enumerate(nums):
        prod *= val
        
        while prod >= k and l<=r:
            prod /= nums[l]
            l += 1
        
        count += (r-l+1)
        
    return count
 

nums = [1,3,6,2,4,1,3,5,2]
k = 10

num_subarray_product([1,3,6,2,4,1,3,5,2], 10)
num_subarray_product([10,5,2,6],  k=100)==8  # 8
num_subarray_product([10,5,2,6,10], k=100)==8  # 10
num_subarray_product([10,2,4,2,5], k=100)==8  # 13
num_subarray_product([1,2,3], k=0 )==0  # (anything ≤1 or k ≤1 boundary)
num_subarray_product([1,1,1], k=2 )==6  # 6 (all subarrays)
num_subarray_product([3,2,5], k=5 )==3  # 2 ( [3], [2], [5] 
num_subarray_product([3,2,5], k=10)==4  # 

nums=[10,5,2,6,10,10,10,2,4,2,5]; k=100
num_subarray_product(nums,k)
# nums=[10,5,2,6,10,104,104,104,10,2,4,2,5]; k=100

num_subarray_product(nums, k)

#%% ============ 6. Longest substring with at most k distinct ===============
# ============================================================================
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

# --- Complexity: --- O(n) time, O(k) space

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


longest_k_distinct("aacvalbcbvvv", k=1) # length 3, substring "vvv"
longest_k_distinct("aacvalbcbvvv", k=2) # length 4, substring "bvvv"
longest_k_distinct("aacvalbcbvvv", k=3) # length 6, substring "bcbvvv"
longest_k_distinct("aacvalbcbvvv", k=4) # length 7, substring "lbcbvvv"
longest_k_distinct("eceba", 2) == 3      
longest_k_distinct("abc", 0) == 0

        

#%% 7. Minimum window substring
# ============================================================================
# Given string s and t, find the shortest contiguous substring of s 
# that contains all characters of t. # return "" if no window exists. 

# 1. init counts or count of chars still needed
# 2. expand window right (move r) until all chars seen. 
# 3. While all characters present:
# - update best substring length
# - remove char leaving the window
# - move l forward
# To use a single variable or dict,
# simply go negative (= surplus). missing = total chars still needed,
# counting duplicates; the window is valid when missing == 0.

# The all(...) check runs over t’s distinct letters at every step, so it’s O(n·m) rather than O(n).

from collections import Counter

s="ADOBECODEBANC"; t="ABC" # "BANC"

def shortestsubstring(s,t):
    need = Counter(t)
    l=0
    minlen = math.inf
    minstr = ""
    
    for r,ch in enumerate(s):
        # if ch in need, decrease count
        # print(f"{s[:r]}[{s[r]}]{s[(r+1):]}")
        if ch in t:
            need[ch] -= 1
        print(f"{s[:r]}[{s[r]}]{s[(r+1):]} || {[k+':'+ str(v) for k,v in zip(need.keys(),need.values())]}")
        

        while all(v <= 0 for v in need.values()) and l<=r:
            print(f"got: {s[l:r+1]} || currlen: {r}-{l}+1 | {r-l+1}")
            curr_len = r-l+1
            # print(f"currlen: {r}-{l}+1 | {r-l+1}")
            if curr_len<minlen:
                print(f"new best: {s[l:r+1]}")
                # print(f"new best: {r} {l} | {r-l+1}")
                minlen = curr_len
                minstr = s[l:r+1]
                
            if s[l] in t:
                need[s[l]]+=1
                print(f"{s[l+1:r+1]} || {[k+':'+ str(v) for k,v in zip(need.keys(),need.values())]}")
            l+=1
        
    return minstr
            

shortestsubstring("ADOBEAD",  t="AB") # "BEA"
shortestsubstring("ADOBECODEBANC",  t="ABC") # "BANC"
shortestsubstring("ADOBECODEBANNC", t="ABC") # BANNC
shortestsubstring("a",  t="aa")  # "" (not enough a's)
shortestsubstring("a",  t="a") # "a" 
shortestsubstring("ab", t="b") # "b"
shortestsubstring("acbbaca", t="aba") # "baca"
shortestsubstring("acbbaca", t="baca")
shortestsubstring("acbbaca", t="")
        

#%% ====== Two-Dict version ==================================================
# --- Idea: ---
# Template C. need = Counter(t). have = counts of needed chars in the window.
# formed = how many DISTINCT chars have have[ch] >= need[ch].
# Window is valid when formed == len(need). Only change formed at the exact
# moment a count crosses its need, in either direction.
# --- Algorithm: ---
# 1. need = Counter(t), have = {}, formed = 0, l = 0
# 2. for r, ch:
#      if ch in need: have[ch] += 1; if have[ch] == need[ch]: formed += 1
#      while formed == len(need):
#          record s[l:r+1] if shorter
#          left = s[l]
#          if left in need: have[left] -= 1; if have[left] < need[left]: formed -= 1
#          l += 1
# 3. return best substring
# --- Example: --- s="acbbaca", t="aba"   need {a:2, b:1}
#          a c b b a c a
# r=4     [a c b b a]        a=2 b=2 valid -> "acbba" (5)
#                            drop a -> a=1 < 2, invalid
# r=6       [c b b a c a]    a=2 valid (6, not better)
#                            drop c -> [b b a c a] (5)
#                            drop b -> [b a c a]   (4) best "baca"
#                            drop b -> b=0 < 1, invalid
# answer "baca"
# --- Complexity: --- O(|s| + |t|) time, O(|t|) space

def min_window(s, t):
    if not s or not t:
        return ""
    need = Counter(t)
    have = {}
    required = len(need)
    formed = 0
    l = 0
    best = math.inf
    bestsub = ""
    for r, ch in enumerate(s):
        if ch in need:
            have[ch] = have.get(ch, 0) + 1
            if have[ch] == need[ch]:
                formed += 1
        while formed == required:
            if r - l + 1 < best:
                best = r - l + 1
                bestsub = s[l:r+1]
            left = s[l]
            if left in need:
                have[left] -= 1
                if have[left] < need[left]:
                    formed -= 1
            l += 1
    return bestsub


min_window("ADOBEAD",  t="AB") # "BEA"
min_window("ADOBECODEBANC",  t="ABC") # "BANC"
min_window("ADOBECODEBANNC", t="ABC") # BANNC
min_window("a",  t="aa")  # "" (not enough a's)
min_window("a",  t="a") # "a" 
min_window("ab", t="b") # "b"
min_window("acbbaca", t="aba") # "baca"
min_window("acbbaca", t="baca")
    