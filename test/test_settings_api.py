# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import giteapy
from giteapy.api.settings_api import SettingsApi  # noqa: E501
from giteapy.rest import ApiException


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self):
        self.api = giteapy.api.settings_api.SettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_general_api_settings(self):
        """Test case for get_general_api_settings

        Get instance's global settings for api  # noqa: E501
        """
        pass

    def test_get_general_attachment_settings(self):
        """Test case for get_general_attachment_settings

        Get instance's global settings for Attachment  # noqa: E501
        """
        pass

    def test_get_general_repository_settings(self):
        """Test case for get_general_repository_settings

        Get instance's global settings for repositories  # noqa: E501
        """
        pass

    def test_get_general_ui_settings(self):
        """Test case for get_general_ui_settings

        Get instance's global settings for ui  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
