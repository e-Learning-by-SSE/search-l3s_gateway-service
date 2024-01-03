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
from l3s_aimeta_client.models.dto_task_preprocess_response_item import DtoTaskPreprocessResponseItem  # noqa: F401,E501

class AllOfDtoTaskPreprocessResponseResults(DtoTaskPreprocessResponseItem):
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
    }
    if hasattr(DtoTaskPreprocessResponseItem, "swagger_types"):
        swagger_types.update(DtoTaskPreprocessResponseItem.swagger_types)

    attribute_map = {
    }
    if hasattr(DtoTaskPreprocessResponseItem, "attribute_map"):
        attribute_map.update(DtoTaskPreprocessResponseItem.attribute_map)

    def __init__(self, *args, **kwargs):  # noqa: E501
        """AllOfDtoTaskPreprocessResponseResults - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None
        DtoTaskPreprocessResponseItem.__init__(self, *args, **kwargs)

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
        if issubclass(AllOfDtoTaskPreprocessResponseResults, dict):
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
        if not isinstance(other, AllOfDtoTaskPreprocessResponseResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
