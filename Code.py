# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 20:01:27 2018

@author: satyam
"""

import pandas as pd
import numpy as np
import folium
org_file=pd.read_csv("DATA_PUNE_WSI_LAT_LONG.csv")
wsi = np.array([])
m=folium.Map(location=[18.25812,73.9321])
#wsi=(41*fatal)+(1*minor)+(4*grevious)
org_file['Fatal'].tolist()
fatal=org_file['Fatal'].values
minor=org_file['MiNor'].values
grevious=org_file['Grevious'].values
k=fatal.size
for i in range(0,k):
    wsi=np.append(wsi,(41*fatal[i])+(1*minor[i])+(4*grevious[i]))
mid_file=pd.DataFrame()
mid_file['WSI']=pd.Series(wsi).values
out_file=pd.concat([org_file,mid_file],axis=1)
out_file.to_html("out_file.html")
for i in range(0,k):
   if wsi[i]>40:
        folium.Marker([out_file['LAT'][i],out_file['LOG'][i]],icon=folium.Icon(color='red')).add_to(m)
   else:
        folium.Marker([out_file['LAT'][i],out_file['LOG'][i]],icon=folium.Icon(color='green')).add_to(m)
folium.LatLngPopup().add_to(m)
m.save("map.html")