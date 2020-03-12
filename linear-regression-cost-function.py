#!/usr/bin/env python
# coding: utf-8

# # linear regression cost function

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[11]:


# defines input
x = np.array([[1,1], [1,2], [1,3]])
y = np.array([[1], [2], [3]])
theta = np.array([[0], [1]])


# In[12]:


plt.subplot(1, 2, 1)
plt.plot(x, y);
plt.xlabel('x axis')
plt.ylabel('y axis');

plt.subplot(1, 2, 2)
plt.scatter(x[:,1], y, s=100, c='g', marker= 'x');
plt.xlabel('x axis')
plt.ylabel('y axis');


# In[13]:


# 1/2(x theta-y)T(x theta-y)
def sse(x, y, theta):
    """DocString: vector """
    prediction = x @ theta #hamun khate h
    error = prediction - y 
    return 0.5 * np.sum(error**2)


# In[29]:


def sse(x, y, theta):
    error = x@theta - y
    return 0.5 * (error.T * error)[0,0]


# In[40]:



theta = np.array([[0], [0.5]])
plt.plot(x, y, theta)
loss = sse(x, y, theta)
print(theta.ravel(), loss)


# In[ ]:





# In[ ]:





# In[ ]:




