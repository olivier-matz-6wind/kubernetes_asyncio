# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.21.7
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


class V1ResourceFieldSelector(object):
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
        'container_name': 'str',
        'divisor': 'str',
        'resource': 'str'
    }

    attribute_map = {
        'container_name': 'containerName',
        'divisor': 'divisor',
        'resource': 'resource'
    }

    def __init__(self, container_name=None, divisor=None, resource=None, local_vars_configuration=None):  # noqa: E501
        """V1ResourceFieldSelector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._container_name = None
        self._divisor = None
        self._resource = None
        self.discriminator = None

        if container_name is not None:
            self.container_name = container_name
        if divisor is not None:
            self.divisor = divisor
        self.resource = resource

    @property
    def container_name(self):
        """Gets the container_name of this V1ResourceFieldSelector.  # noqa: E501

        Container name: required for volumes, optional for env vars  # noqa: E501

        :return: The container_name of this V1ResourceFieldSelector.  # noqa: E501
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this V1ResourceFieldSelector.

        Container name: required for volumes, optional for env vars  # noqa: E501

        :param container_name: The container_name of this V1ResourceFieldSelector.  # noqa: E501
        :type container_name: str
        """

        self._container_name = container_name

    @property
    def divisor(self):
        """Gets the divisor of this V1ResourceFieldSelector.  # noqa: E501

        Specifies the output format of the exposed resources, defaults to \"1\"  # noqa: E501

        :return: The divisor of this V1ResourceFieldSelector.  # noqa: E501
        :rtype: str
        """
        return self._divisor

    @divisor.setter
    def divisor(self, divisor):
        """Sets the divisor of this V1ResourceFieldSelector.

        Specifies the output format of the exposed resources, defaults to \"1\"  # noqa: E501

        :param divisor: The divisor of this V1ResourceFieldSelector.  # noqa: E501
        :type divisor: str
        """

        self._divisor = divisor

    @property
    def resource(self):
        """Gets the resource of this V1ResourceFieldSelector.  # noqa: E501

        Required: resource to select  # noqa: E501

        :return: The resource of this V1ResourceFieldSelector.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this V1ResourceFieldSelector.

        Required: resource to select  # noqa: E501

        :param resource: The resource of this V1ResourceFieldSelector.  # noqa: E501
        :type resource: str
        """
        if self.local_vars_configuration.client_side_validation and resource is None:  # noqa: E501
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

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
        if not isinstance(other, V1ResourceFieldSelector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ResourceFieldSelector):
            return True

        return self.to_dict() != other.to_dict()
