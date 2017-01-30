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


class CommandInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, command_class=None, command_name=None):
        """
        CommandInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'command_class': 'str',
            'command_name': 'str'
        }

        self.attribute_map = {
            'command_class': 'commandClass',
            'command_name': 'commandName'
        }

        self._command_class = command_class
        self._command_name = command_name

    @property
    def command_class(self):
        """
        Gets the command_class of this CommandInfo.

        :return: The command_class of this CommandInfo.
        :rtype: str
        """
        return self._command_class

    @command_class.setter
    def command_class(self, command_class):
        """
        Sets the command_class of this CommandInfo.

        :param command_class: The command_class of this CommandInfo.
        :type: str
        """

        self._command_class = command_class

    @property
    def command_name(self):
        """
        Gets the command_name of this CommandInfo.

        :return: The command_name of this CommandInfo.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        """
        Sets the command_name of this CommandInfo.

        :param command_name: The command_name of this CommandInfo.
        :type: str
        """

        self._command_name = command_name

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