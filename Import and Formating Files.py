#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np


# In[12]:


pwd


# In[13]:


pd.read_csv('example.csv')


# In[14]:


df = pd.read_csv("example.csv")


# In[18]:


df.to_csv("My_output", index=False)


# In[19]:


pd.read_csv("My_output")


# In[23]:


pd.read_excel("Excel_Sample.xlsx", sheet_name = "Sheet1")


# In[29]:


df.to_excel("Excel_Sample2.xlsx", sheet_name = "Newsheet")


# In[30]:


df


# In[37]:


data = pd.read_html("https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list")


# In[39]:


data[0]


# In[40]:


from sqlalchemy import create_engine


# In[41]:


engine = create_engine("sqlite:///:memory:")


# In[45]:


df.to_sql("my_tables", engine)


# In[ ]:




