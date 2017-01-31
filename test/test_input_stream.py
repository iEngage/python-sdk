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
from iengage_client.models.input_stream import InputStream


class TestInputStream(unittest.TestCase):
    """ InputStream unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInputStream(self):
        """
        Test InputStream
        """
        model = iengage_client.models.input_stream.InputStream()


if __name__ == '__main__':
    unittest.main()
