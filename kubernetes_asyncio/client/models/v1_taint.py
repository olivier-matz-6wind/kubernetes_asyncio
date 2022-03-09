# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.21.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class V1Taint(object):
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
        'effect': 'str',
        'key': 'str',
        'time_added': 'datetime',
        'value': 'str'
    }

    attribute_map = {
        'effect': 'effect',
        'key': 'key',
        'time_added': 'timeAdded',
        'value': 'value'
    }

    def __init__(self, effect=None, key=None, time_added=None, value=None, local_vars_configuration=None):  # noqa: E501
        """V1Taint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._effect = None
        self._key = None
        self._time_added = None
        self._value = None
        self.discriminator = None

        self.effect = effect
        self.key = key
        if time_added is not None:
            self.time_added = time_added
        if value is not None:
            self.value = value

    @property
    def effect(self):
        """Gets the effect of this V1Taint.  # noqa: E501

        Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.  # noqa: E501

        :return: The effect of this V1Taint.  # noqa: E501
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this V1Taint.

        Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.  # noqa: E501

        :param effect: The effect of this V1Taint.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and effect is None:  # noqa: E501
            raise ValueError("Invalid value for `effect`, must not be `None`")  # noqa: E501

        self._effect = effect

    @property
    def key(self):
        """Gets the key of this V1Taint.  # noqa: E501

        Required. The taint key to be applied to a node.  # noqa: E501

        :return: The key of this V1Taint.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this V1Taint.

        Required. The taint key to be applied to a node.  # noqa: E501

        :param key: The key of this V1Taint.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def time_added(self):
        """Gets the time_added of this V1Taint.  # noqa: E501

        TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.  # noqa: E501

        :return: The time_added of this V1Taint.  # noqa: E501
        :rtype: datetime
        """
        return self._time_added

    @time_added.setter
    def time_added(self, time_added):
        """Sets the time_added of this V1Taint.

        TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.  # noqa: E501

        :param time_added: The time_added of this V1Taint.  # noqa: E501
        :type: datetime
        """

        self._time_added = time_added

    @property
    def value(self):
        """Gets the value of this V1Taint.  # noqa: E501

        The taint value corresponding to the taint key.  # noqa: E501

        :return: The value of this V1Taint.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this V1Taint.

        The taint value corresponding to the taint key.  # noqa: E501

        :param value: The value of this V1Taint.  # noqa: E501
        :type: str
        """

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1Taint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Taint):
            return True

        return self.to_dict() != other.to_dict()
