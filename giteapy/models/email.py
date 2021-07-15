# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from giteapy.configuration import Configuration


class Email(object):
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
        'email': 'str',
        'primary': 'bool',
        'verified': 'bool'
    }

    attribute_map = {
        'email': 'email',
        'primary': 'primary',
        'verified': 'verified'
    }

    def __init__(self, email=None, primary=None, verified=None, _configuration=None):  # noqa: E501
        """Email - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._primary = None
        self._verified = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if primary is not None:
            self.primary = primary
        if verified is not None:
            self.verified = verified

    @property
    def email(self):
        """Gets the email of this Email.  # noqa: E501


        :return: The email of this Email.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Email.


        :param email: The email of this Email.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def primary(self):
        """Gets the primary of this Email.  # noqa: E501


        :return: The primary of this Email.  # noqa: E501
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this Email.


        :param primary: The primary of this Email.  # noqa: E501
        :type: bool
        """

        self._primary = primary

    @property
    def verified(self):
        """Gets the verified of this Email.  # noqa: E501


        :return: The verified of this Email.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this Email.


        :param verified: The verified of this Email.  # noqa: E501
        :type: bool
        """

        self._verified = verified

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
        if issubclass(Email, dict):
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
        if not isinstance(other, Email):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Email):
            return True

        return self.to_dict() != other.to_dict()
