#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


def multiplyfunction(x,y):
    return x*y


# In[4]:


from joblib import load


# In[5]:


modelcloud=load("cloudregmodel.joblib")


# In[6]:


predict=pd.DataFrame([{"area_sqr_ft":1500,"bedrooms":2}])


# In[8]:


w=modelcloud.predict(predict)


# In[9]:


w


# In[10]:


def cloudregression(x,y):
    predcloud=pd.DataFrame([{"area_sqr_ft":x,"bedrooms":y}])
    wcloud=modelcloud.predict(predcloud)
    cloudresult=wcloud[0]
    return cloudresult
    
    


# In[ ]:




