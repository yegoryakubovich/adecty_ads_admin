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


from flask import Blueprint, request
from werkzeug.exceptions import InternalServerError

from app.adecty_design.interfaces.error import interface_error_get
from app.decorators.admin_get import admin_get


blueprint_errors = Blueprint(
    name='blueprint_errors',
    import_name=__name__,
    url_prefix='/',
)


@blueprint_errors.app_errorhandler(404)
@admin_get(not_return=True)
def errors_404(error: InternalServerError):
    if 'favicon.ico' in request.url:
        return error.get_body()

    interface = interface_error_get(text='Page not found')
    return interface, 404
