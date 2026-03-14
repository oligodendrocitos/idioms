""" two pointers """


#%% 1. reverse array
# given array, reverse it in place
# [1,2,3,4] -> [4,3,2,1]

arr = [1,2,3,4]
l, r = 0, len(arr)-1
print(f"   l,r {l} {r}")

for i in range(4):
    # simultaneous assignment allows getting both at the same time. 
    arr[l], arr[r] = arr[r], arr[l]
    l+=1
    r-=1
    print(f"++ l,r {l} {r}")
    print(f"{arr} \n")



def reverse_array(arr):
    l, r = 0, len(arr)-1
    
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
        
        
# q: how would you do this witout simultaneous assignment? 

#%% 2. valid palindrome
# given string, return True if it reads the same way forward and backward
# "racecar" -> True
# "hello" -> False

s = "racecar"
# s = "hello!"

l,r = 0, len(s)-1

# middle letter doesn't matter if odd, doesn't exist if even. 
while l<r:
    print(f"compare {s[l]} {s[r]}")
    if s[l] != s[r]:
        foo= False
    
    l += 1
    r -= 1


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

nums = [2,7,11,15]
target = 9

l,r = 0, len(nums)-1

while l<r:
    res = nums[l]+nums[r]
    
    if res==target:
        print([l,r])
        break
    elif res<target:
        l+=1
    else:
        r-=1
        
        
def two_sum(nums, target):
    l,r = 0, len(nums)-1
    
    while l<r:
        res = nums[l]+nums[r]
        
        if res==target:
            return [l,r]
        elif res<target:
            l+=1
        else:
            r-=1
            
            
#%% 4. remove duplicates (sorted array)
# remove duplicates in place from sorted array
# return number of unique elements
# [1,1,2,2,3] -> [1,2,3,...]

nums = [1,2,2,3,4,5,5,6]
nums = [1,2,2,3,4,5,5,6]

slow=0 # unique number

for fast in range(1, len(nums)):
# fast=1
    if nums[fast] != nums[slow]:
        print(f"F:{nums[fast]} S:{nums[slow]}")
        slow +=1 # if fast found a new number, add to the unique counter
        nums[slow]=nums[fast] # 
        

nums = [1,2,2,3,4,5,5,6]
def remove_duplicates(nums):
    slow=0
    
    for fast in range(1,len(nums)):
        if nums[slow] != nums[fast]:
            slow+=1
            nums[slow]=nums[fast]
            
    return slow+1

remove_duplicates(nums)
nums = [1,2,2,3,4,5,5,6]
n=remove_duplicates(nums)
print(nums[:n])
# what if you actually want to replace it with 0 or remove it ?

#%% 5. move zeros
# move all zeros to end of array while maintaining relative order of non-zero elements
# [0,1,0,3,12]-> [1,3,12,0,0]

nums = [0,1,0,3,12]

slow=0

fast=0
for fast in range(len(nums)):
    if nums[fast]!=0:
        nums[slow]=nums[fast]
        slow+=1
        
        print(nums)
        
for i in range(slow, len(nums)):
    nums[i]=0

print(nums)


def move_zeros(nums):
    slow=0
    
    for fast in range(len(nums)):
        if nums[fast]!=0:
            nums[slow]=nums[fast]
            nums[slow]+=1

    for i in range(slow,len(nums)):
        nums[i]=0
        
    


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
    l,r = 0, len(arr)-1
    
    while l<r:
        arr[l], arr[r] = arr[r], arr[l]
        l+=1
        r-=1
        
        
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
target = 199
target = 13
target = 18

def two_sum(nums,target):
    l,r = 0, len(nums)-1
    
    while l<r:
        res = nums[l]+nums[r]
        if res==target:
            return [l,r]
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

nums = [1,2,2,3,4,5,5,6]


def remove_dupes(nums):
    slow=0
    
    for fast in range(1,len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow]=nums[fast]
            
    return slow+1


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
    slow=0
    
    for fast in range(len(nums)):
        if nums[fast]!=0:
            nums[slow]=nums[fast]
            slow+=1
            
    for i in range(slow, len(nums)):
        nums[i]=0
        
        
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
    l,r = 0,len(arr)-1
    
    while l<r:
        tmp=arr[l]
        arr[l]=arr[r]
        arr[r]=tmp
        
        r-=1
        l+=1
        
        
reverse(arr)
    
#%% 2. remove dupes and replace them with 0

arr = [1,2,3,3,4]
arr = [1,2,2,3,3,4]

