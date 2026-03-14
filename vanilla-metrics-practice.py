#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 15:41:51 2026

@author: qq20468
"""

import math
import numpy as np
#%% mu, var, stable_var  

# sigsq = 1/n    * SUM (x-mu)^2
#       = SUM (x-mu)^2 / n
# ssq = 1/(n-1)  * SUM (x-mu)^2    # sample var 
# stddev = sqrt (sigsq)
# stddev = sqrt (ssq)           # sample std

def mean(xs):
    if not xs:
        raise ValueError("empty list")
        
    return sum(xs) / len(xs)


def variance(xs, sample=False):
    n=len(xs)
    if not xs:
        raise ValueError("empty list")
    if n<2 and sample:
        raise ValueError("need more values for sample var")
        
    mu = mean(xs)    
    sumsq = sum((x - mu)**2 for x in xs)
    
    if sample:
        return sumsq / (n-1)
    else:
        return sumsq / n
    
        
        
# 1. update mean
# m = m + (x-m) / n
# adjustment = delta / new count
# new mean = old mean + adjustment
# 2. update squared deviations
# get new distance
# old distance * new distance
def stable_var(xs, sample=False):
    M2 = 0
    n = 0
    mu = 0
    
    for x in xs:
        n += 1
        delta = x - mu
        mu += delta/n
        delta2 = x - mu
        M2 += delta * delta2
    
    if sample and n<2:
        raise ValueError("need more values")
    
    if sample:
        return M2 / (n-1)
    else:
        return M2/ n





def std(var):
    # std is just square root of variance. 
    # (pop var for pop std and sample var for sample std)
    return math.sqrt(var)
    


xs = [1, 2, 3, 4]
# xs = [1, 2, 3, 0.5, 3, 1]
mean(xs)
sample=True
sample=False
variance(xs, sample)
stable_var(xs, sample)

print(f"mu: {mean(xs)} var: {variance(xs)} Wvar: {stable_var(xs)}")
print(f"mu: {np.mean(xs)} var: {np.var(xs)}")

#%% Covariance
# given paired obs [(x,y) (x,y) (x,y)...]
# cov(X,Y) = 1/n SUM [(xi-MU_x) * (yi-MU_y)]
# sample cov:
# cov(X,Y) = 1/(n-1) SUM [(xi-MU_x) * (yi-MU_y)]
# i.e. variance:            (x-mu)**2
# COvariance=cross variance (x-mu)(y-mu)

# 1. check same length
# 2. check empty list
# 3. check sample variance has n<2



def covariance(xs,ys,sample=False):
    if not len(xs)==len(ys):
        raise ValueError("need same N")
        
    mux = mean(xs)
    muy = mean(ys)
    
    sumdiff = sum((x-mux)*(y-muy) for x,y in zip(xs,ys))
    
    n=len(xs)
    if sample and n<2:
        raise ValueError("need more values")
    
    if sample:
        return sumdiff/(n-1)
    else:
        return sumdiff/n
        
        
def covariance(xs,ys):
    if not xs:
        raise ValueError("empty list")
    n=len(xs)
    if n!=len(ys):
        raise ValueError("need same N")
    
    mux = sum(xs)/n
    muy = sum(ys)/n
    
    sumdiff = sum((x-mux) * (y-muy) for x,y in zip(xs,ys))
    
    if sample:
        cov = sumdiff /(n-1)
    else:
        cov = sumdiff/(n)
        
    return cov

        
# def covxy(xs,ys):
#     # check for len of x
#     mux= mean(xs)
#     muy = mean(ys)
    
    
#     sumdiff = sum((x-mux)*(y-muy) for x,y in zip(xs,ys))
    
    
    
        
# covariance can also be written as expected value:
# cov(X,Y) = E[XY]-E[X]E[Y]
# i.e. cov = mean xy - mean x * mean y
# so there's an alternative implementation that is numerically less stable:
    
def covXY(xs,ys, sample=False):
    n = len(xs)
    assert n==len(ys)
    
    mux = mean(xs)
    muy = mean(ys)
    
    meanxy = sum(x*y for x,y in zip(xs,ys)) / n
    
    return meanxy - (mux * muy)
    
    

    
        
xs = [1,2,3]
ys = [1,2,3]        
covariance(xs, ys)
covXY(xs, ys)
print(covariance(xs, ys))
print(covXY(xs, ys))
        
xs = [1,2,3]
ys = [3,2,1] 
covariance(xs, ys)
print(covariance(xs, ys))
print(covXY(xs, ys))



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

# The n vs n-1 factor cancels out in correlation.
# So sample and pop correlation are the same. 
# YOU CAN LEAVE OUT SAMPLE FROM ALL CORRELATION FUNCTIONS


import math

def corr_short(xs,ys):
    
    varx = variance(xs)
    vary = variance(ys)
    sigx = math.sqrt(varx)
    sigy = math.sqrt(vary)
    
    covxy = covariance(xs, ys)
    
    rho = covxy / (sigx*sigy)
    return rho
    
    



def corr(xs, ys):
    # chech for empty list
    # check for same n in both inputs
    n = len(xs)
    mux = sum(xs)/n
    muy = sum(ys)/n
    
    varx = sum((x-mux)*(x-mux) for x in xs) / n
    vary = sum((y-muy)*(y-muy) for y in ys) / n
    sdx = math.sqrt(varx)
    sdy = math.sqrt(vary)
    
    covxy = sum((x-mux)*(y-muy) for x,y in zip(xs,ys)) / n
    
    rho = covxy / (sdx*sdy)
    
    return rho
    


xs = [1,2,3,4,3]
ys = [1,2,3,4,3]        
        
# xs = [1,2,3,4,3]
# ys = [4,3,2,1,2] 

# xs = [1,2,3,4,3,1,2,3,4,3]
# ys = [4,3,2,1,2,3,3,2,1,2] 

sample=True
sample=False
print(corr(xs,ys))
print(corr_short(xs,ys))
    
    
#%% single pass corr function

# correlation can also be written as:
#               SUM (x-mux)(y-muy)
# rho = ----------------------------------
#       SQRT{ SUM[x-mux]^2 * SUM[y-muy]^2 }

# 1. get dx, dy
# 2. update running sum of xy, xx, yy
# 3. plug xy, xx, yy in eq above

def corr_onepass(xs,ys):
    # check for same n
    # check for min n = 2
    
    xx=0
    yy=0
    xy=0
    
    mux=mean(xs)
    muy=mean(ys)
    
    for x,y in zip(xs,ys):
        dx = x-mux
        dy = y-muy
        
        xx+= dx*dx
        yy+= dy*dy
        xy+= dx*dy
        
    if xx == 0 or yy == 0:
        raise ValueError("zero variance")
        
    rho = xy/ math.sqrt(xx*yy)
    
    return rho


def corr_onepass(xs,ys):
    # check for same n
    # check for min 2 values
    
    n=len(xs)
    mux = sum(xs)/n
    muy = sum(ys)/n
    
    x2=0
    y2=0
    xy=0
    
    # this is just looping through the sum expressions in the equation above one value at a time
    for x,y in zip(xs,ys):
        dx = x-mux
        dy = y-muy
        # xy = 
        x2 += dx*dx
        y2 += dy*dy
        xy += dx*dy
        
    if x2==0 or y2==0:
        raise ValueError("0 variance!")
    
    rho = xy / math.sqrt(x2*y2)
    
    return rho    
    



xs = [1,2,3,4,3]
ys = [1,2,3,4,3]        # 1

# xs = [1,2,3,4,3]
# ys = [4,3,2,1,2] # -1

xs = [1,2,3,4,3,1,2,3,4,3]
ys = [4,3,2,1,2,3,3,2,1,2] # -0.9587

print(corr_onepass(xs,ys))
print(np.corrcoef(xs,ys))


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
 
 

import math

def entropy(xs):
    n = len(xs)
    if n==0:
        return 0.0
    
    # count freq
    counts = {}
    for x in xs:
        counts[x] = counts.get(x,0) + 1
        
    # compute entropy
    h = 0.0
    for x in counts:
        px = counts[x]/n
        h += px * math.log(px)
        
    # OR:
    # for count in counts.values():
    #     p = count / n
    #     h -= p * math.log2(p)
        
    return h



def entropy(xs):   
    # check x isn't empty
    if not xs:
        raise ValueError("empty")
    n=len(xs)
    counts = {}
    
    for x in xs:
        counts[x] = counts.get(x,0) + 1
        
    h = 0
    for x in counts:
        px = counts[x]/n
        h -= px * math.log2(px)
    
    return h
    

X = ['A', 'A', 'B', 'B', 'B', 'C']
X = ['A','A','A','B'] # ~0.81
# X = [1,1,1,1] # 0
# X = [0,1,0,1] # 1.0

entropy(X)
        

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
# -  
# 4. apply formula

def conditional_entropy(x,y):
    assert len(x) ==len(y)
    n=len(x)
    
    joint_counts = {}
    x_counts = {}
    
    # count joint and marginal
    for xi,yi in zip(x,y):
        joint_counts[(xi,yi)] = joint_counts.get((xi,yi),0) + 1
        x_counts[xi] = x_counts.get(xi,0) + 1
        
    h=0
    
    for (xi,yi), count in joint_counts.items():
        pxy = count/n
        pyGivenx = count / x_counts[xi] 
        h -= pxy * math.log2(pyGivenx)
        
    return h
    

def conditional_entropy(x,y):
    

# 1. should I see how you can go from definition to expanded, or is it just a definition?
# 2. intuition about expanded formula?
# 3. what are different ways to compute pxy?
# 4. what are different ways to compute p(y|x)? (formulas)
# 5. give me several example inputs and outputs for testing each of the three functions

# Perfect dependence
X = [0,0,1,1]
Y = [0,0,1,1] # H=0

# Independent
X = [0,0,1,1]
Y = [0,1,0,1] # H=1

# Partial dependence
X = [0,0,1,1]
Y = [0,1,1,1] # H=0.5


#%% Mutual Information
# I(X;Y) = H(X) - H(X|Y)
# or
# I(X;Y) = SUM_{x,y}: p(x,y)*log[p(x,y) / p(x)p(y)]
# How much knowing X reduces uncertainty about Y

def mi(x,y):
    assert len(x)==len(y)
    n = len(x)
    
    jointCounts = {}
    xCounts = {}
    yCounts = {}
    
    for xi,yi in zip(x,y):
        jointCounts[(xi,yi)] = jointCounts.get((xi,yi), 0) + 1
        xCounts = xCounts.get(xi, 0) + 1
        yCounts = yCounts.get(yi, 0) + 1
    
    mi = 0.0
    
    for (xi,yi), jointCount in jointCounts.items():
        pxy = jointCount / n
        px = xCounts[xi] / n
        py = yCounts[yi] / n
        
        divterm = pxy / (px*py)
        mi += pxy * math.log(divterm)

    
    return mi

# Independent
X = [0,0,1,1]
Y = [0,1,0,1] # MI=0

# Perfect Correlation
X = [0,0,1,1]
Y = [0,0,1,1] # MI=1

# Partial
X = [0,0,1,1]
Y = [0,1,1,1] # MI=0.31

# Is there a more efficient way than to loop through all jointcounts? 

# Derive MI using entropy relation 
# Implement a fully vectorized NumPy version
# Discuss numerical stability
# Or connect this to feature selection in ML

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

     


def confusion_matrix_binary(y_true,y_pred):
    tp=tn=fn=fp=0
    
    for real,pred in zip(y_true,y_pred):
        if real==pred==0:
            tn+=1
            
        elif real==pred==1:
            tp+=1
            
        elif real==0 and pred==1:
            fp+=1
            
        elif real==1 and pred==0:
            fn+=1
            
        else:
            raise ValueError("unrecognized value - expected binary inputs")
            
    return tp,fp,fn,tn

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
# 1. get confusion matrix
# 2. get precision, recall and f1
# return all in dict
    
def classification_metrix(y_true, y_pred):
    tp = tn = fp = fn = 0
    
    for yt, yp in zip(y_true, y_pred):
        if yt == 1 and yp == 1:
            tp += 1
        elif yt == 0 and yp == 0:
            tn += 1
        elif yt == 0 and yp == 1:
            fp += 1
        elif yt == 1 and yp == 0:
            fn += 1
        else:
            raise ValueError("Labels must be 0 or 1")
    
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = (2 * precision * recall / (precision + recall)
          if (precision + recall) else 0.0)
    
    return {
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "tn": tn,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }
        
    
    
def classification_metrix(y_true,y_pred):  
    tp=tn=fp=fn=0
    
    for yt,yp in zip(y_true,y_pred):
        if yt==yp==1:
            tp+=1
        elif yt==yp==0:
            tn+=1
        elif yt==0 and yp==1:
            fp+=1
        elif yt==1 and yp==0:
            fn+=1
            
        else:
            raise ValueError("exp binary values!")
            
    precision = tp / (tp+fp) if (tp+fp) else 0
    recall = tp / (tp+fn) if (tp+fn) else 0
    f1 = (2*precision*recall) / (precision+recall) if (precision+recall) else 0
    
    result={
        'tp':tp,
        'tn':tn,
        'fp':fp,
        'fn':fn,
        'precision':precision,
        'recall':recall,
        'f1':f1
     }
    
    return result


y_true = [1,0,1,1,0,0,1]
y_pred = [1,0,1,0,0,1,1]
classification_metrix(y_true, y_pred)


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

# 1) check that lengths match
# 2. get sorted unique labels (union of pred and true)
# 3. make a label->index dict (if labels aren't ordered ints, matrix indexing won't work)
# 4. init label x label matrix
# 5. for each y, increase count in matrix
    
    
    
def confusion_multiclass(y_true,y_pred):
    n = len(y_true)
    if len(y_pred)!=n:
        raise ValueError("need same length")
    labels = sorted(set(y_true) | set(y_pred))
    k = len(labels)
    label_index = {label:i for i,label in enumerate(labels)}    
    
    mat = [[0]*k for i in range(k)]
    
    for t,p in zip(y_true,y_pred):
        i = label_index(t)
        j = label_index(p)
        mat[i][j] += 1
        
    return mat, labels    
    


def confusion_multiclass(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("Lengths must match")
    # Pipe op is union of the sets - or think of it as OR, i.e. if element is in a or b then add to collection
    labels = sorted(set(y_true) | set(y_pred))
    label_to_index = {label: i for i, label in enumerate(labels)}
    k = len(labels)
    # initialize k x k matrix
    matrix = [[0]*k for _ in range(k)]
    for yt, yp in zip(y_true, y_pred):
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


# 1. init results
# 2. loop through 
# 3. get tp,fp etc. for that class
# 4. calc metrics for that class
# 5. append class metrics to results

def multiclass_metrix(mat):
    res=[]
    
    k=len(mat)
    
    # alt: sum everything, then subtract mat[c,c] to get true negative instead of looping
    alls = sum(mat[i][j]
               for i in range(k)
               for j in range(k))
    
    for c in range(k):
        tp = mat[c][c]
        
        # fp is when predicted 0 but true was something else
        # mat: [[5, 1, 0], [2, 6, 1], [0, 1, 4]], where each list is true vals, # so mat[true][pred] 
        # mat[0][1] : true 0 pred 1, mat[0][2] : true 0 pred 2, 
        # fn is when predicted else but true was 0
        # mat[1][0]
        fp = sum(mat[j][c] for j in range(k) if j!=c)
        fn = sum(mat[c][j] for j in range(k) if j!=c)
        
        # fn is everything apart from tp,fp,fn
        # tn = sum(mat[i][j]
        #          for i in range(k)
        #          for j in range(k)
        #          if i!=c and j!=c)
        tn = alls-(mat[c][c]+fp+fn)
        
        precision = tp / (tp+fp) if (tp+fp) else 0
        recall = tp / (tp+fn) if (tp+fn) else 0
        f1 = (2*precision*recall) / (precision+recall) if (precision+recall) else 0
        
        cr = {
            'class':c,
            'precision':precision,
            'recall':recall,
            'f1':f1
            }
        res.append(cr)
    
    return res
#           Pred
# | True | | 0 | 1 | 2 |
# | ------ | - | - | - |
# | 0      | 5 | 1 | 0 |
# | 1      | 2 | 6 | 1 |
# | 2      | 0 | 1 | 4 |

# y_true = [0, 0, 0, 0, 0, 0, 1,1,1,1,1,1,1,1,1, 2,2,2,2,2,]
# y_pred = [0, 0, 0, 0, 0, 1, 0,0,1,1,1,1,1,1,1, 1,0,1,1,1,]
# labels = sorted(set(y_true) | set(y_pred))

y_true = [0,0,0,0,0,0, 1,1, 1,1,1,1,1,1, 1, 2,2,2,2,2,]
y_pred = [0,0,0,0,0,1, 0,0, 1,1,1,1,1,1, 2, 1,2,2,2,2,]
labels = sorted(set(y_true) | set(y_pred))
k = len(labels)
label_index = {label:i for i,label in enumerate(labels)}  # enumerate goes from 0 so this works!!!

mat, classes = confusion_multiclass(y_true, y_pred)
print(mat)
multiclass_metrix(mat)


