#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
df = pd.read_csv("C:\\Users\\krish\\OneDrive\\Desktop\\Pandas-Demo\\stack-overflow-developer-survey-2019 (1)\survey_results_public.csv")
df


# In[8]:


df.shape


# In[9]:


df.info()


# In[10]:


pd.set_option('display.max_columns', 85)


# In[11]:


pd


# In[12]:


df


# In[13]:


df_schema = pd.read_csv("C:\\Users\\krish\\OneDrive\\Desktop\\Pandas-Demo\\stack-overflow-developer-survey-2019 (1)\survey_results_schema.csv")
df_schema


# In[ ]:




