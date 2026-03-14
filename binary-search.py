""" binary search
Intuition:
    binary search finds a boundary in an ordered, 
    monotonic search space. 
    
    e.g. 
    0 0 0 | 1 1 
    
    
    e.g. 
    Array = [1,3,5,7,9,12,15]
    target = 7
    instead of checking every element, 
    check the middle, then eliminate half the array
       
Use when:
    - array is sorted
    - need to find specific element


 """
#%% 1. classic 
"""Used when:
The array is sorted
You want to find a specific element

Example problem:
Find index of target in sorted array."""

def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1

#%% binary search on the answer


#%% linked list
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
#%%

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


#%% # 1. Linked List Cycle (easy) 
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



def has_cycle(head): 
     

has_cycle(head)


#%% 2. Middle of the Linked List (easy) — return mid node. (Template 2)
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

#%% # 3. Linked List Cycle II (medium) 
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
    
#%% 4. Find the Duplicate Number (medium) 
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

#%% 4.5 Find Dupe (Chatty's version with explanation)



#%% 5. Happy Number (easy) 
# — use tortoise & hare to detect cycle in sequence of sum-of-squares (or use seen set).
# Repeatedly replace number with sum of squares of digits.
# Eventually:
# Either reaches 1
# Or loops in a cycle
# Use fast/slow to detect cycle in the sequence.
# This generalizes cycle detection beyond linked lists.




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