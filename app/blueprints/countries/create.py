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


from flask import Blueprint

from app.adecty_design.interfaces.countries_create import interface_countries_create
from app.decorators.admin_get import admin_get


blueprint_countries_create = Blueprint(
    name='blueprint_countries_create',
    import_name=__name__,
    url_prefix='/create'
)


@blueprint_countries_create.route(rule='/', methods=('GET', 'POST'))
@admin_get(not_return=True)
def route():
    interface = interface_countries_create()
    return interface
