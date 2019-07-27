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


class InteractionCategory(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, category_id=None, category_name=None, category_description=None, interaction_type=None, created_date=None, modified_date=None, status=None, is_subscribed=False, association_id=None, user=None):
        """
        InteractionCategory - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'category_id': 'int',
            'category_name': 'str',
            'category_description': 'str',
            'interaction_type': 'str',
            'created_date': 'datetime',
            'modified_date': 'datetime',
            'status': 'int',
            'is_subscribed': 'bool',
            'association_id': 'str',
            'user': 'User'
        }

        self.attribute_map = {
            'category_id': 'categoryId',
            'category_name': 'categoryName',
            'category_description': 'categoryDescription',
            'interaction_type': 'interactionType',
            'created_date': 'createdDate',
            'modified_date': 'modifiedDate',
            'status': 'status',
            'is_subscribed': 'isSubscribed',
            'association_id': 'associationId',
            'user': 'user'
        }

        self._category_id = category_id
        self._category_name = category_name
        self._category_description = category_description
        self._interaction_type = interaction_type
        self._created_date = created_date
        self._modified_date = modified_date
        self._status = status
        self._is_subscribed = is_subscribed
        self._association_id = association_id
        self._user = user

    @property
    def category_id(self):
        """
        Gets the category_id of this InteractionCategory.


        :return: The category_id of this InteractionCategory.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """
        Sets the category_id of this InteractionCategory.


        :param category_id: The category_id of this InteractionCategory.
        :type: int
        """

        self._category_id = category_id

    @property
    def category_name(self):
        """
        Gets the category_name of this InteractionCategory.


        :return: The category_name of this InteractionCategory.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """
        Sets the category_name of this InteractionCategory.


        :param category_name: The category_name of this InteractionCategory.
        :type: str
        """

        self._category_name = category_name

    @property
    def category_description(self):
        """
        Gets the category_description of this InteractionCategory.


        :return: The category_description of this InteractionCategory.
        :rtype: str
        """
        return self._category_description

    @category_description.setter
    def category_description(self, category_description):
        """
        Sets the category_description of this InteractionCategory.


        :param category_description: The category_description of this InteractionCategory.
        :type: str
        """

        self._category_description = category_description

    @property
    def interaction_type(self):
        """
        Gets the interaction_type of this InteractionCategory.


        :return: The interaction_type of this InteractionCategory.
        :rtype: str
        """
        return self._interaction_type

    @interaction_type.setter
    def interaction_type(self, interaction_type):
        """
        Sets the interaction_type of this InteractionCategory.


        :param interaction_type: The interaction_type of this InteractionCategory.
        :type: str
        """

        self._interaction_type = interaction_type

    @property
    def created_date(self):
        """
        Gets the created_date of this InteractionCategory.


        :return: The created_date of this InteractionCategory.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this InteractionCategory.


        :param created_date: The created_date of this InteractionCategory.
        :type: datetime
        """

        self._created_date = created_date

    @property
    def modified_date(self):
        """
        Gets the modified_date of this InteractionCategory.


        :return: The modified_date of this InteractionCategory.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Sets the modified_date of this InteractionCategory.


        :param modified_date: The modified_date of this InteractionCategory.
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def status(self):
        """
        Gets the status of this InteractionCategory.


        :return: The status of this InteractionCategory.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InteractionCategory.


        :param status: The status of this InteractionCategory.
        :type: int
        """

        self._status = status

    @property
    def is_subscribed(self):
        """
        Gets the is_subscribed of this InteractionCategory.


        :return: The is_subscribed of this InteractionCategory.
        :rtype: bool
        """
        return self._is_subscribed

    @is_subscribed.setter
    def is_subscribed(self, is_subscribed):
        """
        Sets the is_subscribed of this InteractionCategory.


        :param is_subscribed: The is_subscribed of this InteractionCategory.
        :type: bool
        """

        self._is_subscribed = is_subscribed

    @property
    def association_id(self):
        """
        Gets the association_id of this InteractionCategory.


        :return: The association_id of this InteractionCategory.
        :rtype: str
        """
        return self._association_id

    @association_id.setter
    def association_id(self, association_id):
        """
        Sets the association_id of this InteractionCategory.


        :param association_id: The association_id of this InteractionCategory.
        :type: str
        """

        self._association_id = association_id

    @property
    def user(self):
        """
        Gets the user of this InteractionCategory.


        :return: The user of this InteractionCategory.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this InteractionCategory.


        :param user: The user of this InteractionCategory.
        :type: User
        """

        self._user = user

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
