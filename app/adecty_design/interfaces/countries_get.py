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


from app.adecty_design.interface import interface
from app.adecty_design.widgets.action import Action
from app.adecty_design.widgets.header import header_get
from app.adecty_design.widgets.models_viewer_get import models_viewer_get
from app.adecty_design.widgets.unit import Unit
from app.database.models import Country


def interface_countries_get() -> str:
    header = header_get(text='Countries', create_url='/countries/create')

    widgets = [
        header,
    ]

    widgets += models_viewer_get(
        units=[
            Unit(
                id=country.id,
                name='{icon} {name}'.format(
                    icon=country.icon,
                    name=country.name,
                ),
                parameters={
                    'Name': country.name,
                    'Icon': country.icon,
                },
                actions=[
                    Action(
                        name='Update',
                        icon='update.svg',
                        url='/countries/{id}/update'.format(
                            id=country.id,
                        ),
                    ),
                    Action(
                        name='Delete',
                        icon='delete.svg',
                        url='/countries/{id}/delete'.format(
                            id=country.id,
                        ),
                    ),
                ],
            )
            for country in Country.select()
        ],
    )

    interface_html = interface.html_get(
        widgets=widgets,
        active='countries',
    )
    return interface_html
