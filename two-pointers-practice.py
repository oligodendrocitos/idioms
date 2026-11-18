""" 1. two pointers  
- - - - - - - - - - - - - - - - - - - -
1. When Should You Think Two Pointers?

- Array is sorted
- You’re looking for pairs
- You need to merge
- You’re removing duplicates
- You’re shrinking from both ends
- Brute force would be nested loops

If you catch yourself thinking:
"I need to compare elements relative to each other in a sorted structure"
That's two pointers.


- - - - - - - - - - - - - - - - - - - -
2. The 4 Main Two-Pointer Variants


Variant A — Opposite Ends (Converging)

    Used when:
     - Sorted array
     - Looking for pair relationships
     - Maximization/minimization problems
    
    Examples:
     - Two Sum II (sorted)
     - Container With Most Water
     - 3Sum (inner loop)
     - Valid palindrome
    
    Mental template:
    l, r = 0, len(arr) - 1
    while l < r:
        if condition:
            l += 1
        else:
            r -= 1
    
    You adjust:
     - the condition
     - what happens inside
    
    
    
Variant B — Same Direction (Slow / Fast)
    
    Used for:
     - Removing elements in-place
     - Deduplicating sorted array
     - Partitioning
    
    Examples:
     - Remove duplicates from sorted array
     - Move zeros
     - Partition array
     
    Mental template:
    slow = 0
    for fast in range(len(arr)):
        if keep(arr[fast]):
            arr[slow] = arr[fast]
            slow += 1
    
    This pattern avoids extra space.



Variant C — Merge From End
    
    Used when:
        - You need to merge in-place
        - One array has buffer at the end
    
    Example:
     - Merge Sorted Array
    
    Mental template:
    i, j, k = m-1, n-1, m+n-1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    Then handle leftovers.
    
    This is just a specialized opposite-ends case.



- - - - - - - - - - - - - - - - - - - -
Think of slow as:

"the length of the valid prefix"

So:

    [ VALID PART | GARBAGE ]

We are building:

    [1,1,2,2,3 | ...]

Everything after slow doesn't matter.


Or:
    [ valid region | unknown region ]

Where:
    slow = boundary
    fast = scanner

"""




############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
#%% 1. reverse array =========================================================
# ============================================================================
# given array, reverse it in place
# [1,2,3,4] -> [4,3,2,1]
# --- Algorithm: ---
# Left starts at beginning
# Right starts at end
# Swap
# Move inward
# Stop when they cross.


arr = [2,5,7,9,12]
arr = [0,2,2,7,9,12]
arr = []
arr = [0]
arr = [0, 1]

def reverse_array(arr):
    l=0
    r=len(arr)-1
    
    if len(arr)<2:
        return arr
    
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
        
    return arr
        

reverse_array(arr)
reverse_array([2,5,7,9]) == [9,7,5,2]
reverse_array([2,5,7]) == [7, 5, 2]
reverse_array([])
reverse_array([0])
reverse_array([0,1]) == [1,0]
        
#%% 1.5. reverse array without simultaneous assignment
arr=[1,2,3,4,5]

def reverse(arr):
    ...
        

reverse(arr)
reverse_array([2,5,7,9]) == [9,7,5,2]
reverse_array([2,5,7]) == [7, 5, 2]
reverse_array([])
reverse_array([0])
reverse_array([0,1]) == [1,0]

#%% 2. valid palindrome =============================
# ============================================================================
# given string, return True if it reads the same way forward and backward
# "racecar" -> True
# "hello" -> False
# middle letter doesn't matter if odd, doesn't exist if even. 
# --- Algorithm: ---
# Compare left and right
# If mismatch -> False
# Move inward
# If finish -> True

s = "racecar"
# s = "hello!"
# s = "aaaaa"

def is_palindrome(s):
    l=0
    r=len(s)-1
    
    if len(s)<2:
        return True
    
    
    while l<r:
        if s[l]!=s[r]:
            return False
        
        l+=1
        r-=1
        
    return True
    
    



is_palindrome(s)
is_palindrome("racecar") == True  
is_palindrome("hello!")  == False # False 
is_palindrome("abba")    == True  # True
is_palindrome("aba")     == True  # True
is_palindrome("ab")      == False # False 
is_palindrome("a")       == True  # True
is_palindrome("")        == True  # True


#%% 3. Two Sum II ==============================
# ============================================================================
# given sorted array and target, return indices of two numbers 
# that add up to target. 
# nums = [2,7,11,15]
# target = 9
# output: [1,2]
# --- Algorithm: ---
# If sum too small -> move left up
# If sum too big -> move right down

nums = [2,7,11,15]
nums = [2,4,7,11,15]
target = 199 # none
target = 13 # 0,3
target = 18 # 2,3

