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

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class NotificationApi(object):
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

    def add_notification(self, requester_id, client_token, **kwargs):
        """
        Create custom notification
        This service allows a user to create a notification. The following fields(key:value) are required to be present in the Notification JSON object. Refer to the Model & Model Schema of the expected JSON Object for the body of this API. **Required fields**  1. title  2. body  3. extraData  4. roleName OR toUser: { emailId }

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_notification(requester_id, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str requester_id: requesterId can be user id OR email address. (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param Notification body: 
        :param str access_token: Unique session token for user. To get access token user will have to authenticate
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_notification_with_http_info(requester_id, client_token, **kwargs)
        else:
            (data) = self.add_notification_with_http_info(requester_id, client_token, **kwargs)
            return data

    def add_notification_with_http_info(self, requester_id, client_token, **kwargs):
        """
        Create custom notification
        This service allows a user to create a notification. The following fields(key:value) are required to be present in the Notification JSON object. Refer to the Model & Model Schema of the expected JSON Object for the body of this API. **Required fields**  1. title  2. body  3. extraData  4. roleName OR toUser: { emailId }

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_notification_with_http_info(requester_id, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str requester_id: requesterId can be user id OR email address. (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param Notification body: 
        :param str access_token: Unique session token for user. To get access token user will have to authenticate
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['requester_id', 'client_token', 'body', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'requester_id' is set
        if ('requester_id' not in params) or (params['requester_id'] is None):
            raise ValueError("Missing the required parameter `requester_id` when calling `add_notification`")
        # verify the required parameter 'client_token' is set
        if ('client_token' not in params) or (params['client_token'] is None):
            raise ValueError("Missing the required parameter `client_token` when calling `add_notification`")

        resource_path = '/notifications'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'requester_id' in params:
            header_params['requesterId'] = params['requester_id']
        if 'access_token' in params:
            header_params['accessToken'] = params['access_token']
        if 'client_token' in params:
            header_params['clientToken'] = params['client_token']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['default']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='bool',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_notifications(self, type, start, end, requester_id, client_token, **kwargs):
        """
        Get list of notifications
        Return the list of notifications

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_notifications(type, start, end, requester_id, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str type:   /*   Type of count  1) UNREAD   2) READ   3)ALL   */ (required)
        :param int start: start, initial value start from 0 (required)
        :param int end: end (required)
        :param str requester_id: requesterId can be user id OR email address. (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param str fields: Filter fields in result list        /*   **A) Default values -**        1)notificationId       2)message       3)isRead       4)date        **A) Available values-**        1)notificationId       2)message       3)isRead       4)date       5)type       6)byUser       7)entity       8)parentEntity /n */
        :param str access_token: Unique session token for user. To get access token user will have to authenticate
        :return: VerveResponseNotificationList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_notifications_with_http_info(type, start, end, requester_id, client_token, **kwargs)
        else:
            (data) = self.get_notifications_with_http_info(type, start, end, requester_id, client_token, **kwargs)
            return data

    def get_notifications_with_http_info(self, type, start, end, requester_id, client_token, **kwargs):
        """
        Get list of notifications
        Return the list of notifications

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_notifications_with_http_info(type, start, end, requester_id, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str type:   /*   Type of count  1) UNREAD   2) READ   3)ALL   */ (required)
        :param int start: start, initial value start from 0 (required)
        :param int end: end (required)
        :param str requester_id: requesterId can be user id OR email address. (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param str fields: Filter fields in result list        /*   **A) Default values -**        1)notificationId       2)message       3)isRead       4)date        **A) Available values-**        1)notificationId       2)message       3)isRead       4)date       5)type       6)byUser       7)entity       8)parentEntity /n */
        :param str access_token: Unique session token for user. To get access token user will have to authenticate
        :return: VerveResponseNotificationList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'start', 'end', 'requester_id', 'client_token', 'fields', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_notifications" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params) or (params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `get_notifications`")
        # verify the required parameter 'start' is set
        if ('start' not in params) or (params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `get_notifications`")
        # verify the required parameter 'end' is set
        if ('end' not in params) or (params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `get_notifications`")
        # verify the required parameter 'requester_id' is set
        if ('requester_id' not in params) or (params['requester_id'] is None):
            raise ValueError("Missing the required parameter `requester_id` when calling `get_notifications`")
        # verify the required parameter 'client_token' is set
        if ('client_token' not in params) or (params['client_token'] is None):
            raise ValueError("Missing the required parameter `client_token` when calling `get_notifications`")

        resource_path = '/notifications'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'type' in params:
            query_params['type'] = params['type']
        if 'start' in params:
            query_params['start'] = params['start']
        if 'end' in params:
            query_params['end'] = params['end']
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}
        if 'requester_id' in params:
            header_params['requesterId'] = params['requester_id']
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
        if not header_params['Accept']:
            del header_params['Accept']

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
                                            response_type='VerveResponseNotificationList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def mark_all_notification_as_read(self, requester_id, client_token, **kwargs):
        """
        Mark all notification as read
        Allows the user to mark all the notification as read

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mark_all_notification_as_read(requester_id, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str requester_id: requesterId can be user id OR email address. (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param str access_token: Unique session token for user. To get access token user will have to authenticate
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.mark_all_notification_as_read_with_http_info(requester_id, client_token, **kwargs)
        else:
            (data) = self.mark_all_notification_as_read_with_http_info(requester_id, client_token, **kwargs)
            return data

    def mark_all_notification_as_read_with_http_info(self, requester_id, client_token, **kwargs):
        """
        Mark all notification as read
        Allows the user to mark all the notification as read

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mark_all_notification_as_read_with_http_info(requester_id, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str requester_id: requesterId can be user id OR email address. (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param str access_token: Unique session token for user. To get access token user will have to authenticate
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['requester_id', 'client_token', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mark_all_notification_as_read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'requester_id' is set
        if ('requester_id' not in params) or (params['requester_id'] is None):
            raise ValueError("Missing the required parameter `requester_id` when calling `mark_all_notification_as_read`")
        # verify the required parameter 'client_token' is set
        if ('client_token' not in params) or (params['client_token'] is None):
            raise ValueError("Missing the required parameter `client_token` when calling `mark_all_notification_as_read`")

        resource_path = '/notifications/read/all'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'requester_id' in params:
            header_params['requesterId'] = params['requester_id']
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
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['default']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='bool',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def mark_notification_as_read(self, notification_id, requester_id, client_token, **kwargs):
        """
        Mark notification as read
        Allows the user to mark the notification as read

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mark_notification_as_read(notification_id, requester_id, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int notification_id: notification Id (required)
        :param str requester_id: requesterId can be user id OR email address. (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param str access_token: Unique session token for user. To get access token user will have to authenticate
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.mark_notification_as_read_with_http_info(notification_id, requester_id, client_token, **kwargs)
        else:
            (data) = self.mark_notification_as_read_with_http_info(notification_id, requester_id, client_token, **kwargs)
            return data

    def mark_notification_as_read_with_http_info(self, notification_id, requester_id, client_token, **kwargs):
        """
        Mark notification as read
        Allows the user to mark the notification as read

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mark_notification_as_read_with_http_info(notification_id, requester_id, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int notification_id: notification Id (required)
        :param str requester_id: requesterId can be user id OR email address. (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param str access_token: Unique session token for user. To get access token user will have to authenticate
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['notification_id', 'requester_id', 'client_token', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mark_notification_as_read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'notification_id' is set
        if ('notification_id' not in params) or (params['notification_id'] is None):
            raise ValueError("Missing the required parameter `notification_id` when calling `mark_notification_as_read`")
        # verify the required parameter 'requester_id' is set
        if ('requester_id' not in params) or (params['requester_id'] is None):
            raise ValueError("Missing the required parameter `requester_id` when calling `mark_notification_as_read`")
        # verify the required parameter 'client_token' is set
        if ('client_token' not in params) or (params['client_token'] is None):
            raise ValueError("Missing the required parameter `client_token` when calling `mark_notification_as_read`")

        resource_path = '/notifications/read/{notificationId}'.replace('{format}', 'json')
        path_params = {}
        if 'notification_id' in params:
            path_params['notificationId'] = params['notification_id']

        query_params = {}

        header_params = {}
        if 'requester_id' in params:
            header_params['requesterId'] = params['requester_id']
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
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['default']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='bool',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def notification_count(self, type, requester_id, client_token, **kwargs):
        """
        Get notifications count
        Returns the notification count

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.notification_count(type, requester_id, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str type:   /*  Type of count  1) UNREAD   2) READ   3)ALL   */ (required)
        :param str requester_id: requesterId can be user id OR email address. (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param str access_token: Unique session token for user. To get access token user will have to authenticate
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.notification_count_with_http_info(type, requester_id, client_token, **kwargs)
        else:
            (data) = self.notification_count_with_http_info(type, requester_id, client_token, **kwargs)
            return data

    def notification_count_with_http_info(self, type, requester_id, client_token, **kwargs):
        """
        Get notifications count
        Returns the notification count

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.notification_count_with_http_info(type, requester_id, client_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str type:   /*  Type of count  1) UNREAD   2) READ   3)ALL   */ (required)
        :param str requester_id: requesterId can be user id OR email address. (required)
        :param str client_token: Use the Client Token. Please generate it from the Applications section under the Production & Sandbox tabs (required)
        :param str access_token: Unique session token for user. To get access token user will have to authenticate
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'requester_id', 'client_token', 'access_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method notification_count" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params) or (params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `notification_count`")
        # verify the required parameter 'requester_id' is set
        if ('requester_id' not in params) or (params['requester_id'] is None):
            raise ValueError("Missing the required parameter `requester_id` when calling `notification_count`")
        # verify the required parameter 'client_token' is set
        if ('client_token' not in params) or (params['client_token'] is None):
            raise ValueError("Missing the required parameter `client_token` when calling `notification_count`")

        resource_path = '/notifications/count'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'type' in params:
            query_params['type'] = params['type']

        header_params = {}
        if 'requester_id' in params:
            header_params['requesterId'] = params['requester_id']
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
        if not header_params['Accept']:
            del header_params['Accept']

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
                                            response_type='int',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
