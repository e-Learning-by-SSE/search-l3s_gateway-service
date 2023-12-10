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

class LearningStageJsonldLearningStageRead(object):
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
        'context': 'OneOfLearningStageJsonldLearningStageReadContext',
        'id': 'str',
        'type': 'str',
        'id': 'int',
        'task': 'str',
        'course': 'str',
        'prerequisites': 'list[str]',
        'goals': 'list[str]'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'id': 'id',
        'task': 'task',
        'course': 'course',
        'prerequisites': 'prerequisites',
        'goals': 'goals'
    }

    def __init__(self, context=None, id=None, type=None, id=None, task=None, course=None, prerequisites=None, goals=None):  # noqa: E501
        """LearningStageJsonldLearningStageRead - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._id = None
        self._task = None
        self._course = None
        self._prerequisites = None
        self._goals = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if task is not None:
            self.task = task
        if course is not None:
            self.course = course
        if prerequisites is not None:
            self.prerequisites = prerequisites
        if goals is not None:
            self.goals = goals

    @property
    def context(self):
        """Gets the context of this LearningStageJsonldLearningStageRead.  # noqa: E501


        :return: The context of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :rtype: OneOfLearningStageJsonldLearningStageReadContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this LearningStageJsonldLearningStageRead.


        :param context: The context of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :type: OneOfLearningStageJsonldLearningStageReadContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this LearningStageJsonldLearningStageRead.  # noqa: E501


        :return: The id of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LearningStageJsonldLearningStageRead.


        :param id: The id of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this LearningStageJsonldLearningStageRead.  # noqa: E501


        :return: The type of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LearningStageJsonldLearningStageRead.


        :param type: The type of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this LearningStageJsonldLearningStageRead.  # noqa: E501


        :return: The id of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LearningStageJsonldLearningStageRead.


        :param id: The id of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def task(self):
        """Gets the task of this LearningStageJsonldLearningStageRead.  # noqa: E501


        :return: The task of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this LearningStageJsonldLearningStageRead.


        :param task: The task of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :type: str
        """

        self._task = task

    @property
    def course(self):
        """Gets the course of this LearningStageJsonldLearningStageRead.  # noqa: E501


        :return: The course of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :rtype: str
        """
        return self._course

    @course.setter
    def course(self, course):
        """Sets the course of this LearningStageJsonldLearningStageRead.


        :param course: The course of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :type: str
        """

        self._course = course

    @property
    def prerequisites(self):
        """Gets the prerequisites of this LearningStageJsonldLearningStageRead.  # noqa: E501


        :return: The prerequisites of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._prerequisites

    @prerequisites.setter
    def prerequisites(self, prerequisites):
        """Sets the prerequisites of this LearningStageJsonldLearningStageRead.


        :param prerequisites: The prerequisites of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :type: list[str]
        """

        self._prerequisites = prerequisites

    @property
    def goals(self):
        """Gets the goals of this LearningStageJsonldLearningStageRead.  # noqa: E501


        :return: The goals of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._goals

    @goals.setter
    def goals(self, goals):
        """Sets the goals of this LearningStageJsonldLearningStageRead.


        :param goals: The goals of this LearningStageJsonldLearningStageRead.  # noqa: E501
        :type: list[str]
        """

        self._goals = goals

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
        if issubclass(LearningStageJsonldLearningStageRead, dict):
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
        if not isinstance(other, LearningStageJsonldLearningStageRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other