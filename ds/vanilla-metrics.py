#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 15:41:51 2026

@author: qq20468
"""

#%% mean, variance
import math


def mean(xs): 
    if len(xs) == 0:
        raise ValueError("empty list")
        
    total = 0.0
    for x in xs:
        total += x
        
    return total / len(xs)

# alternative

def mean(xs):
    if not xs:
        raise ValueError("empty list")
        
    return sum(xs) / len(xs)



def variance(xs, sample=False):
    n = len(xs)
    if n == 0:
        raise ValueError("empty list")
    if sample and n<2:
        raise ValueError("sample variance needs min n of 2")
        
    mu = mean(xs)
    
    # total=0
    # for x in xs:
    #     diff = (x - mu)
    #     total += diff * diff
        
    # same time complexity, more space
    # total = sum([(x-mu)**2 for x in xs])
    
    # generator expression, avoids extra space, but still pythonic
    total = sum((x - mu)**2 for x in xs)
    
    if sample:
        return total / (n-1) 
    else:
        return total / n


# numerically stable
def variance_welford(xs, sample=False):
    n = 0.
    mean = 0.
    M2 = 0.
    
    for x in xs:
        n+=1
        delta = x-mean
        mean += delta/n
        delta2 = x-mean
        M2 += delta * delta2
        
    if n<1:
        raise ValueError("empty lust")
    if sample:
        if n<2:
            raise ValueError("sample variance needs at least 2 samples")
        return M2/ (n-1)
    else:
        return M2 / n
        
    
def std(var):
    # std is just square root of variance. 
    # (pop var for pop std and sample var for sample std)
    return math.sqrt(var)
    
xs = [1, 2, 3, 4]

mean(xs)
sample=True
# sample=False
variance(xs, sample)
variance_welford(xs, sample)


#%% mu, var, stable_var  - my version

# sigsq = 1/n SUM (x-mu)^2
# ssq = 1/(n-1) SUM (x-mu)^2    # sample var
# stddev = sqrt (sigsq)
# stddev = sqrt (ssq)           # sample std

def mean(xs):
    if not xs:
        raise ValueError("empty list")
        
    return sum(xs) / len(xs)

def variance(xs, sample=False):
    n = len(xs)
    if not xs:
        raise ValueError("empty list")
    if sample and n<2:
        raise ValueError("sample var needs min 2 values")
        
    mu = mean(xs)
    
    tot = sum((x - mu)**2 for x in xs)
    
    if sample:
        return tot / (n-1)
    else:
        return tot / n
    
def stable_var(xs, sample=False):
    n = len(xs)
    if not xs:
        raise ValueError("empty list")
    if sample and n<2:
        raise ValueError("sample var needs min 2 values")
        
    mean = 0.
    n = 0.
    M2 = 0.

    for x in xs:
        n += 1
        delta = x-mean
        mean += delta/n
        delta2 = x-mean
        M2 += delta * delta2
    
    
    if sample:
        return M2 / (n-1)
    else:
        return M2 / n
    
    
mean(xs)
sample=True
# sample=False
variance(xs, sample)
stable_var(xs, sample)


#%% Stable Var - optional plot
# sigsq = 1/n SUM (x-mu)^2
# ssq = 1/(n-1) SUM (x-mu)^2    # sample var
# stddev = sqrt (sigsq)
# stddev = sqrt (ssq)           # sample std

    
def stable_var_plus(xs, sample=False):
    n = len(xs)
    # check if empty list
    # check if sample and n<2
    
    M2=0.
    mean=0.
    n=0.
    res = [[] for i in range(5)]#[0]*5
    
    for x in xs:
        # increase counter
        # get diff from running mean
        # update running mean: m = diff/n
        # get second diff from updated mean
        # get running variance from the two diffs
        n+=1 
        delta=x-mean
        mean=delta/n
        delta2=x-mean
        M2 = delta * delta2
        
        res[0].append(n)
        res[1].append(delta)
        res[2].append(mean)
        res[3].append(delta2)
        res[4].append(M2)
    
    if sample:
        return M2/(n-1), res
    else:
        return M2/n, res
    
mean(xs)
sample=True
# sample=False
variance(xs, sample)
stable_var_plus(xs, sample)

xs = [1, 2, 3, 0.5, 3, 1]
ve,res = stable_var_plus(xs, sample)

# from matplotlib import pyplot as plt
# fig,axs = plt.subplots(4,1)

# axs.flat[0].plot(res[1])
# axs.flat[1].plot(res[2])
# axs.flat[2].plot(res[3])
# axs.flat[3].plot(res[4])

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
    if len(xs)!=len(ys):
        raise ValueError("needs same n for both vars")
    
    if not xs or not ys:
        raise ValueError("empty")
    if sample and len(xs)<2:
        raise ValueError("need min 2 values")
        
    mux = mean(xs)
    muy = mean(ys)
    n=len(xs)
    
    total=0.
    
    for x,y in zip(xs,ys):
        total+= (x-mux) * (y-muy)

    if sample:
        return total/ (n-1)
    else:
        return total/ n
        
        
    
        
# covariance can also be written as expected value:
# cov(X,Y) = E[XY]-E[X]E[Y]
# i.e. cov = mean xy - mean x * mean y
# so there's an alternative implementation that is numerically less stable:
    
def covXY(xs,ys, sample=False):
    n=len(xs)
    
    assert n==len(ys)
    
    mux = mean(xs)
    muy = mean(ys)
    
    mean_xy = sum(x*y for x,y in zip(xs,ys)) / n
   
    cov = mean_xy - mux * muy
    
    if sample:
        return cov * n / (n-1)
    return cov
    
        
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

def corr_short(xs,ys, sample=False):
    assert len(xs)==len(ys)
    
    n=len(xs)
    if n==0:
        raise ValueError("empty")
    if sample and n<2:
        raise ValueError("need more n")
    
    cov=covariance(xs,ys,sample)
    varx = stable_var(xs, sample)
    vary = stable_var(ys, sample)
    
    sdx = math.sqrt(varx)
    sdy = math.sqrt(vary)
    
    if sdx==0 or sdy==0:
        raise ValueError("corr needs sd!=0")
    
    rho = cov / (sdx * sdy)
    
    return rho



def corr(xs, ys, sample=False):
    if len(xs)!=len(ys):
        raise ValueError("need same n")
        
    n=len(xs)
    if n==0:
        raise ValueError("empty")
    if sample and n<2:
        raise ValueError("need more n")
        
    mux,muy = mean(xs), mean(ys)
    total = sum((x-mux)*(y-muy) for x,y in zip(xs,ys))
    if sample:
        cov = total / (n-1)
    else:
        cov = total / n
        
    
    totx = sum((x-mux)**2 for x in xs) 
    toty = sum((y-muy)**2 for y in ys) 
    
    div = (n-1) if sample else n
    varx = totx / div
    vary = toty / div
    sdx = math.sqrt(varx)
    sdy = math.sqrt(vary)
    
    if sdx==0 or sdy==0:
        raise ValueError("corr needs sd!=0")
    
    rho = cov / (sdx * sdy)
    
    return rho

xs = [1,2,3,4,3]
ys = [1,2,3,4,3]        
        
# xs = [1,2,3,4,3]
# ys = [4,3,2,1,2] 

xs = [1,2,3,4,3,1,2,3,4,3]
ys = [4,3,2,1,2,3,3,2,1,2] 

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
# 2. update xy, xx, yy
# 3. plug xy, xx, yy in eq above

def corr_onepass(xs,ys):
    if len(xs)!=len(ys):
        raise ValueError("need same N")
        
    n=len(xs)
    if n<2:
        raise ValueError("need min 2 samples")
        
    mux,muy = mean(xs), mean(ys)
    
    sumXY=0.
    sumX2=0.
    sumY2=0.
    
    for x,y in zip(xs,ys):
        dx = x-mux
        dy = y-muy
        
        sumXY += dx * dy
        sumX2 += dx * dx
        sumY2 += dy * dy
        
    if sumX2 == 0 or sumY2 == 0:
        raise ValueError("zero variance")
    
    
    return sumXY / math.sqrt(sumX2 * sumY2)



xs = [1,2,3,4,3]
ys = [1,2,3,4,3]        

xs = [1,2,3,4,3]
ys = [4,3,2,1,2] 

xs = [1,2,3,4,3,1,2,3,4,3]
ys = [4,3,2,1,2,3,3,2,1,2] 

print(corr_onepass(xs,ys))


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




        


X = ['A', 'A', 'B', 'B', 'B', 'C']
X = ['A','A','A','B'] # ~0.81
X = [1,1,1,1] # 0
X = [0,1,0,1] # 1.0

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

# If knowing X makes Y completely predictable:
# p(y|x)=1
# log(1)=0
# entropy = 0
# If knowing X gives no information:
# p(y|x)=p(y)
# conditional entropy = entropy of Y


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
    
# Perfect dependence
X = [0,0,1,1]
Y = [0,0,1,1] # H=0

# Independent
X = [0,0,1,1]
Y = [0,1,0,1] # H=1

# Partial dependence
X = [0,0,1,1]
Y = [0,1,1,1] # H=0.5

conditional_entropy(X,Y)


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


mi(X,Y)
# Is there a more efficient way than to loop through all jointcounts? 

# Derive MI using entropy relation 
# Implement a fully vectorized NumPy version
# Discuss numerical stability
# Or connect this to feature selection in ML
#%% Entropy Vectorized 
import numpy as np

def entropynp(x):
    x = np.asarray(x)
    n = len(x)
    if n == 0:
        return 0.0
    
    _,counts = np.unique(x, return_counts=True)
    p = counts/n

    return -np.sum(p * np.log2(p))

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


# this works for integer labels, but needs a mapping otherwise!!!
def confusion_multiclass(y_true,y_pred):
    n = len(y_true)
    if len(y_pred)!=n:
        raise ValueError("need same length")
        
    labels = sorted(set(y_true) | set(y_pred))
    k = len(labels)
    
    mat = [[0]*k for i in range(k)]
    
    for t,p in zip(y_true,y_pred):
        mat[t][p] += 1
        
    return mat, labels
        



def confusion_multiclass(y_true,y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("mismatched N")
        
    # !!!! what does this do? and is it efficient? 
    # | is union of the sets - or think of it as OR, i.e. if element is in a or b then add to collection
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



def confusion_multiclass(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("Lengths must match")

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

# 1. init results
# 2. loop through 
# 3. get tp,fp etc. for that class
# 4. calc metrics for that class
# 5. append class metrics to results

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



# | True \ Pred | 0 | 1 | 2 |
# | ----------- | - | - | - |
# | 0           | 5 | 1 | 0 |
# | 1           | 2 | 6 | 1 |
# | 2           | 0 | 1 | 4 |

# y_true = [0, 0, 0, 0, 0, 0, 1,1,1,1,1,1,1,1,1, 2,2,2,2,2,]
# y_pred = [0, 0, 0, 0, 0, 1, 0,0,1,1,1,1,1,1,1, 1,0,1,1,1,]
# labels = sorted(set(y_true) | set(y_pred))

y_true = [0, 0, 0, 0, 0, 0, 1,1,1,1,1,1,1,1,1, 2,2,2,2,2,]
y_pred = [0, 0, 0, 0, 0, 1, 0,0,1,1,1,1,1,1,2, 1,2,2,2,2,]
labels = sorted(set(y_true) | set(y_pred))
k = len(labels)
label_index = {label:i for i,label in enumerate(labels)}  # enumerate goes from 0 so this works!!!

mat, classes = confusion_multiclass(y_true, y_pred)
print(mat)
multiclass_metrix(mat)

#%% Micro vs Macro averaging
# macro average: compute metric for each class, then average
# MacroPrecision = 1/K SUM Precision_{c}
# Every class counts the same — even rare ones.
# So if one class is rare but performs poorly, macro-F1 drops significantly.

# micro average: aggregate tp,fp,fn across all classes first, then compute
# MicroPrecision = SUM tp / [SUM tp + SUM fp]
# this weights by class frequency: classes with more samples contribute more to the metric

# In single-label multi-class classification, micro-F1 equals accuracy.


def micro_macro_metrics(matrix):
    k = len(matrix)
    
    # macro metrics:
    per_class = multiclass_metrix(matrix)
    macro_f1 = sum(c['f1'] for c in per_class) / k
    macro_precision = sum(c['precision'] for c in per_class) / k
    macro_recall = sum(c['recall'] for c in per_class) / k
    
    # micro metrics:
    tpagg = 0
    fpagg = 0
    fnagg = 0
    
    for c in range(k):
        tpagg += matrix[c][c]
        # fp: predicted 0, label something else
        fpagg += sum(matrix[j][c] for j in range(k) if j!=c)
        fnagg += sum(matrix[c][j] for j in range(k) if j!=c)
        
    micro_precision = tpagg / (tpagg+fpagg) if (tpagg+fpagg) else 0
    micro_recall = tpagg / (tpagg+fnagg) if (tpagg+fnagg) else 0
    micro_f1 = ( 2*micro_precision*micro_recall /
                (micro_precision+micro_recall)
                if (micro_precision+micro_recall) else 0)
    macros = [macro_f1, macro_precision, macro_recall]
    micros = [micro_f1, micro_precision, micro_recall]
    
    return macros, micros



def micro_macro_f1(matrix):
    k = len(matrix)

    # per-class metrics
    per_class = multiclass_metrix(matrix)

    # macro F1
    macro_f1 = sum(d["f1"] for d in per_class) / k
    macro_precision = sum(c['precision'] for c in per_class) / k
    macro_recall = sum(c['recall'] for c in per_class) / k

    # micro counts
    total_tp = sum(matrix[c][c] for c in range(k))
    total_fp = sum(
        matrix[r][c]
        for c in range(k)
        for r in range(k)
        if r != c
    )
    total_fn = sum(
        matrix[c][j]
        for c in range(k)
        for j in range(k)
        if j != c
    )

    micro_precision = total_tp / (total_tp + total_fp) if (total_tp + total_fp) else 0.0
    micro_recall = total_tp / (total_tp + total_fn) if (total_tp + total_fn) else 0.0

    micro_f1 = (2 * micro_precision * micro_recall /
                (micro_precision + micro_recall)
                if (micro_precision + micro_recall) else 0.0)

    macros = [macro_f1, macro_precision, macro_recall]
    micros = [micro_f1, micro_precision, micro_recall]
    
    return macros, micros


micro_macro_metrics(mat)


y_true = [0,1,2,0,1,2,0,1,2]
y_pred = [0,2,1,0,0,2,1,1,2]

matrix, labels = confusion_multiclass(y_true, y_pred)
print(matrix)
# print(multiclass_metrix(matrix))
print(micro_macro_f1(matrix))

print(micro_macro_metrics(matrix))



#%% If given probabilities and thresholds:
# given y_true (0/1 labels)
# and y_prob (predicted probabilities for class 1)
    

# Ok, I've now gone through almost all of the data science metrics you listed and their basic, non-vectorized implementations in separate branches of this chat.

# Before I go further into detail for some of these (like gradient descent and linear regression), or start on the vectorized numpy implementations, I need help going through some basic background knowledge.

# 2. AUC / INTEGRATION / DIFFERENTIATION in the previous test I took, the last problem was related to AUC i think? I was supposed to use an (I think) integration method with a name, but I have only done some basic summation of tiny rectangle slice summation in my maths practice, not in code.
# 1. Linear algebra & numpy
# I've refreshed some matrix & vector basics, can you quiz me on whether matrices and vectors can be multiplied/dot producted, whether their shapes are compatible, as well as their numpy implementations?


# !!!!
# 0. give me some example inputs & outputs for binary classification (the function that does everything)
# and for multiclass classification
# 1. What is hashable? E.g. "Assuming labels are integers: 0 ... K-1  or at least hashable"?
# 2. Thresholding probabilities / Give you y_true and predicted probabilities
# 4. how would this implementation for multiclass confusion matrix change if you could use numpy or utilities such as itertools or collections? 
# 5. how do I know what is row and what is column? 
#

#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#%% Gradient descent
# Gradient points in the direction of STEEPEST INCREASE
# Gradient descent = move parameters in the direction that reduces loss
# P = P - lr* G_p L(P)
# where P:  parameters
#       lr: learning rate
#       G_p L(P): gradient of the loss w.r.t. parameters
#       
# 1. assume simplest case (linear regression with 1 parameter)
# y^ = wx+b
# MSE Loss:
# L = 1/n *  SUM_I[yi-(w*xi + b)]**2
# 2. compute gradients by computing partial derivatives

def gradient_step(x,y,w,b,lr):
    n = len(y)
    
    errs = 0
    dw=0
    db=0
    for i in range(n):
        yhat = w*x[i] + b
        err = (y[i]-yhat)
        errs = errs+(err*err)
        
        dw += x[i] * err
        db += err
        
    loss = errs/n
    dw = (-2/n)* dw
    db = (-2/n)* db
    
    w -= lr*dw
    b -= lr*db
    
    return w,b
 

def gradient_step(x,y,w,b,lr):
    n = len(x)
    
    dw = 0
    db = 0
    
    for i in range(n):
        y_hat = w * x[i] + b
        error = y[i] - y_hat
         
        dw += -2 * x[i]*error
        db += -2 * error
        
    dw /= n
    db /= n
    
    w = w-lr*dw
    b = b-lr*db
    
    return w,b


# e.g. 
x = [1,2]
y = [2,4]
w = 0
b = 0
# Predictions:
[0, 0]
# Errors:
[2, 4]

lr=0.05

gradient_step(x, y, w, b, lr)


#%%
def gradient_step_your(x,y,w,b,lr):
    n = len(y)
    errs = 0.0
    dw_acc=0.0
    db_acc=0.0
    for i in range(n):
        yhat = w*x[i] + b
        err = (y[i]-yhat)
        errs += (err*err)
        dw_acc += x[i] * err
        db_acc += err
    loss = errs/n
    dw = (-2.0/n) * dw_acc
    db = (-2.0/n) * db_acc
    w_new = w - lr*dw
    b_new = b - lr*db
    print("your: loss, dw_acc, db_acc, dw, db:", loss, dw_acc, db_acc, dw, db)
    return w_new, b_new

def gradient_step_other(x,y,w,b,lr):
    n = len(x)
    dw=0.0
    db=0.0
    errs=0.0
    for i in range(n):
        yhat = w*x[i] + b
        error = y[i] - yhat
        errs += error*error
        dw += -2.0 * x[i] * error
        db += -2.0 * error
    dw /= n
    db /= n
    loss = errs/n
    w_new = w - lr*dw
    b_new = b - lr*db
    print("other: loss, dw_acc_equiv, db_acc_equiv, dw, db:", loss, -n/2.0 * dw, -n/2.0 * db, dw, db)
    return w_new, b_new

# Example quick test:
x = [1.0, 2.0, 3.0]
y = [2.0, 4.0, 6.0]
print(gradient_step_your(x,y,0.0,0.0,0.1))
print(gradient_step_other(x,y,0.0,0.0,0.1))


#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#########################################################
#%% Linear regression from formula 
# given data:
# (x1,y1), (x2,y2), ... 
# we need:
# yhat = wx + b
# that minimizes MSE:
# 1/n SUM[y - (wx + b)]**2  over all xi yi 

# solution:
# w = COV[x,y] / Var(x)
# b = muy - w*mux

# CLOSED FORM SOLUTION ONLY EXISTS IF WE USE MSE
# 


def linreg_closed(xs,ys):
    n=len(xs)
    if len(ys)!=n:
        raise ValueError("need same n")
        
    mux=sum(xs)/n
    muy=sum(ys)/n
    
    covxi=0
    varx=0
    for xi,yi in zip(xs,ys):
        covxi += (xi-mux)*(yi-muy)
        varx += (xi-mux)*(xi-mux)
        
    covxi /= n
    varx /= n
    
    w = covxi / varx if varx else 0
    b = muy - w*mux
    
    return w,b
        


def linear_regression(xs,ys):
    n=len(xs)
    if n==0 or n!=len(ys):
        raise ValueError("bad input")
        
    # means 
    y_mean = sum(ys)/n
    x_mean = sum(xs)/n
    
    cov=0
    var=0
    
    for x,y in zip(xs,ys):
        dx = x-x_mean
        cov += dx*(y-y_mean)
        var+= dx*dx
        
    if var==0:
        raise ValueError("no")
        
    w=cov/var
    b=y_mean-w*x_mean
    
    return w,b
    
    
xs = [1, 2, 3, 4]
ys = [2, 4, 6, 8]
    
print(linear_regression(xs, ys))
print(linreg_closed(xs, ys))


# Why would you need to use pseudoinverse?
# If XᵀX is not invertible.
# That happens when:
# Features are linearly dependent
# Or rank < p

#%% Expected value
# Mean → average of observed data
# Expected value → theoretical average of a random variable

x = [2, 2, 4, 6]
mean = (2 + 2 + 4 + 6) / 4 # = 3.5

# if RV X takes values:
# X = {1 with p=0.2, 5 with p=0.8}


ex = (2*0.5) + (4*0.25) + (6*0.25) # = 3.5 

# you said 
# If probabilities are uniform (p=1/n), they are identical.
# do you mean the mathematical expressions 
# or that E is the same as mean only if probabilities are uniform? 

# XTX has variance on the diagonal, 
# which I guess is useful because linear regression formula needs variance, 
# but what does the inverse do and why do we then multiply by XT?

#%% Mean, covariance, variance, sd from a probability distribution 
"""
COV(X,Y) = E[XY] - E[X]E[Y]
E[X] = SUM(x_i * p_i)
E[Y] = SUM(y_i * p_i)
E[XY] = SUM(x_i * y_i * p_i)
"""
X = [0, 0, 1, 1]
Y = [1, 2, 1, 2]
P = [0.3, 0.25, 0.15, 0.3]

eX = 0*0.3 + 0*0.25 + 0.15*1 + 0.3*1
eY = 1*0.3 + 2*0.25 + 0.15*1 + 0.3*2

eXY = 0*1*0.3 + 0*2*0.25 + 1*1*0.25 + 1*2*0.3
covXY = eXY - eX*eY


# Variance
# Var(X) = E(X**2) - (E[X])**2
# because variance is 
# Var(x) = E[(x-mux)^2] ; (more like the standard variance formula)
# expanding the square:
# Var(x) = E[x^2 - 2x*mux + mux^2]
# but:
    # - mux = E[x]
    # - E[x] is linear, meaning:
    # E[aA + bB + c] = aE[A] + bE[B] + c   for constants a,b,c
# therefore:
# Var[x] = E[x^2] - (E[x])^2

# or
# Var(X) = Cov(X,X)
# because plugged in the covariance equation:
# Cov(X,X) = E[XX] - E[X]E[X]
#          = E[X*X] - E[X]E[X] 

eX2 = [(x*x)*p for x,p in zip(X,P)]
varx = eX2 - (eX)**2











#%%

# Ok, I've now gone through almost all of the data science metrics you listed and their basic, non-vectorized implementations in separate branches of this chat. 

# Before I go further into detail for some of these (like gradient descent and linear regression), or start on the vectorized numpy implementations, I need help going through some basic background knowledge.

# Here's a list of things I need some help with:

# I also don't know which axis indicates rows or columns (or what dimensions each axis corresponds to) in numpy, so I always need to check what e.g. np.mean(arr, axis=0) shape is 
# Masking/slicing basics would also be useful to know (or whatever you think might be most useful for my end goal here)

