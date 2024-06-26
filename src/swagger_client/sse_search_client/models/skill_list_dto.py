# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SkillListDto(object):
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
        'skills': 'list[SkillDto]'
    }

    attribute_map = {
        'skills': 'skills'
    }

    def __init__(self, skills=None):  # noqa: E501
        """SkillListDto - a model defined in Swagger"""  # noqa: E501
        self._skills = None
        self.discriminator = None
        self.skills = skills

    @property
    def skills(self):
        """Gets the skills of this SkillListDto.  # noqa: E501


        :return: The skills of this SkillListDto.  # noqa: E501
        :rtype: list[SkillDto]
        """
        return self._skills

    @skills.setter
    def skills(self, skills):
        """Sets the skills of this SkillListDto.


        :param skills: The skills of this SkillListDto.  # noqa: E501
        :type: list[SkillDto]
        """
        if skills is None:
            raise ValueError("Invalid value for `skills`, must not be `None`")  # noqa: E501

        self._skills = skills

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
        if issubclass(SkillListDto, dict):
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
        if not isinstance(other, SkillListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
