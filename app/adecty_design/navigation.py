#
# (c) 2023, Yegor Yakubovich, yegoryakubovich.com, personal@yegoryakybovich.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from adecty_design.widgets.required import Navigation, NavigationItem

from app.adecty_design.functions.icon_get import icon_get


navigation_main = Navigation(
    items=[
        NavigationItem(
            id='campaigns',
            name='Campaigns',
            url='/campaigns',
            icon=icon_get(filename='campaigns.svg'),
        ),
        NavigationItem(
            id='countries',
            name='Countries',
            url='/countries',
            icon=icon_get(filename='countries.svg'),
        ),
    ],
)
navigation_none = Navigation(
    items=[],
)
