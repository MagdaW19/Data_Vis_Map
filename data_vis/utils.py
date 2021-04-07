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

"Module with utility functions for generating maps with volcanoes, earthquakes and tsunamis."

import pandas as pd

# Dictionary for translating last eruption date
errupt_dict = {
    'D1':	'LAST KNOWN ERRUPTION: 1964 or later',
    'D2':	'LAST KNOWN ERRUPTION: 1900-1963',
    'D3':	'LAST KNOWN ERRUPTION: 1800-1899',
    'D4':	'LAST KNOWN ERRUPTION: 1700-1799',
    'D5':	'LAST KNOWN ERRUPTION: 1500-1699',
    'D6':	'LAST KNOWN ERRUPTION: A.D. 1-1499',
    'D7':	'LAST KNOWN ERRUPTION: B.C. (Holocene)',
    'U':	'Undated, but probable Holocene eruption',
    'Q':	'Quaternary eruption(s) with the only known Holocene activity being hydrothermal',
    '?':	'Uncertain Holocene eruption'
}

def vol_color(errupt_date):
    """Returns string representing color of the volcano marker based on last erruption date.


    Parameters
    ----------
    errupt_date : str
        Describes last erruption date according to data format.
        One of the following 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'U', 'Q', '?'

    Returns
    -------
    str
        string representing color
    """
    if errupt_date == 'D1':
        return 'red'
    elif errupt_date in ['D2', 'D3', 'D4', 'D5']:
        return 'orange'
    else:
        return 'green'

def load_data(path):
    """Load data saved via API and filter instances without lat and lon.

    Parameters
    ----------
    path : str
        Path to the csv file with data
    """
    data = pd.read_csv(path)
    data = data.dropna(subset=['latitude','longitude'])
    #data = data.to_dict('list')
    return data