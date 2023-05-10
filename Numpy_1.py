#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[5]:


arr_2d = [[1,2,3],[4,5,6],[7,8,9]]

mat = np.array(arr_2d)


# In[6]:


mat


# In[9]:


mat[1][2]
#Similar to list indexing i.e. starting from 0 and...


# In[10]:


mat[0,2]


# In[11]:


mat[1:, 1:]


# In[12]:


list = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16], [17,18,19,20]]

matrix = np.array(list)


# In[13]:


matrix


# In[14]:


matrix[1:3,1:]


# In[15]:


arr = np.arange(0,11)


# In[16]:


arr


# In[17]:


arr > 5


# In[18]:


bool_arr = arr > 5


# In[19]:


bool_arr


# In[20]:


arr[bool_arr]


# In[21]:


arr


# In[22]:


arr[arr>=5]


# In[23]:


det = np.arange(1,51).reshape(5,10)


# In[24]:


det


# In[25]:


det[2:, 1:6]


# In[26]:


det[1:3, 1:3]


# In[ ]:




