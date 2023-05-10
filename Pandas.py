#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd


# In[4]:


labels = ["a","b","c"]
my_data = [10, 20, 30]

arr = np.array(my_data)

d = {"a":10, "b":20, "c":30}


# In[8]:


d


# In[9]:


pd.Series(data = my_data)


# In[10]:


pd.Series(data = my_data, index = labels)


# In[11]:


pd.Series(my_data, labels)


# In[12]:


pd.Series(arr)


# In[13]:


pd.Series(arr, labels)


# In[14]:


pd.Series(d)


# In[19]:


ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'India', 'Japan'])
ser1


# In[23]:


ser2 = pd.Series([1,2,5,4], ["USA", "France", "Italy", "USS"])
ser2


# In[25]:


ser2["Italy"]


# In[26]:


ser1["India"]


# In[ ]:




