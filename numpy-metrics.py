#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 15:41:51 2026


Single-pass scalar loop: 
O(1) extra memory >> good for streaming or huge datasets that don’t fit in RAM.

List comprehensions or building intermediates:
O(n) extra memory >> not acceptable for very large datasets.

Vectorized NumPy/Pandas:
memory cost is O(n x d) (for d dimensions) because you need the array in memory; but operations run in C/BLAS and are much faster.

So: use Welford / streaming when data 
doesn’t fit in RAM or you must process line-by-line; 
use NumPy/Pandas vectorized operations
when you can load data into memory or 
use chunked reading with aggregation.


@author: qq20468
"""
import math

#%% 
import numpy as np

def var_np(x,sample=False):
    x = np.asarray(x, dtype=np.float64)
    # ddof = delta degrees of freedom
    ddof = 1 if sample else 0
    return np.var(x,ddof=ddof)

def sd_np(x,sample=False):
    x = np.asarray(x, dtype=np.float64)
    ddof = 1 if sample else 0
    return np.std(x,ddof=ddof)


def var_vec(x, sample=False):
    x = np.asarray(x, dtype=np.float64)
    mu = x.mean()
    diff = x-mu
    sq = diff*diff

    denom = len(x)-1 if sample else len(x)

    return sq.sum() / denom


def cov_np(x,y, sample=False):
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)

    ddof = 1 if sample else 0
    return np.cov(x,y, ddof=ddof)[0,1]


def cov_vec(x,y,sample=False):
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    # convert to array
    mx = x.mean()
    my = y.mean()     
    
    dx = x-mx
    dy = y-my
    
    denom = len(x)-1 if sample else len(x)
    
    return (dx * dy).sum() / denom



def covmat(X,sample=False):
    # assume rows: samples
    # cols: variables
    X = np.asarray(X, dtype=np.float64)
    n = X.shape[0]
    
    dXmu = X - X.mean(axis=0)
    denom = n-1 if sample else n
    
    return (dXmu.T @ dXmu) / denom
        


# 1. ged mean diff (assume rows=samples)
# 2. get denom
# 3. calc covariance!
def covmat(X,sample=False):
    X = np.asarray(X)
    n = X.shape[0]
    mXd = X - X.mean(axis=0)
    print(X.mean(axis=0).shape)
    
    denom = n-1 if sample else n
    print(n)
    
    return (mXd.T @ mXd) / denom
    


xx = np.random.random((800000, 10))

xx = [[2,6],[1,3],[-1,0]]; xx=np.asarray(xx)
covmat(xx)
np.cov(xx, rowvar=False, ddof=0)

def corr_vec(x, y):
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    
    dx = x - x.mean()
    dy = y - y.mean()
    
    numerator = (dx * dy).sum()
    
    denom = np.sqrt((dx * dx).sum() * (dy * dy).sum())
    
    return numerator / denom


# np.var(x)
# np.cov(xx, rowvar=False)
# np.corrcoef(X, rowvar=False)

#%% mean
    
# generator function to load file as an iterable
def file_generator(filename):
    with open(filename,"r") as f:
        for line in f:
            yield float(line.strip())
            

def mean_streaming(iterable):
    total=0.0 
    n = 0
    
    for value in iterable:
        n+=1
        total+=value
        
    if n==0:
        raise ValueError("mean of empty data")
        
    return total/n

def mean_streamingII(iterable):
    mean=0.0
    count=0
    
    for value in iterable:
        count += 1
        delta = value-mean
        mean += delta/count
        
    if count==0:
        raise ValueError("empty data")
        
    return mean


xs = list(range(50000))
mean_streaming(xs)


def fake_file():
    for i in range(10_000_000): # 10 million numbers
        yield i * 0.1
        
mean_streaming(fake_file()) 
mean_streamingII(fake_file()) 

# for a real file:
# filedata = file_generator('data.txt')
# mean_streaming(filedata)

#%% numpy version
import numpy as np

def mean_numpy(arr):
    arr = np.asarray(arr, dtype=np.float64)
    return arr.mean()

#%% variance & std
# sigsq = 1/n SUM (x-mu)^2
# ssq = 1/(n-1) SUM (x-mu)^2    # sample var
# stddev = sqrt (sigsq)
# stddev = sqrt (ssq)           # sample std


def streaming_variance(iterable, sample=False):
    n=0
    mu=0.0
    m2=0.0
    
    for val in iterable:
        n += 1
        delta = val-mu
        mu += delta/n
        delta2 = val-mu
        m2 += delta*delta2
        
        
    if sample:
        assert n>1
        sigsq = m2/(n-1)
        std = math.sqrt(sigsq)
    else:
        assert n>0
        sigsq = m2/n
        std = math.sqrt(sigsq)
        
    return sigsq, std


streaming_variance(fake_file())     
    
# !!!!
# Provide a short checklist of unit tests for each function (mean, variance, covariance, correlation) that you can copy into your test harness; or
# Or chunked NumPy processing (read CSV in chunks and merge means)?
# 
#%% covariance    
# given paired obs [(x,y) (x,y) (x,y)...]
# cov(X,Y) = 1/n SUM [(xi-MU_x) * (yi-MU_y)]
# sample cov:
# cov(X,Y) = 1/(n-1) SUM [(xi-MU_x) * (yi-MU_y)]
# i.e. variance:            (x-mu)**2
# COvariance=cross variance (x-mu)(y-mu)
   
# for a file        
def pair_file_generator(filename, sep=','):
    with open(filename, 'r') as f:
        for line in f:
            a, b = line.strip().split(sep)
            yield float(a), float(b)
            
def fake2varstream():
    for i in range(10_000):
        yield (i*0.1, -i*0.1)
              
        
def covariance2(iterable, sample=False):
    n=0
    mux = 0.0
    muy = 0.0
    C = 0.0
    
    
    for xraw,yraw in iterable:
        x = float(xraw)
        y = float(yraw)
        n+=1
        dx = x-mux
        mux += dx/n
        dy = y-muy
        muy += dy/n
        C += dx*(muy-y) # !! USE OLD DX
        
    assert n>0
    
    if sample:
        assert n>1
        return C/(n-1)
    else:
        return C/n
    
    
    
def streaming_covariance(pairs_iterable, sample=False):
    n = 0
    mean_x = 0.0
    mean_y = 0.0
    C = 0.0   # accumulator for sum (x-mean_x)*(y-mean_y)
    
    # !!!! how to detect mismatch???
    # esp if iterable can be anything (not just file)
    for x_raw, y_raw in pairs_iterable:
        x = float(x_raw)
        y = float(y_raw)
        n += 1
        dx = x - mean_x
        mean_x += dx / n
        dy = y - mean_y
        mean_y += dy / n
        C += dx * (y - mean_y)   # use updated mean_y here
    
    if sample:
        if n < 2:
            raise ValueError("need at least 2 pairs for sample covariance")
        cov = C / (n - 1)
    else:
        if n == 0:
            raise ValueError("no data")
        cov = C / n
    
    return cov
        
# !!!! how to handle/detect mismatches inside cov function?
#  xy can be any iterable, so solution needs to cover more than just files
# 
#     how can I know when     
        
        
covariance2(fake2varstream())
    
# streaming_covariance(fake2varstream())


#%% covariance nxn
import random
from itertools import chain
# import numpy as np 

def fakeNvarstream(n,seed=10):
    rnd = random.Random(seed)
    for i in range(10_000):
        yield tuple(rnd.random() for i in range(n))

def check_num_elements(iterable):
    it = iter(iterable)
    # get first element
    try:
        first = next(it)
    except StopIteration:
        # raise ValueError("empty iterable")
        return None
    
    try:
        d = len(first) # check len
    except Exception:
        return 1
    
    it = chain([first], it) # put it back
    # or return NONE
    
    return d
    
def _ensure_iterator(iterable):
    """Return an iterator that yields the entire sequence, not losing the first element."""
    it = iter(iterable)
    try:
        first = next(it)
    except StopIteration:
        raise ValueError("empty iterable")
    # if first is a generator, convert to a tuple/list here:
    if not isinstance(first, (list, tuple)):
        # try to convert (covers file lines or generator-of-tokens)
        try:
            first = tuple(first)
        except TypeError:
            # not iterable in that way — treat as single-value vector
            first = (first,)
    return chain([first], it), first



def covarianceN(iterable, sample=False):
    d = check_num_elements(iterable)
    if not d:
        print("no data")
        return None
    if d==1:
        print("covariance needs two variables")
        return None
    # check d is not empty? 
    n=0
    mu = d*[0.0]
    # delta = d*[0.0]
    C = [d*[0.0] for i in range(d)]
    
    for vals in iterable:
        # convert tokens to floats
        fvals = list(float(v) for v in vals)
        # check len - is this inefficient?
        assert len(fvals)==d
        n+=1
        
        delta = (x - m for x,m in zip(fvals,mu))
        mu += (d/n for d in delta)
        delta2 = (x - m for x,m in zip(fvals,mu))
        outr = list(list(i*j for i in delta) for j in delta2)
        
        C += outr
        
        
    assert n>0
    
    if sample:
        assert n>1
        return list([cc/(n-1) for cc in c] for c in C)
        
    else:
        return list([cc/(n) for cc in c] for c in C)
        
        
        
    
var = fakeNvarstream(3)
# var = []
# var = [1,2,3]
covarianceN(var)


a = [1,2,3]
b = [3,4,45]
R = list([a[i]*b[j] for i in range(len(a))] for j in range(len(b)))
# R = list(list(i*j for i in a) for j in b)
# !!!! edge cases? 

#%% DEbugged version

import random
from itertools import chain, islice

def fakeNvarstream(n, seed=10, n_samples=10000):
    """Yield n-dimensional tuples of random floats (one tuple per sample)."""
    rnd = random.Random(seed)
    for _ in range(n_samples):
        yield tuple(rnd.random() for _ in range(n))

def _ensure_iterator(iterable):
    """Return an iterator that yields the entire sequence, not losing the first element."""
    it = iter(iterable)
    try:
        first = next(it)
    except StopIteration:
        raise ValueError("empty iterable")
    # if first is a generator, convert to a tuple/list here:
    if not isinstance(first, (list, tuple)):
        # try to convert (covers file lines or generator-of-tokens)
        try:
            first = tuple(first)
        except TypeError:
            # not iterable in that way — treat as single-value vector
            first = (first,)
    return chain([first], it), first

def covarianceN(iterable, sample=False):
    """
    Streaming covariance for d-dimensional data.
    iterable: yields sequences (lists/tuples) of length d
    Returns: d x d covariance matrix (list of lists)
    """
    iterator, first = _ensure_iterator(iterable)

    # normalize first into a list of floats
    first_row = [float(x) for x in first]
    d = len(first_row)

    # initialize
    n = 0
    mean = [0.0] * d
    C = [[0.0] * d for _ in range(d)]  # accumulator

    for vals in iterator:
        # convert to sequence of floats (handle generator/tuple/list)
        row = [float(x) for x in vals]
        if len(row) != d:
            raise ValueError(f"row length {len(row)} != expected {d}")
        n += 1

        # compute delta = x - mean_old
        delta = [row[i] - mean[i] for i in range(d)]
        # update mean in place
        for i in range(d):
            mean[i] += delta[i] / n
        # compute delta2 = x - mean_new
        delta2 = [row[i] - mean[i] for i in range(d)]

        # update covariance accumulator C (outer product: delta * delta2^T)
        for i in range(d):
            di = delta[i]
            # micro-optimisation: local row reference
            Ci = C[i]
            for j in range(d):
                Ci[j] += di * delta2[j]

    if n == 0:
        raise ValueError("no data")

    denom = (n - 1) if sample else n
    # produce final covariance matrix (divide each element)
    cov = [[C[i][j] / denom for j in range(d)] for i in range(d)]
    return cov


var = fakeNvarstream(3)
covarianceN(var)




#%% Correlation
# sigsq = 1/n SUM (x-mu)^2
# ssq = 1/(n-1) SUM (x-mu)^2    # sample var
# stddev = sqrt (sigsq)
# stddev = sqrt (ssq)           # sample std

# cov(X,Y) = 1/n SUM [(xi-MU_x) * (yi-MU_y)]
# sample cov:
# cov(X,Y) = 1/(n-1) SUM [(xi-MU_x) * (yi-MU_y)]

# rho = Cov(X,Y) / sigx sigy
# where sig is STD


# + single pass corr function

# correlation can also be written as:
#               SUM (x-mux)(y-muy)
# rho = ----------------------------------
#       SQRT{ SUM[x-mux]^2 * SUM[y-muy]^2 }

# 1. get dx, dy
# 2. update xy, xx, yy
# 3. plug xy, xx, yy in eq above

# The n vs n-1 factor cancels out in correlation.
# So sample and pop correlation are the same. 
# YOU CAN LEAVE OUT SAMPLE FROM ALL CORRELATION FUNCTIONS

import math



def streaming_correlation(iterable, sample=False):
    n = 0
    mean_x = 0.0
    mean_y = 0.0
    M2x = 0.0
    M2y = 0.0
    C = 0.0
    
    for x, y in iterable:
        x = float(x)
        y = float(y)
        n += 1

        dx = x - mean_x
        dy = y - mean_y
        
        mean_x += dx / n
        mean_y += dy / n
        
        M2x += dx * (x - mean_x)
        M2y += dy * (y - mean_y)
        
        C += dx * (y - mean_y)
    
    if n == 0:
        raise ValueError("empty iterable")
    
    if sample:
        if n < 2:
            raise ValueError("sample correlation requires at least 2 points")
        denom = n - 1
    else:
        denom = n
    
    var_x = M2x / denom
    var_y = M2y / denom
    cov = C / denom
    
    if var_x == 0 or var_y == 0:
        raise ValueError("correlation undefined for zero variance")
    
    return cov / math.sqrt(var_x * var_y)



def streaming_correlation(iterable, sample=False):
    # assuming x,y
    mux=0.
    muy=0.
    My=0.
    Mx=0.
    C=0.
    n=0

    for x,y in iterable:
        x = float(x)
        y = float(y)
        n+=1
        dx = x-mux
        dy = y-muy
        mux += dx/n
        muy += dy/n
        
        Mx += dx * (x-mux)
        My += dy * (y-muy)
        C += dx * (y-muy) # use old value!
        
        
    assert n>0
    
    if sample:
        assert n>1
        denom=n-1
    else:
        denom=n
    
    varx = Mx/denom
    vary = My/denom
    covXY = C/denom

    rho = covXY / math.sqrt(varx*vary)

    return rho          
        
    


xs = [1,2,3,4,3]
ys = [1,2,3,4,3]        
        
# xs = [1,2,3,4,3]
# ys = [4,3,2,1,2] 

xs = [1,2,3,4,3,1,2,3,4,3]
ys = [4,3,2,1,2,3,3,2,1,2] 

sample=True
sample=False
print(streaming_correlation(zip(xs,ys)))
print(np.corrcoef(xs,ys, rowvar=False))


#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#%% Entropy
# If variable always has the same value: entropy 0
# if values evenly distributed: entropy high
# Max entropy occurs when all outcomes are equally likely

# For a discrete var X:
# H(X) = -SUM_{over all x} [p(x) log p(x)]

# 1. count frequencies
# 2. convert to probabilities
# 3. apply formula
 

def entropy(x):
    x = np.asarray(x)    
    n = x.size
    
    if n==0:
        return 0.0
    
    uniq, counts = np.unique(x, return_counts=True)
    print(counts)
    px = counts/n
    
    H = -(px * np.log2(px)).sum()
    return float(H)
    

def joint_entropy(X):
    # assume X with shape (samples, features)
    # H(X) = sum over all x
    # joint entropy over all pred. vars
    
    X = np.asarray(X)
    n = X.shape[0]
    
    # unique rows = unique joint outcomes
    _, counts = np.unique(X,axis=0,return_counts=True)
    
    p = counts/n
    
    H = -(p * np.log2(p)).sum()
    
    return float(H)    


def entropy_features(X):
    # entropy separately for each!!!
    # returns 
    X = np.asarray(X)
    n_features = X.shape[1]

    H = np.zeros(n_features)

    for i in range(n_features):
        _, counts = np.unique(X[:, i], return_counts=True)
        p = counts / counts.sum()


    H[i] = -(p * np.log2(p)).sum()

    return H



X = ['A', 'A', 'B', 'B', 'B', 'C']
X = ['A','A','A','B'] # ~0.81
X = [1,1,1,1] # 0
X = [0,1,0,1] # 1.0
entropy(X)
        
X = np.array([
    [0,1],
    [0,1],
    [1,0],
    [1,0]
]) # H=1
# X = np.arange(10).reshape((5,2))
# X = np.ones(10).reshape((5,2))
joint_entropy(X)

#%% Conditional Entropy
# Remaining ucertainty once X is known
# H (Y|X) = SUM_{over x} p(x) H(Y|X=x)
# Expanded:
# H (Y|X) = - SUM_{over x,y} p(x,y) log p(y|x)

# because:
# entropy 
# H(X) = - SUM_{x} [p(x) log p(x)]
# cond. entropy is the expected entropy of Y after fixing X.
# H (Y|X) = E_{X} [H(Y|X=x)]
# expanded:
# H (Y|X) = SUM_{x} p(x) H(Y|X=x)
# plug in entropy definition (for fixed x, entropy of y)
# H(Y|X=x) = - SUM_{y} p(y|x) log p(y|x)
# substitute H(Y|X=x) term in expanded equation:
# H(Y|X) = SUM_{x} p(x) [- SUM_{y} p(y|x) log p(y|x)]
# bring sums together: 
# = - SUM_{x,y} p(x) p(y|x) log p(y|x)
# and since p(x)p(y|x) = p(x,y), we get:
    
# H(Y|X)=-SUM_{x,y} p(x,y) log p(y|x)    

# why is Y entropy for a fixed x ( H(Y|X=x) ) dependent on conditionals p(y|x)? 
# 

# 1. Get joint counts (x,y)
# 2. get marginal counts (x)
# 3. compute conditional probabilities
# -  pxy = joint_count / N
# -  p(y|x) = joint_count / x_count
# 4. apply formula
# 5. for continuous values!!!

def discretize(X,bins=10):
    # discretize each column into bins bins
    
    X = np.asarray(X)
    nsamples,nfeatures = X.shape
    Xbinned = np.zeros_like(X)
    
    for i in range(nfeatures):
        # Auto-detect edges. If you know data distribution apriori, can just do something like this:
        # np.round(X[:,i]*100).astype(int)//10
        edges = np.histogram_bin_edges(X[:,i], bins=bins)
        Xbinned[:,i] = np.digitize(X[:,i], edges[1:-1])
        
    return Xbinned

from collections import Counter
import math

# def conditional_entropy_mat(X,y):
    # again assume X shape (samples, variables)
    # and assume 
    # X = np.
    
    

X = [[0,0],[0,1],[1,0],[1,1]]
y = [0,1,1,1] # H=0.5
n = len(y)

bins=10

X = np.asarray(X)
y = np.asarray(y)
Xb = discretize(X,bins=bins)
nsamples,nfeatures = X.shape

H = np.zeros(nfeatures)

for i in range(nfeatures):
    Xi = Xb[:,i]
    
    joint_counts = Counter(zip(Xi,y))
    xc = Counter(Xi)
    
    for (xv, yv), joint in joint_counts.items():
        pxy = joint / nsamples
        pyGx = joint / xc[xv]
        
        H[i] -= pxy * np.log2(pyGx)
        
    # return H
            
        
        
def cond_entropy(X,y,bins=10):
    X = np.asarray(X)
    y = np.asarray(y)
    Xb = discretize(X,bins=bins)
    nsamples,nfeatures = Xb.shape
    H = np.zeros(nfeatures)

    for i in range(nfeatures):
        Xi = Xb[:,i]
        joint_counts = Counter(zip(Xi,y))
        xc = Counter(Xi)
        
        for (xv, yv), joint in joint_counts.items():
            pxy = joint / nsamples
            pyGx = joint / xc[xv]
            
            H[i] -= pxy * np.log2(pyGx)
            
    return H


# # Perfect dependence
# X = [0,0,1,1]
# Y = [0,0,1,1] # H=0

# # Independent
# X = [0,0,1,1]
# Y = [0,1,0,1] # H=1

# # Partial dependence
# X = [0,0,1,1]
# Y = [0,1,1,1] # H=0.5

cond_entropy(X,y)


#%% Mutual Information
# I(X;Y) = H(X) - H(X|Y)
# or
# I(X;Y) = SUM_{x,y}: p(x,y)*log[p(x,y) / p(x)p(y)]
# How much knowing X reduces uncertainty about Y

def entropy(y):

    y = np.asarray(y)

    counts = Counter(y)
    n = len(y)

    H = 0

    for c in counts.values():
        p = c/n
        H -= p * math.log2(p)

    return H


def MI(X, y, bins=10):

    Hy = entropy(y)
    Hy_given_X = cond_entropy(X, y, bins)

    return Hy - Hy_given_X


X =[[0.2],
    [0.3],
    [0.8],
    [0.9]]

Y = [0,0,1,1]



X = [[0.1, 0.2],
     [0.2, 0.3],
     [0.8, 0.1],
     [0.9, 0.5]]

Y = [0,0,1,1]

cond_entropy(X, Y, bins=2)
MI(X,Y, bins=2)


#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#%% Confusion Matrix
# for binary classification, compare pred to true labels. 
# 
#           Pred 1    Pred 0
# Actual 1    TP        FN
# Actual 0    FP        TN
#
# TP = true positive
# TN = true negative
# FP = false positive
# FN = false negative

# 1. init all values
# 2. loop through labels and count

def confusion_matrix_binary(y_true,y_pred):
    tp = tn = fp = fn = 0
    
    for yt, yp in zip(y_true,y_pred):
        if yt==1 and yp==1:
            tp+=1
        elif yt==0 and yp==1:
            fp+=1
        elif yt==1 and yp==0:
            fn+=1
        elif yt==0 and yp==0:
            tn+=1
        else:
            raise ValueError("labels must be binary")
            
    return tp, fp, fn, tn 

     
y_true = [1,0,1,1,0,0,1]
y_pred = [1,0,1,0,0,1,1]

tp, fp, fn, tn = confusion_matrix_binary(y_true, y_pred)
print(tp, fp, fn, tn)


#%% Precision
# Precision = TP / [TP+FP]
#           = True Positive / [True Positive + False Positive]
# Of the predicted positives, how many were correct?
# High precision = few false positives

def precision(tp,fp):
    if tp+fp==0:
        return 0.0
    
    return tp / (tp+fp)


#%% Recall (Sensitivity)
# Recall = TP / [TP+FN]
#        = True Positive / [True Positive + False Negative]
# Of the actual positives, how many did we correctly detect?
# High recall = few false negatives

def recall(tp,fn):
    if tp+fn==0:
        return 0.0
    
    return tp / (tp+fn)

#%% F1 Score
# F1 = 2 * [precision * recall] / [precision + recall]
# F1 balances precision and recall using harmonic mean
# harmonic mean punishes imbalance
# if one of them is small = F1 is small

def f1score(tp,fp,fn):
    p = precision(tp,fp)
    r = recall(tp,fn)
    
    if p+r==0:
        return 0.0
    
    return 2*p*r / (p+r)


#%% All metrics: 
    
def classification_metrix(y_true, y_pred):
    tp = tn = fp = fn = 0
    
    for yt,yp in zip(y_true, y_pred):    
        if yt==yp==1:
            tp+=1
        elif yt==yp==0:
            tn+=1
        elif yt==1 and yp==0:
            fn+=1
        elif yt==0 and yp==1:
            fp+=1
        else:
            raise ValueError('binary labels only pls')
            
        precision = tp / (tp+fp) if (tp+fp) else 0.0
        recall = tp / (tp+fn) if (tp+fn) else 0.0
        f1 = (2*precision*recall / (precision+recall)
              if (precision+recall) else 0.0)
        
        return {
            "tp":tp,
            "fp":fp,
            "fn":fn,
            "tn":tn,
            "precision":precision,
            "recall":recall,
            "f1":f1,
            }
        
#%% MultiClass Confusion Matrix & Metrix
# K x K matrix where
# rows: true labels
# columns: predicted labels
# Entry (i,j) = number of samples with:
# true class = i
# pred class = j
# Diagonal Entries = correct predictions
# Off-diagonal entries = mistakes

# e.g. 3 classes 0 1 2:
#    0 1 2 
# 0  5 1 0
# 1  2 6 1
# 2  0 1 4

# Assuming labels are integers: 0 ... K-1
# or at least hashable

# 1) Using sorted unique labels
# 1. check that vectors the same lenght
# 2. get labels how ???
# 3. make a label->index dict
# 4. init label x label matrix
# 5. for each y, increase count in matrix

def confusion_multiclass(y_true,y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("mismatched N")
        
        # !!!! what does this do? and is it efficient? 
        labels = sorted(set(y_true) | set(y_pred))
        label_to_index = {label: i for i,label in enumerate(labels)}
        k = len(labels)
        
        # init k x k matrix
        matrix = [[0]*k for _ in range(k)]
        
        for yt, yp in zip(y_true,y_pred):
            i = label_to_index[yt]
            j = label_to_index[yp]
            
            matrix[i][j] += 1
            
    return matrix, labels


# TP = diagonal
# FP = sum of column c except diagonal
# FN = sum of row c except diagonal
# TN = everything else

def multiclass_metrix(matrix):
    k = len(matrix)
    results = []
    
    for c in range(k):
        tp = matrix[c][c]
        
        # !!!! why not slice?
        fp = sum(matrix[r][c] for r in range(k) if r!=c)
        fn = sum(matrix[c][j] for j in range(k) if j!=c)
        tn = sum(matrix[r][j]
                 for r in range(k)
                 for j in range(k)
                 if r != c and j != c)
        
        precision = tp / (tp+fp) if (tp+fp) else 0
        recall = tp / (tp+fn) if (tp+fn) else 0
        f1 = (2*precision*recall / (precision+recall) 
              if (precision+recall) else 0)
        
        results.append({"class":c,
                        "precision":precision,
                        "recall":recall,
                        "f1":f1})


    return results


#%% Micro vs Macro averaging
# macro average: compute metric for each class, then average
# MacroPrecision = 1/K SUM Precision_{c}

# micro average: aggregate tp,fp,fn across all classes first, then compute
# MicroPrecision = SUM tp / [SUM tp + SUM fp]
# this weights by class frequency


# 0. give me some example inputs & outputs for binary classification (the function that does everything)
# and for multiclass classification
# 1. What is hashable? E.g. "Assuming labels are integers: 0 ... K-1  or at least hashable"?
# 2. Thresholding probabilities / Give you y_true and predicted probabilities
# 3. Macro vs micro averaging
# 4. how would this implementation for multiclass confusion matrix change if you could use numpy or utilities such as itertools or collections? 
# 5. how do I know what is row and what is column? 
#