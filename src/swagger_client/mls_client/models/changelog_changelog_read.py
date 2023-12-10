# coding: utf-8

"""
    MLS2 API

    Central API  # noqa: E501

    OpenAPI spec version: 0.7.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ChangelogChangelogRead(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'version': 'str',
        'type': 'str',
        'text': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'type': 'type',
        'text': 'text'
    }

    def __init__(self, id=None, version=None, type=None, text=None):  # noqa: E501
        """ChangelogChangelogRead - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._version = None
        self._type = None
        self._text = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if type is not None:
            self.type = type
        if text is not None:
            self.text = text

    @property
    def id(self):
        """Gets the id of this ChangelogChangelogRead.  # noqa: E501


        :return: The id of this ChangelogChangelogRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChangelogChangelogRead.


        :param id: The id of this ChangelogChangelogRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this ChangelogChangelogRead.  # noqa: E501


        :return: The version of this ChangelogChangelogRead.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ChangelogChangelogRead.


        :param version: The version of this ChangelogChangelogRead.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def type(self):
        """Gets the type of this ChangelogChangelogRead.  # noqa: E501


        :return: The type of this ChangelogChangelogRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChangelogChangelogRead.


        :param type: The type of this ChangelogChangelogRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def text(self):
        """Gets the text of this ChangelogChangelogRead.  # noqa: E501


        :return: The text of this ChangelogChangelogRead.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ChangelogChangelogRead.


        :param text: The text of this ChangelogChangelogRead.  # noqa: E501
        :type: str
        """

        self._text = text

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ChangelogChangelogRead, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChangelogChangelogRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other