def two_sum(nums,target):
    l=0
    r=len(nums)-1
    
    
    while l<r:
        s = nums[l]+nums[r]
        
        if s==target:
            return (l,r)
        
        elif s<target:
            l+=1
        else:
            r-=1
            
    
    return None
    
           



foo = two_sum(nums, target)
print(foo)

two_sum([2,4,7,11,15], 199)  # None
two_sum([2,4,7,11,15], 13)   # 0,3
two_sum([2,4,7,11,15], 18)   # 2,3
two_sum([2,7,11,15], 13)     # 0,2
two_sum([2,7,11,15], 18)     # 1,2
            
#%% 4. remove duplicates (sorted array) =====================
# ============================================================================
# remove duplicates in place from sorted array
# return number of unique elements
# [1,1,2,2,3] -> [1,2,3,...]
# --- Idea: ---
# slow = points to the last unique element position
# fast = scans ahead
# When new value appears -> increase & write it at slow
# --- Algorithm: ---
# 1. loop through indices starting from 1
# 2. compare numbers
# - if number @ fast is the same as number @ slow, nothing happens (fast increases by 1)
# - if numbers are different, slow increases by 1, and the new value gets written

# 0 1 2 3 4    
# 3 3 9 7 1    s=0, f=1
# 3 3 9 7 1 -> s=0, f=2
# _   _
# 3 3 9 7 1    s!=f, increase s, put 9@s
# 3 9 9 7 1 -> s=1, f=3
#   _   _
# 3 9 9 7 1    s!=f
# 3 9 7 7 1 -> s=2, f=4
#     _   _   
# 3 9 7 7 1    s!=f
# 3 9 7 1 1 -> END


nums = [1,2,2,3,4,5,5,6]
#         0,1,2,3,4,5,6,7 
# nums = [1,2,2,3,4,5,5,6]
# 


def remove_dupes(nums):
    slow=0
    
    for fast in range(1,len(nums)):
        if nums[fast]!=nums[slow]:
            slow+=1
            nums[slow]=nums[fast]
            
    
    nuniq=slow+1
    return nuniq
    
            


remove_dupes(nums)
remove_dupes([1,2,2,3,4,5,5,6]) # 6
remove_dupes([3,3,9,7])         # 3
remove_dupes([3,9,9])           # 2
remove_dupes([3,3])             # 1
remove_dupes([1,2,2,3,4,5,5,6]) # 6
remove_dupes([1])               # 1

#%% 5. move zeros =============================
# ============================================================================
# move all zeros to end of array while maintaining relative order of non-zeros
# [0,1,0,3,12]-> [1,3,12,0,0]
# --- Idea: ---
# slow = next spot for a non-zero
# fast = scans every number
# After finishing, fill rest with zeros
# --- Algorithm: ---
# 1. loop through indices starting from 0
# 2. if fast points to a non-zero, place it at slow AND increase slow index
#   
# 0,1,2,3,4
# 0,1,0,3,12 f=[0] 
# 0,1,0,3,12 f=[1] move 1->[0] 
# 1,1,0,3,12 f=[2]
# 1,1,0,3,12 f=[3] move 3->[1]
# 1,3,0,3,12 f=[4] move 12->[2]
# 1,3,12,3,12 END

nums = [0,1,0,3,12]
nums = [0,1,0,0,3,12,1,0]
#      [0,1,2,3,4,5, 6,7]

def move_zeros(nums):
    slow=0
    
    for fast in range(len(nums)):
        if nums[fast]!=0:
            nums[slow]=nums[fast]
            slow+=1
            
    
    for i in range(slow,len(nums)):
        nums[i]=0
        
    return nums
        
            
move_zeros(nums)
move_zeros([0,1,0,3,12]) == [1,3,12,0,0]
move_zeros([1,1,0,3,12]) == [1,1,3,12,0]
move_zeros([0,0,3]) == [3,0,0]
move_zeros([0,1]) == [1,0]


#%% 6. remove all instances ============================
# ============================================================================
# remove all instances of val in-place
# return new length
# nums = [3,2,2,3], val = 3 -> [2,2]
# --- Idea: ---
# slow = next spot for a value we keep / slow points to last non-del val spot
# fast = scans forward to search for non-target values.
# --- Algorithm: ---
# 1. loop through all indices
# 2. if fast points to a value we want to keep:
#    - place value @ slow
#    - increase slow
#
# nums = [3,2,2,3], val = 3
#  _
# [3,2,2,3] fast=0 -> 3 == val, ignore
# [3,2,2,3]
#  _ _
# [3,2,2,3] fast=1 -> 2 != val, keep it
# [2,2,2,3] write nums[slow] = 2, slow=1
#    _ _
# [2,2,2,3] fast=2 -> 2 != val, keep it
# [2,2,2,3] write nums[slow] = 2, slow=2
#      _ _
# [2,2,2,3] fast=3 -> 3 == val, ignore
# [2,2,2,3]
#
# result:
# [2,2] new length = slow = 2



