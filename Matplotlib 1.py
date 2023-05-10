#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import numpy as np 
import pandas as pd


# In[4]:


x = np.linspace(0,5,11)
y = x**2


# In[5]:


x


# In[6]:


y


# In[7]:


# THERE ARE TWO METHODS TO PLOT IN PYTHON USING MATPLOTLIB
# ONE IS FUNCTIONAL AND THE OTHER IS OBJECT ORIENTED


# In[12]:


# FUNTIONAL
plt.plot(x,y,"r")
plt.xlabel("X LABEL")
plt.ylabel("Y LABEL")
plt.title("TITLE")
plt.show()


# In[16]:


# MULTIPLOT ON THE SAME CANVAS
plt.subplot(1,2,1)
plt.plot(x,y,"r")

plt.subplot(1,2,2)
plt.plot(y,x,"b")

plt.show()


# In[42]:


# OBJECT ORIENTED METHOD
fig = plt.figure()  # this figure object is kind of like a blank canvas in which we add stuff(axis, title etc.)
axes1 = fig.add_axes([0.1,0.1,0.8,0.8]) #list in the axes method- [left, bottom, width, height]

axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes2.plot(y,x, "r")
axes2.set_xlabel("X axis")
axes2.set_ylabel("Y axis")
axes2.set_title("OP title")

axes1.plot(x,y)
axes1.set_xlabel("X Label")
axes1.set_ylabel("Y label")
axes1.set_title("OG title")


# In[56]:


fig,axes = plt.subplots(nrows=1, ncols=2)

axes[-2].plot(x,y,"y")
axes[-2].set_title("OG")

axes[-1].plot(y,x)
axes[-1].set_title("OP")

plt.tight_layout() # recommended to always use this to avoid over lappings


# # Figure Size, Aspect Ratio and DPI

# In[84]:


fig,axes = plt.subplots(nrows = 2, ncols= 1,figsize = (8,5))

axes[0].plot(x,x**2, "r")
axes[1].plot(x,x**0.5)

plt.tight_layout()


# In[85]:


fig.savefig("graph.png", dpi=1000)


# In[88]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,x**2, label = "Square")
ax.plot(x,x**3, label = "Cube")

ax.legend(loc = 0)
#loc in legend specifies the location where the legend will appear 
#loc is from 0 to 10 and there is a documentation page for location and the corresponding number
#else just loc = (xcoordinate, ycoordinate)


# In[ ]:




