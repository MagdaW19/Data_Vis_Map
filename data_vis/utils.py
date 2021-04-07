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

# Dictionary for translating last eruption date
errupt_date_dict = {
    'D1':	'Last known eruption 1964 or later',
    'D2':	'Last known eruption 1900-1963',
    'D3':	'Last known eruption 1800-1899',
    'D4':	'Last known eruption 1700-1799',
    'D5':	'Last known eruption 1500-1699',
    'D6':	'Last known eruption A.D. 1-1499',
    'D7':	'Last known eruption B.C. (Holocene)',
    'U':	'Undated, but probable Holocene eruption',
    'Q':	'Quaternary eruption(s) with the only known Holocene activity being hydrothermal'
    '?':	'Uncertain Holocene eruption'
}

