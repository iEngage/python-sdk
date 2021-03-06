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
from iengage_client.apis.collaboration_api import CollaborationApi
from iengage_client.models.blog import Blog
from iengage_client.models.discussion import Discussion
from iengage_client.models.comment import Comment




class TestCollaborationApi(unittest.TestCase):
    """ CollaborationApi unit test stubs """

    def setUp(self):
        iengage_client.configuration.access_token = None
        self.api = iengage_client.apis.collaboration_api.CollaborationApi()

    def tearDown(self):
        pass

    def test_add_comment_blog(self):
        """
        Test case for add_comment_blog

        Comment on posted blog
        """
        requesterId = None;
        clientToken = None;
        blogid = 649503
        c = Comment()
        c.comment_text = "My Comment 2"

        print(self.api.add_comment_blog(blogid,requesterId,clientToken,body=c))
        pass

    def test_add_comment_discussion(self):
        """
        Test case for add_comment_discussion

        Comment on discussion
        """
        requesterId = None;
        clientToken = None;
        did = 649517
        c = Comment()
        c.comment_text = "My discussion comment is there 1"
        print(self.api.add_comment_discussion(did,requesterId,clientToken,body=c))

        pass

    def test_delete_blog(self):
        """
        Test case for delete_blog

        Delete blog
        """
        requesterId = None;
        clientToken = None;
        bid = 649503
        print(self.api.delete_blog(bid,requesterId,clientToken))

        pass

    def test_delete_blog_comment(self):
        """
        Test case for delete_blog_comment

        Delete blog comment
        """
        requesterId = None;
        clientToken = None;
        bcid = 649571
        print(self.api.delete_blog_comment(bcid,requesterId,clientToken))
        pass

    def test_delete_discussion(self):
        """
        Test case for delete_discussion

        Delete discussion
        """
        requesterId = None;
        clientToken = None;
        did = 649517
        print(self.api.delete_discussion(did,requesterId,clientToken))
        pass

    def test_delete_discussion_comment(self):
        """
        Test case for delete_discussion_comment

        Delete discussion comment
        """
        requesterId = None;
        clientToken = None;
        dcid = 649536
        print(self.api.delete_discussion_comment(dcid,requesterId,clientToken))
        pass

    def test_get_blog_comments(self):
        """
        Test case for get_blog_comments

        Get list of comments on blog
        """
        requesterId = None;
        clientToken = None;
        bid = 649503
        start = 0
        end = 10

        print(self.api.get_blog_comments(bid,start,end,requesterId,clientToken))
        pass

    def test_get_blogs(self):
        """
        Test case for get_blogs

        Get list of blogs
        """
        requesterId = None;
        clientToken = None;
        association = 533856
        start = 0
        end = 10
        print(self.api.get_blogs(association,start,end,requesterId,clientToken))
        pass

    def test_get_discussion_comments(self):
        """
        Test case for get_discussion_comments

        Get list of comments on discussion
        """
        requesterId = None;
        clientToken = None;
        did = 649517
        start = 0
        end = 10
        print(self.api.get_discussion_comments(did,start,end,requesterId,clientToken))

        pass

    def test_get_discussions(self):
        """
        Test case for get_discussions

        Get list of discussions
        """
        requesterId = None;
        clientToken = None;
        association = 533856
        start = 0
        end = 10
        print(self.api.get_discussions(association, start, end, requesterId, clientToken))
        pass

    def test_get_user_subscribed_blogs(self):
        """
        Test case for get_user_subscribed_blogs

        Get list of blogs subscribed by user
        """
        requesterId = None;
        clientToken = None;
        userId = 532893
        start = 0
        end = 10
        print(self.api.get_user_subscribed_blogs(userId,start,end,requesterId,clientToken))

        pass

    def test_get_user_subscribed_discussions(self):
        """
        Test case for get_user_subscribed_discussions

        Get list of discussions subscribed by user
        """
        requesterId = None;
        clientToken = None;
        userId = 532893
        start = 0
        end = 10
        print(self.api.get_user_subscribed_discussions(userId,start,end,requesterId,clientToken))
        pass

    def test_post_blog(self):
        """
        Test case for post_blog

        Post blog
        """
        requesterId = None;
        clientToken = None;
        b = Blog()
        b.association = 533856
        b.title = 'Test title'
        b.description = 'Test descriptionTest descriptionTest descriptionTest descriptionTest descriptionTest descriptionTest descriptionTest descriptionTest descriptionTest descriptionTest descriptionTest descriptionTest descriptionTest descriptionTest descriptionTest description'

        print(self.api.post_blog(requesterId,clientToken,body=b))

        pass

    def test_start_discussion(self):
        """
        Test case for start_discussion

        Start discussion
        """
        requesterId = None;
        clientToken = None;
        d = Discussion()
        d.association = 533856;
        d.subject = "today discussion subject"
        d.description = "today discussion subject description"

        print(self.api.start_discussion(requesterId,clientToken,body=d))


        pass

    def test_subscribe_blog(self):
        """
        Test case for subscribe_blog

        Subscribe blog
        """
        requesterId = None;
        clientToken = None;
        bid = 649503
        print(self.api.subscribe_blog(bid,requesterId,clientToken))
        pass

    def test_subscribe_discussion(self):
        """
        Test case for subscribe_discussion

        Subscribe discussion
        """
        requesterId = None;
        clientToken = None;
        did = 649517
        print(self.api.subscribe_discussion(did,requesterId,clientToken))
        pass

    def test_unsubscribe_blog(self):
        """
        Test case for unsubscribe_blog

        Unsubscribe blog
        """
        requesterId = None;
        clientToken = None;
        bid = 649503
        print(self.api.unsubscribe_blog(bid,requesterId,clientToken))
        pass

    def test_unsubscribe_discussion(self):
        """
        Test case for unsubscribe_discussion

        Unsubscribe discussion
        """
        requesterId = None;
        clientToken = None;
        did = 649517
        print(self.api.unsubscribe_discussion(did,requesterId,clientToken))
        pass

    def test_update_blog(self):
        """
        Test case for update_blog

        Update blog
        """
        requesterId = None;
        clientToken = None;
        bid = 649503
        btitle = 'Test title'
        bdesc = "Test DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest DescriptionTest Description"
        print(self.api.update_blog(bid,btitle,bdesc,requesterId,clientToken))
        pass

    def test_update_blog_comment(self):
        """
        Test case for update_blog_comment

        Update blog comment
        """
        requesterId = None;
        clientToken = None;
        cid = 649529
        comment = "Updated blog comment"
        print(self.api.update_blog_comment(cid,comment,requesterId,clientToken))
        pass

    def test_update_discussion(self):
        """
        Test case for update_discussion

        Update discussion
        """
        requesterId = None;
        clientToken = None;
        did = 649517
        dsub = "today discussion subject "
        ddesc = "today discussion description 1000"

        print(self.api.update_discussion(did,dsub,ddesc,requesterId,clientToken))
        pass

    def test_update_discussion_comment(self):
        """
        Test case for update_discussion_comment

        Update discussion comment
        """
        requesterId = None;
        clientToken = None;
        dcid = 649536
        dcomment = "Hello comment discussion"
        print(self.api.update_discussion_comment(dcid,dcomment,requesterId,clientToken))
        pass


if __name__ == '__main__':
    unittest.main()
