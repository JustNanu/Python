#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Numpy is a Linear Algebra library for python, the reason it is so 
important for Data Science with Python is that almost all of the 
libraries in the PyData Ecosystem rely on NumPy as one of their main
blocks. Also is extremely fast.

"""


# In[2]:


#NumPy Arrays

my_list = [1,2,3,4,5]

import numpy as np

arr = np.array(my_list)

arr


# In[5]:


my_mat = [[1,2,3], [4,5,6], [7,8,9]]

np.array(my_mat)


# In[9]:


np.arange(0,11,2)

#np.arange(start, Upto(but not including), step size)-- To generate a Array


# In[10]:


np.zeros(4)


# In[64]:


np.zeros((4,3))


# In[12]:


np.ones((3,3))


# In[4]:


np.ones((4,5))*3


# In[16]:


#np.linspace(start, upto & including, No. of elements)
#So below, 10 evenly spaced points from 0 to 5 both inclusive and printing an one DIEMENSIONAL ARRAY 

np.linspace(0,5,10)


# In[19]:


#Identity Matrix in a Python
#Always a square a matrix

np.eye(4)


# In[4]:


#Arrays of Random Numbers
#Random array of uniform distribution from zero to one

np.random.rand(6)


# In[23]:


np.random.rand(3,3)


# In[25]:


#Array of random numbers from a Standard Normal Distribution

np.random.randn(4,4)


# In[32]:


#Ramndom Integers
np.random.randint(1,100,10)


# In[7]:


arr = np.arange(25)

arr.reshape(5,5)


# In[38]:


#INDEXING AND SELECTIONS

import numpy as np

arr = np.arange(0,11)


# In[39]:


arr


# In[43]:


arr[3:9]


# In[44]:


arr[4]


# In[45]:


arr [:7]


# In[46]:


#Numpy arrrays differ from python list because of thier ability to broadcast

arr[0:5] = 100


# In[47]:


arr


# In[48]:


arr = np.arange(0,11)


# In[49]:


arr


# In[52]:


slice_of_arr = arr[0:6]


# In[51]:


slice_of_arr


# In[55]:


slice_of_arr[:] = 99


# In[56]:


slice_of_arr


# In[57]:


arr


# In[58]:


arr_copy = arr.copy()


# In[59]:


arr_copy


# In[60]:


arr_copy[:] = 110


# In[61]:


arr_copy


# In[62]:


arr


# In[69]:


np.arange(1,101).reshape(10,10)/100


# In[ ]:




