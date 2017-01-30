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


class Group(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, group_id=None, group_name=None, group_type=None, category=None, description=None, current_user_following=False, start_date=None, due_date=None, ideas_count=None, friends_ideas_count=None, followers_count=None, participants_count=None, friends_participants_count=None):
        """
        Group - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'group_id': 'int',
            'group_name': 'str',
            'group_type': 'str',
            'category': 'str',
            'description': 'str',
            'current_user_following': 'bool',
            'start_date': 'datetime',
            'due_date': 'datetime',
            'ideas_count': 'int',
            'friends_ideas_count': 'int',
            'followers_count': 'int',
            'participants_count': 'int',
            'friends_participants_count': 'int'
        }

        self.attribute_map = {
            'group_id': 'groupId',
            'group_name': 'groupName',
            'group_type': 'groupType',
            'category': 'category',
            'description': 'description',
            'current_user_following': 'currentUserFollowing',
            'start_date': 'startDate',
            'due_date': 'dueDate',
            'ideas_count': 'ideasCount',
            'friends_ideas_count': 'friendsIdeasCount',
            'followers_count': 'followersCount',
            'participants_count': 'participantsCount',
            'friends_participants_count': 'friendsParticipantsCount'
        }

        self._group_id = group_id
        self._group_name = group_name
        self._group_type = group_type
        self._category = category
        self._description = description
        self._current_user_following = current_user_following
        self._start_date = start_date
        self._due_date = due_date
        self._ideas_count = ideas_count
        self._friends_ideas_count = friends_ideas_count
        self._followers_count = followers_count
        self._participants_count = participants_count
        self._friends_participants_count = friends_participants_count

    @property
    def group_id(self):
        """
        Gets the group_id of this Group.

        :return: The group_id of this Group.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this Group.

        :param group_id: The group_id of this Group.
        :type: int
        """

        self._group_id = group_id

    @property
    def group_name(self):
        """
        Gets the group_name of this Group.

        :return: The group_name of this Group.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """
        Sets the group_name of this Group.

        :param group_name: The group_name of this Group.
        :type: str
        """

        self._group_name = group_name

    @property
    def group_type(self):
        """
        Gets the group_type of this Group.

        :return: The group_type of this Group.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """
        Sets the group_type of this Group.

        :param group_type: The group_type of this Group.
        :type: str
        """

        self._group_type = group_type

    @property
    def category(self):
        """
        Gets the category of this Group.

        :return: The category of this Group.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Group.

        :param category: The category of this Group.
        :type: str
        """

        self._category = category

    @property
    def description(self):
        """
        Gets the description of this Group.

        :return: The description of this Group.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Group.

        :param description: The description of this Group.
        :type: str
        """

        self._description = description

    @property
    def current_user_following(self):
        """
        Gets the current_user_following of this Group.

        :return: The current_user_following of this Group.
        :rtype: bool
        """
        return self._current_user_following

    @current_user_following.setter
    def current_user_following(self, current_user_following):
        """
        Sets the current_user_following of this Group.

        :param current_user_following: The current_user_following of this Group.
        :type: bool
        """

        self._current_user_following = current_user_following

    @property
    def start_date(self):
        """
        Gets the start_date of this Group.

        :return: The start_date of this Group.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this Group.

        :param start_date: The start_date of this Group.
        :type: datetime
        """

        self._start_date = start_date

    @property
    def due_date(self):
        """
        Gets the due_date of this Group.

        :return: The due_date of this Group.
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """
        Sets the due_date of this Group.

        :param due_date: The due_date of this Group.
        :type: datetime
        """

        self._due_date = due_date

    @property
    def ideas_count(self):
        """
        Gets the ideas_count of this Group.

        :return: The ideas_count of this Group.
        :rtype: int
        """
        return self._ideas_count

    @ideas_count.setter
    def ideas_count(self, ideas_count):
        """
        Sets the ideas_count of this Group.

        :param ideas_count: The ideas_count of this Group.
        :type: int
        """

        self._ideas_count = ideas_count

    @property
    def friends_ideas_count(self):
        """
        Gets the friends_ideas_count of this Group.

        :return: The friends_ideas_count of this Group.
        :rtype: int
        """
        return self._friends_ideas_count

    @friends_ideas_count.setter
    def friends_ideas_count(self, friends_ideas_count):
        """
        Sets the friends_ideas_count of this Group.

        :param friends_ideas_count: The friends_ideas_count of this Group.
        :type: int
        """

        self._friends_ideas_count = friends_ideas_count

    @property
    def followers_count(self):
        """
        Gets the followers_count of this Group.

        :return: The followers_count of this Group.
        :rtype: int
        """
        return self._followers_count

    @followers_count.setter
    def followers_count(self, followers_count):
        """
        Sets the followers_count of this Group.

        :param followers_count: The followers_count of this Group.
        :type: int
        """

        self._followers_count = followers_count

    @property
    def participants_count(self):
        """
        Gets the participants_count of this Group.

        :return: The participants_count of this Group.
        :rtype: int
        """
        return self._participants_count

    @participants_count.setter
    def participants_count(self, participants_count):
        """
        Sets the participants_count of this Group.

        :param participants_count: The participants_count of this Group.
        :type: int
        """

        self._participants_count = participants_count

    @property
    def friends_participants_count(self):
        """
        Gets the friends_participants_count of this Group.

        :return: The friends_participants_count of this Group.
        :rtype: int
        """
        return self._friends_participants_count

    @friends_participants_count.setter
    def friends_participants_count(self, friends_participants_count):
        """
        Sets the friends_participants_count of this Group.

        :param friends_participants_count: The friends_participants_count of this Group.
        :type: int
        """

        self._friends_participants_count = friends_participants_count

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
