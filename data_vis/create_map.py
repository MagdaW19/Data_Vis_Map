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

import folium


m = folium.Map(location=[52.229675, 21.012230], tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name='My Markers')
fg.add_child(folium.Marker(location=[52.23,21.10],
                           popup='I am a happy marker',
                           icon=folium.Icon(color='green') ))

fg.add_child(folium.Marker(location=[52.13,21.05],
                           popup='I am a happy marker',
                           icon=folium.Icon(color='blue') ))

m.add_child(fg)
m.save('maps/Map1.html')



