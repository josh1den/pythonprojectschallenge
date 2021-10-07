#!/usr/bin/env python
# coding: utf-8

# Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these: 
# 
# "ho-tel"
# "cat"
# "met-a-phor"
# "ter-min-a-tor"
# 
# Your function should count the number of syllables and return it.
# 
# For example, the call count("ho-tel") should return 2.

# In[1]:


def count(string):
    '''Takes a single string parameter divided into
    syllables by hyphens and returns the syllable count
    '''
    return len(string.split('-'))


# In[2]:


count('ho-tel')


# In[ ]:




