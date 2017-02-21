# coding: utf-8

"""
    Stakeholder engagement API

    This API enables Intelligent Engagement for your Business. iEngage is a platform that combines process, augmented intelligence and rewards to help you intelligently engage customers.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AugmentedIntelligenceApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_interaction(self, text, logged_in_user_id, access_token, client_token, **kwargs):
        """
        Get the type of interaction
        Classifies text to question, complaint or suggestion
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_interaction(text, logged_in_user_id, access_token, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str text: Text to be classified (required)
        :param str logged_in_user_id: User id of logged / authenticated user (required)
        :param str access_token: Unique session token for user. To get access token user will have to authenticate (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :return: VerveResponseFlowFinder
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_interaction_with_http_info(text, logged_in_user_id, access_token, client_token, **kwargs)
        else:
            (data) = self.get_interaction_with_http_info(text, logged_in_user_id, access_token, client_token, **kwargs)
            return data

    def get_interaction_with_http_info(self, text, logged_in_user_id, access_token, client_token, **kwargs):
        """
        Get the type of interaction
        Classifies text to question, complaint or suggestion
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_interaction_with_http_info(text, logged_in_user_id, access_token, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str text: Text to be classified (required)
        :param str logged_in_user_id: User id of logged / authenticated user (required)
        :param str access_token: Unique session token for user. To get access token user will have to authenticate (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :return: VerveResponseFlowFinder
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['text', 'logged_in_user_id', 'access_token', 'client_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_interaction" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'text' is set
        if ('text' not in params) or (params['text'] is None):
            raise ValueError("Missing the required parameter `text` when calling `get_interaction`")
        # verify the required parameter 'logged_in_user_id' is set
        if ('logged_in_user_id' not in params) or (params['logged_in_user_id'] is None):
            raise ValueError("Missing the required parameter `logged_in_user_id` when calling `get_interaction`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_interaction`")
        # verify the required parameter 'client_token' is set
        if ('client_token' not in params) or (params['client_token'] is None):
            raise ValueError("Missing the required parameter `client_token` when calling `get_interaction`")


        collection_formats = {}

        resource_path = '/machineLearning/interactionType'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'text' in params:
            query_params['text'] = params['text']

        header_params = {}
        if 'logged_in_user_id' in params:
            header_params['loggedInUserId'] = params['logged_in_user_id']
        if 'access_token' in params:
            header_params['accessToken'] = params['access_token']
        if 'client_token' in params:
            header_params['clientToken'] = params['client_token']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['default']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='VerveResponseFlowFinder',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_popular_tag(self, start_time, end_time, start, end, logged_in_user_id, access_token, client_token, **kwargs):
        """
        Get list of popular tag of interactions
        Return the most popular tag of given interaction type
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_popular_tag(start_time, end_time, start, end, logged_in_user_id, access_token, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int start_time: start time (required)
        :param int end_time: end time (required)
        :param int start: start (required)
        :param int end: end (required)
        :param str logged_in_user_id: User id of logged / authenticated user (required)
        :param str access_token: Unique session token for user. To get access token user will have to authenticate (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param str interaction_type: Interaction Type <br/>1)Question<br/>2)Complaint<br/>3)Idea<br/>4)Blog<br/>5)Discussion
        :param str sentiment_type: Sentiment Type <br/>1)Positive<br/>2)Negative<br/> 3)Neutral
        :param str additional_information: additional information
        :return: VerveResponseTagList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_popular_tag_with_http_info(start_time, end_time, start, end, logged_in_user_id, access_token, client_token, **kwargs)
        else:
            (data) = self.get_popular_tag_with_http_info(start_time, end_time, start, end, logged_in_user_id, access_token, client_token, **kwargs)
            return data

    def get_popular_tag_with_http_info(self, start_time, end_time, start, end, logged_in_user_id, access_token, client_token, **kwargs):
        """
        Get list of popular tag of interactions
        Return the most popular tag of given interaction type
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_popular_tag_with_http_info(start_time, end_time, start, end, logged_in_user_id, access_token, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int start_time: start time (required)
        :param int end_time: end time (required)
        :param int start: start (required)
        :param int end: end (required)
        :param str logged_in_user_id: User id of logged / authenticated user (required)
        :param str access_token: Unique session token for user. To get access token user will have to authenticate (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param str interaction_type: Interaction Type <br/>1)Question<br/>2)Complaint<br/>3)Idea<br/>4)Blog<br/>5)Discussion
        :param str sentiment_type: Sentiment Type <br/>1)Positive<br/>2)Negative<br/> 3)Neutral
        :param str additional_information: additional information
        :return: VerveResponseTagList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_time', 'end_time', 'start', 'end', 'logged_in_user_id', 'access_token', 'client_token', 'interaction_type', 'sentiment_type', 'additional_information']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_popular_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start_time' is set
        if ('start_time' not in params) or (params['start_time'] is None):
            raise ValueError("Missing the required parameter `start_time` when calling `get_popular_tag`")
        # verify the required parameter 'end_time' is set
        if ('end_time' not in params) or (params['end_time'] is None):
            raise ValueError("Missing the required parameter `end_time` when calling `get_popular_tag`")
        # verify the required parameter 'start' is set
        if ('start' not in params) or (params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `get_popular_tag`")
        # verify the required parameter 'end' is set
        if ('end' not in params) or (params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `get_popular_tag`")
        # verify the required parameter 'logged_in_user_id' is set
        if ('logged_in_user_id' not in params) or (params['logged_in_user_id'] is None):
            raise ValueError("Missing the required parameter `logged_in_user_id` when calling `get_popular_tag`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_popular_tag`")
        # verify the required parameter 'client_token' is set
        if ('client_token' not in params) or (params['client_token'] is None):
            raise ValueError("Missing the required parameter `client_token` when calling `get_popular_tag`")


        collection_formats = {}

        resource_path = '/analytics/popular/tags'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'interaction_type' in params:
            query_params['interactionType'] = params['interaction_type']
        if 'sentiment_type' in params:
            query_params['sentimentType'] = params['sentiment_type']
        if 'additional_information' in params:
            query_params['additionalInformation'] = params['additional_information']
        if 'start_time' in params:
            query_params['startTime'] = params['start_time']
        if 'end_time' in params:
            query_params['endTime'] = params['end_time']
        if 'start' in params:
            query_params['start'] = params['start']
        if 'end' in params:
            query_params['end'] = params['end']

        header_params = {}
        if 'logged_in_user_id' in params:
            header_params['loggedInUserId'] = params['logged_in_user_id']
        if 'access_token' in params:
            header_params['accessToken'] = params['access_token']
        if 'client_token' in params:
            header_params['clientToken'] = params['client_token']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['default']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='VerveResponseTagList',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_sentiment(self, start_time, end_time, logged_in_user_id, access_token, client_token, **kwargs):
        """
        Get sentiment count of interactions
        Returns the sum of the sentiment count of given interaction type
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sentiment(start_time, end_time, logged_in_user_id, access_token, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int start_time: start time (required)
        :param int end_time: end time (required)
        :param str logged_in_user_id: User id of logged / authenticated user (required)
        :param str access_token: Unique session token for user. To get access token user will have to authenticate (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param str interaction_type: Interaction Type <br/>1)Question<br/>2)Complaint<br/>3)Idea<br/>4)Blog<br/>5)Discussion
        :param str additional_information: additional information
        :return: VerveResponseSentimentAnalytics
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_sentiment_with_http_info(start_time, end_time, logged_in_user_id, access_token, client_token, **kwargs)
        else:
            (data) = self.get_sentiment_with_http_info(start_time, end_time, logged_in_user_id, access_token, client_token, **kwargs)
            return data

    def get_sentiment_with_http_info(self, start_time, end_time, logged_in_user_id, access_token, client_token, **kwargs):
        """
        Get sentiment count of interactions
        Returns the sum of the sentiment count of given interaction type
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sentiment_with_http_info(start_time, end_time, logged_in_user_id, access_token, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int start_time: start time (required)
        :param int end_time: end time (required)
        :param str logged_in_user_id: User id of logged / authenticated user (required)
        :param str access_token: Unique session token for user. To get access token user will have to authenticate (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param str interaction_type: Interaction Type <br/>1)Question<br/>2)Complaint<br/>3)Idea<br/>4)Blog<br/>5)Discussion
        :param str additional_information: additional information
        :return: VerveResponseSentimentAnalytics
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_time', 'end_time', 'logged_in_user_id', 'access_token', 'client_token', 'interaction_type', 'additional_information']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sentiment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start_time' is set
        if ('start_time' not in params) or (params['start_time'] is None):
            raise ValueError("Missing the required parameter `start_time` when calling `get_sentiment`")
        # verify the required parameter 'end_time' is set
        if ('end_time' not in params) or (params['end_time'] is None):
            raise ValueError("Missing the required parameter `end_time` when calling `get_sentiment`")
        # verify the required parameter 'logged_in_user_id' is set
        if ('logged_in_user_id' not in params) or (params['logged_in_user_id'] is None):
            raise ValueError("Missing the required parameter `logged_in_user_id` when calling `get_sentiment`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_sentiment`")
        # verify the required parameter 'client_token' is set
        if ('client_token' not in params) or (params['client_token'] is None):
            raise ValueError("Missing the required parameter `client_token` when calling `get_sentiment`")


        collection_formats = {}

        resource_path = '/analytics/sentiments'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'interaction_type' in params:
            query_params['interactionType'] = params['interaction_type']
        if 'additional_information' in params:
            query_params['additionalInformation'] = params['additional_information']
        if 'start_time' in params:
            query_params['startTime'] = params['start_time']
        if 'end_time' in params:
            query_params['endTime'] = params['end_time']

        header_params = {}
        if 'logged_in_user_id' in params:
            header_params['loggedInUserId'] = params['logged_in_user_id']
        if 'access_token' in params:
            header_params['accessToken'] = params['access_token']
        if 'client_token' in params:
            header_params['clientToken'] = params['client_token']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['default']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='VerveResponseSentimentAnalytics',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_tag_entity_sentiments(self, tag_name, start_time, end_time, start, end, logged_in_user_id, access_token, client_token, **kwargs):
        """
        Get list of tag entity sentiment
        Return the list of tag entity sentiments
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tag_entity_sentiments(tag_name, start_time, end_time, start, end, logged_in_user_id, access_token, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag_name: tag name (required)
        :param int start_time: start time (required)
        :param int end_time: end time (required)
        :param int start: start (required)
        :param int end: end (required)
        :param str logged_in_user_id: User id of logged / authenticated user (required)
        :param str access_token: Unique session token for user. To get access token user will have to authenticate (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param str sentiment_type: Sentiment Type <br/>1)Positive<br/>2)Negative<br/>3)Neutral
        :param str additional_information: additional information
        :return: VerveResponseEntitySentimentList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_tag_entity_sentiments_with_http_info(tag_name, start_time, end_time, start, end, logged_in_user_id, access_token, client_token, **kwargs)
        else:
            (data) = self.get_tag_entity_sentiments_with_http_info(tag_name, start_time, end_time, start, end, logged_in_user_id, access_token, client_token, **kwargs)
            return data

    def get_tag_entity_sentiments_with_http_info(self, tag_name, start_time, end_time, start, end, logged_in_user_id, access_token, client_token, **kwargs):
        """
        Get list of tag entity sentiment
        Return the list of tag entity sentiments
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tag_entity_sentiments_with_http_info(tag_name, start_time, end_time, start, end, logged_in_user_id, access_token, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag_name: tag name (required)
        :param int start_time: start time (required)
        :param int end_time: end time (required)
        :param int start: start (required)
        :param int end: end (required)
        :param str logged_in_user_id: User id of logged / authenticated user (required)
        :param str access_token: Unique session token for user. To get access token user will have to authenticate (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param str sentiment_type: Sentiment Type <br/>1)Positive<br/>2)Negative<br/>3)Neutral
        :param str additional_information: additional information
        :return: VerveResponseEntitySentimentList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_name', 'start_time', 'end_time', 'start', 'end', 'logged_in_user_id', 'access_token', 'client_token', 'sentiment_type', 'additional_information']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tag_entity_sentiments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_name' is set
        if ('tag_name' not in params) or (params['tag_name'] is None):
            raise ValueError("Missing the required parameter `tag_name` when calling `get_tag_entity_sentiments`")
        # verify the required parameter 'start_time' is set
        if ('start_time' not in params) or (params['start_time'] is None):
            raise ValueError("Missing the required parameter `start_time` when calling `get_tag_entity_sentiments`")
        # verify the required parameter 'end_time' is set
        if ('end_time' not in params) or (params['end_time'] is None):
            raise ValueError("Missing the required parameter `end_time` when calling `get_tag_entity_sentiments`")
        # verify the required parameter 'start' is set
        if ('start' not in params) or (params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `get_tag_entity_sentiments`")
        # verify the required parameter 'end' is set
        if ('end' not in params) or (params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `get_tag_entity_sentiments`")
        # verify the required parameter 'logged_in_user_id' is set
        if ('logged_in_user_id' not in params) or (params['logged_in_user_id'] is None):
            raise ValueError("Missing the required parameter `logged_in_user_id` when calling `get_tag_entity_sentiments`")
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params) or (params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `get_tag_entity_sentiments`")
        # verify the required parameter 'client_token' is set
        if ('client_token' not in params) or (params['client_token'] is None):
            raise ValueError("Missing the required parameter `client_token` when calling `get_tag_entity_sentiments`")


        collection_formats = {}

        resource_path = '/analytics/tag/entitySentiment'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'tag_name' in params:
            query_params['tagName'] = params['tag_name']
        if 'sentiment_type' in params:
            query_params['sentimentType'] = params['sentiment_type']
        if 'additional_information' in params:
            query_params['additionalInformation'] = params['additional_information']
        if 'start_time' in params:
            query_params['startTime'] = params['start_time']
        if 'end_time' in params:
            query_params['endTime'] = params['end_time']
        if 'start' in params:
            query_params['start'] = params['start']
        if 'end' in params:
            query_params['end'] = params['end']

        header_params = {}
        if 'logged_in_user_id' in params:
            header_params['loggedInUserId'] = params['logged_in_user_id']
        if 'access_token' in params:
            header_params['accessToken'] = params['access_token']
        if 'client_token' in params:
            header_params['clientToken'] = params['client_token']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['default']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='VerveResponseEntitySentimentList',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