def remove_dupes_with_zero(arr):
    slow=0
    
    for fast in range(len(arr)):
        
        if fast==0 or arr[fast] != arr[fast-1]:
            arr[slow]=arr[fast]
            slow+=1
            
    for i in range(slow, len(arr)):
        arr[i]=0
        
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
    n = len(nums)
    res = [0] * n 
    l,r,k = 0, n-1, n-1
    
    # l,r = 0, len(nums)-1
    # res = [0]*len(nums)
    # k=len(res)-1
    
    while l <= r:
        if abs(nums[l])>abs(nums[r]):
            res[k] = nums[l] * nums[l]
            l+=1
        else:
            res[k] = nums[r] * nums[r]
            r-=1
            
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

def max_area(height: List[int]) -> int:
    l, r = 0, len(height)-1
    
    max_arr = min(height[l], height[r]) * (r-l)
    max_ind = [l,r]
    
    while l<r:
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
            
        # calculate new area and compare:
        arr = min(height[l], height[r]) * (r-l)
        
        if arr>max_arr:
            max_arr = arr
            max_ind = [l,r]
            
    return max_arr
    
    
max_area(h)
    

def max_ar(height: List[int]) -> int:
    l, r = 0, len(height)-1
    best = 0

    while l<r:
        h = min(height[l], height[r])
        best = max(best, h*(r-l))
        
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
            
    return best

max_ar(h)


#%% 3. 3Sum
# given array nums, return all unique triplets [a,b,c]
# such that a+b+c == 0
# triplets should be returned without duplicates
# order inside a triplet is usually nondecreasing
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
nums = [-1,0,1,2,-1,-4]
nums = [-1,0,1,2,-1,-4, -4]

nums.sort()
print(f"sorted: {nums}")

n=len(nums)
res=[]

i = 1
# for i in range(n-2):
if i>0 and nums[i] == nums[i-1]: # skips dupes
    # continue
    print("cont")

target = -nums[i] # why -nums[i]? 
l,r = i+1, n-1



for i in range(n-2):
    if i>0 and nums[i] == nums[i-1]: # skips dupes
        continue
        # print("cont")
    
    target = -nums[i] # why -nums[i]? 
    l,r = i+1, n-1
    print(f"target, lr: {target}  {l} {r}")


while l<r:
    s = nums[l] + nums[r]
    if s==target:
        res.append([nums[i], nums[l], nums[r]])
        
        while l<r and nums[l] == nums[l+1]:
            l +=1
        while l<r and nums[r] == nums[r-1]:
            r-=1
        
        l +=1
        r -=1
        
    elif s<target:
        l+=1
    else:
        r-=1
        
        
        

def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        l, r = i + 1, n - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                res.append([nums[i], nums[l], nums[r]])
                # skip duplicates for l and r
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif s < target:
                l += 1
            else:
                r -= 1
    return res


#%% 3Sum: function 

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
   
nums = [-1,0,1,2,-1,-4]
# Expected (order may vary): [[-1,-1,2], [-1,0,1]]
nums = [] 
# Expected: []
nums = [0,0,0,0]
# Expected: [[0,0,0]]   # only one unique triplet
nums = [-2,0,1,1,2]
# Expected (order may vary): [[-2,0,2], [-2,1,1]]

def sum3(arr):
    arr.sort()
    print(arr)
    trips = []
    
    for i in range(len(arr)-3):        
        if i>0 and arr[i]==arr[i-1]:
            continue
        
        num = arr[i]       
        l=i+1
        r=len(arr)-1
        
        while l<r:
            print(f" {num} + {arr[l]} + {arr[r]}")
            s = num + arr[l] + arr[r]
            if s==0:
                trips.append([num, arr[l], arr[r]])
                
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


sum3(arr)


#%% 3sum: non-function test

trips = []
arr.sort()

# for i in range(len(arr)):
for i in range(len(arr)-2):
    num = arr[i]
    
    if i>0 and arr[i]==arr[i-1]:
        # skip duplicate
        continue
    
    l,r = i+1, len(arr)-1
    while l<r:
        s = arr[i] + arr[l] + arr[r]
        
        if s==0:
            trips.append([arr[i], arr[l], arr[r]])
            print(trips)
            # change both counters. Why not just 1? 
            # because in [a,b,c,d,e], if a+b+e==0, the only way a+b+d==0
            # is if d==e, which means they are dupes, which means we want to skip them!
            
            # so: while next value is the same, keep moving pointer:
            # Move off the current solution, then skip duplicates.
            l+=1
            r-=1
            while arr[l]==arr[l-1] and l<r:
                l+=1
            while arr[r]==arr[r+1] and l<r:
                r-=1
                        
            # alternative version:
            # val_l = nums[l]
            # val_r = nums[r]
            
            # while l < r and nums[l] == val_l:
            #     l += 1
            # while l < r and nums[r] == val_r:
            #     r -= 1
            
        elif s<0:
            # why not check for dupes in the other cases? 
            # since s!=target we haven't appended anything to the triplets list. 
            # we only care if we RECORD a duplicate in the triplets, not if we
            # check the same combination again. 
            # increase left
            l+=1
            
        else:
            # s>0: decrease right
            r-=1
            
    
    
    