nums = [3,2,2,3]
val=3

def remove_all_instances(nums, val):
    slow=0
    
    for fast in range(len(nums)):
        if nums[fast]!=val:
            nums[slow]=nums[fast]
            slow+=1
            
    return slow


remove_all_instances(nums, val)
remove_all_instances([1,2,3,2,4,2], 2) # 3
remove_all_instances([1,2,1,2,1,2], 1) # 3
remove_all_instances([1,2,1,2,1,2], 2) # 3
remove_all_instances([1,2,1,2,1],   2) # 3


#%% 7. Remove all but 2 copies (sorted array) =============
# ============================================================================
# Remove duplicates in-place so that each unique element appears at most twice.
# Maintain the relative order of elements and return the new length.
# (ONLY works in sorted array)
# [1,1,1,2,2,3] -> [1,1,2,2,3]
# --- Idea: ---
# slow = next position where a valid element should be written
# fast = scans every element, starting from index 2
# rule:
# keep nums[fast] only if nums[fast] != nums[slow-2]
#
# Why this works:
# The first 2 elements are always allowed, so slow starts at 2.
# Everything before slow is already valid (at most 2 copies per value).
# If nums[fast] == nums[slow-2], then adding the current value
# would result in 3 copies of that value.
# If nums[fast] != nums[slow-2], the value can safely be added.
# This works because the array is sorted, so duplicates are consecutive.
#
# --- Algorithm: ---
# 1. if the array has 2 or fewer elements, return its length
# 2. initialize slow = 2 (first two elements are always kept)
# 3. loop through indices starting from fast = 2
# 4. if nums[fast] != nums[slow-2]:
#    - write nums[fast] at nums[slow]
#    - increase slow
# 5. otherwise, skip the element
# 6. return slow (number of valid elements)

# --- Example: ---
# nums = [1,1,1,2,2,3]
#      _
# [1,1,1,2,2,3] fast=2 -> 1 == nums[slow-2] (1), skip
# [1,1,1,2,2,3] slow=2
#      _ _
# [1,1,1,2,2,3] fast=3 -> 2 != nums[slow-2] (1), keep
# [1,1,2,2,2,3] write nums[slow] = 2, slow=3
#        _
# [1,1,2,2,2,3] fast=4 -> 2 == nums[slow-2] (1)? NO, keep
# [1,1,2,2,2,3] write nums[slow] = 2, slow=4
#          _ _
# [1,1,2,2,2,3] fast=5 -> 3 != nums[slow-2] (2), keep
# [1,1,2,2,3,3] write nums[slow] = 3, slow=5
#
# result:
# [1,1,2,2,3] new length = slow = 5

# --- Example: ---
#              [1, 1, 1, 2, 2, 3]        
#              s-2    sf            1==1  <0    -> f++
#              s-2    s  f          2!=1 -3  <0 -> f++
#                 s-2    s  f       2!=1  -2  <0 -> f++
#                             f     3!=2   <0  -> 

#  possible array starts: 
# [1,1,1] [0,1,1] [0,0,1] [0,1,2]
# in any of these cases, first two copies don'ŧ matter in relation to each other (!). 


# keep an element if fast-2
nums = [1,1,1,2,2,3]
# nums = [0,1,1,2,2,3]
# nums = [0,1,1,2,2,2,2,3]

    
def remove_duplicates_allow_2(nums):
    nums.sort()
    slow=2
    
    for fast in range(2,len(nums)):
        if nums[fast]!=nums[slow-2]:
            nums[slow]=nums[fast]
            slow+=1
            
    return nums[:slow]
            
            



remove_duplicates_allow_2(nums)
remove_duplicates_allow_2([0,1,1,2,2,3])
remove_duplicates_allow_2([0,1,1,2,2,2,2,3])
remove_duplicates_allow_2([1,1,1,2,2,2,2,3])
remove_duplicates_allow_2([0,0,1,2,2,2,2,3])


#%% 8. Move all negatives to the left (order preserved) =========
# ============================================================================
# Move all negative numbers to the beginning of the array.
# Preserve the relative order of negative and non-negative elements.
# [1,-1,3,-2,0] -> [-1,-2,1,3,0]
# --- Idea: ---
# Can't swap because that messes the relative order of non-negative elements. 
# In-place stable version : Insert each negative where it belongs
# and shift the block of positives right by one.
# --- Algorithm: ---
# 1. initialize slow = 0
# 2. Scan the array from left to right, keeping track of where the next
#    negative should go (slow).
# 3. When a negative is found:
#   - save the negative value temporarily
#   - shift all elements between slow and fast one position to the right 
#   - (start from the right!!!)
#   - insert the negative at slow
#   - increase slow
# 4. If fast finds a non-negative, skip it.
# 5. return nums
#
# --- Complexity: ---
# Time: O(n²) worst case - each negative may require shifting O(n) elements
# Space: O(1) - only a temporary variable and pointers are used

