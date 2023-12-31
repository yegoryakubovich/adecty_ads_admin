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


from app.adecty_design.widgets.action import Action


class Unit:
    id: str | None
    name: str | None
    parameters: dict | None
    actions: list[Action] | None

    def __init__(self, id: str = None, name: str = None, parameters: dict = None, actions: list[Action] = None):
        self.id = id
        self.name = name
        self.parameters = parameters
        self.actions = actions
