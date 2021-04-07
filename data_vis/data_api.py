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

"""Script that downloads data regarding volcanoes, earthquakes and tsunamis using API.

Source: https://www.ngdc.noaa.gov/
NCEI Volcano Location Database. NOAA National Centers for Environmental Information.
National Geophysical Data Center / World Data Service (NGDC/WDS): NCEI/WDS Global Significant Volcanic Eruptions Database.
NOAA National Centers for Environmental Information. doi:10.7289/V5JW8BSH
National Geophysical Data Center / World Data Service (NGDC/WDS): NCEI/WDS Global Significant Earthquake Database.
NOAA National Centers for Environmental Information. doi:10.7289/V5TD9V7K
National Geophysical Data Center / World Data Service: NCEI/WDS Global Historical Tsunami Database.
NOAA National Centers for Environmental Information. doi:10.7289/V5PN93H7

"""

import requests
import pandas as pd

# API urls for data
url_volloc = 'https://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/volcanolocs'
url_earthquakes = 'https://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/earthquakes'
url_tsunamis = 'https://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/tsunamis/events'

urls = [url_volloc, url_earthquakes, url_tsunamis]

# filepaths to save the data
fp_volloc = 'data/volloc.csv'
fp_earthquakes = 'data/earthquakes.csv'
fp_tsunamis = 'data/tsunamis.csv'

fps = [fp_volloc, fp_earthquakes, fp_tsunamis]

# Downloading data via API and saving as csv
for url, fp in zip(urls, fps):
    data = requests.get(url=url)
    data_dict = data.json()['items']
    pd.DataFrame(data_dict).to_csv(fp, index=False)

print('Succesfully downloaded data using API (https://www.ngdc.noaa.gov/) and saved in folder data')

