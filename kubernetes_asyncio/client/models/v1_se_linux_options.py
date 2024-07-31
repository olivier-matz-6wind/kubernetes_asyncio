# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.30.3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class V1SELinuxOptions(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'level': 'str',
        'role': 'str',
        'type': 'str',
        'user': 'str'
    }

    attribute_map = {
        'level': 'level',
        'role': 'role',
        'type': 'type',
        'user': 'user'
    }

    def __init__(self, level=None, role=None, type=None, user=None, local_vars_configuration=None):  # noqa: E501
        """V1SELinuxOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._level = None
        self._role = None
        self._type = None
        self._user = None
        self.discriminator = None

        if level is not None:
            self.level = level
        if role is not None:
            self.role = role
        if type is not None:
            self.type = type
        if user is not None:
            self.user = user

    @property
    def level(self):
        """Gets the level of this V1SELinuxOptions.  # noqa: E501

        Level is SELinux level label that applies to the container.  # noqa: E501

        :return: The level of this V1SELinuxOptions.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this V1SELinuxOptions.

        Level is SELinux level label that applies to the container.  # noqa: E501

        :param level: The level of this V1SELinuxOptions.  # noqa: E501
        :type level: str
        """

        self._level = level

    @property
    def role(self):
        """Gets the role of this V1SELinuxOptions.  # noqa: E501

        Role is a SELinux role label that applies to the container.  # noqa: E501

        :return: The role of this V1SELinuxOptions.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this V1SELinuxOptions.

        Role is a SELinux role label that applies to the container.  # noqa: E501

        :param role: The role of this V1SELinuxOptions.  # noqa: E501
        :type role: str
        """

        self._role = role

    @property
    def type(self):
        """Gets the type of this V1SELinuxOptions.  # noqa: E501

        Type is a SELinux type label that applies to the container.  # noqa: E501

        :return: The type of this V1SELinuxOptions.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1SELinuxOptions.

        Type is a SELinux type label that applies to the container.  # noqa: E501

        :param type: The type of this V1SELinuxOptions.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def user(self):
        """Gets the user of this V1SELinuxOptions.  # noqa: E501

        User is a SELinux user label that applies to the container.  # noqa: E501

        :return: The user of this V1SELinuxOptions.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this V1SELinuxOptions.

        User is a SELinux user label that applies to the container.  # noqa: E501

        :param user: The user of this V1SELinuxOptions.  # noqa: E501
        :type user: str
        """

        self._user = user

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1SELinuxOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1SELinuxOptions):
            return True

        return self.to_dict() != other.to_dict()
