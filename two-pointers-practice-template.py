""" two pointers """




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
arr = [0,2,2,5,7,9,12]

def reverse_array(arr):

        
        
reverse_array(arr)
print(arr)

        

#%% 2. valid palindrome
# given string, return True if it reads the same way forward and backward
# "racecar" -> True
# "hello" -> False

# Compare left and right
# If mismatch -> False
# Move inward
# If finish -> True

s = "racecar"
# s = "hello!"
# s = "aaaaa"

def is_palindrome(s):


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
target = 199
target = 13
target = 18

def two_sum(nums,target):



foo = two_sum(nums, target)
print(foo)
            
#%% 4. remove duplicates (sorted array)
# remove duplicates in place from sorted array
# return number of unique elements
# [1,1,2,2,3] -> [1,2,3,...]

# slow = position of next unique spot
# fast scans
# When new value appears -> write it at slow

nums = [1,2,2,3,4,5,5,6]


def remove_dupes(nums):



remove_dupes(nums)
    

#%% 5. move zeros
# move all zeros to end of array while maintaining relative order of non-zero elements
# [0,1,0,3,12]-> [1,3,12,0,0]

# slow tracks where next non-zero goes
# fast scans
# After finishing, fill rest with zeros

nums = [0,1,0,3,12]
nums = [0,1,0,0,3,12,0,0]

def move_zeros(nums):

        
move_zeros(nums)
print(nums)


############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
#%% 1. reverse array without simultaneous assignment

arr=[1,2,3,4,5]

def reverse(arr):

        
reverse(arr)
    
#%% 2. remove dupes and replace them with 0

arr = [1,2,3,3,4]
arr = [1,2,2,3,3,4]

def remove_dupes_with_zero(arr):

        
remove_dupes_with_zero(arr)
print(arr)
    

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

arr = []
arr = [-2, -1]
arr = [0,1,2]
arr = [-5, -3, -1]
arr = [-4, -1, 0, 3, 10]
arr = [-10, -4, -1, 0, 3, 10]

def sorted_squares(nums: List[int]) -> List[int]:



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
h=[1,8,6,2,5,4,8,3,7]; 
# h=[1,8,6,2,5,4,18,3,7]; 
# h=[1,18,6,2,5,18,3,7]; 
# h=[1,1,1,1,1,1,1,1]; 
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

        
def three_sum(nums: List[int]) -> List[List[int]]:
  
    
    
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


# nums = [-5, -4, -3, -3, -2, -1, 0, 1, 2, 3, 3, 5, 8]
nums = [-3, -3, -2, -1, 0, 1, 2,2,2]
# nums = [-3, -1, 2,2]
# nums = [-3, -1, 2,2,2]
# nums = [-3, -1,-1, 2,2,2]
# nums = [-3, -1,-1,-1,1,1,2,2,2]
sum4(nums)

#%% 4sum - recursion


def sum4rec(arr):