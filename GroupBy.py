#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Groupby allows us to group together rows based off pf a 
column and perform an aggregate function on them.

"""


# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}


# In[3]:


df = pd.DataFrame(data)


# In[4]:


df


# In[9]:


byComp = df.groupby("Company")


# In[16]:


byComp.sum()


# In[15]:


byComp.sum().loc["FB"]


# In[17]:


df.groupby("Company").min()


# In[19]:


#####FUCKING IMPORTANT AS HELLLLLL

df.groupby("Company").describe().transpose()


# In[ ]:




