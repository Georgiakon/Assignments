#!/usr/bin/env python
# coding: utf-8

# In[58]:


#import the necessary libraries
import pandas as pd
import numpy as np
get_ipython().system('conda install -c conda lxml')
get_ipython().system('pip install et_xmlfile')
get_ipython().system('pip install bs4')
get_ipython().system('pip install html5lib')
get_ipython().system('pip install lxml')
import bs4.builder._lxml
from lxml import etree
import requests
from bs4 import BeautifulSoup


# In[157]:


r = requests.get("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")

soup = BeautifulSoup(r.content,features="lxml")

table = soup.find_all('table')[0]

df = pd.read_html(str(table))

ne=pd.DataFrame(df[0])


# In[158]:


ne.head(12)


# In[159]:


#Ignore cells with a borough that is Not assigned
ne = ne[ne.Borough != "Not assigned"]


# In[160]:


ne.head(12)


# In[171]:


ne2=ne


# In[172]:


#Replace bogus \n from data

ne2['Neighborhood']=ne2['Neighborhood'].apply(lambda x: x.replace(' / ', ','))

ne2.head(12)


# In[191]:


# To change the row indexes
ne2=ne2.rename(index = lambda x: x +4)
ne2.head(12)


# In[166]:


type(ne2.Neighborhood)


# In[192]:


ne2.shape


# In[199]:


df=pd.read_csv('http://cocl.us/Geospatial_data')


# In[196]:


ne2.dtypes


# In[200]:


df.dtypes


# In[206]:


#rename Postal Code in df
df.rename(columns={'Postal Code':'Postal code'}, inplace=True)
df.head(12)


# In[205]:


#join ne2 and df by Postal code column to form table
ne2df=ne2.merge(df,on='Postal code',how='left')
ne2df.head(12)


# In[ ]:




