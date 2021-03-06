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


class NER(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, serial=None, object=None, entity=None):
        """
        NER - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'serial': 'int',
            'object': 'str',
            'entity': 'str'
        }

        self.attribute_map = {
            'serial': 'serial',
            'object': 'object',
            'entity': 'entity'
        }

        self._serial = serial
        self._object = object
        self._entity = entity

    @property
    def serial(self):
        """
        Gets the serial of this NER.


        :return: The serial of this NER.
        :rtype: int
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this NER.


        :param serial: The serial of this NER.
        :type: int
        """

        self._serial = serial

    @property
    def object(self):
        """
        Gets the object of this NER.


        :return: The object of this NER.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this NER.


        :param object: The object of this NER.
        :type: str
        """

        self._object = object

    @property
    def entity(self):
        """
        Gets the entity of this NER.


        :return: The entity of this NER.
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this NER.


        :param entity: The entity of this NER.
        :type: str
        """

        self._entity = entity

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
