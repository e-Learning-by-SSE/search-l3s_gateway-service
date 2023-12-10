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

class UserComment(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'last_editor': 'str',
        'user': 'str',
        'organization': 'str',
        'content': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'last_editor': 'lastEditor',
        'user': 'user',
        'organization': 'organization',
        'content': 'content'
    }

    def __init__(self, created_at=None, updated_at=None, id=None, last_editor=None, user=None, organization=None, content=None):  # noqa: E501
        """UserComment - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._last_editor = None
        self._user = None
        self._organization = None
        self._content = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id
        if last_editor is not None:
            self.last_editor = last_editor
        self.user = user
        self.organization = organization
        if content is not None:
            self.content = content

    @property
    def created_at(self):
        """Gets the created_at of this UserComment.  # noqa: E501


        :return: The created_at of this UserComment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserComment.


        :param created_at: The created_at of this UserComment.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this UserComment.  # noqa: E501


        :return: The updated_at of this UserComment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UserComment.


        :param updated_at: The updated_at of this UserComment.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this UserComment.  # noqa: E501


        :return: The id of this UserComment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserComment.


        :param id: The id of this UserComment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def last_editor(self):
        """Gets the last_editor of this UserComment.  # noqa: E501


        :return: The last_editor of this UserComment.  # noqa: E501
        :rtype: str
        """
        return self._last_editor

    @last_editor.setter
    def last_editor(self, last_editor):
        """Sets the last_editor of this UserComment.


        :param last_editor: The last_editor of this UserComment.  # noqa: E501
        :type: str
        """

        self._last_editor = last_editor

    @property
    def user(self):
        """Gets the user of this UserComment.  # noqa: E501


        :return: The user of this UserComment.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserComment.


        :param user: The user of this UserComment.  # noqa: E501
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def organization(self):
        """Gets the organization of this UserComment.  # noqa: E501


        :return: The organization of this UserComment.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this UserComment.


        :param organization: The organization of this UserComment.  # noqa: E501
        :type: str
        """
        if organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def content(self):
        """Gets the content of this UserComment.  # noqa: E501


        :return: The content of this UserComment.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this UserComment.


        :param content: The content of this UserComment.  # noqa: E501
        :type: str
        """

        self._content = content

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
        if issubclass(UserComment, dict):
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
        if not isinstance(other, UserComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other