def move_negatives_left(nums):
    slow=0
    
    
    for fast in range(1, len(nums)):
        if nums[fast]<0:
            tmp=nums[fast]
            
            i=fast
            while i>slow:
                nums[i]=nums[i-1]
                i-=1
                
            nums[slow]=tmp
            slow+=1
            
    return nums
                
            
    
move_negatives_left( [1,-1,3,-2,0]) # [-1, -2, 1, 3, 0]
move_negatives_left( [-1,1,3,-2,0]) # [-2, -1, 1, 3, 0]
move_negatives_left( [0,2,3])       # 
move_negatives_left( [1,-3,2,0,-2]) # [-3, -2, 1, 2, 0]
    

#%% ==== Option 2: Use extra space ======
# --- Idea: ---
# Instead of shifting elements in-place, build two separate lists:
# one containing negatives and one containing non-negatives.
# Concatenate them and overwrite the original list.
# --- Algorithm: ---
# 1. Collect all negative elements in their original order.
# 2. Collect all non-negative elements in their original order.
# 3. Concatenate both lists and overwrite the original array.
# --- Complexity: ---
# Time: O(n) - each element is visited a constant number of times
# Space: O(n) - additional lists are created


def move_negatives_left_extra_space(nums):
    ...

move_negatives_left( [1,-1,3,-2,0])
move_negatives_left( [-1,1,3,-2,0])
move_negatives_left( [0,2,3])
move_negatives_left( [1,-3,2,0,-2])

#%% 9. Partition array by pivot (like quicksort step) ==============
# ============================================================================
# Move all elements smaller than pivot to the left side of the array.
# Elements >= pivot remain on the right.
#
# [3,2,1,5,6,4], pivot=3 -> [2,1,3,5,6,4]
#
# There are two approaches:
# A. Stable partition: preserve relative order within groups
# B. In-place partition: use swaps, relative order is not preserved
#
# === A. Stable partition ===
# --- Idea: ---
# You must keep the original relative order of elements.
# No pointers present. 
# Mental model:
#     first collect all < pivot
#     then all == pivot
#     then all > pivot
#
# Concatenate the groups and overwrite the original array.
# Since elements are collected in their original order, the partition is stable.
# This is much easier than trying to do it in-place while preserving order.
# --- Example: ---
# nums = [9,12,5,10,14,3,10], pivot=10
# [9,5,3]             collect elements < 10
# [10,10]             collect elements == 10
# [12,14]             collect elements > 10
#
# [9,5,3,10,10,12,14] concatenate all three groups
#
# --- Complexity: ---
# Time: O(n) - each element is visited a constant number of times
# Space: O(n) - additional lists are created


def partition_array(nums, pivot):
    ...
            
    

partition_array([3,2,1,5,6,4], 3)

#%% === B. In-place partition ===
# Sometimes the problem only asks you to partition, not preserve order.
# Then you can use two pointers.
# Move all elements < pivot to the left.
# Elements >= pivot remain on the right (not necessarily sorted).
#
# [3,2,1,5,6,4], pivot=3 -> [2,1,3,5,6,4]
#
# --- Idea: ---
# slow = next position for an element < pivot
# fast = scans every element
#
# When fast finds an element < pivot:
#   - swap it with nums[slow]
#   - increase slow
# Otherwise, skip it.
#
# This gradually builds two regions:
# [ < pivot | >= pivot ]
#
# --- Example: ---
# nums = [3,2,1,5,6,4], pivot=3
#  _
# [3,2,1,5,6,4] fast=0 -> 3 >= pivot, ignore
# [3,2,1,5,6,4]
#  _ _
# [3,2,1,5,6,4] fast=1 -> 2 < pivot, swap with slow(0)
# [2,3,1,5,6,4] swap(0,1), slow=1
#    _ _
# [2,3,1,5,6,4] fast=2 -> 1 < pivot, swap with slow(1)
# [2,1,3,5,6,4] swap(1,2), slow=2
#      _ _
# [2,1,3,5,6,4] fast=3 -> 5 >= pivot, ignore
# [2,1,3,5,6,4]
#      _   _
# [2,1,3,5,6,4] fast=4 -> 6 >= pivot, ignore
# [2,1,3,5,6,4]
#      _     _
# [2,1,3,5,6,4] fast=5 -> 4 >= pivot, ignore
# [2,1,3,5,6,4]
#
# result:
# [2,1,3,5,6,4]
#
# slow=2 marks the boundary between the two groups.
#
# --- Complexity: ---
# Time: O(n) - each element is visited once
# Space: O(1) - only two pointers are used


def partition_array_inplace(nums, pivot):
    slow=0
    
    for fast in range(len(nums)):
        if nums[fast]<pivot:
            nums[slow],nums[fast] = nums[fast],nums[slow]
            slow+=1
            
    return nums
            

