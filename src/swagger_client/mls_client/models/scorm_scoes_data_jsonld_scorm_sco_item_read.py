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

class ScormScoesDataJsonldScormScoItemRead(object):
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
        'context': 'OneOfScormScoesDataJsonldScormScoItemReadContext',
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type'
    }

    def __init__(self, context=None, id=None, type=None):  # noqa: E501
        """ScormScoesDataJsonldScormScoItemRead - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def context(self):
        """Gets the context of this ScormScoesDataJsonldScormScoItemRead.  # noqa: E501


        :return: The context of this ScormScoesDataJsonldScormScoItemRead.  # noqa: E501
        :rtype: OneOfScormScoesDataJsonldScormScoItemReadContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ScormScoesDataJsonldScormScoItemRead.


        :param context: The context of this ScormScoesDataJsonldScormScoItemRead.  # noqa: E501
        :type: OneOfScormScoesDataJsonldScormScoItemReadContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this ScormScoesDataJsonldScormScoItemRead.  # noqa: E501


        :return: The id of this ScormScoesDataJsonldScormScoItemRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScormScoesDataJsonldScormScoItemRead.


        :param id: The id of this ScormScoesDataJsonldScormScoItemRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ScormScoesDataJsonldScormScoItemRead.  # noqa: E501


        :return: The type of this ScormScoesDataJsonldScormScoItemRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScormScoesDataJsonldScormScoItemRead.


        :param type: The type of this ScormScoesDataJsonldScormScoItemRead.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ScormScoesDataJsonldScormScoItemRead, dict):
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
        if not isinstance(other, ScormScoesDataJsonldScormScoItemRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other