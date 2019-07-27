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
from iengage_client.apis.bpm_api import BPMApi


class TestBPMApi(unittest.TestCase):
    """ BPMApi unit test stubs """

    def setUp(self):
        iengage_client.configuration.access_token = None
        self.api = iengage_client.apis.bpm_api.BPMApi()

    def tearDown(self):
        pass

    def test_assign_wf_task(self):
        """
        Test case for assign_wf_task

        Assign task
        """
        assigneeUserId = None;
        taskId = 641009;
        requesterId = None;
        clientToken = None;
        print(self.api.assign_wf_task(assigneeUserId,taskId,requesterId,clientToken))
        requesterId = None;
        clientToken = None;
        pass

    def test_complete_wf_task(self):
        """
        Test case for complete_wf_task

        Complete task
        """
        userId = None
        taskId = 641009
        requesterId = None;
        clientToken = None;
        print(self.api.complete_wf_task(userId,taskId,requesterId,clientToken))
        pass

    def test_get_bpm_tasks(self):
        """
        Test case for get_bpm_tasks

        Get task by task id
        """
        userId = None
        taskId = 641009
        requesterId = None;
        clientToken = None;
        print(self.api.get_bpm_tasks(userId,taskId,requesterId,clientToken))
        pass

    def test_get_search_task(self):
        """
        Test case for get_search_task

        Get list of BPM task assigned to user
        """
        userId = None
        searchString = "true"
        completed = False
        searchByUserRoles = False;
        start = 0
        end = 10
        requesterId = None;
        clientToken = None;
        print(self.api.get_search_task(userId,searchString,completed,searchByUserRoles,start,end,requesterId,clientToken))
        pass

    def test_get_tasks_by_entity(self):
        """
        Test case for get_tasks_by_entity

        Get list of BPM task assigned to user
        """
        userId = None
        entityId = 112233
        completed = False
        start = 0
        end = 10
        search_by_user_roles = False
        requesterId = None;
        clientToken = None;
        print(self.api.get_tasks_by_entity(userId,end,completed,search_by_user_roles,start,end,requesterId,clientToken))
        pass

    def test_get_user_bpm_tasks(self):
        """
        Test case for get_user_bpm_tasks

        Get list of BPM task assigned to user
        """
        userId = None
        entityId = 112233
        completed = False
        start = 0
        end =10
        search_by_user_roles = False
        requesterId = None;
        clientToken = None;
        print(self.api.get_user_bpm_tasks(userId,completed,start,end,requesterId,clientToken))
        pass

    def test_get_user_roles_bpm_tasks(self):
        """
        Test case for get_user_roles_bpm_tasks

        Get list of BPM task assigned to user roles
        """
        userId = None
        entityId = 112233
        completed = False
        start = 0
        end = 10
        search_by_user_roles = False
        requesterId = None;
        clientToken = None;
        print(self.api.get_user_roles_bpm_tasks(userId,completed,start,end,requesterId,clientToken))
        pass


if __name__ == '__main__':
    unittest.main()
