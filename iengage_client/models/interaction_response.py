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

from pprint import pformat
from six import iteritems
import re


class InteractionResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, response_id=None, response_description=None, interaction_id=None, responding_user=None, created_date=None, is_marked_response=False, no_of_likes=None, no_of_dislikes=None, reply_count=None, is_liked=False, is_disliked=False, interaction_type=None):
        """
        InteractionResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'response_id': 'int',
            'response_description': 'str',
            'interaction_id': 'int',
            'responding_user': 'User',
            'created_date': 'datetime',
            'is_marked_response': 'bool',
            'no_of_likes': 'int',
            'no_of_dislikes': 'int',
            'reply_count': 'int',
            'is_liked': 'bool',
            'is_disliked': 'bool',
            'interaction_type': 'str'
        }

        self.attribute_map = {
            'response_id': 'responseId',
            'response_description': 'responseDescription',
            'interaction_id': 'interactionId',
            'responding_user': 'respondingUser',
            'created_date': 'createdDate',
            'is_marked_response': 'isMarkedResponse',
            'no_of_likes': 'noOfLikes',
            'no_of_dislikes': 'noOfDislikes',
            'reply_count': 'replyCount',
            'is_liked': 'isLiked',
            'is_disliked': 'isDisliked',
            'interaction_type': 'interactionType'
        }

        self._response_id = response_id
        self._response_description = response_description
        self._interaction_id = interaction_id
        self._responding_user = responding_user
        self._created_date = created_date
        self._is_marked_response = is_marked_response
        self._no_of_likes = no_of_likes
        self._no_of_dislikes = no_of_dislikes
        self._reply_count = reply_count
        self._is_liked = is_liked
        self._is_disliked = is_disliked
        self._interaction_type = interaction_type

    @property
    def response_id(self):
        """
        Gets the response_id of this InteractionResponse.


        :return: The response_id of this InteractionResponse.
        :rtype: int
        """
        return self._response_id

    @response_id.setter
    def response_id(self, response_id):
        """
        Sets the response_id of this InteractionResponse.


        :param response_id: The response_id of this InteractionResponse.
        :type: int
        """

        self._response_id = response_id

    @property
    def response_description(self):
        """
        Gets the response_description of this InteractionResponse.


        :return: The response_description of this InteractionResponse.
        :rtype: str
        """
        return self._response_description

    @response_description.setter
    def response_description(self, response_description):
        """
        Sets the response_description of this InteractionResponse.


        :param response_description: The response_description of this InteractionResponse.
        :type: str
        """

        self._response_description = response_description

    @property
    def interaction_id(self):
        """
        Gets the interaction_id of this InteractionResponse.


        :return: The interaction_id of this InteractionResponse.
        :rtype: int
        """
        return self._interaction_id

    @interaction_id.setter
    def interaction_id(self, interaction_id):
        """
        Sets the interaction_id of this InteractionResponse.


        :param interaction_id: The interaction_id of this InteractionResponse.
        :type: int
        """

        self._interaction_id = interaction_id

    @property
    def responding_user(self):
        """
        Gets the responding_user of this InteractionResponse.


        :return: The responding_user of this InteractionResponse.
        :rtype: User
        """
        return self._responding_user

    @responding_user.setter
    def responding_user(self, responding_user):
        """
        Sets the responding_user of this InteractionResponse.


        :param responding_user: The responding_user of this InteractionResponse.
        :type: User
        """

        self._responding_user = responding_user

    @property
    def created_date(self):
        """
        Gets the created_date of this InteractionResponse.


        :return: The created_date of this InteractionResponse.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this InteractionResponse.


        :param created_date: The created_date of this InteractionResponse.
        :type: datetime
        """

        self._created_date = created_date

    @property
    def is_marked_response(self):
        """
        Gets the is_marked_response of this InteractionResponse.


        :return: The is_marked_response of this InteractionResponse.
        :rtype: bool
        """
        return self._is_marked_response

    @is_marked_response.setter
    def is_marked_response(self, is_marked_response):
        """
        Sets the is_marked_response of this InteractionResponse.


        :param is_marked_response: The is_marked_response of this InteractionResponse.
        :type: bool
        """

        self._is_marked_response = is_marked_response

    @property
    def no_of_likes(self):
        """
        Gets the no_of_likes of this InteractionResponse.


        :return: The no_of_likes of this InteractionResponse.
        :rtype: int
        """
        return self._no_of_likes

    @no_of_likes.setter
    def no_of_likes(self, no_of_likes):
        """
        Sets the no_of_likes of this InteractionResponse.


        :param no_of_likes: The no_of_likes of this InteractionResponse.
        :type: int
        """

        self._no_of_likes = no_of_likes

    @property
    def no_of_dislikes(self):
        """
        Gets the no_of_dislikes of this InteractionResponse.


        :return: The no_of_dislikes of this InteractionResponse.
        :rtype: int
        """
        return self._no_of_dislikes

    @no_of_dislikes.setter
    def no_of_dislikes(self, no_of_dislikes):
        """
        Sets the no_of_dislikes of this InteractionResponse.


        :param no_of_dislikes: The no_of_dislikes of this InteractionResponse.
        :type: int
        """

        self._no_of_dislikes = no_of_dislikes

    @property
    def reply_count(self):
        """
        Gets the reply_count of this InteractionResponse.


        :return: The reply_count of this InteractionResponse.
        :rtype: int
        """
        return self._reply_count

    @reply_count.setter
    def reply_count(self, reply_count):
        """
        Sets the reply_count of this InteractionResponse.


        :param reply_count: The reply_count of this InteractionResponse.
        :type: int
        """

        self._reply_count = reply_count

    @property
    def is_liked(self):
        """
        Gets the is_liked of this InteractionResponse.


        :return: The is_liked of this InteractionResponse.
        :rtype: bool
        """
        return self._is_liked

    @is_liked.setter
    def is_liked(self, is_liked):
        """
        Sets the is_liked of this InteractionResponse.


        :param is_liked: The is_liked of this InteractionResponse.
        :type: bool
        """

        self._is_liked = is_liked

    @property
    def is_disliked(self):
        """
        Gets the is_disliked of this InteractionResponse.


        :return: The is_disliked of this InteractionResponse.
        :rtype: bool
        """
        return self._is_disliked

    @is_disliked.setter
    def is_disliked(self, is_disliked):
        """
        Sets the is_disliked of this InteractionResponse.


        :param is_disliked: The is_disliked of this InteractionResponse.
        :type: bool
        """

        self._is_disliked = is_disliked

    @property
    def interaction_type(self):
        """
        Gets the interaction_type of this InteractionResponse.


        :return: The interaction_type of this InteractionResponse.
        :rtype: str
        """
        return self._interaction_type

    @interaction_type.setter
    def interaction_type(self, interaction_type):
        """
        Sets the interaction_type of this InteractionResponse.


        :param interaction_type: The interaction_type of this InteractionResponse.
        :type: str
        """

        self._interaction_type = interaction_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
