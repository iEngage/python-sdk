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

import iengage_client
from iengage_client.rest import ApiException
from iengage_client.apis.augmented_intelligence_api import AugmentedIntelligenceApi


class TestAugmentedIntelligenceApi(unittest.TestCase):
    """ AugmentedIntelligenceApi unit test stubs """

    def setUp(self):
        self.api = iengage_client.apis.augmented_intelligence_api.AugmentedIntelligenceApi()

    def tearDown(self):
        pass

    def test_get_interaction(self):
        """
        Test case for get_interaction

        Get the type of interaction
        """
        pass

    def test_get_popular_tag(self):
        """
        Test case for get_popular_tag

        Get list of popular tag of interactions
        """
        pass

    def test_get_sentiment(self):
        """
        Test case for get_sentiment

        Get sentiment count of interactions
        """
        pass

    def test_get_tag_entity_sentiments(self):
        """
        Test case for get_tag_entity_sentiments

        Get list of tag entity sentiment
        """
        pass


if __name__ == '__main__':
    unittest.main()
