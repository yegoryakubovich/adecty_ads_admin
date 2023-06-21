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


from app.database.models.admin import Admin
from app.database.models.account import Account
from app.database.models.country import Country
from app.database.models.group import Group, GroupStates
from app.database.models.group_country import GroupCountry
from app.database.models.message import Message, MessageStates
from app.database.models.proxy import Proxy
from app.database.models.session_group import SessionGroup
from app.database.models.session_proxy import SessionProxy
from app.database.models.tag import Tag
from app.database.models.group_tag import GroupTag
from app.database.models.session import Session, SessionStates


__all__ = (
    # Main
    Account,
    Admin,
    Country,
    Tag,

    # Proxies
    Proxy,

    # Groups
    Group,
    GroupCountry,
    GroupTag,

    # Sessions
    Session,
    SessionGroup,
    SessionProxy,

    # Messages
    Message,

    # States
    GroupStates,
    SessionStates,
    MessageStates,
)


models = (
    Account,
    Admin,
    Country,
    Tag,
    Proxy,
    Group,
    GroupCountry,
    GroupTag,
    Session,
    SessionGroup,
    SessionProxy,
    Message,
)
