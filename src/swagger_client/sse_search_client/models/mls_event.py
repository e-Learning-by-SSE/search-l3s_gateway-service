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

class MLSEvent(object):
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
        'entity_type': 'str',
        'method': 'str',
        'id': 'str',
        'payload': 'object',
        'task_todo_payload': 'object'
    }

    attribute_map = {
        'entity_type': 'entityType',
        'method': 'method',
        'id': 'id',
        'payload': 'payload',
        'task_todo_payload': 'taskTodoPayload'
    }

    def __init__(self, entity_type=None, method=None, id=None, payload=None, task_todo_payload=None):  # noqa: E501
        """MLSEvent - a model defined in Swagger"""  # noqa: E501
        self._entity_type = None
        self._method = None
        self._id = None
        self._payload = None
        self._task_todo_payload = None
        self.discriminator = None
        self.entity_type = entity_type
        self.method = method
        self.id = id
        self.payload = payload
        if task_todo_payload is not None:
            self.task_todo_payload = task_todo_payload

    @property
    def entity_type(self):
        """Gets the entity_type of this MLSEvent.  # noqa: E501

        Which entity is concerned by the event? User/Task/TaskTodo/TaskTodoInfo  # noqa: E501

        :return: The entity_type of this MLSEvent.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this MLSEvent.

        Which entity is concerned by the event? User/Task/TaskTodo/TaskTodoInfo  # noqa: E501

        :param entity_type: The entity_type of this MLSEvent.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501
        allowed_values = ["User", "TaskTodo", "TaskTodoInfo", "Task", "Other"]  # noqa: E501
        if entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def method(self):
        """Gets the method of this MLSEvent.  # noqa: E501

        What kind is the event of? PUT/POST/DELETE  # noqa: E501

        :return: The method of this MLSEvent.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this MLSEvent.

        What kind is the event of? PUT/POST/DELETE  # noqa: E501

        :param method: The method of this MLSEvent.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501
        allowed_values = ["PUT", "POST", "DELETE", "Other"]  # noqa: E501
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def id(self):
        """Gets the id of this MLSEvent.  # noqa: E501

        The unique id used in the MLS system for the entity.  # noqa: E501

        :return: The id of this MLSEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MLSEvent.

        The unique id used in the MLS system for the entity.  # noqa: E501

        :param id: The id of this MLSEvent.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def payload(self):
        """Gets the payload of this MLSEvent.  # noqa: E501

        The complete entity (including its id and all other attributes existing in the MLS system)  # noqa: E501

        :return: The payload of this MLSEvent.  # noqa: E501
        :rtype: object
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this MLSEvent.

        The complete entity (including its id and all other attributes existing in the MLS system)  # noqa: E501

        :param payload: The payload of this MLSEvent.  # noqa: E501
        :type: object
        """
        if payload is None:
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        self._payload = payload

    @property
    def task_todo_payload(self):
        """Gets the task_todo_payload of this MLSEvent.  # noqa: E501

        A special payload to get the parent object of a taskTodoInfo object. Only existent for this kind of object.  # noqa: E501

        :return: The task_todo_payload of this MLSEvent.  # noqa: E501
        :rtype: object
        """
        return self._task_todo_payload

    @task_todo_payload.setter
    def task_todo_payload(self, task_todo_payload):
        """Sets the task_todo_payload of this MLSEvent.

        A special payload to get the parent object of a taskTodoInfo object. Only existent for this kind of object.  # noqa: E501

        :param task_todo_payload: The task_todo_payload of this MLSEvent.  # noqa: E501
        :type: object
        """

        self._task_todo_payload = task_todo_payload

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
        if issubclass(MLSEvent, dict):
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
        if not isinstance(other, MLSEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
