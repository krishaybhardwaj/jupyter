#!/usr/bin/env python
# coding: utf-8

# In[15]:


people = {
    "first": ["Krishay", 'Rajeev', 'Vishakha', 'Vedika'],
    
    "last": ["Bhardwaj", 'Bhardwaj', 'Bhardwaj', 'Bhardwaj'],
    
    "email": ["krishay.bh@gmail.com", 'rony_bh@gmail.com', 'vishakha@gmail.com', 'vedika.bh@gmail.com']    
    
}


# In[10]:


import pandas as pd


# In[20]:


df = pd.DataFrame(people)


# In[21]:


df


# In[22]:


df['email']


# In[23]:


df[['first', 'email']]


# In[26]:


df.last


# In[27]:


df.iloc[1]


# In[31]:


df.iloc[[0, 1, 2], 2]


# In[ ]:




