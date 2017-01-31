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


class Interaction(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, interaction_id=None, interaction_title=None, interaction_description=None, interaction_type=None, issuer=None, no_of_responses=None, is_closed=False, created_date=None, last_updated_date=None, video_id=None, file_url=None, file_entity_name=None, is_subscribed=False, sentiment=None, sentiment_details=None, sentiment_weightage=None, entity=None, attachment_list=None):
        """
        Interaction - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'interaction_id': 'int',
            'interaction_title': 'str',
            'interaction_description': 'str',
            'interaction_type': 'str',
            'issuer': 'User',
            'no_of_responses': 'int',
            'is_closed': 'bool',
            'created_date': 'datetime',
            'last_updated_date': 'datetime',
            'video_id': 'str',
            'file_url': 'str',
            'file_entity_name': 'str',
            'is_subscribed': 'bool',
            'sentiment': 'str',
            'sentiment_details': 'Sentiment',
            'sentiment_weightage': 'float',
            'entity': 'list[NER]',
            'attachment_list': 'list[Multimedia]'
        }

        self.attribute_map = {
            'interaction_id': 'interactionId',
            'interaction_title': 'interactionTitle',
            'interaction_description': 'interactionDescription',
            'interaction_type': 'interactionType',
            'issuer': 'issuer',
            'no_of_responses': 'noOfResponses',
            'is_closed': 'isClosed',
            'created_date': 'createdDate',
            'last_updated_date': 'lastUpdatedDate',
            'video_id': 'videoId',
            'file_url': 'fileURL',
            'file_entity_name': 'fileEntityName',
            'is_subscribed': 'isSubscribed',
            'sentiment': 'sentiment',
            'sentiment_details': 'sentimentDetails',
            'sentiment_weightage': 'sentimentWeightage',
            'entity': 'entity',
            'attachment_list': 'attachmentList'
        }

        self._interaction_id = interaction_id
        self._interaction_title = interaction_title
        self._interaction_description = interaction_description
        self._interaction_type = interaction_type
        self._issuer = issuer
        self._no_of_responses = no_of_responses
        self._is_closed = is_closed
        self._created_date = created_date
        self._last_updated_date = last_updated_date
        self._video_id = video_id
        self._file_url = file_url
        self._file_entity_name = file_entity_name
        self._is_subscribed = is_subscribed
        self._sentiment = sentiment
        self._sentiment_details = sentiment_details
        self._sentiment_weightage = sentiment_weightage
        self._entity = entity
        self._attachment_list = attachment_list

    @property
    def interaction_id(self):
        """
        Gets the interaction_id of this Interaction.

        :return: The interaction_id of this Interaction.
        :rtype: int
        """
        return self._interaction_id

    @interaction_id.setter
    def interaction_id(self, interaction_id):
        """
        Sets the interaction_id of this Interaction.

        :param interaction_id: The interaction_id of this Interaction.
        :type: int
        """

        self._interaction_id = interaction_id

    @property
    def interaction_title(self):
        """
        Gets the interaction_title of this Interaction.

        :return: The interaction_title of this Interaction.
        :rtype: str
        """
        return self._interaction_title

    @interaction_title.setter
    def interaction_title(self, interaction_title):
        """
        Sets the interaction_title of this Interaction.

        :param interaction_title: The interaction_title of this Interaction.
        :type: str
        """

        self._interaction_title = interaction_title

    @property
    def interaction_description(self):
        """
        Gets the interaction_description of this Interaction.

        :return: The interaction_description of this Interaction.
        :rtype: str
        """
        return self._interaction_description

    @interaction_description.setter
    def interaction_description(self, interaction_description):
        """
        Sets the interaction_description of this Interaction.

        :param interaction_description: The interaction_description of this Interaction.
        :type: str
        """

        self._interaction_description = interaction_description

    @property
    def interaction_type(self):
        """
        Gets the interaction_type of this Interaction.

        :return: The interaction_type of this Interaction.
        :rtype: str
        """
        return self._interaction_type

    @interaction_type.setter
    def interaction_type(self, interaction_type):
        """
        Sets the interaction_type of this Interaction.

        :param interaction_type: The interaction_type of this Interaction.
        :type: str
        """

        self._interaction_type = interaction_type

    @property
    def issuer(self):
        """
        Gets the issuer of this Interaction.

        :return: The issuer of this Interaction.
        :rtype: User
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this Interaction.

        :param issuer: The issuer of this Interaction.
        :type: User
        """

        self._issuer = issuer

    @property
    def no_of_responses(self):
        """
        Gets the no_of_responses of this Interaction.

        :return: The no_of_responses of this Interaction.
        :rtype: int
        """
        return self._no_of_responses

    @no_of_responses.setter
    def no_of_responses(self, no_of_responses):
        """
        Sets the no_of_responses of this Interaction.

        :param no_of_responses: The no_of_responses of this Interaction.
        :type: int
        """

        self._no_of_responses = no_of_responses

    @property
    def is_closed(self):
        """
        Gets the is_closed of this Interaction.

        :return: The is_closed of this Interaction.
        :rtype: bool
        """
        return self._is_closed

    @is_closed.setter
    def is_closed(self, is_closed):
        """
        Sets the is_closed of this Interaction.

        :param is_closed: The is_closed of this Interaction.
        :type: bool
        """

        self._is_closed = is_closed

    @property
    def created_date(self):
        """
        Gets the created_date of this Interaction.

        :return: The created_date of this Interaction.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this Interaction.

        :param created_date: The created_date of this Interaction.
        :type: datetime
        """

        self._created_date = created_date

    @property
    def last_updated_date(self):
        """
        Gets the last_updated_date of this Interaction.

        :return: The last_updated_date of this Interaction.
        :rtype: datetime
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """
        Sets the last_updated_date of this Interaction.

        :param last_updated_date: The last_updated_date of this Interaction.
        :type: datetime
        """

        self._last_updated_date = last_updated_date

    @property
    def video_id(self):
        """
        Gets the video_id of this Interaction.

        :return: The video_id of this Interaction.
        :rtype: str
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """
        Sets the video_id of this Interaction.

        :param video_id: The video_id of this Interaction.
        :type: str
        """

        self._video_id = video_id

    @property
    def file_url(self):
        """
        Gets the file_url of this Interaction.

        :return: The file_url of this Interaction.
        :rtype: str
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        """
        Sets the file_url of this Interaction.

        :param file_url: The file_url of this Interaction.
        :type: str
        """

        self._file_url = file_url

    @property
    def file_entity_name(self):
        """
        Gets the file_entity_name of this Interaction.

        :return: The file_entity_name of this Interaction.
        :rtype: str
        """
        return self._file_entity_name

    @file_entity_name.setter
    def file_entity_name(self, file_entity_name):
        """
        Sets the file_entity_name of this Interaction.

        :param file_entity_name: The file_entity_name of this Interaction.
        :type: str
        """

        self._file_entity_name = file_entity_name

    @property
    def is_subscribed(self):
        """
        Gets the is_subscribed of this Interaction.

        :return: The is_subscribed of this Interaction.
        :rtype: bool
        """
        return self._is_subscribed

    @is_subscribed.setter
    def is_subscribed(self, is_subscribed):
        """
        Sets the is_subscribed of this Interaction.

        :param is_subscribed: The is_subscribed of this Interaction.
        :type: bool
        """

        self._is_subscribed = is_subscribed

    @property
    def sentiment(self):
        """
        Gets the sentiment of this Interaction.

        :return: The sentiment of this Interaction.
        :rtype: str
        """
        return self._sentiment

    @sentiment.setter
    def sentiment(self, sentiment):
        """
        Sets the sentiment of this Interaction.

        :param sentiment: The sentiment of this Interaction.
        :type: str
        """

        self._sentiment = sentiment

    @property
    def sentiment_details(self):
        """
        Gets the sentiment_details of this Interaction.

        :return: The sentiment_details of this Interaction.
        :rtype: Sentiment
        """
        return self._sentiment_details

    @sentiment_details.setter
    def sentiment_details(self, sentiment_details):
        """
        Sets the sentiment_details of this Interaction.

        :param sentiment_details: The sentiment_details of this Interaction.
        :type: Sentiment
        """

        self._sentiment_details = sentiment_details

    @property
    def sentiment_weightage(self):
        """
        Gets the sentiment_weightage of this Interaction.

        :return: The sentiment_weightage of this Interaction.
        :rtype: float
        """
        return self._sentiment_weightage

    @sentiment_weightage.setter
    def sentiment_weightage(self, sentiment_weightage):
        """
        Sets the sentiment_weightage of this Interaction.

        :param sentiment_weightage: The sentiment_weightage of this Interaction.
        :type: float
        """

        self._sentiment_weightage = sentiment_weightage

    @property
    def entity(self):
        """
        Gets the entity of this Interaction.

        :return: The entity of this Interaction.
        :rtype: list[NER]
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this Interaction.

        :param entity: The entity of this Interaction.
        :type: list[NER]
        """

        self._entity = entity

    @property
    def attachment_list(self):
        """
        Gets the attachment_list of this Interaction.

        :return: The attachment_list of this Interaction.
        :rtype: list[Multimedia]
        """
        return self._attachment_list

    @attachment_list.setter
    def attachment_list(self, attachment_list):
        """
        Sets the attachment_list of this Interaction.

        :param attachment_list: The attachment_list of this Interaction.
        :type: list[Multimedia]
        """

        self._attachment_list = attachment_list

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