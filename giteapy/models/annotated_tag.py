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


class AnnotatedTag(object):
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
        'message': 'str',
        'object': 'AnnotatedTagObject',
        'sha': 'str',
        'tag': 'str',
        'tagger': 'CommitUser',
        'url': 'str',
        'verification': 'PayloadCommitVerification'
    }

    attribute_map = {
        'message': 'message',
        'object': 'object',
        'sha': 'sha',
        'tag': 'tag',
        'tagger': 'tagger',
        'url': 'url',
        'verification': 'verification'
    }

    def __init__(self, message=None, object=None, sha=None, tag=None, tagger=None, url=None, verification=None, _configuration=None):  # noqa: E501
        """AnnotatedTag - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message = None
        self._object = None
        self._sha = None
        self._tag = None
        self._tagger = None
        self._url = None
        self._verification = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if object is not None:
            self.object = object
        if sha is not None:
            self.sha = sha
        if tag is not None:
            self.tag = tag
        if tagger is not None:
            self.tagger = tagger
        if url is not None:
            self.url = url
        if verification is not None:
            self.verification = verification

    @property
    def message(self):
        """Gets the message of this AnnotatedTag.  # noqa: E501


        :return: The message of this AnnotatedTag.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AnnotatedTag.


        :param message: The message of this AnnotatedTag.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def object(self):
        """Gets the object of this AnnotatedTag.  # noqa: E501


        :return: The object of this AnnotatedTag.  # noqa: E501
        :rtype: AnnotatedTagObject
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this AnnotatedTag.


        :param object: The object of this AnnotatedTag.  # noqa: E501
        :type: AnnotatedTagObject
        """

        self._object = object

    @property
    def sha(self):
        """Gets the sha of this AnnotatedTag.  # noqa: E501


        :return: The sha of this AnnotatedTag.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this AnnotatedTag.


        :param sha: The sha of this AnnotatedTag.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def tag(self):
        """Gets the tag of this AnnotatedTag.  # noqa: E501


        :return: The tag of this AnnotatedTag.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this AnnotatedTag.


        :param tag: The tag of this AnnotatedTag.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def tagger(self):
        """Gets the tagger of this AnnotatedTag.  # noqa: E501


        :return: The tagger of this AnnotatedTag.  # noqa: E501
        :rtype: CommitUser
        """
        return self._tagger

    @tagger.setter
    def tagger(self, tagger):
        """Sets the tagger of this AnnotatedTag.


        :param tagger: The tagger of this AnnotatedTag.  # noqa: E501
        :type: CommitUser
        """

        self._tagger = tagger

    @property
    def url(self):
        """Gets the url of this AnnotatedTag.  # noqa: E501


        :return: The url of this AnnotatedTag.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AnnotatedTag.


        :param url: The url of this AnnotatedTag.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def verification(self):
        """Gets the verification of this AnnotatedTag.  # noqa: E501


        :return: The verification of this AnnotatedTag.  # noqa: E501
        :rtype: PayloadCommitVerification
        """
        return self._verification

    @verification.setter
    def verification(self, verification):
        """Sets the verification of this AnnotatedTag.


        :param verification: The verification of this AnnotatedTag.  # noqa: E501
        :type: PayloadCommitVerification
        """

        self._verification = verification

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
        if issubclass(AnnotatedTag, dict):
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
        if not isinstance(other, AnnotatedTag):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnnotatedTag):
            return True

        return self.to_dict() != other.to_dict()
