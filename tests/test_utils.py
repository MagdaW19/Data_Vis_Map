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

"Module for testing utility functions of create_map module."
import unittest
from data_vis import utils
import pandas as pd

class TestUtils(unittest.TestCase):
    def test_load_data(self):
        path = 'tests/data_t/volloc.csv'
        data = pd.read_csv(path)
        data = data.dropna(subset=['latitude','longitude'])
        data.equals(utils.load_data(path))

    def test_vol_color(self):
        self.assertEqual(utils.vol_color('D1'), 'red')
        self.assertEqual(utils.vol_color('D2'), 'orange')
        self.assertEqual(utils.vol_color('U'), 'green')
        



if __name__ == '__main__':
    unittest.main()
