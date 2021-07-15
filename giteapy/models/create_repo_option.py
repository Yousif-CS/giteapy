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


class CreateRepoOption(object):
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
        'auto_init': 'bool',
        'default_branch': 'str',
        'description': 'str',
        'gitignores': 'str',
        'issue_labels': 'str',
        'license': 'str',
        'name': 'str',
        'private': 'bool',
        'readme': 'str',
        'template': 'bool',
        'trust_model': 'str'
    }

    attribute_map = {
        'auto_init': 'auto_init',
        'default_branch': 'default_branch',
        'description': 'description',
        'gitignores': 'gitignores',
        'issue_labels': 'issue_labels',
        'license': 'license',
        'name': 'name',
        'private': 'private',
        'readme': 'readme',
        'template': 'template',
        'trust_model': 'trust_model'
    }

    def __init__(self, auto_init=None, default_branch=None, description=None, gitignores=None, issue_labels=None, license=None, name=None, private=None, readme=None, template=None, trust_model=None, _configuration=None):  # noqa: E501
        """CreateRepoOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_init = None
        self._default_branch = None
        self._description = None
        self._gitignores = None
        self._issue_labels = None
        self._license = None
        self._name = None
        self._private = None
        self._readme = None
        self._template = None
        self._trust_model = None
        self.discriminator = None

        if auto_init is not None:
            self.auto_init = auto_init
        if default_branch is not None:
            self.default_branch = default_branch
        if description is not None:
            self.description = description
        if gitignores is not None:
            self.gitignores = gitignores
        if issue_labels is not None:
            self.issue_labels = issue_labels
        if license is not None:
            self.license = license
        self.name = name
        if private is not None:
            self.private = private
        if readme is not None:
            self.readme = readme
        if template is not None:
            self.template = template
        if trust_model is not None:
            self.trust_model = trust_model

    @property
    def auto_init(self):
        """Gets the auto_init of this CreateRepoOption.  # noqa: E501

        Whether the repository should be auto-intialized?  # noqa: E501

        :return: The auto_init of this CreateRepoOption.  # noqa: E501
        :rtype: bool
        """
        return self._auto_init

    @auto_init.setter
    def auto_init(self, auto_init):
        """Sets the auto_init of this CreateRepoOption.

        Whether the repository should be auto-intialized?  # noqa: E501

        :param auto_init: The auto_init of this CreateRepoOption.  # noqa: E501
        :type: bool
        """

        self._auto_init = auto_init

    @property
    def default_branch(self):
        """Gets the default_branch of this CreateRepoOption.  # noqa: E501

        DefaultBranch of the repository (used when initializes and in template)  # noqa: E501

        :return: The default_branch of this CreateRepoOption.  # noqa: E501
        :rtype: str
        """
        return self._default_branch

    @default_branch.setter
    def default_branch(self, default_branch):
        """Sets the default_branch of this CreateRepoOption.

        DefaultBranch of the repository (used when initializes and in template)  # noqa: E501

        :param default_branch: The default_branch of this CreateRepoOption.  # noqa: E501
        :type: str
        """

        self._default_branch = default_branch

    @property
    def description(self):
        """Gets the description of this CreateRepoOption.  # noqa: E501

        Description of the repository to create  # noqa: E501

        :return: The description of this CreateRepoOption.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRepoOption.

        Description of the repository to create  # noqa: E501

        :param description: The description of this CreateRepoOption.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def gitignores(self):
        """Gets the gitignores of this CreateRepoOption.  # noqa: E501

        Gitignores to use  # noqa: E501

        :return: The gitignores of this CreateRepoOption.  # noqa: E501
        :rtype: str
        """
        return self._gitignores

    @gitignores.setter
    def gitignores(self, gitignores):
        """Sets the gitignores of this CreateRepoOption.

        Gitignores to use  # noqa: E501

        :param gitignores: The gitignores of this CreateRepoOption.  # noqa: E501
        :type: str
        """

        self._gitignores = gitignores

    @property
    def issue_labels(self):
        """Gets the issue_labels of this CreateRepoOption.  # noqa: E501

        Label-Set to use  # noqa: E501

        :return: The issue_labels of this CreateRepoOption.  # noqa: E501
        :rtype: str
        """
        return self._issue_labels

    @issue_labels.setter
    def issue_labels(self, issue_labels):
        """Sets the issue_labels of this CreateRepoOption.

        Label-Set to use  # noqa: E501

        :param issue_labels: The issue_labels of this CreateRepoOption.  # noqa: E501
        :type: str
        """

        self._issue_labels = issue_labels

    @property
    def license(self):
        """Gets the license of this CreateRepoOption.  # noqa: E501

        License to use  # noqa: E501

        :return: The license of this CreateRepoOption.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this CreateRepoOption.

        License to use  # noqa: E501

        :param license: The license of this CreateRepoOption.  # noqa: E501
        :type: str
        """

        self._license = license

    @property
    def name(self):
        """Gets the name of this CreateRepoOption.  # noqa: E501

        Name of the repository to create  # noqa: E501

        :return: The name of this CreateRepoOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRepoOption.

        Name of the repository to create  # noqa: E501

        :param name: The name of this CreateRepoOption.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def private(self):
        """Gets the private of this CreateRepoOption.  # noqa: E501

        Whether the repository is private  # noqa: E501

        :return: The private of this CreateRepoOption.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this CreateRepoOption.

        Whether the repository is private  # noqa: E501

        :param private: The private of this CreateRepoOption.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def readme(self):
        """Gets the readme of this CreateRepoOption.  # noqa: E501

        Readme of the repository to create  # noqa: E501

        :return: The readme of this CreateRepoOption.  # noqa: E501
        :rtype: str
        """
        return self._readme

    @readme.setter
    def readme(self, readme):
        """Sets the readme of this CreateRepoOption.

        Readme of the repository to create  # noqa: E501

        :param readme: The readme of this CreateRepoOption.  # noqa: E501
        :type: str
        """

        self._readme = readme

    @property
    def template(self):
        """Gets the template of this CreateRepoOption.  # noqa: E501

        Whether the repository is template  # noqa: E501

        :return: The template of this CreateRepoOption.  # noqa: E501
        :rtype: bool
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this CreateRepoOption.

        Whether the repository is template  # noqa: E501

        :param template: The template of this CreateRepoOption.  # noqa: E501
        :type: bool
        """

        self._template = template

    @property
    def trust_model(self):
        """Gets the trust_model of this CreateRepoOption.  # noqa: E501

        TrustModel of the repository  # noqa: E501

        :return: The trust_model of this CreateRepoOption.  # noqa: E501
        :rtype: str
        """
        return self._trust_model

    @trust_model.setter
    def trust_model(self, trust_model):
        """Sets the trust_model of this CreateRepoOption.

        TrustModel of the repository  # noqa: E501

        :param trust_model: The trust_model of this CreateRepoOption.  # noqa: E501
        :type: str
        """
        allowed_values = ["default", "collaborator", "committer", "collaboratorcommitter"]  # noqa: E501
        if (self._configuration.client_side_validation and
                trust_model not in allowed_values):
            raise ValueError(
                "Invalid value for `trust_model` ({0}), must be one of {1}"  # noqa: E501
                .format(trust_model, allowed_values)
            )

        self._trust_model = trust_model

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
        if issubclass(CreateRepoOption, dict):
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
        if not isinstance(other, CreateRepoOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateRepoOption):
            return True

        return self.to_dict() != other.to_dict()
