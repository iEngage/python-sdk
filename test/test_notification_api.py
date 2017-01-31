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
from iengage_client.apis.notification_api import NotificationApi


class TestNotificationApi(unittest.TestCase):
    """ NotificationApi unit test stubs """

    def setUp(self):
        self.api = iengage_client.apis.notification_api.NotificationApi()

    def tearDown(self):
        pass

    def test_get_notifications(self):
        """
        Test case for get_notifications

        Get list of notifications
        """
        pass

    def test_mark_all_notification_as_read(self):
        """
        Test case for mark_all_notification_as_read

        Mark all notification as read
        """
        pass

    def test_mark_notification_as_read(self):
        """
        Test case for mark_notification_as_read

        Mark notification as read
        """
        pass

    def test_notification_count(self):
        """
        Test case for notification_count

        Get notifications count
        """
        pass


if __name__ == '__main__':
    unittest.main()
