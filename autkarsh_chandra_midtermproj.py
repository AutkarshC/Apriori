#!/usr/bin/env python
# coding: utf-8

# Importing libraries

# In[1]:


import pandas as pd
import itertools
from itertools import combinations
from itertools import chain


# Importing dataset

# In[2]:


df = pd.read_csv("/Users/utkarshchandra/Downloads/DM/amzn.csv",header=None)


# In[3]:


df.head()


# Calculating a list of all the records

# In[4]:


records = []
for i in range(0, len(df)):
    records.append([str(df.values[i,j]) for j in range(0, len(df.columns))])
print('The list of all records are:')
print('=============================================================================================================')
print('')
print(records)


# Removing nan values from the list of records

# In[5]:


items = sorted([item for sublist in records for item in sublist if item != 'nan'])


# Taking minimum support and confidence from user

# In[6]:


minSupport=float(input('Enter the minimum support, enter interger values between 1 to 100: '))
print('')
if minSupport < 1 or minSupport > 100:
    print('Error, Please re-enter integer values between 1 to 100')
else:
    minSupport = (minSupport / 100) * len(df)


# In[7]:


minConfidence=float(input('Enter the minimum confidence interval, enter interger values between 1 to 100: '))
print('')
if minConfidence < 1 or minConfidence > 100:
    print('Error, Please re-enter integer values between 1 to 100')
else:
    minConfidence = minConfidence / 100


# In[8]:


def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)


# In[9]:


def check_subset_frequency(itemset, l, n):
    if n>1:    
        subsets = list(itertools.combinations(itemset, n))
    else:
        subsets = itemset
    for iter1 in subsets:
        if not iter1 in l:
            return False
    return True


# Calculation of support greater than minimum support for C1

# In[10]:


def iteration_1(items, minimum_support_count):
    c1 = {i:items.count(i) for i in items}
    l1 = {}
    for key, value in c1.items():
        if value >= minimum_support_count:
            l1[key] = value 
    
    return c1, l1
c1, l1 = iteration_1(items, minSupport)


# Calculation of support for 2nd iteration with support greater than minimum support C2

# In[11]:


def iteration_2(l1, records, minimum_support_count):
    l1 = sorted(list(l1.keys()))
    L1 = list(itertools.combinations(l1, 2))
    c2 = {}
    l2 = {}
    for iter1 in L1:
        count = 0
        for iter2 in records:

            if sublist(iter1, iter2):
                count+=1
        c2[iter1] = count
    for key, value in c2.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l1, 1):
                l2[key] = value 
    
    return c2, l2
c2, l2 = iteration_2(l1, records, minSupport)


# Calculation of support for 3rd iteration with support greater than minimum support C3

# In[12]:


def iteration_3(l2, records, minimum_support_count):
    l2 = list(l2.keys())
    L2 = sorted(list(set([item for t in l2 for item in t])))
    L2 = list(itertools.combinations(L2, 3))
    c3 = {}
    l3 = {}
    for iter1 in L2:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count+=1
        c3[iter1] = count
    for key, value in c3.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l2, 2):
                l3[key] = value 
        
    return c3, l3
c3, l3 = iteration_3(l2, records, minSupport)


# Calculation of support for 4th iteration with support greater than minimum support C4

# In[13]:


def iteration_4(l3, records, minimum_support_count):
    l3 = list(l3.keys())
    L3 = sorted(list(set([item for t in l3 for item in t])))
    L3 = list(itertools.combinations(L3, 4))
    c4 = {}
    l4 = {}
    for iter1 in L3:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count+=1
        c4[iter1] = count
    for key, value in c4.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l3, 3):
                l4[key] = value 
        
    return c4, l4
c4, l4 = iteration_4(l3, records, minSupport)


# Calculation of support for 5th iteration with support greater than minimum support C5

# In[14]:


