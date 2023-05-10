#!/usr/bin/env python
# coding: utf-8

# # Plot Appearence

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


x = np.linspace(0,5,11)
y = x**2


# In[26]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, y, color = "orange", lw= 1, alpha = 0.5, ls = "-", marker= ".",
        markersize = 10, markerfacecolor = "pink", markeredgewidth = 3, markeredgecolor = "green")
#lw is linewidth
#ls is linestyle
#alpha is basically the transparency of the line


# In[40]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,x**3, color = "pink", lw= 3, ls = "--")

ax.set_xlim([0,1])
ax.set_ylim([0,2])


# In[ ]:


"""
 http://www.matplotlib.org - The project web page for matplotlib.
 https://github.com/matplotlib/matplotlib - The source code for matplotlib.
 http://matplotlib.org/gallery.html - A large gallery showcaseing various types of plots matplotlib can create. Highly recommended! 
 http://www.loria.fr/~rougier/teaching/matplotlib - A good matplotlib tutorial.
 http://scipy-lectures.github.io/matplotlib/matplotlib.html - Another good matplotlib reference.
""""

