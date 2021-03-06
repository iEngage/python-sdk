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


class SentimentAnalytics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, positive=None, negative=None, neutral=None, total=None):
        """
        SentimentAnalytics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'positive': 'int',
            'negative': 'int',
            'neutral': 'int',
            'total': 'int'
        }

        self.attribute_map = {
            'positive': 'positive',
            'negative': 'negative',
            'neutral': 'neutral',
            'total': 'total'
        }

        self._positive = positive
        self._negative = negative
        self._neutral = neutral
        self._total = total

    @property
    def positive(self):
        """
        Gets the positive of this SentimentAnalytics.


        :return: The positive of this SentimentAnalytics.
        :rtype: int
        """
        return self._positive

    @positive.setter
    def positive(self, positive):
        """
        Sets the positive of this SentimentAnalytics.


        :param positive: The positive of this SentimentAnalytics.
        :type: int
        """

        self._positive = positive

    @property
    def negative(self):
        """
        Gets the negative of this SentimentAnalytics.


        :return: The negative of this SentimentAnalytics.
        :rtype: int
        """
        return self._negative

    @negative.setter
    def negative(self, negative):
        """
        Sets the negative of this SentimentAnalytics.


        :param negative: The negative of this SentimentAnalytics.
        :type: int
        """

        self._negative = negative

    @property
    def neutral(self):
        """
        Gets the neutral of this SentimentAnalytics.


        :return: The neutral of this SentimentAnalytics.
        :rtype: int
        """
        return self._neutral

    @neutral.setter
    def neutral(self, neutral):
        """
        Sets the neutral of this SentimentAnalytics.


        :param neutral: The neutral of this SentimentAnalytics.
        :type: int
        """

        self._neutral = neutral

    @property
    def total(self):
        """
        Gets the total of this SentimentAnalytics.


        :return: The total of this SentimentAnalytics.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this SentimentAnalytics.


        :param total: The total of this SentimentAnalytics.
        :type: int
        """

        self._total = total

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