partition_array_inplace([3,2,1,5,6,4], 3)
partition_array_inplace([3,2,1,5,6,4], 4)
partition_array_inplace([5,2,1,3,6,4], 4)
partition_array_inplace([5,2,4,3,6,1], 4)

#%% 10. Sort colors (Dutch National Flag) ===================
# ============================================================================
# Sort an array containing only 0s, 1s, and 2s, in-place.
# Group all 0s first, then 1s, then 2s.
# [2,0,2,1,1,0] -> [0,0,1,1,2,2]
# 
# Core idea:
# Use three pointers to maintain four regions:
#
# [ 0s | 1s | unprocessed | 2s ]
#       ^    ^           ^
#      low  mid         high
#
# low  = next position where a 0 should go
# mid  = current element being examined
# high = next position where 2 should go
#
# Or think about it as three regions:
#     left side: all 0s
#     middle: all 1s
#     right side: all 2s
# 
# 
# The logic:
# 1. Start with low and mid at the beginning, high at the end.
# At every step, nums[mid] is one of:
# Case 0
# If nums[mid] == 0:
#     swap it with nums[low]
#     move both low and mid forward
# Case 1
# If nums[mid] == 1:
#     just move mid forward
# Case 2
# If nums[mid] == 2:
#     swap it with nums[high]
#     move high backward
#     do not move mid yet, because the swapped-in value at mid still needs checking
# 4. Continue until mid passes high (no unprocessed elements remain).
#
# --- Example: ---
# nums = [2,0,2,1,1,0]
# low=0, mid=0, high=5
#  _         _
# [2,0,2,1,1,0] mid=0 -> 2, swap with high(5)
# [0,0,2,1,1,2] swap(0,5), high=4, mid stays at 0
#  _       _
# [0,0,2,1,1,2] mid=0 -> 0, swap with low(0)
# [0,0,2,1,1,2] swap(0,0), low=1, mid=1
#    _     _
# [0,0,2,1,1,2] mid=1 -> 0, swap with low(1)
# [0,0,2,1,1,2] swap(1,1), low=2, mid=2
#      _   _
# [0,0,2,1,1,2] mid=2 -> 2, swap with high(4)
# [0,0,1,1,2,2] swap(2,4), high=3, mid stays at 2
#      _ _
# [0,0,1,1,2,2] mid=2 -> 1, already in correct region
# [0,0,1,1,2,2] mid=3
#        _
# [0,0,1,1,2,2] mid=3 -> 1, already in correct region
# [0,0,1,1,2,2] mid=4
#
# mid=4 > high=3, stop
#
# result:
# [0,0,1,1,2,2]
#
# --- Why this works: ---
# At every step, the array is divided into four regions:
#
# [ 0s | 1s | unprocessed | 2s ]
#
# Everything before low is already 0.
# Everything between low and mid is already 1.
# Everything after high is already 2.
# Only the region between mid and high remains unprocessed.
#
# Each operation shrinks the unprocessed region until nothing remains.
#
# IMPORTANT:
# When swapping with high, do NOT advance mid.
# The element swapped in from high has not been examined yet.
#
# When swapping with low, advance BOTH low and mid.
# The element swapped in from low is either 1 or the same element,
# so it does not need to be examined again.
#
# --- Complexity: ---
# Time: O(n) - each step shrinks the unprocessed region
# Space: O(1) - only three pointers are used


def sort_colors(nums):
    lo=0
    mid=0
    hi=len(nums)-1
    
    while mid<hi:
        if nums[mid]==0:
            nums[lo],nums[mid]=nums[mid],nums[lo]
            mid+=1
            lo+=1
        elif nums[mid]==1:
            mid+=1
        
        else:
            # nums[mid]==2
            nums[mid]=nums[hi]
            nums[hi]=2
            hi-=1
            
    return nums
        
    

sort_colors([2,0,2,1,1,0])
sort_colors([1,0,2,1,2,0])


############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
#%% ====================== MEDIUM PROBLEMS ==================
# ===========================================================
# ===========================================================
# ===========================================================
#%% 1. Squares of a sorted array =========================
# ============================================================================
# given sorted array of ints, return new array of squares in sorted order
# Input: [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]
# --- Idea: ---
# l = leftmost unprocessed element
# r = rightmost unprocessed element
# k = next position to fill in the result (starting from the end)
#
# The largest squared value is at whichever end has the larger absolute value;
# use two pointers at the ends
# write the biggest squares into the result from the back to the front.
#
# --- Example: ---
# nums = [-4,-1,0,3,10];  res  = [0,0,0,0,0]
#  __        __
# [-4,-1,0,3,10] >> abs(-4) < abs(10) >> [0,0,0,0,100], k=3
#  __      _
# [-4,-1,0,3,10] >> [0,0,0,16,100], k=2
#     __   _
# [-4,-1,0,3,10] >> [0,0,9,16,100], k=1
#     __ _
# [-4,-1,0,3,10] >> [0,1,9,16,100] k=0
#        _
# [-4,-1,0,3,10] l=r=2, >> [0,1,9,16,100] k=-1
#
# result: [0,1,9,16,100]


