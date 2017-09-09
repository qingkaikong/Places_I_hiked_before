import folium
from locations import *

# Add the USGS style tile
url_base = 'http://server.arcgisonline.com/ArcGIS/rest/services/'
service = 'NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}'
tileset = url_base + service

map_1 = folium.Map(location=[37.8716, -122.2727], zoom_start=9,\
        control_scale = True, tiles=tileset, attr='USGS style')

for key in locations.keys():
    loc = locations[key]

    map_1.add_children(
        folium.Marker(loc, popup = key))

map_1.save('hikes.html')

import os

os.system('scp hikes.html kongqk@andy.geo.berkeley.edu:public_html/fun/hikes.html')
