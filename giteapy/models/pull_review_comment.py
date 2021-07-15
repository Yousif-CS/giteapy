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

from swagger_client.configuration import Configuration


class PullReviewComment(object):
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
        'body': 'str',
        'commit_id': 'str',
        'created_at': 'datetime',
        'diff_hunk': 'str',
        'html_url': 'str',
        'id': 'int',
        'original_commit_id': 'str',
        'original_position': 'int',
        'path': 'str',
        'position': 'int',
        'pull_request_review_id': 'int',
        'pull_request_url': 'str',
        'resolver': 'User',
        'updated_at': 'datetime',
        'user': 'User'
    }

    attribute_map = {
        'body': 'body',
        'commit_id': 'commit_id',
        'created_at': 'created_at',
        'diff_hunk': 'diff_hunk',
        'html_url': 'html_url',
        'id': 'id',
        'original_commit_id': 'original_commit_id',
        'original_position': 'original_position',
        'path': 'path',
        'position': 'position',
        'pull_request_review_id': 'pull_request_review_id',
        'pull_request_url': 'pull_request_url',
        'resolver': 'resolver',
        'updated_at': 'updated_at',
        'user': 'user'
    }

    def __init__(self, body=None, commit_id=None, created_at=None, diff_hunk=None, html_url=None, id=None, original_commit_id=None, original_position=None, path=None, position=None, pull_request_review_id=None, pull_request_url=None, resolver=None, updated_at=None, user=None, _configuration=None):  # noqa: E501
        """PullReviewComment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._body = None
        self._commit_id = None
        self._created_at = None
        self._diff_hunk = None
        self._html_url = None
        self._id = None
        self._original_commit_id = None
        self._original_position = None
        self._path = None
        self._position = None
        self._pull_request_review_id = None
        self._pull_request_url = None
        self._resolver = None
        self._updated_at = None
        self._user = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if commit_id is not None:
            self.commit_id = commit_id
        if created_at is not None:
            self.created_at = created_at
        if diff_hunk is not None:
            self.diff_hunk = diff_hunk
        if html_url is not None:
            self.html_url = html_url
        if id is not None:
            self.id = id
        if original_commit_id is not None:
            self.original_commit_id = original_commit_id
        if original_position is not None:
            self.original_position = original_position
        if path is not None:
            self.path = path
        if position is not None:
            self.position = position
        if pull_request_review_id is not None:
            self.pull_request_review_id = pull_request_review_id
        if pull_request_url is not None:
            self.pull_request_url = pull_request_url
        if resolver is not None:
            self.resolver = resolver
        if updated_at is not None:
            self.updated_at = updated_at
        if user is not None:
            self.user = user

    @property
    def body(self):
        """Gets the body of this PullReviewComment.  # noqa: E501


        :return: The body of this PullReviewComment.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this PullReviewComment.


        :param body: The body of this PullReviewComment.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def commit_id(self):
        """Gets the commit_id of this PullReviewComment.  # noqa: E501


        :return: The commit_id of this PullReviewComment.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this PullReviewComment.


        :param commit_id: The commit_id of this PullReviewComment.  # noqa: E501
        :type: str
        """

        self._commit_id = commit_id

    @property
    def created_at(self):
        """Gets the created_at of this PullReviewComment.  # noqa: E501


        :return: The created_at of this PullReviewComment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PullReviewComment.


        :param created_at: The created_at of this PullReviewComment.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def diff_hunk(self):
        """Gets the diff_hunk of this PullReviewComment.  # noqa: E501


        :return: The diff_hunk of this PullReviewComment.  # noqa: E501
        :rtype: str
        """
        return self._diff_hunk

    @diff_hunk.setter
    def diff_hunk(self, diff_hunk):
        """Sets the diff_hunk of this PullReviewComment.


        :param diff_hunk: The diff_hunk of this PullReviewComment.  # noqa: E501
        :type: str
        """

        self._diff_hunk = diff_hunk

    @property
    def html_url(self):
        """Gets the html_url of this PullReviewComment.  # noqa: E501


        :return: The html_url of this PullReviewComment.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this PullReviewComment.


        :param html_url: The html_url of this PullReviewComment.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def id(self):
        """Gets the id of this PullReviewComment.  # noqa: E501


        :return: The id of this PullReviewComment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PullReviewComment.


        :param id: The id of this PullReviewComment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def original_commit_id(self):
        """Gets the original_commit_id of this PullReviewComment.  # noqa: E501


        :return: The original_commit_id of this PullReviewComment.  # noqa: E501
        :rtype: str
        """
        return self._original_commit_id

    @original_commit_id.setter
    def original_commit_id(self, original_commit_id):
        """Sets the original_commit_id of this PullReviewComment.


        :param original_commit_id: The original_commit_id of this PullReviewComment.  # noqa: E501
        :type: str
        """

        self._original_commit_id = original_commit_id

    @property
    def original_position(self):
        """Gets the original_position of this PullReviewComment.  # noqa: E501


        :return: The original_position of this PullReviewComment.  # noqa: E501
        :rtype: int
        """
        return self._original_position

    @original_position.setter
    def original_position(self, original_position):
        """Sets the original_position of this PullReviewComment.


        :param original_position: The original_position of this PullReviewComment.  # noqa: E501
        :type: int
        """

        self._original_position = original_position

    @property
    def path(self):
        """Gets the path of this PullReviewComment.  # noqa: E501


        :return: The path of this PullReviewComment.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PullReviewComment.


        :param path: The path of this PullReviewComment.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def position(self):
        """Gets the position of this PullReviewComment.  # noqa: E501


        :return: The position of this PullReviewComment.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PullReviewComment.


        :param position: The position of this PullReviewComment.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def pull_request_review_id(self):
        """Gets the pull_request_review_id of this PullReviewComment.  # noqa: E501


        :return: The pull_request_review_id of this PullReviewComment.  # noqa: E501
        :rtype: int
        """
        return self._pull_request_review_id

    @pull_request_review_id.setter
    def pull_request_review_id(self, pull_request_review_id):
        """Sets the pull_request_review_id of this PullReviewComment.


        :param pull_request_review_id: The pull_request_review_id of this PullReviewComment.  # noqa: E501
        :type: int
        """

        self._pull_request_review_id = pull_request_review_id

    @property
    def pull_request_url(self):
        """Gets the pull_request_url of this PullReviewComment.  # noqa: E501


        :return: The pull_request_url of this PullReviewComment.  # noqa: E501
        :rtype: str
        """
        return self._pull_request_url

    @pull_request_url.setter
    def pull_request_url(self, pull_request_url):
        """Sets the pull_request_url of this PullReviewComment.


        :param pull_request_url: The pull_request_url of this PullReviewComment.  # noqa: E501
        :type: str
        """

        self._pull_request_url = pull_request_url

    @property
    def resolver(self):
        """Gets the resolver of this PullReviewComment.  # noqa: E501


        :return: The resolver of this PullReviewComment.  # noqa: E501
        :rtype: User
        """
        return self._resolver

    @resolver.setter
    def resolver(self, resolver):
        """Sets the resolver of this PullReviewComment.


        :param resolver: The resolver of this PullReviewComment.  # noqa: E501
        :type: User
        """

        self._resolver = resolver

    @property
    def updated_at(self):
        """Gets the updated_at of this PullReviewComment.  # noqa: E501


        :return: The updated_at of this PullReviewComment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PullReviewComment.


        :param updated_at: The updated_at of this PullReviewComment.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user(self):
        """Gets the user of this PullReviewComment.  # noqa: E501


        :return: The user of this PullReviewComment.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PullReviewComment.


        :param user: The user of this PullReviewComment.  # noqa: E501
        :type: User
        """

        self._user = user

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
        if issubclass(PullReviewComment, dict):
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
        if not isinstance(other, PullReviewComment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PullReviewComment):
            return True

        return self.to_dict() != other.to_dict()
