#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


arr = np.random.randn(6,2)


# In[3]:


# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[4]:


df = pd.DataFrame(arr,hier_index,["A","B"])


# In[5]:


df


# In[6]:


df.loc["G1"].loc[1]


# In[7]:


df.index.names = ["Groups", "Num"]


# In[8]:


df


# In[9]:


df.loc["G2"].loc[2]["B"]


# In[10]:


df.loc["G1"].loc[3]["B"]


# In[11]:


#Cross Section Method

df.xs(1, level ="Num")


# # Missing Data

# In[12]:


import numpy as np 
import pandas as pd


# In[13]:


d = {"A":[1,2,np.nan], "B":[5,np.nan,np.nan], "C":[1,2,3]}


# In[14]:


df1 = pd.DataFrame(d)


# In[15]:


df1


# In[16]:


df1.dropna()


# In[17]:


df1.dropna(axis = 1)


# In[18]:


df1.dropna(thresh = 2)


# In[19]:


df1.fillna(value = "FILL VALUE")


# In[30]:


df1["A"].fillna(value = df1["A"].mean())


# In[ ]:





# In[ ]:


list = []

