# coding: utf-8

"""
    iEngage 2.0 API

    This API enables Intelligent Engagement for your Business. iEngage is a platform that combines process, augmented intelligence and rewards to help you intelligently engage customers.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import iengage_client
from iengage_client.rest import ApiException
from iengage_client.models.interaction_category import InteractionCategory


class TestInteractionCategory(unittest.TestCase):
    """ InteractionCategory unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInteractionCategory(self):
        """
        Test InteractionCategory
        """
        model = iengage_client.models.interaction_category.InteractionCategory()


if __name__ == '__main__':
    unittest.main()
