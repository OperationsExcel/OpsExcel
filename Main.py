#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


st.title("First Streamlit Application")


# In[3]:


if st.button("Trial button"):
    print("Button activated")


# In[4]:


value1=st.number_input('First input',min_value=1,step=2,max_value=20)


# In[ ]:


value2=st.number_input('Second input',min_value=2,step=3,max_value=30)

if st.button("Total button"):
    print("Total button clicked")
    print(value1+value2)


# In[9]:


from Multfunc import multiplyfunction


# In[10]:


if st.button("Function import value button"):
    print("In function import button")
    print(value1*value2)


# In[ ]:




