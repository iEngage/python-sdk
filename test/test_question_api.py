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
from iengage-client.apis.question_api import QuestionApi


class TestQuestionApi(unittest.TestCase):
    """ QuestionApi unit test stubs """

    def setUp(self):
        self.api = iengage-client.apis.question_api.QuestionApi()

    def tearDown(self):
        pass

    def test_add_answer(self):
        """
        Test case for add_answer

        Answer the specified question
        """
        pass

    def test_add_question(self):
        """
        Test case for add_question

        Share question without attachment
        """
        pass

    def test_add_question_0(self):
        """
        Test case for add_question_0

        Share question with attachment
        """
        pass

    def test_create_question_category(self):
        """
        Test case for create_question_category

        Create question category
        """
        pass

    def test_delete_answer(self):
        """
        Test case for delete_answer

        Delete answer
        """
        pass

    def test_delete_question(self):
        """
        Test case for delete_question

        Delete question
        """
        pass

    def test_delete_question_category(self):
        """
        Test case for delete_question_category

        Delete question category
        """
        pass

    def test_dislike_answer(self):
        """
        Test case for dislike_answer

        Dislike answer
        """
        pass

    def test_get_answers(self):
        """
        Test case for get_answers

        Get list of answers by questionId
        """
        pass

    def test_get_friends_questions(self):
        """
        Test case for get_friends_questions

        Get list of questions shared by friends
        """
        pass

    def test_get_question(self):
        """
        Test case for get_question

        Get question by id
        """
        pass

    def test_get_question_categories(self):
        """
        Test case for get_question_categories

        Get the list of question categories
        """
        pass

    def test_get_questions_for_user(self):
        """
        Test case for get_questions_for_user

        Get list of all questions visible to the user
        """
        pass

    def test_get_recommend_question(self):
        """
        Test case for get_recommend_question

        Get list of recommended questions
        """
        pass

    def test_get_recommended_questions_from_db(self):
        """
        Test case for get_recommended_questions_from_db

        Get list of recommended questions from DB
        """
        pass

    def test_get_recommended_users_from_db(self):
        """
        Test case for get_recommended_users_from_db

        Get list of recommended Users from DB
        """
        pass

    def test_get_user_questions(self):
        """
        Test case for get_user_questions

        Get list of questions shared by user
        """
        pass

    def test_get_user_subscribed_question_categories(self):
        """
        Test case for get_user_subscribed_question_categories

        Get list of question categories subscribed by the user
        """
        pass

    def test_get_user_subscribed_questions(self):
        """
        Test case for get_user_subscribed_questions

        Get list of questions subscribed by user
        """
        pass

    def test_like_answer(self):
        """
        Test case for like_answer

        Like answer
        """
        pass

    def test_mark_as_an_answer(self):
        """
        Test case for mark_as_an_answer

        Mark answer as a answer
        """
        pass

    def test_search_questions(self):
        """
        Test case for search_questions

        Get list of matching questions
        """
        pass

    def test_subscribe_question(self):
        """
        Test case for subscribe_question

        Subscribe question
        """
        pass

    def test_subscribe_question_category(self):
        """
        Test case for subscribe_question_category

        Subscribe question category
        """
        pass

    def test_unmark_as_an_answer(self):
        """
        Test case for unmark_as_an_answer

        Unmark answer as a answer
        """
        pass

    def test_unsubscribe_question(self):
        """
        Test case for unsubscribe_question

        Unsubscribe question
        """
        pass

    def test_unsubscribe_question_category(self):
        """
        Test case for unsubscribe_question_category

        Unsubscribe question category
        """
        pass

    def test_update_answer(self):
        """
        Test case for update_answer

        Update answer
        """
        pass

    def test_update_question(self):
        """
        Test case for update_question

        Update question
        """
        pass

    def test_update_question_category(self):
        """
        Test case for update_question_category

        Update question category
        """
        pass


if __name__ == '__main__':
    unittest.main()
