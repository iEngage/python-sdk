# coding: utf-8

"""
    iEngage 2.0 API

    This API enables Intelligent Engagement for your Business. iEngage is a platform that combines process, augmented intelligence and rewards to help you intelligently engage customers.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class QuestionCategory(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, category_id=None, category_name=None, category_description=None, category_type=None, created_date=None, modified_date=None, status=None, is_subscribed=False):
        """
        QuestionCategory - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'category_id': 'int',
            'category_name': 'str',
            'category_description': 'str',
            'category_type': 'str',
            'created_date': 'datetime',
            'modified_date': 'datetime',
            'status': 'int',
            'is_subscribed': 'bool'
        }

        self.attribute_map = {
            'category_id': 'categoryId',
            'category_name': 'categoryName',
            'category_description': 'categoryDescription',
            'category_type': 'categoryType',
            'created_date': 'createdDate',
            'modified_date': 'modifiedDate',
            'status': 'status',
            'is_subscribed': 'isSubscribed'
        }

        self._category_id = category_id
        self._category_name = category_name
        self._category_description = category_description
        self._category_type = category_type
        self._created_date = created_date
        self._modified_date = modified_date
        self._status = status
        self._is_subscribed = is_subscribed

    @property
    def category_id(self):
        """
        Gets the category_id of this QuestionCategory.

        :return: The category_id of this QuestionCategory.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """
        Sets the category_id of this QuestionCategory.

        :param category_id: The category_id of this QuestionCategory.
        :type: int
        """

        self._category_id = category_id

    @property
    def category_name(self):
        """
        Gets the category_name of this QuestionCategory.

        :return: The category_name of this QuestionCategory.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """
        Sets the category_name of this QuestionCategory.

        :param category_name: The category_name of this QuestionCategory.
        :type: str
        """

        self._category_name = category_name

    @property
    def category_description(self):
        """
        Gets the category_description of this QuestionCategory.

        :return: The category_description of this QuestionCategory.
        :rtype: str
        """
        return self._category_description

    @category_description.setter
    def category_description(self, category_description):
        """
        Sets the category_description of this QuestionCategory.

        :param category_description: The category_description of this QuestionCategory.
        :type: str
        """

        self._category_description = category_description

    @property
    def category_type(self):
        """
        Gets the category_type of this QuestionCategory.

        :return: The category_type of this QuestionCategory.
        :rtype: str
        """
        return self._category_type

    @category_type.setter
    def category_type(self, category_type):
        """
        Sets the category_type of this QuestionCategory.

        :param category_type: The category_type of this QuestionCategory.
        :type: str
        """

        self._category_type = category_type

    @property
    def created_date(self):
        """
        Gets the created_date of this QuestionCategory.

        :return: The created_date of this QuestionCategory.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this QuestionCategory.

        :param created_date: The created_date of this QuestionCategory.
        :type: datetime
        """

        self._created_date = created_date

    @property
    def modified_date(self):
        """
        Gets the modified_date of this QuestionCategory.

        :return: The modified_date of this QuestionCategory.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Sets the modified_date of this QuestionCategory.

        :param modified_date: The modified_date of this QuestionCategory.
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def status(self):
        """
        Gets the status of this QuestionCategory.

        :return: The status of this QuestionCategory.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this QuestionCategory.

        :param status: The status of this QuestionCategory.
        :type: int
        """

        self._status = status

    @property
    def is_subscribed(self):
        """
        Gets the is_subscribed of this QuestionCategory.

        :return: The is_subscribed of this QuestionCategory.
        :rtype: bool
        """
        return self._is_subscribed

    @is_subscribed.setter
    def is_subscribed(self, is_subscribed):
        """
        Sets the is_subscribed of this QuestionCategory.

        :param is_subscribed: The is_subscribed of this QuestionCategory.
        :type: bool
        """

        self._is_subscribed = is_subscribed

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
