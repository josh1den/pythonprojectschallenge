#!/usr/bin/env python
# coding: utf-8

# Write a function named capital_indexes. The function takes a single parameter, which is a string. The function should return a list of all the indexes in the string that have capital letters. 
# 
# For example, calling capital_indexes('HeLlO') should return the list [0, 2, 4].

# In[5]:


def capital_indices(string):
    '''returns a list of all indices in the 
       string that have capital letters'''
    index = [s for s in range(len(string)) if string[s].isupper()]
    return index


# In[6]:


capital_indices('HeLlO')


# In[7]:


capital_indices('ThaTsGoOD')