#%% 3Sum closest
# Modify to solve 3Sum Closest (find triplet sum closest to target). 
# Same outer loop + two-pointer idea; keep track of best diff.

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

import math

def sum3close(arr, target):
    arr.sort()
    
    for i in range(len(arr)-2):
        # if i>0 and arr[i]==arr[i-1]:
            # continue
        
        num=arr[i]
        l,r = i+1, len(arr)-1
        bestdiff = math.inf
        bestsum = math.inf
        bestel = []
        
        while l<r:
            s = num+arr[l]+arr[r]
            print(f" {num} + {arr[l]} + {arr[r]}")
            if s==target:
                return [num, arr[l], arr[r]]
            
            if abs(s-target)<bestdiff:
                bestel = [num, arr[l], arr[r]]
                bestdiff=abs(s-target)
                bestsum=s
            
                # l+=1
                # r-=1
                # while l<r and arr[l]==arr[l-1]:
                #     l+=1
                # while l<r and arr[r]==arr[r+1]:
                #     r-=1
            
            if s<target:
                l+=1
            else:
                r-=1
                
    return bestel, bestdiff, bestsum
                
        
nums = [-1, 2, 1, -4];
target = 1


def thrsumclosest(arr, target):
    arr.sort()
    
    # decide which one of these you want to return
    trip=[]
    bestsum=math.inf
    
    for i in range(len(arr)-3):
        num=arr[i]
        
        l,r=i+1,len(arr)-1
        
        while l<r:
            s = arr[i] + arr[l] +arr[r]
            
            if s==target:
                return [arr[i], arr[l], arr[r]]
            
            if abs(s-target)<abs(bestsum-target):
                bestsum=s
                trip = [arr[i], arr[l], arr[r]]
                
            if s<target:
                l+=1
            else:
                r-=1
                
            
    
#%% 3Sum closest: chat's version:
from typing import List

def sum3close(nums, target):
    nums.sort()
    
    n=len(nums)
    # initialize with first three (assume n >= 3)
    
    best = nums[0] + nums[1] + nums[2]
    for i in range(n-2):
        l,r = i+1, n-1
        
        while l<r:
            cur = nums[i]+nums[l]+nums[r]
            if abs(cur-target)<abs(best-target):
                best=cur
            if cur==target:
                return cur
            elif cur<target:
                l+=1
            else:
                r-=1
                
    return best


def three_sum_closest_triplet(nums: List[int], target: int):
    nums.sort()
    n = len(nums)
    best = nums[0] + nums[1] + nums[2]
    best_triplet = (nums[0], nums[1], nums[2])
    for i in range(n - 2):
        l, r = i + 1, n - 1
        while l < r:
            cur = nums[i] + nums[l] + nums[r]
            if abs(cur - target) < abs(best - target):
                best = cur
                best_triplet = (nums[i], nums[l], nums[r])
            if cur == target:
                return target, (nums[i], nums[l], nums[r])
            elif cur < target:
                l += 1
            else:
                r -= 1
    return best, list(best_triplet)

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

n=7
js=1
for i in range(n-3):
    for j in range(js,n-2):
        print(f"{i}{j}")
    js+=1
    
    
n=7
js=1
for i in range(n-3):
    for j in range(i+1,n-2):
        print(f"{i}{j}")
    js+=1

#%%


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

# nums = [-5, -4, -3, -3, -2, -1, 0, 1, 2, 3, 3, 5, 8]
nums = [-3, -3, -2, -1, 0, 1, 2,2,2]
# nums = [-3, -1, 2,2]
# nums = [-3, -1, 2,2,2]
# nums = [-3, -1,-1, 2,2,2]
# nums = [-3, -1,-1,-1,1,1,2,2,2]
sum4(nums)



def foursum(arr):
    arr.sort()
    
    quads=[]
    
    for i in range(len(arr)-3):
        if i>0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1,len(arr)-2):
            
            num = arr[i]+arr[j]
            l,r = j+1, len(arr)-1
            
            while l<r:
                s = num+arr[l]+arr[r]
                
                if s==0:
                    quads.append([arr[i],arr[j],arr[l],arr[r],])
                    
                    l+=1
                    r-=1
                    
                    if l<r and arr[l]==arr[l-1]:
                        l+=1
                    if l<r and arr[r]==arr[r+1]:
                        r-=1
                        
                elif s<0:
                    l+=1
                else:
                    r-=1
                    
    return quads


foursum(nums)
                    
            
#%% 4sum - recursion



#%% 4sum - chat's version

def sum4(nums):
    nums.sort()
    n=len(nums)
    res=[]
    for i in range(n-3):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1, n-2):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            
            l,r = j+1, n-1
            while l<r:
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    # skip duplicates for l and r
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
    return res


from typing import List

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

def four_sum_recursive(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    return k_sum(nums, 4, target, 0)