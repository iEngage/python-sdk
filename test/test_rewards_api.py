# coding: utf-8

"""
    Stakeholder engagement API

    This API enables Intelligent Engagement for your Business. iEngage is a platform that combines process, augmented intelligence and rewards to help you intelligently engage customers.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import iengage-client
from iengage-client.rest import ApiException
from iengage-client.apis.rewards_api import RewardsApi


class TestRewardsApi(unittest.TestCase):
    """ RewardsApi unit test stubs """

    def setUp(self):
        self.api = iengage-client.apis.rewards_api.RewardsApi()

    def tearDown(self):
        pass

    def test_get_top_friends(self):
        """
        Test case for get_top_friends

        Get list of top friends
        """
        pass

    def test_get_top_users(self):
        """
        Test case for get_top_users

        Get list of top users
        """
        pass

    def test_get_user_points(self):
        """
        Test case for get_user_points

        Get list of user points
        """
        pass


if __name__ == '__main__':
    unittest.main()