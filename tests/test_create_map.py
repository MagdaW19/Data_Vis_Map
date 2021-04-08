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

"Module with unit tests for create_map module."
import unittest
from data_vis import create_map
import os
import folium

class TestCreateMap(unittest.TestCase):
    def setUp(self):
        create_map.create_map(loc=[41.87, 12.56],
                   tiles = "Stamen Terrain", 
                   zoom_start=6,
                   data_dir='tests/data_t',
                   save_path='tests/data_t/Map_New.html')
        self.maxDiff=50

    def tearDown(self):
        os.remove('tests/data_t/Map_New.html')
        self.maxDiff=None

    def test_create_map(self):
        target_file = 'tests/data_t/map_target.html'
        new_file = 'tests/data_t/Map_New.html'

        with open(target_file, "r", encoding='utf-8') as f:
            text_target= f.read()
            
        self.assertGreater(len(text_target), 1000)

    def test_add_volcano(self):
        vol =  create_map.add_volcanoes('tests/data_t/volloc.csv')
        self.assertIsInstance(vol, folium.FeatureGroup)

    def test_add_events(self):
        vol =  create_map.add_events('tests/data_t/tsunamis.csv')
        self.assertIsInstance(vol, folium.FeatureGroup)

if __name__ == '__main__':
    unittest.main()