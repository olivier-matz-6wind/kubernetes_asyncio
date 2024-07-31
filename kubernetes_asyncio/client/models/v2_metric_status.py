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


class V2MetricStatus(object):
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
        'container_resource': 'V2ContainerResourceMetricStatus',
        'external': 'V2ExternalMetricStatus',
        'object': 'V2ObjectMetricStatus',
        'pods': 'V2PodsMetricStatus',
        'resource': 'V2ResourceMetricStatus',
        'type': 'str'
    }

    attribute_map = {
        'container_resource': 'containerResource',
        'external': 'external',
        'object': 'object',
        'pods': 'pods',
        'resource': 'resource',
        'type': 'type'
    }

    def __init__(self, container_resource=None, external=None, object=None, pods=None, resource=None, type=None, local_vars_configuration=None):  # noqa: E501
        """V2MetricStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._container_resource = None
        self._external = None
        self._object = None
        self._pods = None
        self._resource = None
        self._type = None
        self.discriminator = None

        if container_resource is not None:
            self.container_resource = container_resource
        if external is not None:
            self.external = external
        if object is not None:
            self.object = object
        if pods is not None:
            self.pods = pods
        if resource is not None:
            self.resource = resource
        self.type = type

    @property
    def container_resource(self):
        """Gets the container_resource of this V2MetricStatus.  # noqa: E501


        :return: The container_resource of this V2MetricStatus.  # noqa: E501
        :rtype: V2ContainerResourceMetricStatus
        """
        return self._container_resource

    @container_resource.setter
    def container_resource(self, container_resource):
        """Sets the container_resource of this V2MetricStatus.


        :param container_resource: The container_resource of this V2MetricStatus.  # noqa: E501
        :type container_resource: V2ContainerResourceMetricStatus
        """

        self._container_resource = container_resource

    @property
    def external(self):
        """Gets the external of this V2MetricStatus.  # noqa: E501


        :return: The external of this V2MetricStatus.  # noqa: E501
        :rtype: V2ExternalMetricStatus
        """
        return self._external

    @external.setter
    def external(self, external):
        """Sets the external of this V2MetricStatus.


        :param external: The external of this V2MetricStatus.  # noqa: E501
        :type external: V2ExternalMetricStatus
        """

        self._external = external

    @property
    def object(self):
        """Gets the object of this V2MetricStatus.  # noqa: E501


        :return: The object of this V2MetricStatus.  # noqa: E501
        :rtype: V2ObjectMetricStatus
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this V2MetricStatus.


        :param object: The object of this V2MetricStatus.  # noqa: E501
        :type object: V2ObjectMetricStatus
        """

        self._object = object

    @property
    def pods(self):
        """Gets the pods of this V2MetricStatus.  # noqa: E501


        :return: The pods of this V2MetricStatus.  # noqa: E501
        :rtype: V2PodsMetricStatus
        """
        return self._pods

    @pods.setter
    def pods(self, pods):
        """Sets the pods of this V2MetricStatus.


        :param pods: The pods of this V2MetricStatus.  # noqa: E501
        :type pods: V2PodsMetricStatus
        """

        self._pods = pods

    @property
    def resource(self):
        """Gets the resource of this V2MetricStatus.  # noqa: E501


        :return: The resource of this V2MetricStatus.  # noqa: E501
        :rtype: V2ResourceMetricStatus
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this V2MetricStatus.


        :param resource: The resource of this V2MetricStatus.  # noqa: E501
        :type resource: V2ResourceMetricStatus
        """

        self._resource = resource

    @property
    def type(self):
        """Gets the type of this V2MetricStatus.  # noqa: E501

        type is the type of metric source.  It will be one of \"ContainerResource\", \"External\", \"Object\", \"Pods\" or \"Resource\", each corresponds to a matching field in the object. Note: \"ContainerResource\" type is available on when the feature-gate HPAContainerMetrics is enabled  # noqa: E501

        :return: The type of this V2MetricStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V2MetricStatus.

        type is the type of metric source.  It will be one of \"ContainerResource\", \"External\", \"Object\", \"Pods\" or \"Resource\", each corresponds to a matching field in the object. Note: \"ContainerResource\" type is available on when the feature-gate HPAContainerMetrics is enabled  # noqa: E501

        :param type: The type of this V2MetricStatus.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, V2MetricStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2MetricStatus):
            return True

        return self.to_dict() != other.to_dict()
