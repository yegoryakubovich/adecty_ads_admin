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


from adecty_design.properties import Font, Margin, Padding
from adecty_design.widgets import Text, Card


class ModelsViewerTypes:
    cards = 'cards'


def models_viewer_get(type: str = ModelsViewerTypes.cards, models=None):
    widgets = []
    if not models:
        widgets += [
            Text(
                text='Selected models do not exist',
                font=Font(size=18),
                margin=Margin(horizontal=12),
            ),
        ]
        return widgets

    for model in models:
        if type == ModelsViewerTypes.cards:
            widgets += [
                Card(
                    widgets=[
                        Text(
                            text=str(model.id),
                        ),
                    ],
                    margin=Margin(horizontal=12),
                    padding=Padding(vertical=24, horizontal=18),
                ),
            ]

    return widgets
