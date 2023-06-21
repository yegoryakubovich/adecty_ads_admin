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


from peewee import PrimaryKeyField, IntegerField, CharField, BooleanField

from app.database.db import BaseModel


class GroupStates:
    checking_waiting = 'checking_waiting'
    checking = 'checking'
    waiting = 'waiting'


class Group(BaseModel):
    id = PrimaryKeyField()
    name = CharField(max_length=128)
    state = CharField(max_length=32, default=GroupStates.checking_waiting)
    subcribers = IntegerField()
    captcha_type = CharField(max_length=128)
    captcha_data = CharField(max_length=128)
    captcha_have = BooleanField(default=False)
    images_can = BooleanField(default=False)
    url_can = BooleanField(default=False)
    bigtext_can = BooleanField(default=False)

    class Meta:
        db_table = 'groups'
