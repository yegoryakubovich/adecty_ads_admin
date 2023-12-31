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

from app.adecty_design.interfaces.main import interface_main_get
from app.blueprints.account import blueprint_account
from app.blueprints.countries import blueprint_countries
from app.blueprints.errors import blueprint_errors
from app.decorators.admin_get import admin_get


blueprint_main = Blueprint(
    name='blueprint_main',
    import_name=__name__,
    url_prefix='/',
)
blueprint_main.register_blueprint(blueprint=blueprint_errors)
blueprint_main.register_blueprint(blueprint=blueprint_account)
blueprint_main.register_blueprint(blueprint=blueprint_countries)


@blueprint_main.route(rule='/', endpoint='main_get', methods=('GET', ))
@admin_get(not_return=True)
def main_get():
    interface = interface_main_get()
    return interface, 200