def iteration_5(l4, records, minimum_support_count):
    l4 = list(l4.keys())
    L4 = sorted(list(set([item for t in l4 for item in t])))
    L4 = list(itertools.combinations(L4, 5))
    c5 = {}
    l5 = {}
    for iter1 in L4:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count+=1
        c5[iter1] = count
    for key, value in c5.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l4, 4):
                l5[key] = value 
        
    return c5, l5
c5, l5 = iteration_5(l4, records, minSupport)


# Calculation of support for 6th iteration with support greater than minimum support C6

# In[15]:


def iteration_6(l5, records, minimum_support_count):
    l5 = list(l5.keys())
    L5 = sorted(list(set([item for t in l5 for item in t])))
    L5 = list(itertools.combinations(L5, 6))
    c6 = {}
    l6 = {}
    for iter1 in L5:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count+=1
        c6[iter1] = count
    for key, value in c6.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l5, 5):
                l6[key] = value 
        
    return c6, l6
c6, l6 = iteration_6(l5, records, minSupport)


# Calculation of support for 7th iteration with support greater than minimum support C7

# In[16]:


def iteration_7(l6, records, minimum_support_count):
    l6 = list(l6.keys())
    L6 = sorted(list(set([item for t in l6 for item in t])))
    L6 = list(itertools.combinations(L6, 7))
    c7 = {}
    l7 = {}
    for iter1 in L6:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count+=1
        c7[iter1] = count
    for key, value in c7.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l6, 6):
                l7[key] = value 
        
    return c7, l7
c7, l7 = iteration_7(l6, records, minSupport)


# Calculation of support for 8th iteration with support greater than minimum support C8

# In[17]:


def iteration_8(l7, records, minimum_support_count):
    l7 = list(l7.keys())
    L7 = sorted(list(set([item for t in l7 for item in t])))
    L7 = list(itertools.combinations(L7, 8))
    c8 = {}
    l8 = {}
    for iter1 in L7:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count+=1
        c8[iter1] = count
    for key, value in c8.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l7, 7):
                l8[key] = value 
        
    return c8, l8
c8, l8 = iteration_8(l7, records, minSupport)


# Calculation of support for 9th iteration with support greater than minimum support C9

# In[18]:


def iteration_9(l8, records, minimum_support_count):
    l8 = list(l8.keys())
    L8 = sorted(list(set([item for t in l8 for item in t])))
    L8 = list(itertools.combinations(L8, 9))
    c9 = {}
    l9 = {}
    for iter1 in L8:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count+=1
        c9[iter1] = count
    for key, value in c9.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l8, 8):
                l9[key] = value 
        
    return c9, l9
c9, l9 = iteration_9(l8, records, minSupport)


# All support items

# In[19]:


itemlist = {**l1, **l2, **l3, **l4, **l5, **l6, **l7, **l8, **l9}


# In[20]:


print('Support is given as:')
print('===========================================================================================================')
itemlist


# In[21]:


a2 = list(l2.keys())
a3 = list(l3.keys())
a4 = list(l4.keys())
a5 = list(l5.keys())
a6 = list(l6.keys())
a7 = list(l7.keys())
a8 = list(l8.keys())
a9 = list(l9.keys())


# In[22]:


a = [a2, a3, a4, a5, a6, a7, a8, a9]


# In[23]:


def support_count(item):
    item = list(item)
    cnt = 0
    for i in range(len(records)):
        f1 = records[i]
        if set(item).issubset(set(f1)):
            cnt = cnt + 1
    return(cnt)


# In[24]:


print("Association Rules are given as: ")
print('===========================================================================================================')
for i in range(len(a)):                   
    for j in range(len(a[i])):
        s=a[i][j]
        a1=[]
        for m in range(1,len(s)):
            a1=list(combinations(s,m))
            for k in range(len(a1)):
                x1=list(a1[k])
                y1=list(set(s)^set(x1))
                confidence = support_count(list(s))/support_count(list(x1))
                if confidence >= minConfidence:
                    print(x1,'==>',y1)
                    print('confidence=',confidence)
                    print('')


# In[ ]:




