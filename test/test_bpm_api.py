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
from iengage-client.apis.bpm_api import BPMApi


class TestBPMApi(unittest.TestCase):
    """ BPMApi unit test stubs """

    def setUp(self):
        self.api = iengage-client.apis.bpm_api.BPMApi()

    def tearDown(self):
        pass

    def test_assign_wf_task(self):
        """
        Test case for assign_wf_task

        Assign task
        """
        pass

    def test_complete_wf_task(self):
        """
        Test case for complete_wf_task

        Complete task
        """
        pass

    def test_get_bpm_tasks(self):
        """
        Test case for get_bpm_tasks

        Get task by task id
        """
        pass

    def test_get_search_task(self):
        """
        Test case for get_search_task

        Get list of BPM task assigned to user
        """
        pass

    def test_get_tasks_by_entity(self):
        """
        Test case for get_tasks_by_entity

        Get list of BPM task assigned to user
        """
        pass

    def test_get_user_bpm_tasks(self):
        """
        Test case for get_user_bpm_tasks

        Get list of BPM task assigned to user
        """
        pass

    def test_get_user_roles_bpm_tasks(self):
        """
        Test case for get_user_roles_bpm_tasks

        Get list of BPM task assigned to user roles
        """
        pass


if __name__ == '__main__':
    unittest.main()