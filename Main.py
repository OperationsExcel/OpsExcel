#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st


# In[4]:


st.title("Streamlit Cloud Application Demo")


# In[5]:


if st.button("Control Button"):
    st.success("Control activation!")
    print("Button activated")


# In[6]:


value1=st.number_input('Area in Square Feet',min_value=650,step=20,max_value=1800)


# In[7]:


value2=st.number_input('Number of bedrooms',min_value=2,step=1,max_value=3)

if st.button("Total button"):
    print("Total button clicked")
    st.success(value1+value2)


# In[8]:


from Multfunc import multiplyfunction


# In[9]:


if st.button("Function import value button"):
    print("In function import button")
    value3=multiplyfunction(value1,value2)
    st.success(value3)


# In[11]:


from Multfunc import cloudregression


# In[12]:


if st.button("Calculate Value of Property"):
    print("In function import button")
    value3=cloudregression(value1,value2)
    st.success(value3)


# In[ ]:




