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

class ExternalContentExternalContentOrganizationRead(object):
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
        'license_model': 'str',
        'supplier': 'str'
    }

    attribute_map = {
        'license_model': 'licenseModel',
        'supplier': 'supplier'
    }

    def __init__(self, license_model=None, supplier=None):  # noqa: E501
        """ExternalContentExternalContentOrganizationRead - a model defined in Swagger"""  # noqa: E501
        self._license_model = None
        self._supplier = None
        self.discriminator = None
        if license_model is not None:
            self.license_model = license_model
        if supplier is not None:
            self.supplier = supplier

    @property
    def license_model(self):
        """Gets the license_model of this ExternalContentExternalContentOrganizationRead.  # noqa: E501


        :return: The license_model of this ExternalContentExternalContentOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """Sets the license_model of this ExternalContentExternalContentOrganizationRead.


        :param license_model: The license_model of this ExternalContentExternalContentOrganizationRead.  # noqa: E501
        :type: str
        """

        self._license_model = license_model

    @property
    def supplier(self):
        """Gets the supplier of this ExternalContentExternalContentOrganizationRead.  # noqa: E501


        :return: The supplier of this ExternalContentExternalContentOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this ExternalContentExternalContentOrganizationRead.


        :param supplier: The supplier of this ExternalContentExternalContentOrganizationRead.  # noqa: E501
        :type: str
        """

        self._supplier = supplier

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
        if issubclass(ExternalContentExternalContentOrganizationRead, dict):
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
        if not isinstance(other, ExternalContentExternalContentOrganizationRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other