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


# In[210]:


#!conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values


# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

# import k-means from clustering stage
from sklearn.cluster import KMeans

get_ipython().system('pip install folium')
import folium # map rendering library


# In[211]:


#finding Toronto address
address = 'Toronto'

geolocator = Nominatim(user_agent="ny_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude


# In[218]:


# create map of Toronto using latitude and longitude values
map_toronto = folium.Map(location=[latitude, longitude], zoom_start=9)


# In[215]:


#constructing dataframes for each borough
df1 = ne2df[ne2df['Borough'] == 'Downtown Toronto']
df2 = ne2df[ne2df['Borough'] == 'North York']
df3 = ne2df[ne2df['Borough'] == 'Scarborough']
df4 = ne2df[ne2df['Borough'] == 'Etobicoke']
df5 = ne2df[ne2df['Borough'] == 'Central Toronto']
df6 = ne2df[ne2df['Borough'] == 'West Toronto']
df7 = ne2df[ne2df['Borough'] == 'York']
df8 = ne2df[ne2df['Borough'] == 'East Toronto']
df9 = ne2df[ne2df['Borough'] == 'East York']
df10 = ne2df[ne2df['Borough'] == 'Mississauga']


# In[217]:


#colour coding boroughs in Toronto
for lat, lng, borough, neighborhood in zip(df1['Latitude'], df1['Longitude'], df1['Borough'], df1['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)  
for lat, lng, borough, neighborhood in zip(df2['Latitude'], df2['Longitude'], df2['Borough'], df2['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)
for lat, lng, borough, neighborhood in zip(df3['Latitude'], df3['Longitude'], df3['Borough'], df3['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='green',
        fill=True,
        fill_color='green',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)
for lat, lng, borough, neighborhood in zip(df4['Latitude'], df4['Longitude'], df4['Borough'], df4['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='yellow',
        fill=True,
        fill_color='yellow',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)
for lat, lng, borough, neighborhood in zip(df5['Latitude'], df5['Longitude'], df5['Borough'], df5['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='purple',
        fill=True,
        fill_color='purple',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)
for lat, lng, borough, neighborhood in zip(df6['Latitude'], df6['Longitude'], df6['Borough'], df6['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='orange',
        fill=True,
        fill_color='orange',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)
for lat, lng, borough, neighborhood in zip(df7['Latitude'], df7['Longitude'], df7['Borough'], df7['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='darkred',
        fill=True,
        fill_color='darkred',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)
for lat, lng, borough, neighborhood in zip(df8['Latitude'], df8['Longitude'], df8['Borough'], df8['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='white',
        fill=True,
        fill_color='white',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)
for lat, lng, borough, neighborhood in zip(df9['Latitude'], df9['Longitude'], df9['Borough'], df9['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='black',
        fill=True,
        fill_color='black',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)
for lat, lng, borough, neighborhood in zip(df10['Latitude'], df10['Longitude'], df10['Borough'], df10['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='pink',
        fill=True,
        fill_color='pink',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)


map_toronto


# In[ ]:




