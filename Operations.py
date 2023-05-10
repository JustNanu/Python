#!/usr/bin/env python
# coding: utf-8

# # Pandas - Operations

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


df = pd.DataFrame({"col1": [1,2,3,4], 
                   "col2":[444,555,666,444], 
                   "col3":["abc","def","ghi","xyz"]})
df.head()


# In[4]:


df["col2"].unique()


# In[5]:


df['col2'].nunique()


# In[6]:


df['col2'].value_counts()


# In[7]:


df[df["col1"]>2]


# In[8]:


#Apply method

def times2(x):
    return x*2


# In[9]:


df["col2"].sum()


# In[10]:


df["col1"].apply(times2)


# In[11]:


df["col2"].apply(lambda x: x*2)


# In[12]:


df


# In[13]:


#removing columns


# In[14]:


df.drop("col1", axis = 1)


# In[16]:


df.columns


# In[17]:


df.index


# In[24]:


df.sort_values("col2")


# In[25]:


#to find if there is null values in the dataframe
df.isnull()


# In[27]:


data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)


# In[28]:


df


# In[34]:


df.pivot_table(values = 'D', index = ["A","B"], columns = ["C"] )


# In[ ]:





# In[ ]:




