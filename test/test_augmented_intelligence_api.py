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
from iengage_client.apis.augmented_intelligence_api import AugmentedIntelligenceApi

class TestAugmentedIntelligenceApi(unittest.TestCase):
    """ AugmentedIntelligenceApi unit test stubs """

    def setUp(self):
        iengage_client.configuration.access_token = None
        self.api = iengage_client.apis.augmented_intelligence_api.AugmentedIntelligenceApi()

    def tearDown(self):
        pass


    def test_classify(self):
        """
        Test case for classify

        Classifies using your classifier
        """
        text = "Peace"
        id = 536852
        client_token = None

        api_response = self.api.classify(text,id,client_token);
        print(api_response)
        pass;



    def test_get_entities(self):
        """
        Test case for get_entities

        Extracts entities from text
        """
        id = 643570
        text = "Bug"
        client_token = None

        api_response = self.api.get_entities(id,text,client_token);
        print(api_response)

        pass

    def test_get_interaction_type(self):
        """
        Test case for get_interaction_type

        Returns the type of interaction
        """
        text = "Bug"
        client_token = None
        resp = self.api.get_interaction_type(text,client_token)
        print(resp)
        pass

    def test_get_keywords(self):
        """
        Test case for get_keywords

        Returns the keywords of the sentence
        """
        text = "Bug"
        client_token = None
        print(self.api.get_keywords(text,client_token))
        pass

    def test_get_popular_tag(self):
        """
        Test case for get_popular_tag

        Get list of popular tag of interactions
        """
        startTime = 20190101;
        endTime = 20190102;
        start = 0
        end = 10
        requester_id = None;
        client_token = None;
        print(self.api.get_popular_tag(startTime,endTime,start,end,requester_id,client_token))
        pass

    def test_get_sentiment(self):
        """
        Test case for get_sentiment

        Get sentiment count of interactions
        """
        startTime = 20190101;
        endTime = 20190102;
        requester_id = None;
        client_token = None;
        print(self.api.get_sentiment(startTime,endTime,requester_id,client_token))
        pass

    def test_get_tag_entity_sentiments(self):
        """
        Test case for get_tag_entity_sentiments

        Get list of tag entity sentiment
        """
        tagName = "Bug";
        startTime = 20190101;
        endTime = 20190102;
        start = 0
        end = 10
        requester_id = None;
        client_token = None;
        print(self.api.get_tag_entity_sentiments(tagName,startTime,endTime,start,end,requester_id,client_token))
        pass

    def test_sentiment(self):
        """
        Test case for sentiment

        Analyzes the sentiment of the content
        """
        text = "Bug"
        client_token = None
        print(self.api.sentiment(text,client_token))
        pass


if __name__ == '__main__':
    unittest.main()