from typing import List
import math

arr = []
arr = [-2, -1]
arr = [0,1,2]
arr = [-5, -3, -1]
arr = [-4, -1, 0, 3, 10]
arr = [-10, -4, -1, 0, 3, 10]

def sorted_squares(nums: List[int]) -> List[int]:
    l=0
    r=len(nums)-1
    ans=[0]*len(nums)
    
    if len(nums)<1:
        return []
    
    i=len(ans)-1
    while l<=r:
        if abs(nums[l])>abs(nums[r]):
            ans[i]=nums[l]**2
            l+=1
        else:
            ans[i]=nums[r]**2
            r-=1
            
        i-=1
        
    return ans
            


sorted_squares([])
sorted_squares([-2, -1])
sorted_squares([0,1,2])
sorted_squares([-2,0,1,2])
sorted_squares([-5, -3, -1])
sorted_squares([-4, -1, 0, 3, 10])
sorted_squares([-4, -1, 2, 3, 10])
sorted_squares([-10, -4, -1, 0, 3, 10])

        
#%% 2. Container with most water ==========================
# ============================================================================
# Given array height in which  
# each element represents height of vertical line at that position
# choose two lines such that together with the x axis they form a container that holds most water
# water area bettween lines l r:
# min(height[l], height[r]) * (r-l)
# xxx|________ɹxxx
# --- Idea: ---
# Start wide (l=0, r=n-1). 
# If h[l]<h[r], any container formed by moving r will decrease y, 
# since x is determined by min value, height can't improve past l. 
# the only way to get bigger height is by moving l inward. 
# (same goes for the reversed case where h[l]>h[r])
# --- Complexity: --- O(n) time, O(1) space

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
h=[1,8,6,2,5,4,8,3,7];  # 49
n=len(h)
l,r =1, n-1
# l,r =1, n-3
min(h[l], h[r]) * (r-l)
# x * y 


from typing import List


def max_area(height: List[int]) -> int:
    l=0
    r=len(height)-1
    max_ar = 0
    max_id = []
    
    
    while l<r:
        ar = min(height[l],height[r]) * (r-l)
        
        max_ar=max(max_ar, ar)
        
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
            
    return max_ar
        
    
        
        
        
max_area(h)
max_area([1,8,6,2,5,4,8,3,7])  # 49 (1,8)
max_area([1,8,6,2,5,4,18,3,7]) # 49 (1,8)
max_area([1,18,6,2,5,18,3,7])  # 72 (1,5)
max_area([1,1,1,1,1,1,1,1])    # 7  (0,7)



#%% 3. 3Sum ==================================================================
# ============================================================================
# given array nums, return all UNIQUE triplets [a,b,c] with a+b+c == 0.
# Input:  [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2], [-1,0,1]]
# order inside a triplet is usually nondecreasing
# --- Algorithm: ---
# 1. sort arr
# 2. fix first number: at each i, treat arr[i] as the first number in the triplet
#    The other two must sum to -nums[i]
# 3. Duplicates: after sorting, equal values sit next to each other, so
#   - skip i if nums[i] == nums[i-1] (same first number = same triplets)
#   - after a hit, move l and r past copies of the values just used
# 4. set up two pointers for the subarray to the right of i
# 5. while l<r: compute sum of the three elements
# - if sum==0, append new triplet, increase l,r counters BUT skip duplicates
# - if sum<0, increase l
# - if sum>0, decrease r
# 6. continue until l meets r
# 7. return triplets
# --- Example: ---
#              [-4,-1,-1, 0, 1, 2]   sum     
# i=0 (-4)      i   l           r    -3  <0 -> l++
#               i      l        r    -3  <0 -> l++
#               i         l     r    -2  <0 -> l++
#               i            l  r    -1  <0 -> l++   (l meets r, next i)
# i=1 (-1)          i  l        r     0  found [-1,-1,2]; l++, r--
#                   i     l  r        0  found [-1,0,1];  l++, r-- -> stop
# i=2 (-1)      same as nums[i-1] ->  skip
# i=3 ( 0)                i  l  r     3  >0 -> r--       -> stop
# --- Q: does skipping duplicate i miss [-2,1,1] in [-2,0,1,1,2]? ---
# No. The skip only compares nums[i] with nums[i-1]. l and r can still
# land on equal values (1 and 1), so [-2,1,1] is found from i=0.
# --- Complexity: --- O(n^2) time, O(1) extra space (besides the output)

