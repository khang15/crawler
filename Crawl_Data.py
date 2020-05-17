#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from lxml import html
import json


# In[2]:


headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'}


# In[3]:


res_list = requests.get('https://batdongsan.com.vn/', headers=headers)
root = html.fromstring(res_list.content)


# In[5]:


a_link = root.xpath('//a')


# In[9]:


all_links = [a.attrib['href'] for a in a_link]


# In[10]:


all_links


# In[ ]:




