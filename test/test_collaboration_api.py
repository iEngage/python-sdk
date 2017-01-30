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
from iengage-client.apis.collaboration_api import CollaborationApi


class TestCollaborationApi(unittest.TestCase):
    """ CollaborationApi unit test stubs """

    def setUp(self):
        self.api = iengage-client.apis.collaboration_api.CollaborationApi()

    def tearDown(self):
        pass

    def test_add_comment_blog(self):
        """
        Test case for add_comment_blog

        Comment on posted blog
        """
        pass

    def test_add_comment_discussion(self):
        """
        Test case for add_comment_discussion

        Comment on discussion
        """
        pass

    def test_delete_blog(self):
        """
        Test case for delete_blog

        Delete blog
        """
        pass

    def test_delete_blog_comment(self):
        """
        Test case for delete_blog_comment

        Delete blog comment
        """
        pass

    def test_delete_discussion(self):
        """
        Test case for delete_discussion

        Delete discussion
        """
        pass

    def test_delete_discussion_comment(self):
        """
        Test case for delete_discussion_comment

        Delete discussion comment
        """
        pass

    def test_get_blog_comments(self):
        """
        Test case for get_blog_comments

        Get list of comments on blog
        """
        pass

    def test_get_blogs(self):
        """
        Test case for get_blogs

        Get list of blogs
        """
        pass

    def test_get_discussion_comments(self):
        """
        Test case for get_discussion_comments

        Get list of comments on discussion
        """
        pass

    def test_get_discussions(self):
        """
        Test case for get_discussions

        Get list of discussions
        """
        pass

    def test_get_user_subscribed_blogs(self):
        """
        Test case for get_user_subscribed_blogs

        Get list of blogs subscribed by user
        """
        pass

    def test_get_user_subscribed_discussions(self):
        """
        Test case for get_user_subscribed_discussions

        Get list of discussions subscribed by user
        """
        pass

    def test_post_blog(self):
        """
        Test case for post_blog

        Post blog
        """
        pass

    def test_start_discussion(self):
        """
        Test case for start_discussion

        Start discussion
        """
        pass

    def test_subscribe_blog(self):
        """
        Test case for subscribe_blog

        Subscribe blog
        """
        pass

    def test_subscribe_discussion(self):
        """
        Test case for subscribe_discussion

        Subscribe discussion
        """
        pass

    def test_unsubscribe_blog(self):
        """
        Test case for unsubscribe_blog

        Unsubscribe blog
        """
        pass

    def test_unsubscribe_discussion(self):
        """
        Test case for unsubscribe_discussion

        Unsubscribe discussion
        """
        pass

    def test_update_blog(self):
        """
        Test case for update_blog

        Update blog
        """
        pass

    def test_update_blog_comment(self):
        """
        Test case for update_blog_comment

        Update blog comment
        """
        pass

    def test_update_discussion(self):
        """
        Test case for update_discussion

        Update discussion
        """
        pass

    def test_update_discussion_comment(self):
        """
        Test case for update_discussion_comment

        Update discussion comment
        """
        pass


if __name__ == '__main__':
    unittest.main()