nums = [-1,0,1,2,-1,-4, -4]
nums = [-1,0,1,2,-1,-4]
# if we're skipping first duplicates, doesn't that mean we wouldn't catch -2,1,1?

        
def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    trips=[]

    
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
            
        l=i+1
        r=len(nums)-1
        while l<r:
            trip = (nums[i],nums[l],nums[r])
            s = sum(trip)
            if s==0:
                trips.append(trip)
                
                l+=1
                r-=1
                
                while l<r and nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r+1]:
                    r-=1
                
                
            elif s<0:
                l+=1
            else:
                r-=1
    
    return trips
                
                
        
    

three_sum(nums)
three_sum([-1,0,1,2,-1,-4])# [[-1,-1,2],[-1,0,1]]
three_sum([])            # []
three_sum([0,0,0,0])     # [[0,0,0]] 
three_sum( [-2,0,1,1,2]) # [[-2,0,2], [-2,1,1]]
three_sum( [-2,0,1,1,1,2])   # [[-2,0,2], [-2,1,1]]
three_sum( [-2,0,1,1,1,2,2]) # [[-2,0,2], [-2,1,1]]


#%% 4. 3Sum Closest ================================
# ============================================================================
# Modify to solve 3Sum Closest (find triplet sum closest to target). 
# Return the SUM of the triplet whose sum is closest to target.
# (Exactly one answer, so no duplicate handling needed.)
# Input:  nums = [-1,2,1,-4], target = 1
# Output: 2    (-1 + 2 + 1)
# --- Idea: ---
# Same outer loop + two-pointer as 3Sum, but instead of collecting hits, 
# keep the best sum so far. 
# l/r still move towards the target: too small -> l++, too big -> r--.
# --- Algorithm: ---
# 1. sort; best = nums[0] + nums[1] + nums[2]   (a real sum, not inf)
# 2. for i in 0..n-3:
#      l, r = i+1, n-1
#      while l < r:
#        s = nums[i] + nums[l] + nums[r]
#        if |s - target| < |best - target|: best = s
#        s == target -> return s (can't do better)
#        s <  target -> l++
#        s >  target -> r--
# 3. return best
# --- Example: ---  target = 1, best starts at -4
#              [-4,-1, 1, 2]
# i=0 (-4)      i  l     r     s=-3  best=-3   <t -> l++
#               i     l  r     s=-1  best=-1   <t -> l++  -> stop
# i=1 (-1)         i  l  r     s= 2  best= 2   >t -> r--  -> stop
# answer: 2
# --- Complexity: --- O(n^2) time, O(1) space


# 1. sort arr
# 2. fix first number: at each i, treat arr[i] as the first number in the triplet
# 3. don't care about dupe logic here
# 4. set up two pointers for the subarray to the right of i
# 5. while l<r: compute sum of the three elements
# - if sum==target, return 
# - if difference between sum and target is smaller than best diff so far, save new best
# - if s<target increase l
# - if s>target, decrease r
# 6. continue until l meets r
# 7. return best

def three_sum_closest(nums: List[int], target: int) -> int:
    if len(nums)<3:
        return None
    
    best=sum(nums[:3])
    
    for i in range(len(nums)-2):
        l=i+1
        r=len(nums)-1
        
        while l<r:
            s = nums[i]+nums[l]+nums[r]
            
            if abs(s-target)<abs(best-target):
                best=s
            
            if s==target:
                return s
            elif s<target:
                l+=1
            else:
                r-=1
                
    return best
        
        
                
            

assert three_sum_closest([-1,2,1,-4], 1) == 2
assert three_sum_closest([0,0,0], 1) == 0
assert three_sum_closest([1,1,1,0], 100) == 3
three_sum_closest([-1,2,1,-4], 1)
    
#%% 5. 4Sum (nested loops) ============================
# ============================================================================
# Return all UNIQUE quadruplets [a,b,c,d] with a+b+c+d == target.
# Input:  nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]
# --- Idea: ---
# Sort array.
# Either:
# Two nested loops for the first two elements, then two-pointer for the remaining (O(n³)), OR
# Use a recursive kSum reduction: kSum(nums, k, target) calls kSum(nums, k-1, target - nums[i]) and ends with two-pointer for k==2.
# 3Sum with one more fixed number: i fixes the 1st, j fixes the 2nd,
# l/r find the last two. Same duplicate rule at EVERY level (to ensure UNIQUE quads):
#   skip i if nums[i] == nums[i-1]       (i > 0)
#   skip j if nums[j] == nums[j-1]       (j > i+1, NOT j > 0)
# j > i+1 matters: j's first value is allowed to equal nums[i],
# e.g. [-1,-1,1,1] needs i=0 and j=1 both on -1.
# --- Algorithm: ---
# 1. sort
# 2. for i in 0..n-4:            skip duplicate i
#      for j in i+1..n-3:        skip duplicate j
#        l, r = j+1, n-1
#        two-pointer scan exactly as in 3Sum, comparing to target
# 3. return quads
# --- Example: ---
#                    [-2,-1, 0, 0, 1, 2]
# i=0 j=1 (-2,-1)      i  j  l        r    -1  l++
#                      i  j     l     r    -1  l++
#                      i  j        l  r     0  found [-2,-1,1,2]
# i=0 j=2 (-2, 0)      i     j  l     r     0  found [-2,0,0,2]
# i=0 j=3              same as nums[2] -> skip
# i=1 j=2 (-1, 0)         i  j  l     r     1  r--
#                         i  j  l  r        0  found [-1,0,0,1]
# i=1 j=3              skip;   i=2 j=3: 0+0+1+2 = 3, r-- -> stop
# --- Complexity: --- O(n^3) time, O(1) extra space

