#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:03:10 2026

@author: qq20468
"""


#%% numpy ---------------------------------------------------------------------
import numpy as np

arr = np.random.randint(0,9,(2,3))
arr.shape
arr.T
# arr.reshape(...)
np.mean(arr, axis=0)
np.sum(arr, axis=1)

m = 3
n = 4
np.zeros((m,n))
np.ones((m,n))
np.eye(n)

#%% Shape conventions
# Convention
# If array shape is:
# (n_rows, n_columns)
# Axis 0 >> rows
# Axis 1 >> columns
# Example:
arr = np.array([[1,2,3],
                [4,5,6]])


arr.shape
# Shape: (2, 3)
# 2 rows
# 3 columns

# axis=0: collapse rows, compute down columns
# -> mean of each column 
np.mean(arr,axis=0)

# axis=1: collapse columns, compute across rows
# -> mean of each row
np.mean(arr,axis=1)


## Visual Trick
# Axis number tells you which direction disappears.
# - axis=0 → rows disappear → result keeps columns
# - axis=1 → columns disappear → result keeps rows

#%% Broadcasting
"""
1. Compare shapes from the right (last dim first)
A shape: (4,3)    Comparison:   (4, 3)
b shape: (3,)                   (   3)
2. Dimensions are compatible if a) they are EQUAL, or
                                b) one of them is 1
3. Missing dimensions are treated as 1  
 e.g. (3,)  behaves like  (1,3)
 
!!!!!
1D vectors (4,) are treated as a column vector
for MULTIPLICATION 
 
Examples: 
A = np.ones((4,3))
b = np.array([1,2,3,4])
 
A = (4,3)
b = (3,)
3 & 3 -> OK
4 & 1 -> OK (nothing=1)

A = (4,3)
b = (4,)
3 & 4 -> not ok

b[:, np.newaxis] <- changes shape
A = (4,3)
b = (4,1)
3 & 1 -> OK
4 & 4 -> OK

b = np.array([1,2,3]) :: shape (3,)  implicitly (1,3)
b = np.array([[1],[2],[3]]) :: shape (3,1)
b.reshape(1,3) >> array([[1, 2, 3]]) (single row again)

(4,) behaves like (1,4) or (4,1) 
during broadcasting, depending on context.

 A shape (n,) acts like a row when combined with (n,m) or (k,n) depending on alignment;
 use reshape(1,-1) or [:, np.newaxis] when you need to make the intent explicit.
 To subtract row means (mean over columns for each row): X - np.mean(X, axis=1, keepdims=True)
 so the returned mean is shape (3,1) and broadcasts across columns.
 keepdims=True is handy: np.mean(X, axis=0, keepdims=True) returns shape (1,3) which can be clearer.
"""
# Works 
A = np.ones((4,3))
b = np.array([1,2,3]) # 3,
A + b
A@b

# Nope
A = np.ones((4,3))
b = np.array([1,2,3,4]) # 4,
# A + b
# A@b

# 3 adding axis to b fixes it
A = np.ones((4,3))
b = np.array([1,2,3,4])
A + b[:, np.newaxis]


# 4 works
A = np.ones((5,4))
b = np.array([10,20,30,40])
A - b

#5 
A = np.ones((5,4))
b = np.array([10,20,30,40])
A - b.reshape(-1,1) # (4,) to (4,1)

# 6 subtract row means 
X = np.random.randn(6,3)
row_means = np.mean(X, axis=1)
# a) option 1: add new dim
X - row_means[:, np.newaxis]
# b) option 2: 
row_means = np.mean(X, axis=1, keepdims=True) # (6, 1)
X - row_means

# 7 scale each column
X = np.ones((3,4))
scales = np.array([1,10,100,1000])
X_scaled = X * scales 


# 8 add bias per row
X = np.ones((5,3))
bias = np.array([0.1, 0.2, 0.3])
Xb = X+bias

# 9 works
A = np.ones((2,3,4))
b = np.array([1,2,3,4])
A + b

#10 nope
# A = np.ones((2,3,4))
# b = np.array([1,2,3])
# A + b


v = np.ones((4,1))
w = np.arange(1,5)[np.newaxis,:] # 1,4
# w = np.arange(1,5)[None,:] # 1,4
v@w

#%% things that don't work are commented out
A = np.ones((7,1))
b = np.array([1,2,3])
A + b

A = np.ones((7,3))
b = np.array([[1],[2],[3]])
# A + b

A = np.ones((4,5,6))
b = np.ones((5,6))
A + b

X = np.random.randn(10,4)
col_means = np.mean(X, axis=0) # shape 4,
X - col_means #[:, np.newaxis] # 

A = np.ones((5,1,4))
b = np.ones((4,))
A + b

A = np.ones((5,1,4))
b = np.ones((1,4))
A + b

A = np.ones((5,2,4))
b = np.ones((2,1))
A + b

A = np.ones((3,4))
b = np.ones((3,))
A + b[:, None]

# Write both shapes.
# Align from the right.
# Compare dimension by dimension.
# If mismatch and neither is 1: error.


#%% reshape
"""
For an array with shape (a, b, c):
axis=0   >> first dimension (a)
axis=1   >> second (b)
axis=2   >> third (c)
axis=-1  >> last dimension (c)
axis=-2  >> second-to-last (b)

