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
from iengage-client.apis.interaction_api import InteractionApi


class TestInteractionApi(unittest.TestCase):
    """ InteractionApi unit test stubs """

    def setUp(self):
        self.api = iengage-client.apis.interaction_api.InteractionApi()

    def tearDown(self):
        pass

    def test_add_interaction(self):
        """
        Test case for add_interaction

        Share interaction without attachment
        """
        pass

    def test_add_interaction_0(self):
        """
        Test case for add_interaction_0

        Share interaction with attachment
        """
        pass

    def test_add_response(self):
        """
        Test case for add_response

        Response the specified interaction
        """
        pass

    def test_create_interaction_category(self):
        """
        Test case for create_interaction_category

        Create interaction category
        """
        pass

    def test_delete_interaction(self):
        """
        Test case for delete_interaction

        Delete interaction
        """
        pass

    def test_delete_interaction_category(self):
        """
        Test case for delete_interaction_category

        Delete interaction category
        """
        pass

    def test_delete_response(self):
        """
        Test case for delete_response

        Delete response
        """
        pass

    def test_dislike_response(self):
        """
        Test case for dislike_response

        Dislike response
        """
        pass

    def test_get_friends_interactions(self):
        """
        Test case for get_friends_interactions

        Get list of interactions shared by friends
        """
        pass

    def test_get_interaction(self):
        """
        Test case for get_interaction

        Get interaction by id
        """
        pass

    def test_get_interaction_categories(self):
        """
        Test case for get_interaction_categories

        Get the list of interaction categories
        """
        pass

    def test_get_interactions_for_user(self):
        """
        Test case for get_interactions_for_user

        Get list of all interactions visible to the user
        """
        pass

    def test_get_recommend_interactions(self):
        """
        Test case for get_recommend_interactions

        Get list of recommended interactions
        """
        pass

    def test_get_recommended_interactins_from_db(self):
        """
        Test case for get_recommended_interactins_from_db

        Get list of recommended interactions from DB
        """
        pass

    def test_get_recommended_users_from_db(self):
        """
        Test case for get_recommended_users_from_db

        Get list of recommended Users from DB
        """
        pass

    def test_get_responses(self):
        """
        Test case for get_responses

        Get list of responses by interactionId
        """
        pass

    def test_get_user_interactions(self):
        """
        Test case for get_user_interactions

        Get list of interactions shared by user
        """
        pass

    def test_get_user_subscribed_interaction_categories(self):
        """
        Test case for get_user_subscribed_interaction_categories

        Get list of interaction categories subscribed by the user
        """
        pass

    def test_get_user_subscribed_interactions(self):
        """
        Test case for get_user_subscribed_interactions

        Get list of interactions subscribed by user
        """
        pass

    def test_like_response(self):
        """
        Test case for like_response

        Like response
        """
        pass

    def test_mark_as_an_response(self):
        """
        Test case for mark_as_an_response

        Mark response as a response
        """
        pass

    def test_search_interactions(self):
        """
        Test case for search_interactions

        Get list of matching interactions
        """
        pass

    def test_subscribe_interactin_category(self):
        """
        Test case for subscribe_interactin_category

        Subscribe interaction category
        """
        pass

    def test_subscribe_interaction(self):
        """
        Test case for subscribe_interaction

        Subscribe interaction
        """
        pass

    def test_unmark_as_an_response(self):
        """
        Test case for unmark_as_an_response

        Unmark response as a response
        """
        pass

    def test_unsubscribe_interactin_category(self):
        """
        Test case for unsubscribe_interactin_category

        Unsubscribe interaction category
        """
        pass

    def test_unsubscribe_interaction(self):
        """
        Test case for unsubscribe_interaction

        Unsubscribe interaction
        """
        pass

    def test_update_interaction(self):
        """
        Test case for update_interaction

        Update interaction
        """
        pass

    def test_update_interaction_category(self):
        """
        Test case for update_interaction_category

        Update interaction category
        """
        pass

    def test_update_response(self):
        """
        Test case for update_response

        Update response
        """
        pass


if __name__ == '__main__':
    unittest.main()
