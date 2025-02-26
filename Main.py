#!/usr/bin/env python
# coding: utf-8

# In[8]:


import streamlit as st


# In[9]:


st.title("Streamlit Cloud Application Demo")


# In[10]:


if st.button("Control Button"):
    st.success("Control activation!")
    print("Button activated")


# In[11]:


value1=st.number_input('First input',min_value=1,step=2,max_value=20)


# In[12]:


value2=st.number_input('Second input',min_value=2,step=3,max_value=30)

if st.button("Total button"):
    print("Total button clicked")
    st.success(value1+value2)


# In[13]:


from Multfunc import multiplyfunction


# In[16]:


if st.button("Function import value button"):
    print("In function import button")
    value3=multiplyfunction(value1,value2)
    st.success(value3)


# In[ ]:




