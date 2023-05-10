#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


from numpy.random import randn


# In[4]:


np.random.seed(101)


# In[5]:


df = pd.DataFrame(randn(5,4), ["A","B","C","D","E"], ["W","X","Y","Z"])


# In[6]:


df


# In[7]:


df["W"]


# In[8]:


df[["W","Z"]]


# In[9]:


#Creating a new Column
df["new"] = df["W"] + df["Y"]
df


# In[10]:


#Removing a Column
df.drop('new', axis =1, inplace = True)


# In[11]:


df


# In[12]:


df.drop("E")

#Here axis is already defined as zero
#axis = zero 0 for columns(a, b, c, d)
#axis = one 1 for rows(w, x, y, z)
#also inplace = true to permanently delete anything


# In[13]:


df.loc["A"]


# In[14]:


df.iloc[2]


# # Conditional Selection

# In[15]:


booldf = df > 0 


# In[16]:


booldf


# In[17]:


df[booldf]


# In[18]:


df[df>0]


# In[19]:


df["W"]>0


# In[20]:


#Only those rows are shown where the value of W column is non null

resultdf = df[df["W"]>0]


# In[21]:


df[df["Z"]<0]


# In[22]:


resultdf["X"]

#instead of doing this i.e. assigning a new value to df[df["W"]>0] this all can be done in one step
#Next CEll


# In[23]:


df[df["W"]>0]["X"]


# In[24]:


df[df["W"]>0][["X","Y"]]


# In[25]:


boolser = df["W"]>0
result = df[boolser]

mycols = ["X","Y"]
result[mycols]


# In[26]:


result


# In[27]:


#For multiple conditions 
#And/OR operators are used
#& and | (pipe operator)

df[(df["W"]>0) & (df["Y"]>1)]


# In[28]:


df[(df["W"]>0) | (df["Y"]>1)]


# In[29]:


#Resetting the Indexes
df.reset_index()


# In[30]:


newind = "CA NY WY OR CO"
State = newind.split()


# In[31]:


df["States"] = State


# In[32]:


df


# In[34]:


df.set_index("States")


# In[ ]:




