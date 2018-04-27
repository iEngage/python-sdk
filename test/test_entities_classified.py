# coding: utf-8

"""
    iEngage 2.0 API

    This API enables Intelligent Engagement for your Business. iEngage is a platform that combines process, augmented intelligence and rewards to help you intelligently engage customers.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import iengage_client
from iengage_client.rest import ApiException
from iengage_client.models.entities_classified import EntitiesClassified


class TestEntitiesClassified(unittest.TestCase):
    """ EntitiesClassified unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEntitiesClassified(self):
        """
        Test EntitiesClassified
        """
        model = iengage_client.models.entities_classified.EntitiesClassified()


if __name__ == '__main__':
    unittest.main()
