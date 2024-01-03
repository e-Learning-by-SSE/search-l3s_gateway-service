# coding: utf-8

"""
    L3S AI-Meta Service(AIMS) for SEARCH

    Welcome to the Swagger UI documentation site!  # noqa: E501

    OpenAPI spec version: 0.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DtoContentTagsResponseItem(object):
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
        'task_id': 'str',
        'content_tags': 'list[str]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'content_tags': 'content_tags'
    }

    def __init__(self, task_id=None, content_tags=None):  # noqa: E501
        """DtoContentTagsResponseItem - a model defined in Swagger"""  # noqa: E501
        self._task_id = None
        self._content_tags = None
        self.discriminator = None
        if task_id is not None:
            self.task_id = task_id
        if content_tags is not None:
            self.content_tags = content_tags

    @property
    def task_id(self):
        """Gets the task_id of this DtoContentTagsResponseItem.  # noqa: E501

        The task ID  # noqa: E501

        :return: The task_id of this DtoContentTagsResponseItem.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this DtoContentTagsResponseItem.

        The task ID  # noqa: E501

        :param task_id: The task_id of this DtoContentTagsResponseItem.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def content_tags(self):
        """Gets the content_tags of this DtoContentTagsResponseItem.  # noqa: E501

        List of Content Tags  # noqa: E501

        :return: The content_tags of this DtoContentTagsResponseItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._content_tags

    @content_tags.setter
    def content_tags(self, content_tags):
        """Sets the content_tags of this DtoContentTagsResponseItem.

        List of Content Tags  # noqa: E501

        :param content_tags: The content_tags of this DtoContentTagsResponseItem.  # noqa: E501
        :type: list[str]
        """

        self._content_tags = content_tags

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
        if issubclass(DtoContentTagsResponseItem, dict):
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
        if not isinstance(other, DtoContentTagsResponseItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
