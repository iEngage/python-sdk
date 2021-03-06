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


class Blog(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, blog_id=None, title=None, description=None, user=None, creation_time=None, association=None, sentiment=None, sentiment_details=None, sentiment_weightage=None, entity=None):
        """
        Blog - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'blog_id': 'int',
            'title': 'str',
            'description': 'str',
            'user': 'User',
            'creation_time': 'datetime',
            'association': 'int',
            'sentiment': 'str',
            'sentiment_details': 'Sentiment',
            'sentiment_weightage': 'float',
            'entity': 'list[NER]'
        }

        self.attribute_map = {
            'blog_id': 'blogId',
            'title': 'title',
            'description': 'description',
            'user': 'user',
            'creation_time': 'creationTime',
            'association': 'association',
            'sentiment': 'sentiment',
            'sentiment_details': 'sentimentDetails',
            'sentiment_weightage': 'sentimentWeightage',
            'entity': 'entity'
        }

        self._blog_id = blog_id
        self._title = title
        self._description = description
        self._user = user
        self._creation_time = creation_time
        self._association = association
        self._sentiment = sentiment
        self._sentiment_details = sentiment_details
        self._sentiment_weightage = sentiment_weightage
        self._entity = entity

    @property
    def blog_id(self):
        """
        Gets the blog_id of this Blog.


        :return: The blog_id of this Blog.
        :rtype: int
        """
        return self._blog_id

    @blog_id.setter
    def blog_id(self, blog_id):
        """
        Sets the blog_id of this Blog.


        :param blog_id: The blog_id of this Blog.
        :type: int
        """

        self._blog_id = blog_id

    @property
    def title(self):
        """
        Gets the title of this Blog.


        :return: The title of this Blog.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Blog.


        :param title: The title of this Blog.
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """
        Gets the description of this Blog.


        :return: The description of this Blog.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Blog.


        :param description: The description of this Blog.
        :type: str
        """

        self._description = description

    @property
    def user(self):
        """
        Gets the user of this Blog.


        :return: The user of this Blog.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Blog.


        :param user: The user of this Blog.
        :type: User
        """

        self._user = user

    @property
    def creation_time(self):
        """
        Gets the creation_time of this Blog.


        :return: The creation_time of this Blog.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this Blog.


        :param creation_time: The creation_time of this Blog.
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def association(self):
        """
        Gets the association of this Blog.


        :return: The association of this Blog.
        :rtype: int
        """
        return self._association

    @association.setter
    def association(self, association):
        """
        Sets the association of this Blog.


        :param association: The association of this Blog.
        :type: int
        """

        self._association = association

    @property
    def sentiment(self):
        """
        Gets the sentiment of this Blog.


        :return: The sentiment of this Blog.
        :rtype: str
        """
        return self._sentiment

    @sentiment.setter
    def sentiment(self, sentiment):
        """
        Sets the sentiment of this Blog.


        :param sentiment: The sentiment of this Blog.
        :type: str
        """

        self._sentiment = sentiment

    @property
    def sentiment_details(self):
        """
        Gets the sentiment_details of this Blog.


        :return: The sentiment_details of this Blog.
        :rtype: Sentiment
        """
        return self._sentiment_details

    @sentiment_details.setter
    def sentiment_details(self, sentiment_details):
        """
        Sets the sentiment_details of this Blog.


        :param sentiment_details: The sentiment_details of this Blog.
        :type: Sentiment
        """

        self._sentiment_details = sentiment_details

    @property
    def sentiment_weightage(self):
        """
        Gets the sentiment_weightage of this Blog.


        :return: The sentiment_weightage of this Blog.
        :rtype: float
        """
        return self._sentiment_weightage

    @sentiment_weightage.setter
    def sentiment_weightage(self, sentiment_weightage):
        """
        Sets the sentiment_weightage of this Blog.


        :param sentiment_weightage: The sentiment_weightage of this Blog.
        :type: float
        """

        self._sentiment_weightage = sentiment_weightage

    @property
    def entity(self):
        """
        Gets the entity of this Blog.


        :return: The entity of this Blog.
        :rtype: list[NER]
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this Blog.


        :param entity: The entity of this Blog.
        :type: list[NER]
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