def four_sum(nums: List[int], target: int) -> List[List[int]]:
    ...

assert four_sum([1,0,-1,0,-2,2], 0) == [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]
assert four_sum([2,2,2,2,2], 8) == [[2,2,2,2]]
assert four_sum([-1,-1,1,1], 0) == [[-1,-1,1,1]]
four_sum([1,0,-1,0,-2,2], 0)

# nums = [-5, -4, -3, -3, -2, -1, 0, 1, 2, 3, 3, 5, 8]
nums = [-3, -3, -2, -1, 0, 1, 2,2,2]
# nums = [-3, -1, 2,2]
# nums = [-3, -1, 2,2,2]
# nums = [-3, -1,-1, 2,2,2]
# nums = [-3, -1,-1,-1,1,1,2,2,2]
            

#%% 6. kSum (recursive) ==============================
# ============================================================================
# Generalise 3Sum/4Sum: all unique k-tuples that sum to target.
# 4Sum = k_sum(nums, 4, target, 0) on a sorted array.
# --- Idea: ---
# Each level fixes ONE number and asks for a (k-1)Sum on the rest:
#   k_sum(k, target, start)
#     fix nums[i]  -> k_sum(k-1, target - nums[i], i+1)
#       ...        -> k == 2: plain l/r Two Sum II scan  (base case)
# Then glue nums[i] onto the front of every tuple that comes back.
# Duplicate rule at each level: skip i if i > start and nums[i] == nums[i-1].
# --- Algorithm: ---
# k_sum(nums, k, target, start):          # nums already sorted
#   if k == 2: return two_sum_all(nums, target, start)
#   res = []
#   for i in start..n-k:
#     skip duplicate i
#     for tup in k_sum(nums, k-1, target - nums[i], i+1):
#       res.append([nums[i]] + tup)
#   return res
# Optional pruning: stop early if k*nums[start] > target (smallest possible
# sum too big) or k*nums[-1] < target (largest possible sum too small).
# --- Example: ---  nums = [-2,-1,0,0,1,2], k = 4, target = 0
# k=4  fix -2 -> k=3, target  2, start 1
#   k=3  fix -1 -> k=2, target  3, start 2 -> l/r finds (1,2)  -> [-2,-1,1,2]
#   k=3  fix  0 -> k=2, target  2, start 3 -> l/r finds (0,2)  -> [-2,0,0,2]
# k=4  fix -1 -> k=3, target  1, start 2
#   k=3  fix  0 -> k=2, target  1, start 3 -> l/r finds (0,1)  -> [-1,0,0,1]
# --- Complexity: --- O(n^(k-1)) time, O(k) recursion depth

def two_sum_all(nums: List[int], target: int, start: int) -> List[List[int]]:
    ...


def k_sum(nums: List[int], k: int, target: int, start: int = 0) -> List[List[int]]:
    ...


def four_sum_rec(nums: List[int], target: int) -> List[List[int]]:
    ...

assert four_sum_rec([1,0,-1,0,-2,2], 0) == [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]
assert four_sum_rec([2,2,2,2,2], 8) == [[2,2,2,2]]
assert four_sum_rec([-1,-1,1,1], 0) == [[-1,-1,1,1]]
assert k_sum(sorted([-1,0,1,2,-1,-4]), 3, 0) == [[-1,-1,2], [-1,0,1]]   # 3Sum
assert k_sum([], 2, 0) == []
four_sum_rec([1,0,-1,0,-2,2], 0)


#%% kSum visual
# kSum is just "keep reducing the problem"
#
# k=4:
#   fix one number
#   solve 3Sum on the remainder
#
# k=3:
#   fix one number
#   solve 2Sum on the remainder
#
# k=2:
#   use the standard l/r two-pointer scan
#
# picture:
# kSum(nums, 4, target, start)
#   -> choose nums[i]
#   -> kSum(nums, 3, target - nums[i], i+1)
#       -> choose nums[j]
#       -> kSum(nums, 2, target - nums[i] - nums[j], j+1)
#           -> l/r scan
#
# base case:
# 2Sum in sorted array
#   if sum too small -> l++
#   if sum too big   -> r--
#   if equal         -> record pair

