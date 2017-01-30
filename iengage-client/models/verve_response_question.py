# coding: utf-8

"""
    Stakeholder engagement API

    This API enables Intelligent Engagement for your Business. iEngage is a platform that combines process, augmented intelligence and rewards to help you intelligently engage customers.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VerveResponseQuestion(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, status_code=None, message=None, list=None, data=None, records=None):
        """
        VerveResponseQuestion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status_code': 'str',
            'message': 'str',
            'list': 'list[Question]',
            'data': 'Question',
            'records': 'int'
        }

        self.attribute_map = {
            'status_code': 'statusCode',
            'message': 'message',
            'list': 'list',
            'data': 'data',
            'records': 'records'
        }

        self._status_code = status_code
        self._message = message
        self._list = list
        self._data = data
        self._records = records

    @property
    def status_code(self):
        """
        Gets the status_code of this VerveResponseQuestion.

        :return: The status_code of this VerveResponseQuestion.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """
        Sets the status_code of this VerveResponseQuestion.

        :param status_code: The status_code of this VerveResponseQuestion.
        :type: str
        """

        self._status_code = status_code

    @property
    def message(self):
        """
        Gets the message of this VerveResponseQuestion.

        :return: The message of this VerveResponseQuestion.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this VerveResponseQuestion.

        :param message: The message of this VerveResponseQuestion.
        :type: str
        """

        self._message = message

    @property
    def list(self):
        """
        Gets the list of this VerveResponseQuestion.

        :return: The list of this VerveResponseQuestion.
        :rtype: list[Question]
        """
        return self._list

    @list.setter
    def list(self, list):
        """
        Sets the list of this VerveResponseQuestion.

        :param list: The list of this VerveResponseQuestion.
        :type: list[Question]
        """

        self._list = list

    @property
    def data(self):
        """
        Gets the data of this VerveResponseQuestion.

        :return: The data of this VerveResponseQuestion.
        :rtype: Question
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this VerveResponseQuestion.

        :param data: The data of this VerveResponseQuestion.
        :type: Question
        """

        self._data = data

    @property
    def records(self):
        """
        Gets the records of this VerveResponseQuestion.

        :return: The records of this VerveResponseQuestion.
        :rtype: int
        """
        return self._records

    @records.setter
    def records(self, records):
        """
        Sets the records of this VerveResponseQuestion.

        :param records: The records of this VerveResponseQuestion.
        :type: int
        """

        self._records = records

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
