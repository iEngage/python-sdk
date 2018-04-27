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


class Milestone(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, milestone_id=None, milestone_title=None, milestone_description=None, status=None, priority=None, due_date=None, created_date=None):
        """
        Milestone - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'milestone_id': 'int',
            'milestone_title': 'str',
            'milestone_description': 'str',
            'status': 'int',
            'priority': 'int',
            'due_date': 'datetime',
            'created_date': 'datetime'
        }

        self.attribute_map = {
            'milestone_id': 'milestoneId',
            'milestone_title': 'milestoneTitle',
            'milestone_description': 'milestoneDescription',
            'status': 'status',
            'priority': 'priority',
            'due_date': 'dueDate',
            'created_date': 'createdDate'
        }

        self._milestone_id = milestone_id
        self._milestone_title = milestone_title
        self._milestone_description = milestone_description
        self._status = status
        self._priority = priority
        self._due_date = due_date
        self._created_date = created_date

    @property
    def milestone_id(self):
        """
        Gets the milestone_id of this Milestone.

        :return: The milestone_id of this Milestone.
        :rtype: int
        """
        return self._milestone_id

    @milestone_id.setter
    def milestone_id(self, milestone_id):
        """
        Sets the milestone_id of this Milestone.

        :param milestone_id: The milestone_id of this Milestone.
        :type: int
        """

        self._milestone_id = milestone_id

    @property
    def milestone_title(self):
        """
        Gets the milestone_title of this Milestone.

        :return: The milestone_title of this Milestone.
        :rtype: str
        """
        return self._milestone_title

    @milestone_title.setter
    def milestone_title(self, milestone_title):
        """
        Sets the milestone_title of this Milestone.

        :param milestone_title: The milestone_title of this Milestone.
        :type: str
        """

        self._milestone_title = milestone_title

    @property
    def milestone_description(self):
        """
        Gets the milestone_description of this Milestone.

        :return: The milestone_description of this Milestone.
        :rtype: str
        """
        return self._milestone_description

    @milestone_description.setter
    def milestone_description(self, milestone_description):
        """
        Sets the milestone_description of this Milestone.

        :param milestone_description: The milestone_description of this Milestone.
        :type: str
        """

        self._milestone_description = milestone_description

    @property
    def status(self):
        """
        Gets the status of this Milestone.

        :return: The status of this Milestone.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Milestone.

        :param status: The status of this Milestone.
        :type: int
        """

        self._status = status

    @property
    def priority(self):
        """
        Gets the priority of this Milestone.

        :return: The priority of this Milestone.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this Milestone.

        :param priority: The priority of this Milestone.
        :type: int
        """

        self._priority = priority

    @property
    def due_date(self):
        """
        Gets the due_date of this Milestone.

        :return: The due_date of this Milestone.
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """
        Sets the due_date of this Milestone.

        :param due_date: The due_date of this Milestone.
        :type: datetime
        """

        self._due_date = due_date

    @property
    def created_date(self):
        """
        Gets the created_date of this Milestone.

        :return: The created_date of this Milestone.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this Milestone.

        :param created_date: The created_date of this Milestone.
        :type: datetime
        """

        self._created_date = created_date

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