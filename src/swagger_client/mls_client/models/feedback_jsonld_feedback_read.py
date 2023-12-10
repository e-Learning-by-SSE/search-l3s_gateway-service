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

class FeedbackJsonldFeedbackRead(object):
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
        'id': 'str',
        'type': 'str',
        'id': 'int',
        'text': 'str',
        'area': 'str',
        'creator': 'str',
        'screenshots': 'list[str]',
        'is_problem': 'bool',
        'votes': 'list[UserFeedbackJsonldFeedbackRead]',
        'likes': 'int',
        'dislikes': 'int',
        'comment': 'str'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'id': 'id',
        'text': 'text',
        'area': 'area',
        'creator': 'creator',
        'screenshots': 'screenshots',
        'is_problem': 'isProblem',
        'votes': 'votes',
        'likes': 'likes',
        'dislikes': 'dislikes',
        'comment': 'comment'
    }

    def __init__(self, id=None, type=None, id=None, text=None, area='feedback', creator=None, screenshots=None, is_problem=True, votes=None, likes=None, dislikes=None, comment=None):  # noqa: E501
        """FeedbackJsonldFeedbackRead - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._id = None
        self._text = None
        self._area = None
        self._creator = None
        self._screenshots = None
        self._is_problem = None
        self._votes = None
        self._likes = None
        self._dislikes = None
        self._comment = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if text is not None:
            self.text = text
        if area is not None:
            self.area = area
        if creator is not None:
            self.creator = creator
        if screenshots is not None:
            self.screenshots = screenshots
        if is_problem is not None:
            self.is_problem = is_problem
        if votes is not None:
            self.votes = votes
        if likes is not None:
            self.likes = likes
        if dislikes is not None:
            self.dislikes = dislikes
        if comment is not None:
            self.comment = comment

    @property
    def id(self):
        """Gets the id of this FeedbackJsonldFeedbackRead.  # noqa: E501


        :return: The id of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FeedbackJsonldFeedbackRead.


        :param id: The id of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this FeedbackJsonldFeedbackRead.  # noqa: E501


        :return: The type of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FeedbackJsonldFeedbackRead.


        :param type: The type of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this FeedbackJsonldFeedbackRead.  # noqa: E501


        :return: The id of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FeedbackJsonldFeedbackRead.


        :param id: The id of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def text(self):
        """Gets the text of this FeedbackJsonldFeedbackRead.  # noqa: E501


        :return: The text of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this FeedbackJsonldFeedbackRead.


        :param text: The text of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def area(self):
        """Gets the area of this FeedbackJsonldFeedbackRead.  # noqa: E501


        :return: The area of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this FeedbackJsonldFeedbackRead.


        :param area: The area of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :type: str
        """

        self._area = area

    @property
    def creator(self):
        """Gets the creator of this FeedbackJsonldFeedbackRead.  # noqa: E501


        :return: The creator of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this FeedbackJsonldFeedbackRead.


        :param creator: The creator of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def screenshots(self):
        """Gets the screenshots of this FeedbackJsonldFeedbackRead.  # noqa: E501


        :return: The screenshots of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._screenshots

    @screenshots.setter
    def screenshots(self, screenshots):
        """Sets the screenshots of this FeedbackJsonldFeedbackRead.


        :param screenshots: The screenshots of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :type: list[str]
        """

        self._screenshots = screenshots

    @property
    def is_problem(self):
        """Gets the is_problem of this FeedbackJsonldFeedbackRead.  # noqa: E501


        :return: The is_problem of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :rtype: bool
        """
        return self._is_problem

    @is_problem.setter
    def is_problem(self, is_problem):
        """Sets the is_problem of this FeedbackJsonldFeedbackRead.


        :param is_problem: The is_problem of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :type: bool
        """

        self._is_problem = is_problem

    @property
    def votes(self):
        """Gets the votes of this FeedbackJsonldFeedbackRead.  # noqa: E501


        :return: The votes of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :rtype: list[UserFeedbackJsonldFeedbackRead]
        """
        return self._votes

    @votes.setter
    def votes(self, votes):
        """Sets the votes of this FeedbackJsonldFeedbackRead.


        :param votes: The votes of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :type: list[UserFeedbackJsonldFeedbackRead]
        """

        self._votes = votes

    @property
    def likes(self):
        """Gets the likes of this FeedbackJsonldFeedbackRead.  # noqa: E501


        :return: The likes of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :rtype: int
        """
        return self._likes

    @likes.setter
    def likes(self, likes):
        """Sets the likes of this FeedbackJsonldFeedbackRead.


        :param likes: The likes of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :type: int
        """

        self._likes = likes

    @property
    def dislikes(self):
        """Gets the dislikes of this FeedbackJsonldFeedbackRead.  # noqa: E501


        :return: The dislikes of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :rtype: int
        """
        return self._dislikes

    @dislikes.setter
    def dislikes(self, dislikes):
        """Sets the dislikes of this FeedbackJsonldFeedbackRead.


        :param dislikes: The dislikes of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :type: int
        """

        self._dislikes = dislikes

    @property
    def comment(self):
        """Gets the comment of this FeedbackJsonldFeedbackRead.  # noqa: E501


        :return: The comment of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this FeedbackJsonldFeedbackRead.


        :param comment: The comment of this FeedbackJsonldFeedbackRead.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(FeedbackJsonldFeedbackRead, dict):
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
        if not isinstance(other, FeedbackJsonldFeedbackRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other