""" fast-slow pointers
Intuition:
    use two pointers that move at different speeds. 
    usually slow moves 1 step, fast moves 2.
    The difference in speed gives you information about cycles, distances or relative positions:
        - if there's a cycle, fast will eventually lap slow and they meet
        - if there's no cycle, fast reaches the end and they never meet
        - the meeting point gives information for finding the start of the cycle
        
When to use:
    - detect a cycle in a linked list
    - find the start node of a cycle in a linked list
    - find the middle node of a linked list
    - detect cycle-like behaviour in arrays or sequences
    - solve problems where 2 relative speeds encode a relation


A linked list:
    
A linked list is a sequence of nodes, where each node stores:
- a value
- a reference (pointer) to the next node

[1 | •] → [2 | •] → [3 | •] → [4 | None]    
Each box is a node object.
Each node has: val, next    
There is no indexing, so you can'ŧ do head[2]

e.g. here, a cycle starts at C:

A → B → C → D → E
          ↑     ↓
          H ← G ← F


Templates:
    
1) Detect cycle in a linked list
We are not comparing values.
We are comparing node identity (memory location).
So, saying 
    if slow is fast:
means both pointers reference the exact same node object.
    

def has_cycle(head):
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow is fast:
        return True
return False



2) Find middle node
    
def middle_node(head):
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow
    


3) Find cycle start (Floyd’s algorithm)
1. detect meeting
2. move one pointer to head, then advance both by 1 - they meet at cycle start


def detect_cycle_start(head):
    slow = fast = head
    # 1) detect
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None  # no cycle

    # 2) find start
    ptr = head
    while ptr is not slow:
        ptr = ptr.next
        slow = slow.next
    return ptr

A → B → C → D → E
          ↑     ↓
          H ← G ← F

AA
BC
CE
DG
EC
FE
GG << slow is fast
H
C

AG
BH
CC << ptr is slow
D
E

cycle length k = 6
entry point is mu=2 (or 3) steps from head
when slow and fast meet, fast has taken 2t steps and slow t steps;
t=7 2t=14 (I count 13?)
difference t=m*k

From the meeting point, if you move ptr from head and 
slow from meeting point 1 steps each, 
they will meet at cycle entry after mu steps
because meeting point is k-(mu%k) steps from cycle entry




4) Find duplicate in array using cycle detection
If array values are in 1..n and array length n+1, treat next index as f(x)=nums[x]

def find_duplicate(nums):
    # Phase 1: find intersection
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    # Phase 2: find entrance
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    return hare
    
    

 """

#%% 1. linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = b   # creates a cycle

# this gives
# 1 → 2 → 3 → 4
#       ↑     ↓
#       ← ← ←


# traversing a linked list:
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c        
# This gives a → b → c → None

head = a
curr = head
while curr:
    print(curr.val)
    curr = curr.next
    
# reversing a linked list
# turn 
# 1 → 2 → 3 → None
# into
# 3 → 2 → 1 → None
#%% 2. reverse linked list

def reverse_list(head): # assumes you know the starting node!
    prev=None
    curr=head
    
    while curr:
        nxt = curr.next  # save next
        curr.next = prev # reverse pointer
        prev = curr      # make prev refer to curr for next round / move prev forward
        curr = nxt       # make curr refer to nxt for next round / move curr forward
        
        
    return prev


# e.g.
# prev = None
# curr = 1
# Save 2
# Point 1 → None
# set prev to 1
# set curr to 2
# and now:
# 1 → None
# 2 → 3
# repeat until 

        

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c     

head = reverse_list(a)
# head is now 3
curr = head
while curr:
    print(curr.val)
    curr = curr.next
    
    
# recursive version:
def reverse_list(head):
    if not head or not head.next:
        return head
    
    new_head = reverse_list(head.next)
    head.next.next = head
    head.next = None

    return new_head


#%% 3. Linked List Cycle (easy) 
# detect if cycle exists. (Template 1)

class ListNode:
    def __init__(self,  val=0, next=None):
        self.next = next
        self.val = val

# empty
a1 = None

# single node no cycle 
a2 = ListNode()

# single node with next=self (cycle) 
a3 = ListNode()
a3.next = a3

# 3-node cycle.
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = b   # creates a cycle


head = a1 # empty
# head = a2 # single node no cycle 
# head = a3 # single node with next=self (cycle) 
# head = a  # 3-node cycle.


def has_cycle(head):
    fast = slow = head
    
    while fast and fast.next: # if there's no cycle, it will reach an end! infinite loops impossible!
        slow = slow.next
        fast = fast.next.next
        
        if slow is fast:
            return True
        
    return False



     

has_cycle(head)


#%% 4. Middle of the Linked List (easy) — return mid node. (Template 2)
# Implement middle_node, run on even length (4 nodes) and odd (5 nodes).

# even length (4 nodes) 
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
# a > b > c > d

# odd (5 nodes)
a1 = ListNode('a')
b1 = ListNode('b')
c1 = ListNode('c')
d1 = ListNode('d')
e1 = ListNode('e')
a1.next = b1
b1.next = c1
c1.next = d1
d1.next = e1
# a > b > c > d > e
# 

