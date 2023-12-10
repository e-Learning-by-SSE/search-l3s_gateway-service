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

class InlineResponse200HydrasearchHydramapping(object):
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
        'type': 'str',
        'variable': 'str',
        '_property': 'str',
        'required': 'bool'
    }

    attribute_map = {
        'type': '@type',
        'variable': 'variable',
        '_property': 'property',
        'required': 'required'
    }

    def __init__(self, type=None, variable=None, _property=None, required=None):  # noqa: E501
        """InlineResponse200HydrasearchHydramapping - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._variable = None
        self.__property = None
        self._required = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if variable is not None:
            self.variable = variable
        if _property is not None:
            self._property = _property
        if required is not None:
            self.required = required

    @property
    def type(self):
        """Gets the type of this InlineResponse200HydrasearchHydramapping.  # noqa: E501


        :return: The type of this InlineResponse200HydrasearchHydramapping.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse200HydrasearchHydramapping.


        :param type: The type of this InlineResponse200HydrasearchHydramapping.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def variable(self):
        """Gets the variable of this InlineResponse200HydrasearchHydramapping.  # noqa: E501


        :return: The variable of this InlineResponse200HydrasearchHydramapping.  # noqa: E501
        :rtype: str
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this InlineResponse200HydrasearchHydramapping.


        :param variable: The variable of this InlineResponse200HydrasearchHydramapping.  # noqa: E501
        :type: str
        """

        self._variable = variable

    @property
    def _property(self):
        """Gets the _property of this InlineResponse200HydrasearchHydramapping.  # noqa: E501


        :return: The _property of this InlineResponse200HydrasearchHydramapping.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this InlineResponse200HydrasearchHydramapping.


        :param _property: The _property of this InlineResponse200HydrasearchHydramapping.  # noqa: E501
        :type: str
        """

        self.__property = _property

    @property
    def required(self):
        """Gets the required of this InlineResponse200HydrasearchHydramapping.  # noqa: E501


        :return: The required of this InlineResponse200HydrasearchHydramapping.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this InlineResponse200HydrasearchHydramapping.


        :param required: The required of this InlineResponse200HydrasearchHydramapping.  # noqa: E501
        :type: bool
        """

        self._required = required

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
        if issubclass(InlineResponse200HydrasearchHydramapping, dict):
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
        if not isinstance(other, InlineResponse200HydrasearchHydramapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other