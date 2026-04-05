""" two pointers  
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



Variant C — Merge From End (Your Example)
    
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
#%% 1. reverse array
# given array, reverse it in place
# [1,2,3,4] -> [4,3,2,1]

# Left starts at beginning
# Right starts at end
# Swap
# Move inward
# Stop when they cross.

arr = [2,5,7,9,12]
arr = [0,2,2,7,9,12]

def reverse_array(arr):
    l = 0
    r = len(arr)-1
    
    while l<r:
        arr[l], arr[r] = arr[r], arr[l]
        
        l+=1
        r-=1
        
    return arr
        

        
        
    

reverse_array(arr)
print(arr)

        
#%% 1.5 without simultaneous assignment
arr=[1,2,3,4,5]

def reverse(arr):
    l,r = 0,len(arr)-1
    
    while l<r:
        tmp=arr[l]
        arr[l]=arr[r]
        arr[r]=tmp
        r-=1
        l+=1
        

reverse(arr)

#%% 2. valid palindrome
# given string, return True if it reads the same way forward and backward
# "racecar" -> True
# "hello" -> False

# Compare left and right
# If mismatch -> False
# Move inward
# If finish -> True

s = "racecar"
s = "hello!"
# s = "aaaaa"

def is_palindrome(s):
    l,r = 0, len(s)-1
    
    while l<r:
        if s[l] != s[r]:
            return False
        
        l+=1
        r-=1
        
    return True



is_palindrome(s)


#%% 3. Two Sum II
# given sorted array and target, return indices of two numbers 
# that add up to target. 
# nums = [2,7,11,15]
# target = 9
# [1,2]
# If sum too small -> move left up
# If sum too big -> move right down

nums = [2,7,11,15]
target = 199 # none
target = 13 # 0,2
target = 18 # 1,2

def two_sum(nums,target):
    l=0
    r=len(nums)-1
    
    while l<r:
        res = nums[l]+nums[r]
        if res==target:
            return (l,r)
        elif res<target:
            l+=1
        else:
            r-=1
            
    return None




        


foo = two_sum(nums, target)
print(foo)
            
#%% 4. remove duplicates (sorted array)
# remove duplicates in place from sorted array
# return number of unique elements
# [1,1,2,2,3] -> [1,2,3,...]

# slow = position of next unique spot
# fast scans
# When new value appears -> write it at slow

# 1. loop through indices starting from 1
# 2. compare numbers
# - if number @ fast is the same as number @ slow, nothing happens (fast increases by 1)
# - if numbers are different, slow increases by 1, and the new value gets written

# slow = points to the last unique element position
# fast = scans ahead
# When new value appears -> increase & write it at slow


# 0 1 2 3 4    s=0, f=1
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
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow]=nums[fast]
            
            
    # print(f"{slow} {fast}")
    print(f"{nums}")
    return slow+1




remove_dupes(nums)
    


# alternative implementation
# compare adjacent elements (fast vs fast-1)
# no reasoning about slow in the condition

def remove_dupes(nums):
    if not nums:
        return 0
    
    slow=1
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast-1]:
            nums[slow] = nums[fast]
            
            slow += 1



#%% 5. move zeros
# move all zeros to end of array while maintaining relative order of non-zero elements
# [0,1,0,3,12]-> [1,3,12,0,0]

# slow tracks where next non-zero goes
# fast scans
# After finishing, fill rest with zeros
# fast and slow start at the same spot

nums = [0,1,0,3,12]
nums = [0,1,0,0,3,12,1,0]
#      [0,1,2,3,4,5, 6,7]

# 0,1,2,3,4
# 0,1,0,3,12 f=[0] 
# 0,1,0,3,12 f=[1] move 1->[0] 
# 1,1,0,3,12 f=[2]
# 1,1,0,3,12 f=[3] move 3->[1]
# 1,3,0,3,12 f=[4] move 12->[2]
# 1,3,12,3,12 END

# 1. start at ix 0
# 2. if number at fast ix isn't a zero, put it in slow AND increase slow index


def move_zeros(nums):
    slow=0
    
    for fast in range(0,len(nums)):
        if nums[fast]!=0:
            nums[slow] = nums[fast]
            slow+=1
            
    for i in range(slow, len(nums)):
        nums[i] = 0
        
    return nums
            
    
        
move_zeros(nums)
print(nums)


# alternative implementation
# instead of write and overwrite, 
# swap non-zero forward
nums = [0,1,0,0,3,12,1,0]
#      [0,1,2,3,4,5, 6,7]

def move_zeros(nums):
    slow = 0
    
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1



# TODO
# look at more problems like these two, 
# you don't have a good sense of why the solution differs the way
# it does between them. 

#%% 6. remove all instances
# remove all instances of val in-place
# return new length
# nums = [3,2,2,3], val = 3 -> [2,2]

nums = [3,2,2,3]
val=3
# 3 2 2 3
# 0 1 2 3

# slow points to last non-del val spot
# fast scans
    
def remove_all_instances(nums, val):
    slow=0
    
    for fast in range(len(nums)):
        if nums[fast]!=val:
            nums[slow] = nums[fast]
            slow+=1
            
    print(nums)
    return slow

remove_all_instances(nums, val)


# %% 7. Remove all but 2 copies (sorted array)
# [1,1,1,2,2,3] -> [1,1,2,2,3]

# keep an element if fast-2
nums = [1,1,1,2,2,3]
# nums = [0,1,1,2,2,3]
# nums = [0,1,1,2,2,2,2,3]
#  1 1 1 2 2 3
#  0 1 2 3 4 5

# 1 1 2 2 2 3 f=3 
# 0 1 2 3 4 5 0==2, move 3 to 2

# 1 1 2 2 2 3 f=4 
# 0 1 2 3 4 5 

# 1 1 2 2 2 3 f=5 
# 0 1 2 3 4 5 4==2, move 5 to 4

# 1 1 1 2 2 3 f=2, f==f-2, s=2
# 1 1 2 2 2 3 f=3, f!=f-2  f>>s
# 1 1 2 2 2 3 f=4, f==f-2, s=4
# 1 1 2 2 3 3 f=5, f!=f-2  f>>s

#  possible array starts: 
# [1,1,1] [0,1,1] [0,0,1] [0,1,2]
# in any of these cases, first two copies don'ŧ matter in relation to each other (!). 
# earliest possible element to replace:

    
def remove_duplicates_allow_2(nums):
    if len(nums) <= 2:
        return len(nums)
    
    slow = 2
    
    for fast in range(2, len(nums)):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
            
    nums[:] = nums[:slow]   # shrink the list in place
    print(nums)
    return slow

remove_duplicates_allow_2(nums)

#%% 8. Move all negatives to the left (order preserved)
# [1,-1,3,-2,0] -> [-1,-2,1,3,0]

nums = [1,-1,3,-2,0]

# Option 1: Use extra space
# This is the simplest and most common in Python.
def move_negatives_left(nums):
    negatives = [x for x in nums if x < 0]
    non_negatives = [x for x in nums if x >= 0]
    nums[:] = negatives + non_negatives
    return nums
# [1, -1, 3, -2, 0] -> [-1, -2, 1, 3, 0]


# Option 2: In-place stable version
# If you want to do it in-place, you can insert each negative where it belongs and shift the block of positives right by one.
def move_negatives_left(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] < 0:
            temp = nums[fast]
            i = fast
            while i > slow:
                nums[i] = nums[i - 1]
                i -= 1
            nums[slow] = temp
            slow += 1
    return nums


move_negatives_left(nums)



#%% 9. Partition array by pivot (like quicksort step)
# nums = [3,2,1,5,6,4], pivot = 3
# -> [2,1,3,5,6,4] (order of groups matters)
nums = [3,2,1,5,6,4]


nums = [9,12,5,10,14,3,10]
pivot = 10
# output: [9,5,3,10,10,12,14]

# 1) Partition array by pivot
# There are two common versions of this problem:
# A. Stable partition
# You must keep the original relative order of elements less than, equal to, and greater than the pivot.
# Mental model:
#     first collect all < pivot
#     then all == pivot
#     then all > pivot
# This is much easier than trying to do it in-place while preserving order.


def partition_array(nums, pivot):
    less = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    greater = [x for x in nums if x > pivot]
    nums[:] = less + equal + greater
    return nums


# B. In-place partition, order not preserved
# Sometimes the problem only asks you to partition, not preserve order.
# Then you can use two pointers:
def partition_array_inplace(nums, pivot):
    i = 0
    for j in range(len(nums)):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums




#%% 10. Sort colors (Dutch national flag)
# [2,0,2,1,1,0] -> [0,0,1,1,2,2]

nums = [2,0,2,1,1,0]

def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            
            
    

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

# 1. Squares of a sorted array
# given sorted array of ints, return new array of squares in sorted order
# Input: [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]

# The largest squared value is at whichever end has the larger absolute value;
# use two pointers at the ends
# write the biggest squares into the result from the back to the front.


from typing import List
import math

arr = []
arr = [-2, -1]
arr = [0,1,2]
arr = [-5, -3, -1]
# arr = [-4, -1, 0, 3, 10]
# arr = [-10, -4, -1, 0, 3, 10]

def sorted_squares(nums: List[int]) -> List[int]:
    n = len(nums)
    l,r,k = 0, n-1, n-1
    res = [0] * n
    
    while l<=r:
        if abs(nums[l]) < abs(nums[r]):
            res[k] = nums[r]*nums[r]
            r-=1
        else: #if abs(nums[l]) > abs(nums[r]):
            res[k] = nums[l]*nums[l]
            l+=1
            
        k-=1    
    
    
    return res
    



sorted_squares(arr)

        
#%% 2. container with most water
# given array height
# each element represents height of vertical line at that position
# choose two lines such that together with the x axis they form a container that holds most water
# water area bettween lines l r:
# min(height[l], height[r]) * (r-l)
# xxx|________ɹxxx
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# h=[1,8,6,2,5,4,8,3,7];  # 49
# h=[1,8,6,2,5,4,18,3,7]; # 49 
# h=[1,18,6,2,5,18,3,7];  # 72
# h=[1,1,1,1,1,1,1,1];    # 7
n=len(h)
l,r =1, n-1
# l,r =1, n-3
min(h[l], h[r]) * (r-l)
# x * y 

# if h[l]<h[r], any container formed by moving r will decrease y, 
# since x is determined by min value, height can't improve past l. 
# the only way to get bigger height is by moving l inward. 
# (same goes for the reversed case where h[l]>h[r])

from typing import List


def max_ar(height: List[int]) -> int:
    l=0
    n=len(height)
    r=n-1
    maxar=0
    
    while l<r:
        hr=height[r]
        hl=height[l]
        
        ar = min(hr,hl) * (r-l)
        maxar=max(maxar,ar)
        
        if hr<hl:
            r-=1
        else:
            l+=1
            
    
    return maxar


max_ar(h)






#%% 3. 3Sum
# given array nums, return all unique triplets [a,b,c]
# such that a+b+c == 0
# triplets should be returned without duplicates
# order inside a triplet is usually nondecreasing

# 1. sort arr
# 2. fix first number: at each i, treat arr[i] as the first number in the triplet
# 3. because the array is sorted, skip duplicate first elements
# e.g. in  arr=[-2,0,0,2,2] search for triplets starting with [-2,0,2] 
# 4. set up two pointers for the subarray to the right of i
# 5. while l<r: compute sum of the three elements
# - if sum==0, append new triplet, increase l,r counters BUT skip duplicates
# - if sum<0, increase l
# - if sum>0, decrease r
# 6. continue until l meets r
# 7. return triplets


# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
nums = [-1,0,1,2,-1,-4]
nums = [-1,0,1,2,-1,-4, -4]
nums = [-1,0,1,2,-1,-4]
# Expected (order may vary): [[-1,-1,2], [-1,0,1]]
nums = [] 
# Expected: []
nums = [0,0,0,0]
# Expected: [[0,0,0]]   # only one unique triplet
nums = [-2,0,1,1,2]
# Expected (order may vary): [[-2,0,2], [-2,1,1]]

# if we're skipping first duplicates, doesn't that mean we wouldn't catch -2,1,1?

        
def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort() 
    n=len(nums)
    trips = []
    
    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        
        target=-nums[i]
        l = i+1
        r = n-1
        
        while l<r:
            res = nums[i]+nums[l]+nums[r]
            
            if res==0:
                trips.append([nums[i],nums[l],nums[r]])
                
                l+=1
                r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r+1]:
                    r-=1
                
            
            elif res<0:
                l+=1
            else:
                r-=1
                
    return trips
        
        
    

# [0 1 2 3 4 5 6 7]

    

three_sum(nums)
#%% 3Sum closest
# Modify to solve 3Sum Closest (find triplet sum closest to target). 
# Same outer loop + two-pointer idea; keep track of best diff.

# 1. Sort nums.
# 2. Initialize best_sum as the sum of any three elements (common: nums[0]+nums[1]+nums[2]) or inf sentinel.
# 3. For each i from 0 to n-3:
# - Set left = i+1, right = n-1.
# - While left < right:
#     cur = nums[i] + nums[left] + nums[right]
#     If abs(cur - target) < abs(best_sum - target): update best_sum = cur (and optionally remember the triplet).
#     If cur == target: return target (best possible).
#     If cur < target: left += 1 (we need a bigger sum).
#     Else (cur > target): right -= 1.
# 4. After loops, return best_sum (or the triplet if you stored it).

import math

def sum3close(arr, target):
    arr.sort()
    n=len(arr)
    best = arr[1]+arr[2]+arr[3]
    
    for i in range(n-3):
        l=i+1
        r=n-1
        
        while l<r:
            cur = arr[i]+arr[l]+arr[r]
            
            if abs(cur-target) < abs (best-target):
                best=cur
                
            if cur==target:
                return cur
            if cur<target:
                l+=1
            else:
                r-=1
                
    return best
    
        
nums = [-1, 2, 1, -4];
target = 1

sum3close(nums, target)
    

#%% 4sum - nested loop
# Practice 3 problems back-to-back: 3Sum, 3Sum Closest, and 4Sum (4Sum generalizes outer loop twice or recursion + two-pointer inside).

# 1. sort arr
# 2. fix first number: at each i, treat arr[i] as the first number in the triplet
# 3. because the array is sorted, skip duplicate first elements
# e.g. in  arr=[-2,0,0,2,2] search for triplets starting with [-2,0,2] 
# 4. set up two pointers for the subarray to the right of i
# 5. while l<r: compute sum of the three elements
# - if sum==0, append new triplet, increase l,r counters BUT skip duplicates
# - if sum<0, increase l
# - if sum>0, decrease r
# 6. continue until l meets r
# 7. return triplets

# Sort array.
# Either:
# Two nested loops for the first two elements, then two-pointer for the remaining (O(n³)), OR
# Use a recursive kSum reduction: kSum(nums, k, target) calls kSum(nums, k-1, target - nums[i]) and ends with two-pointer for k==2.
# Must handle duplicates (skip equal i/j) to avoid duplicate quadruplets.

# [0, 1, 2, 3, 4, 5]
# [0], [1], 2, 3, 4, 5] 01
# [0], 1, [2], 3, 4, 5] 02
# [0], 1, 2, [3], 4, 5] 03
# 0, [1], [2], 3, 4, 5] 12
# 0, [1], 2, [3], 4, 5] 13
# 0, 1, [2], [3], 4, 5] 23
# 0, 1, [2], [3], 4, 5, 6] 23

def sum4(arr):
    arr.sort()
    
    



def sum4(arr):
    arr.sort()
    print(arr)
    trips = []
    js=1
    for i in range(len(arr)-3):
        if i>0 and arr[i]==arr[i-1]:
            continue
        # for j in range(js, len(arr)-2):       # previous version that was almost right 
        for j in range(i+1, len(arr)-2):        
            if j>0 and arr[j]==arr[j-1]:
                continue
            if i==j:
                continue
    # for i in range(len(arr)-3):
    #     # if i>0 and arr[i]==arr[i-1]:
    #     #     continue
    #     for j in range(js, len(arr)-2):        
    #         # if j>0 and arr[j]==arr[j-1]:
    #         #     continue
    #         if i==j:
    #             continue
            # if curr ij is the same as previous ij?
            # currij = (arr[i], arr[j])
            # previj = (arr[i-1], arr[j-1])
            # if (i>0 and j>0) and currij==previj: #arr[j]==arr[j-1]
            #     continue

            num = arr[i] + arr[j]   
            print(f"ij {i}{j}  {arr[i]} {arr[j]}")
            l=j+1
            r=len(arr)-1
            
            while l<r:
                # print(f" {num} + {arr[l]} + {arr[r]}")
                s = num + arr[l] + arr[r]
                if s==0:
                    trips.append([arr[i], arr[j], arr[l], arr[r]])
                    
                    l+=1
                    r-=1
                    
                    while l<r and arr[l]==arr[l-1]: # if l matches the previous element
                        l+=1
                    while l<r and arr[r]==arr[r+1]: # same for right
                        r-=1
                        
                elif s<0:
                    l+=1
                    
                else:
                    r-=1
                
    return trips


def foursum(arr):
    arr.sort()
    quads=[]
    
    for i in range(len(arr)-3):
        if i>0 and arr[i]==arr[i-1]:
            continue
        
        for j in range(i+1, len(arr)-2):
            num = arr[i]+arr[j]
            l,r = j+1,len(arr)-1
            
            while l<r:
                s = num+arr[l]+arr[r]
                
                if s==0:
                    quads.append([arr[i],arr[j],arr[l],arr[r],])
                    
                    l+=1
                    r-=1
                    
                    while l<r and arr[l]==arr[l-1]:
                        l+=1
                    while l<r and arr[r]==arr[r+1]:
                        r-=1
                        
                elif s<0:
                    l+=1
                else:
                    r-=1
                    
    return quads
            


# nums = [-5, -4, -3, -3, -2, -1, 0, 1, 2, 3, 3, 5, 8]
nums = [-3, -3, -2, -1, 0, 1, 2,2,2]
# nums = [-3, -1, 2,2]
# nums = [-3, -1, 2,2,2]
# nums = [-3, -1,-1, 2,2,2]
# nums = [-3, -1,-1,-1,1,1,2,2,2]
sum4(nums)

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

#%% Ksum

def ksum(arr,k,target,start):
    


def k_sum(nums, k, target, start):
    n = len(nums)
    res = []
    # not enough numbers
    if start >= n or n - start < k:
        return res
    # pruning: smallest/largest possible sums
    if k * nums[start] > target:
        return res
    if k * nums[-1] < target:
        return res

    if k == 2:
        # two-pointer base case
        l, r = start, n - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1
                # skip duplicates
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif s < target:
                l += 1
            else:
                r -= 1
        return res

    # recursive case
    for i in range(start, n - k + 1):
        if i > start and nums[i] == nums[i - 1]:
            continue
        sub = k_sum(nums, k - 1, target - nums[i], i + 1)
        for comb in sub:
            res.append([nums[i]] + comb)
    return res



#%% 4sum - recursion


def sum4rec(arr):