# even length (4 nodes) 
head = a
# odd (5 nodes)
head = a1

def middle_node(head):
    fast = slow = head
    
    while fast and fast.next:
        print(f"{fast.val}")
        slow = slow.next
        fast = fast.next.next
        
    print(f"middle node: {slow.val}")
    return slow
    


middle_node(head)

#%% 5. Linked List Cycle II (medium) 
# — return entry node of cycle. (Template 3)
# Phase 1: detect meeting
# Phase 2: reset one pointer to head

# entry node c
a1 = ListNode('a')
b1 = ListNode('b')
c1 = ListNode('c')
d1 = ListNode('d')
e1 = ListNode('e')
a1.next = b1
b1.next = c1
c1.next = d1
d1.next = e1
# e1.next = c1
# e1.next = b1 # entry node b
# e1.next = None # no cycle

head = a1

def cycle_start(head):
    # 1. detect meeting
    slow = fast = head
    c = False
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow is fast:
            c=True
            break
    
    if not c:
        return None
    #equivalent, shorter (comment out varaible c stuff):
    # else:
        # loop exited because fast hit the end -> no cycle
        # return None
    # 2. find start
    ptr = head
    
    while ptr is not slow:
        ptr = ptr.next
        slow = slow.next
        
    return ptr
    



cycle_start(head)
# print(cycle_start(head).val)
    
#%% 6. Find the Duplicate Number (medium) 
# — treat array as linked list. (Template 4)
# Given:
# nums has length n+1
# values are in [1, n] (because you don't want to point back to index 0 where hare and tortoise are initialised)
# one duplicate exists 

arr = [1, 2, 3, 2, 4]
# what about unordered??
arr = [1, 3, 4, 2, 4]
arr = [1, 3, 5, 4, 5, 2]

# Interpret:
# index → nums[index]
# as a pointer.
# This forms a cycle.
# Use fast/slow to find duplicate.


# [1, 3, 4, 2, 4]
#  0  1  2  3  4
# 1. T=1 H=1 >>   a[T]=3  a[H]=3 a[3]=2 
# 2. T=3 H=2 >>   a[T]=2  a[H]=4 a[4]=4 
# 2. T=2 H=4 >>   a[T]=4  a[H]=4 a[4]=4  >> T==H >> END

# [3, 2, 1, 3, 4]
#  0  1  2  3  4
# 1. T=3 H=3 >>   a[T]=3  a[H]=3 a[3]=3 
# 2. T=3 H=3 >>   a[T]=3  a[H]=3 a[3]=3  >> T==H >> END


# if there's a 0
# [1, 3, 4, 0, 4]
#  0  1  2  3  4


# THINK OF THIS AS A GRAPH
# nums = [3, 2, 1, 3, 4]
# index:  0  1  2  3  4
# edges: 0->3, 1->2, 2->1, 3->3, 4->4

# DUPE = ELEMENT THAT GETS POINTED TO TWICE
# Since a dupe, by definition, appears in the list twice, 
# there will be two indices referring to it. (e.g. above, 0->3 3->3)

def find_dupe(arr):
    # 1. find intersection
    tortoise = arr[0]
    hare = arr[0]
    
    while True:
        tortoise = arr[tortoise] # use tortoise as index
        hare = arr[arr[hare]] # use the value AT tortoise (1st iter) as index
        print(f"{tortoise} :: {hare} ")
        
        if tortoise == hare:
            break
            
    # 2. find entrance
    ent = arr[0]
    
    while ent != tortoise:
        tortoise = arr[tortoise]
        ent = arr[ent]
        print(f"phase 2  {tortoise} :: {ent} ")
        
    # if arr[index] == ind
    return ent


find_dupe(arr)

#%% 6.5 Find Dupe (Chatty's version with explanation)
# 1. Use two pointers tortoise and hare. Start both at nums[0].
# 2. Move tortoise one step: tortoise = nums[tortoise]. Move hare two steps: hare = nums[nums[hare]]. Repeat until they meet.
# 3. When they meet, set tortoise = nums[0] again, keep hare at meeting point.
# 4. Move both one step at a time: tortoise = nums[tortoise], hare = nums[hare], until they meet again. That meeting value is the duplicate.

# The problem guarantees at least one duplicate and that all values are in 1..n. The algorithm relies on that.
# If constraints were different (e.g., values outside 1..n or no guaranteed duplicate), the mapping-to-indices trick might not apply.
# This approach returns a duplicate (if there are multiple, it finds one of them).

from typing import List

def find_duplicate(nums: List[int]) -> int:
    # Phase 1: find intersection
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Phase 2: find entrance to the cycle
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    return hare


#%% 7. Happy Number (easy) 
# — use tortoise & hare to detect cycle in sequence of sum-of-squares (or use seen set).
# Repeatedly replace number with sum of squares of digits.
# Eventually:
# Either reaches 1
# Or loops in a cycle
# Use fast/slow to detect cycle in the sequence.
# This generalizes cycle detection beyond linked lists.


