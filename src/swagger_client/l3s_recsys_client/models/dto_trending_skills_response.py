# coding: utf-8

"""
    L3S Recommendation Service for SEARCH

    Welcome to the Swagger UI documentation site!  # noqa: E501

    OpenAPI spec version: 0.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DtoTrendingSkillsResponse(object):
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
        'topk': 'str',
        'trending_skills': 'list[str]'
    }

    attribute_map = {
        'topk': 'topk',
        'trending_skills': 'trending_skills'
    }

    def __init__(self, topk=None, trending_skills=None):  # noqa: E501
        """DtoTrendingSkillsResponse - a model defined in Swagger"""  # noqa: E501
        self._topk = None
        self._trending_skills = None
        self.discriminator = None
        if topk is not None:
            self.topk = topk
        if trending_skills is not None:
            self.trending_skills = trending_skills

    @property
    def topk(self):
        """Gets the topk of this DtoTrendingSkillsResponse.  # noqa: E501

        number of top Trending Skills  # noqa: E501

        :return: The topk of this DtoTrendingSkillsResponse.  # noqa: E501
        :rtype: str
        """
        return self._topk

    @topk.setter
    def topk(self, topk):
        """Sets the topk of this DtoTrendingSkillsResponse.

        number of top Trending Skills  # noqa: E501

        :param topk: The topk of this DtoTrendingSkillsResponse.  # noqa: E501
        :type: str
        """

        self._topk = topk

    @property
    def trending_skills(self):
        """Gets the trending_skills of this DtoTrendingSkillsResponse.  # noqa: E501

        List of Trending Skills  # noqa: E501

        :return: The trending_skills of this DtoTrendingSkillsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._trending_skills

    @trending_skills.setter
    def trending_skills(self, trending_skills):
        """Sets the trending_skills of this DtoTrendingSkillsResponse.

        List of Trending Skills  # noqa: E501

        :param trending_skills: The trending_skills of this DtoTrendingSkillsResponse.  # noqa: E501
        :type: list[str]
        """

        self._trending_skills = trending_skills

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
        if issubclass(DtoTrendingSkillsResponse, dict):
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
        if not isinstance(other, DtoTrendingSkillsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
