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


class DataFlavor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, mime_type=None, human_presentable_name=None, primary_type=None, sub_type=None, default_representation_class_as_string=None, flavor_java_file_list_type=False, flavor_remote_object_type=False, flavor_serialized_object_type=False, flavor_text_type=False, mime_type_serialized_object=False, representation_class_byte_buffer=False, representation_class_char_buffer=False, representation_class_input_stream=False, representation_class_reader=False, representation_class_remote=False, representation_class_serializable=False):
        """
        DataFlavor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'mime_type': 'str',
            'human_presentable_name': 'str',
            'primary_type': 'str',
            'sub_type': 'str',
            'default_representation_class_as_string': 'str',
            'flavor_java_file_list_type': 'bool',
            'flavor_remote_object_type': 'bool',
            'flavor_serialized_object_type': 'bool',
            'flavor_text_type': 'bool',
            'mime_type_serialized_object': 'bool',
            'representation_class_byte_buffer': 'bool',
            'representation_class_char_buffer': 'bool',
            'representation_class_input_stream': 'bool',
            'representation_class_reader': 'bool',
            'representation_class_remote': 'bool',
            'representation_class_serializable': 'bool'
        }

        self.attribute_map = {
            'mime_type': 'mimeType',
            'human_presentable_name': 'humanPresentableName',
            'primary_type': 'primaryType',
            'sub_type': 'subType',
            'default_representation_class_as_string': 'defaultRepresentationClassAsString',
            'flavor_java_file_list_type': 'flavorJavaFileListType',
            'flavor_remote_object_type': 'flavorRemoteObjectType',
            'flavor_serialized_object_type': 'flavorSerializedObjectType',
            'flavor_text_type': 'flavorTextType',
            'mime_type_serialized_object': 'mimeTypeSerializedObject',
            'representation_class_byte_buffer': 'representationClassByteBuffer',
            'representation_class_char_buffer': 'representationClassCharBuffer',
            'representation_class_input_stream': 'representationClassInputStream',
            'representation_class_reader': 'representationClassReader',
            'representation_class_remote': 'representationClassRemote',
            'representation_class_serializable': 'representationClassSerializable'
        }

        self._mime_type = mime_type
        self._human_presentable_name = human_presentable_name
        self._primary_type = primary_type
        self._sub_type = sub_type
        self._default_representation_class_as_string = default_representation_class_as_string
        self._flavor_java_file_list_type = flavor_java_file_list_type
        self._flavor_remote_object_type = flavor_remote_object_type
        self._flavor_serialized_object_type = flavor_serialized_object_type
        self._flavor_text_type = flavor_text_type
        self._mime_type_serialized_object = mime_type_serialized_object
        self._representation_class_byte_buffer = representation_class_byte_buffer
        self._representation_class_char_buffer = representation_class_char_buffer
        self._representation_class_input_stream = representation_class_input_stream
        self._representation_class_reader = representation_class_reader
        self._representation_class_remote = representation_class_remote
        self._representation_class_serializable = representation_class_serializable

    @property
    def mime_type(self):
        """
        Gets the mime_type of this DataFlavor.

        :return: The mime_type of this DataFlavor.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """
        Sets the mime_type of this DataFlavor.

        :param mime_type: The mime_type of this DataFlavor.
        :type: str
        """

        self._mime_type = mime_type

    @property
    def human_presentable_name(self):
        """
        Gets the human_presentable_name of this DataFlavor.

        :return: The human_presentable_name of this DataFlavor.
        :rtype: str
        """
        return self._human_presentable_name

    @human_presentable_name.setter
    def human_presentable_name(self, human_presentable_name):
        """
        Sets the human_presentable_name of this DataFlavor.

        :param human_presentable_name: The human_presentable_name of this DataFlavor.
        :type: str
        """

        self._human_presentable_name = human_presentable_name

    @property
    def primary_type(self):
        """
        Gets the primary_type of this DataFlavor.

        :return: The primary_type of this DataFlavor.
        :rtype: str
        """
        return self._primary_type

    @primary_type.setter
    def primary_type(self, primary_type):
        """
        Sets the primary_type of this DataFlavor.

        :param primary_type: The primary_type of this DataFlavor.
        :type: str
        """

        self._primary_type = primary_type

    @property
    def sub_type(self):
        """
        Gets the sub_type of this DataFlavor.

        :return: The sub_type of this DataFlavor.
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """
        Sets the sub_type of this DataFlavor.

        :param sub_type: The sub_type of this DataFlavor.
        :type: str
        """

        self._sub_type = sub_type

    @property
    def default_representation_class_as_string(self):
        """
        Gets the default_representation_class_as_string of this DataFlavor.

        :return: The default_representation_class_as_string of this DataFlavor.
        :rtype: str
        """
        return self._default_representation_class_as_string

    @default_representation_class_as_string.setter
    def default_representation_class_as_string(self, default_representation_class_as_string):
        """
        Sets the default_representation_class_as_string of this DataFlavor.

        :param default_representation_class_as_string: The default_representation_class_as_string of this DataFlavor.
        :type: str
        """

        self._default_representation_class_as_string = default_representation_class_as_string

    @property
    def flavor_java_file_list_type(self):
        """
        Gets the flavor_java_file_list_type of this DataFlavor.

        :return: The flavor_java_file_list_type of this DataFlavor.
        :rtype: bool
        """
        return self._flavor_java_file_list_type

    @flavor_java_file_list_type.setter
    def flavor_java_file_list_type(self, flavor_java_file_list_type):
        """
        Sets the flavor_java_file_list_type of this DataFlavor.

        :param flavor_java_file_list_type: The flavor_java_file_list_type of this DataFlavor.
        :type: bool
        """

        self._flavor_java_file_list_type = flavor_java_file_list_type

    @property
    def flavor_remote_object_type(self):
        """
        Gets the flavor_remote_object_type of this DataFlavor.

        :return: The flavor_remote_object_type of this DataFlavor.
        :rtype: bool
        """
        return self._flavor_remote_object_type

    @flavor_remote_object_type.setter
    def flavor_remote_object_type(self, flavor_remote_object_type):
        """
        Sets the flavor_remote_object_type of this DataFlavor.

        :param flavor_remote_object_type: The flavor_remote_object_type of this DataFlavor.
        :type: bool
        """

        self._flavor_remote_object_type = flavor_remote_object_type

    @property
    def flavor_serialized_object_type(self):
        """
        Gets the flavor_serialized_object_type of this DataFlavor.

        :return: The flavor_serialized_object_type of this DataFlavor.
        :rtype: bool
        """
        return self._flavor_serialized_object_type

    @flavor_serialized_object_type.setter
    def flavor_serialized_object_type(self, flavor_serialized_object_type):
        """
        Sets the flavor_serialized_object_type of this DataFlavor.

        :param flavor_serialized_object_type: The flavor_serialized_object_type of this DataFlavor.
        :type: bool
        """

        self._flavor_serialized_object_type = flavor_serialized_object_type

    @property
    def flavor_text_type(self):
        """
        Gets the flavor_text_type of this DataFlavor.

        :return: The flavor_text_type of this DataFlavor.
        :rtype: bool
        """
        return self._flavor_text_type

    @flavor_text_type.setter
    def flavor_text_type(self, flavor_text_type):
        """
        Sets the flavor_text_type of this DataFlavor.

        :param flavor_text_type: The flavor_text_type of this DataFlavor.
        :type: bool
        """

        self._flavor_text_type = flavor_text_type

    @property
    def mime_type_serialized_object(self):
        """
        Gets the mime_type_serialized_object of this DataFlavor.

        :return: The mime_type_serialized_object of this DataFlavor.
        :rtype: bool
        """
        return self._mime_type_serialized_object

    @mime_type_serialized_object.setter
    def mime_type_serialized_object(self, mime_type_serialized_object):
        """
        Sets the mime_type_serialized_object of this DataFlavor.

        :param mime_type_serialized_object: The mime_type_serialized_object of this DataFlavor.
        :type: bool
        """

        self._mime_type_serialized_object = mime_type_serialized_object

    @property
    def representation_class_byte_buffer(self):
        """
        Gets the representation_class_byte_buffer of this DataFlavor.

        :return: The representation_class_byte_buffer of this DataFlavor.
        :rtype: bool
        """
        return self._representation_class_byte_buffer

    @representation_class_byte_buffer.setter
    def representation_class_byte_buffer(self, representation_class_byte_buffer):
        """
        Sets the representation_class_byte_buffer of this DataFlavor.

        :param representation_class_byte_buffer: The representation_class_byte_buffer of this DataFlavor.
        :type: bool
        """

        self._representation_class_byte_buffer = representation_class_byte_buffer

    @property
    def representation_class_char_buffer(self):
        """
        Gets the representation_class_char_buffer of this DataFlavor.

        :return: The representation_class_char_buffer of this DataFlavor.
        :rtype: bool
        """
        return self._representation_class_char_buffer

    @representation_class_char_buffer.setter
    def representation_class_char_buffer(self, representation_class_char_buffer):
        """
        Sets the representation_class_char_buffer of this DataFlavor.

        :param representation_class_char_buffer: The representation_class_char_buffer of this DataFlavor.
        :type: bool
        """

        self._representation_class_char_buffer = representation_class_char_buffer

    @property
    def representation_class_input_stream(self):
        """
        Gets the representation_class_input_stream of this DataFlavor.

        :return: The representation_class_input_stream of this DataFlavor.
        :rtype: bool
        """
        return self._representation_class_input_stream

    @representation_class_input_stream.setter
    def representation_class_input_stream(self, representation_class_input_stream):
        """
        Sets the representation_class_input_stream of this DataFlavor.

        :param representation_class_input_stream: The representation_class_input_stream of this DataFlavor.
        :type: bool
        """

        self._representation_class_input_stream = representation_class_input_stream

    @property
    def representation_class_reader(self):
        """
        Gets the representation_class_reader of this DataFlavor.

        :return: The representation_class_reader of this DataFlavor.
        :rtype: bool
        """
        return self._representation_class_reader

    @representation_class_reader.setter
    def representation_class_reader(self, representation_class_reader):
        """
        Sets the representation_class_reader of this DataFlavor.

        :param representation_class_reader: The representation_class_reader of this DataFlavor.
        :type: bool
        """

        self._representation_class_reader = representation_class_reader

    @property
    def representation_class_remote(self):
        """
        Gets the representation_class_remote of this DataFlavor.

        :return: The representation_class_remote of this DataFlavor.
        :rtype: bool
        """
        return self._representation_class_remote

    @representation_class_remote.setter
    def representation_class_remote(self, representation_class_remote):
        """
        Sets the representation_class_remote of this DataFlavor.

        :param representation_class_remote: The representation_class_remote of this DataFlavor.
        :type: bool
        """

        self._representation_class_remote = representation_class_remote

    @property
    def representation_class_serializable(self):
        """
        Gets the representation_class_serializable of this DataFlavor.

        :return: The representation_class_serializable of this DataFlavor.
        :rtype: bool
        """
        return self._representation_class_serializable

    @representation_class_serializable.setter
    def representation_class_serializable(self, representation_class_serializable):
        """
        Sets the representation_class_serializable of this DataFlavor.

        :param representation_class_serializable: The representation_class_serializable of this DataFlavor.
        :type: bool
        """

        self._representation_class_serializable = representation_class_serializable

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