# You start with a number n. Repeatedly replace it with:
# the sum of the squares of its digits

# Example:
# 19 -> 1^2 + 9^2 = 82
# 82 -> 8^2 + 2^2 = 68
# 68 -> 6^2 + 8^2 = 100
# 100 -> 1

# A number is happy if this process eventually reaches 1.
# If it never reaches 1, it must fall into a cycle.

# Why fast/slow works here:
# The sequence of numbers is like a linked list:
#     each number points to the next number in the sequence
#     either the sequence ends at 1
#     or it repeats forever in a cycle

# So we can use the same cycle-detection idea:
#     slow moves one step
#     fast moves two steps

# If fast == slow, we found a cycle.
# If fast reaches 1, the number is happy.

# I. how to get digits
x = 4232
# digit = x % 10 # last digit (remainder of 10s)
# x //= 10       # removes last digit (full 10s)


seq=[]
n = 253
tortoise = 2*2 + 5*5 + 3*3


def next_num(x):
    # get next sum of sq of digits of x
    ssq = 0
    st = "SSQ: "
    st2=f"DIG: {x} "
    while x>0:
        digit = x % 10
        ssq += digit*digit
        st = st + f"{(digit*digit)} + "
        
        x //= 10
        st2 = st2+f"{x} "
        
        
    st = st[:-2] + f"= {ssq}"
    print(st)
    print(st2)
    return ssq


next_num(x)

def happy_number(x):
    # You start with a number n. Repeatedly replace it with:
    # the sum of the squares of its digits
    # A number is happy if this process eventually reaches 1.
    # If it never reaches 1, it must fall into a cycle.
    tortoise = x
    hare = x
    
    while True:
        tortoise = next_num(tortoise)
        hare = next_num(next_num(hare))
        
        if tortoise==1 or hare==1:
            return True
        if tortoise==hare:
            return False
        
        
happy_number(x)


#%% 7.5 Chatty's solution: 
    
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def next_num(x):
            total = 0
            while x > 0:
                digit = x % 10
                total += digit * digit
                x //= 10
            return total

        while n != 1 and n not in seen:
            seen.add(n)
            n = next_num(n)

        return n == 1
    


# function version of the same thing

def next_num(x):
    ssq=0
    while x>0:
        digit = x % 10
        ssq += digit*digit
        x //= 10
        
    return ssq


def isHappy(n):
    seen=set()
    
    while n!=1 and n not in seen:
        seen.add(n)
        n = next_num(n)
        
    return n==1

#%% 8. Palindrome linked list
# A linked list is a palindrome if it reads the same forward and backward.
# Example:
# 1 -> 2 -> 2 -> 1
# or
# 1 -> 2 -> 3 -> 2 -> 1

# The trick is:
# find the middle,
# reverse the second half,
# compare the first half and the reversed second half.


# For a list like:
# 1 -> 2 -> 3 -> 2 -> 1

# we do:
# 1. move slow and fast until the middle,
# 2. reverse from slow onward,
# 3. compare nodes from the start and from the reversed second half.



# test cases:
#[]               # -> True
#[1]              # -> True
#[1,2]            # -> False
#[1,1]            # -> True
#[1,2,1]          # -> True
#[1,2,2,1]        # -> True
#[1,2,3,2,1]      # -> True
#[1,2,3,4,5]      # -> False

#%% 8. Find start of cycle in functional graph


#%%
# 1. you told me to Implement has_cycle and run on: empty, single node no cycle, single node with next=self (cycle), a 3-node cycle. Is  a=None; head=a what you mean by empty? 
# 2. what's the desired behavior for middle node in cases with even number of nodes? My method returns 3 in a linked list with 4 nodes. 
# 3. whats the most elegant way to handle no cycle cases in floyds? 
# 4. 


# Practice problems (try in this order)

# 1. Linked List Cycle (easy) — detect if cycle exists. (Template 1)

# 2. Middle of the Linked List (easy) — return mid node. (Template 2)

# 3. Linked List Cycle II (medium) — return entry node of cycle. (Template 3)

# 4. Find the Duplicate Number (medium) — treat array as linked list. (Template 4)

# 5. Happy Number (easy) — use tortoise & hare to detect cycle in sequence of sum-of-squares (or use seen set).

# 6. Find start of cycle in functional graph (advanced) — variations where f(x) is given.

# For each problem:
# Sketch why fast/slow applies (what is the sequence and how is "next" defined).
# Write the two-phase code when needed.
# Edge-case: empty input / single node / no cycle.

    
# Implement has_cycle, run on: empty, single node no cycle, single node with next=self (cycle), a 3-node cycle.

# Implement middle_node, run on even length (4 nodes) and odd (5 nodes).

# Implement detect_cycle_start on a short linked list with cycle and verify.


#options:
# Walk through a concrete python implementation of the 4 functions above with a simple ListNode class and small tests you can paste into your editor?
# Or give 6 curated LeetCode problems (IDs/names) connected to fast/slow for you to practice in order?