np.mean(X, axis=-1) :: Take mean along the last dimension.
"""
x = np.array([1,2,3,4,5,6]) # (6,)
x.reshape(2,3) # shape 2,3

# -1: figure out this dimension automatically
x = np.array([1,2,3,4,5,6]) # (6,)
x.reshape(-1,3) # shape 2,3

x = np.array([10,20,30,40]) # shape 4, (implicit 4,1)
x.reshape(-1,1) # shape 4,1
# reshape(-1,1) changes a 1D array to a column vector

(4,)    # ambiguous
(4,1)   # column vector
(1,4)   # row vector
# (4,) behaves like (1,4) with added leading dimensions of 1
# during broadcasting, depending on context.


#%% stacking & concatenation
# Axis 0 : stack vertically (add rows)
# Axis 1 : stack horizontally (add columns)
A = np.ones((2,3))
B = np.zeros((2,3))
np.concatenate([A,B], axis=0) # shape 4,3
np.concatenate([A,B], axis=1) # shape 2,6

np.vstack([A,B]) # vertical stack, axis=0
np.hstack([A,B]) #  axis=1 

# np.stack adds a new dimension AT the axis position:
np.stack([A,B], axis=0) # 2,2,3

np.stack([A,A,B,B], axis=0) # 4,2,3
np.stack([A,A,B,B], axis=1) # 2,4,3
np.stack([A,A,B,B], axis=2) # 2,3,4

a = np.array([[1,2],
              [3,4]])   # (2,2)
b = np.array([[5,6],
              [7,8]])   # (2,2)
np.stack([a,b], axis=0) # 4,2,3
np.stack([a,b], axis=1) # 4,2,3
np.stack([a,b], axis=2) # 4,2,3


n = 3
x = np.ones(shape=(n,))
y = np.ones(shape=(n,))
np.column_stack((x,y)) # (n,2) (x and y become columns)

# Note: vstack will automatically convert 1D arrays into 2D rows.
a = np.array([1,2]) # shape 2,
b = np.array([3,4]) # shape 2,
np.vstack([a,b]).shape
np.concatenate([a,b], axis=0).shape

x = np.array([1,2,3,4]) 
# reshape into 4,1 without reshape
x[:, None]
np.expand_dims(x, axis=1) #!!!!


# can you make concatenate stack 1d arrays as separate rows at all? 
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
np.concatenate([a[None,:], b[None,:]], axis=0)


# You asked: can we get shape (1,4,4)?
# Yes - but not directly from those.
# You’d need to reshape first.
# Example:
A = np.ones((3,4))
b = np.array([1,2,3,4]) #(4,)
# np.stack([A,b], axis=0) # won't work: stack needs exactly the same dims
A2 = A[:,:]   # (3,4)
b2 = b[None,:]  # (1,4)
# np.stack([A2,b2],axis=0)
# np.vstack([A2,b2])

# !!!! repeat some value to generate trial index 
# e.g. A2 (3,4) b2(1,4) ti=[3x[1], 1x[2]] 

#%% 
img1 = np.arange(1,7).reshape(2,3)
img2 = np.arange(7,13).reshape(2,3)

# 1. Stack them into a dataset of 2 images. (2,2,3)
np.stack([img1,img2], axis=0)

# 2. Now stack them so that the last dimension represents image number.
np.stack([img1,img2], axis=2) # OR
np.stack([img1,img2], axis=-1) 
# check:
# np.stack([img1,img2], axis=2)[:,:,0] #returns an image

# 3. Suppose you have 5 such images in a list.
# How do you stack them into:
# (n_images, height, width)
# np.stack([img1,...,img5], axis=0)
np.stack([img1,img2,img1,img2,img1], axis=0)


# You have RGB image:
# Red channel: (2,3)
# Green channel: (2,3)
# Blue channel: (2,3)
# Stack them so final shape is:
# (2,3,3)
# Where last dimension is color channel.
r = np.arange(1,7).reshape(2,3)
g = np.arange(7,13).reshape(2,3)
b = np.arange(13,19).reshape(2,3)

np.stack([r,g,b], axis=-1)
np.stack([r,g,b], axis=-1).shape
np.stack([r,g,b], axis=-1)[:,:,0]


#%% Masking and boolean indexing
x = np.array([1,2,3,4])
mask = x>2
x[mask]

# mask rows
# select rows where first column > 2
X = np.array([[1,2],
              [3,4],
              [5,6]])

X[X[:,0]>2]
# X[X[:,0]>2]=0

# modify with mask
x = np.array([-1,2,-3,4])
x[x<0] = 0
x

# conditional selection (like an if/else statement)
x = np.array([1,2,3,4])
np.where(x>2, 1, 0)
# np.where(condition, value_if_true, value_if_false)

# np.where(condition) returns indices
np.where(x > 2)

# more complex expressions (select rows where first column>2)
np.where(X[:,0] > 2)

# How to get indices instead of mask?
# np.where(condition)
# np.nonzero(condition)
x = np.array([1,2,3,4])
np.where(x > 2)
np.nonzero(x%2==0)



#%% linalg
# 1. dot product
# Result is scalar
# If vectors point same direction: large positive
# If perpendicular: 0
# If opposite direction: negative

a = [1,2,3]
b = [4,5,6]
np.dot(a,b) # = 1*4 + 2*5 + 3*6


a = np.array([1,2,3])
b = np.array([4,5,6])
np.dot(a,b)
a @ b
np.vdot(a,b)
(a*b).sum()

#%% 2. matrix multiplication
# Shapes rule
# If:
# A is shape (m × n)
# B is shape (n × k)
# Then:
# A @ B is shape (m × k)
# Inner dimensions must match.

A = np.ones((3,2)) # (3 × 2)
B = np.ones((2,4)) # (2 × 4)
A @ B #  (3 × 4)


#%% 3. Matrix x vector
# A = (3×2)
# w = (2×1)
# A @ w → (3×1)
# Each row gets dot-producted with w.
A = np.ones((3,2)) # (3 × 2)
w = np.ones((2,1)) # (2 × 4)
A @ w 


A = np.array([[1,2],
              [3,4],
              [5,6]])
w = np.array([10,20])

A@w 


# Why this matters for linear regression:
# If:
# X = (n_samples × n_features)
# w = (n_features × 1)
# Then:
# X @ w → (n_samples × 1)
# That gives predictions.
#%%
# Broadcasting does NOT apply to matrix multiplication.
# Broadcasting is for elementwise operations only.

import numpy as np
A = np.random.randn(3,4)
B = np.random.randn(4,2)
v = np.random.randn(4)

A @ B
np.dot(A, B)
A.dot(B)
# the same ^^

v * v
v @ v
# different


# Vector v has shape (4,)
# Matrix A has shape (3, 4)
# Can we compute A @ v?

# v has shape (4,)
# w has shape (4,)
# What does v @ w compute? 

# v has shape (4, 1)
# w has shape (1, 4)
# What is v @ w shape?
# What kind of object is this? Outer

# A has shape (3, 4)
# v has shape (3,)
# Can we compute A @ v?


x = np.random.randint(-3,3,(100,5))
w = np.random.randint(0,5,(5,))
x@w
(x@w).shape
# !!!! is w recast to 5,1 automatically? I thought inner dims must match

#%% 4. matrix inverse 
# The inverse of A (A⁻¹) exists if:
# A is square (n × n)
# determinant ≠ 0
# A(A⁻¹) = I  (identity)

# In regression:
# (XT X)-1 XT y
# Only works if matrix is invertible.
# In practice, we often use:
X = np.random.normal(size=(3,3)).round(1)
X = np.random.randint(0,8,(3,3))
np.linalg.pinv(X)

# Pseudo-inverse (safer).

# !!!!!
# Give you 5 short problems where you must decide between Counter / defaultdict
# Give you 5 mini problems where you choose the correct itertools tool
# - Do a **shape intuition drill session**
# - Or go deeper into linear algebra intuition for regression
# - Or build a minimal “NumPy fluency checklist” you can rehearse weekly  
# what is matrix rank, intuitively? 
# Give you stacking / reshaping / masking / slicing drills (several quick tasks), or
# Give tricky broadcasting traps and ask you to fix them, or
# Continue with the harder NumPy implementation tasks you requested earlier.

#%% 5. Other matrix operations

X = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

xm = np.mean(X,axis=0)
np.mean(X,axis=0).shape

# center the matrix
col_means = np.mean(X, axis=0)         # shape (3,)
X_centered = X - col_means             # broadcasting: (3,3) - (3,) -> (3,3)
# explicit equivalent:
X_centered2 = X - col_means[np.newaxis, :]   # (1,3) broadcasts to (3,3)
# or
X_centered3 = X - col_means.reshape(1, -1)


X.T @ X



# cosyne similarity = dot  / norm

a = np.array([1,2,3])
b = np.array([4,5,6])

cos_sim = np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

