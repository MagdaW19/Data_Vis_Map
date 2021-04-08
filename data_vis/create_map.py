# Copyright 2021 Magda Wójcicka

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module creating maps with multiple points using folium package
"""
import os
import folium
import pandas as pd

from math import isnan

from data_vis.utils import load_data, vol_color, errupt_dict


def add_volcanoes(path):
    """
    Functions creating folium.FeatureGroup using path to file with data
    about volcanoes.

    Parameters
    ----------
    path : str
        path to the csv file with volcano locations from data API

    Returns
    -------
    folium.FeatureGroup
        Group of folium.Markers that functions like one layer on the map
    """
    fvol = folium.FeatureGroup(name='Volcanoes')
    vol_data = load_data(path)
    vol_data = vol_data.to_dict('list')
    vols = zip(vol_data['latitude'],
               vol_data['longitude'],
               vol_data['name'],
               vol_data['location'],
               vol_data['timeErupt'],
                )

    # Creating markers for each volcanoe
    for lat, lon, name, loc, errupt in vols:
        popup_text = f"VOLCANO <br> NAME: {name} <br> LOCATION: {loc}<br>"
        popup_text +=f"{errupt_dict.get(errupt, 'Unknown last erruption date')}"

        fvol.add_child(folium.CircleMarker(location=[lat, lon],
                                            tooltip=popup_text,
                                            radius=12, 
                                            fill_color=vol_color(errupt),
                                            color='black',
                                            fill_opacity=0.75
                                            )
                       )
    
    return fvol

def add_events(path, name='Tsunamis', check=True, color='darkblue'):
    """
    Functions creating folium.FeatureGroup using path to file with data
    about natural disasters. By default events are filtered and only 
    the most significant ones are shown (associated with at least one human 
    death).

    Parameters
    ----------
    path : str
        path to the csv file with volcano locations from data API
    name: str, optional
        Name of the feature group. Default name is 'Tsunamis'
    check: bool, optional
        If True data about is filtered and only the ones associates
        with human deaths are shows. Default is True.
    color: str, optional
        Color of the marker on the map.


    Returns
    -------
    folium.FeatureGroup
        Group of folium.Markers that functions like one layer on the map
    """
    ftsu = folium.FeatureGroup(name=name, opacity=0.7)
    tsu_data = load_data(path) 
    if check:
        my_filter = (tsu_data['deathsAmountOrderTotal']>=1.)&(tsu_data['eqMagnitude']>=3.)
        tsu_data = tsu_data[my_filter]

    tsu_data = tsu_data.to_dict('list')
    tsu = zip(tsu_data['latitude'],
               tsu_data['longitude'],
               tsu_data['locationName'],
               tsu_data['year'],
               tsu_data['month'],
               tsu_data['day'],
               tsu_data['deathsAmountOrderTotal'],
                )

    # Creating markers for each event
    for lat, lon, loc, YY, MM, DD, death in tsu:
        popup_text = f"EVENT: {name} <br> DATE: {YY:.0f}-{MM:.0f}-{DD:.0f} <br> LOCATION: {loc}<br>"
        popup_text += f"DEATHS: {death} <br>" 

        ftsu.add_child(folium.Marker(location=[lat,lon],
                                    tooltip=popup_text,
                                    icon=folium.Icon(prefix='fa',
                                                     color=color,
                                                    icon='exclamation-circle'
                                                    )
                                    )
                        )
    
    return ftsu



def create_map(loc=[52.2, 21.0], tiles = "Stamen Terrain", check=True,
              zoom_start=6, save_path='maps/Map1.html', data_dir='data'):
    """
    Functions that creates map with markers for volcanoes, earthquakes and tsunamis.
    Map is saved as html file and can be used as part of the website

    Parameters
    ----------
    save_path : str
        path to save html file with generated map
    check: bool, optional
        If True data about events is filtered and only the ones associates
        with human deaths are shown. Default is True.
    loc: obj::list of float, optional
        List with two float values latitude and longitude. Default location
        is in Poland.
    tiles: str
        type of tiles available in folium.Map class
    zoom_start: int
        starting value for map zoom
    data_dir: str
        path to dir where files


    Returns
    -------
    folium.Map
        Map with markers locating natural disasters.
    """
    # Creating and displaying map
    m = folium.Map(location=loc, tiles = tiles, zoom_start=zoom_start)

    data_tsu = os.path.join(data_dir, 'tsunamis.csv')
    data_earth = os.path.join(data_dir, 'earthquakes.csv')
    data_vol = os.path.join(data_dir, 'volloc.csv')

    m.add_child(add_events(data_tsu))
    m.add_child(add_events(data_earth, name='Earthquakes', color='darkgreen', check=check))
    m.add_child(add_volcanoes(data_vol))

    m.add_child(folium.LayerControl())
    m.save(save_path)
    return m



