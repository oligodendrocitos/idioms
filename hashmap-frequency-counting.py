""" hashmap / frequency counting
Intuition:
    Instead of scanning the array repeatedly, 
    store information as you go. 
    
    Check for 'has this information already been stored?'
    

When to use:
    - you need O(1) lookup 
    - You're counting occurrences
    - You're checking if something 'has appeared before''
    - You're matching complements (e.g., target - x)
    - You need frequency comparison (anagrams, duplicates)
    - Nested loops would otherwise be O(n^2)

keywords:
    'find pairs'
    'count occurences'
    'group by'
    'check if exists'


 """
#%% 1. frequency counting
"""
- anagrams
- duplicates
- most frequent element
- char counting
"""

arr = [1,2,3]
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1


# alt
from collections import Counter
freq = Counter(arr)


#%% 2. Two Sum/ Complement lookup
"""
- need pair summing to target
- check if complement exists
"""
nums = [1,2,3]
target = 2

seen = {}

for i, x in enumerate(nums):
    complement = target - x
    if complement in seen:
        # return [seen[complement], i]
        print( [seen[complement], i])
    seen[x] = i


#%% 3. Prefix Sum + Hashmap
"""
- subarray sum equals k
"""

prefix = 0
count = 0
freq = {0: 1}

k = 2

for x in nums:
    prefix += x
    if prefix - k in freq:
        count += freq[prefix - k]
    freq[prefix] = freq.get(prefix, 0) + 1

#%% 4. Grouping
"""
- group anagrams
"""
groups = {}

words = ['foo','bar','bat','baz','bab','rar']

for word in words:
    key=tuple(sorted(word))
    groups.setdefault(key,[]).append(word)
    
    
# return list(groups.values())
print( list(groups.values()))
