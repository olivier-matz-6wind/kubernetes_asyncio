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


class V2beta1PodsMetricSource(object):
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
        'metric_name': 'str',
        'selector': 'V1LabelSelector',
        'target_average_value': 'str'
    }

    attribute_map = {
        'metric_name': 'metricName',
        'selector': 'selector',
        'target_average_value': 'targetAverageValue'
    }

    def __init__(self, metric_name=None, selector=None, target_average_value=None, local_vars_configuration=None):  # noqa: E501
        """V2beta1PodsMetricSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._metric_name = None
        self._selector = None
        self._target_average_value = None
        self.discriminator = None

        self.metric_name = metric_name
        if selector is not None:
            self.selector = selector
        self.target_average_value = target_average_value

    @property
    def metric_name(self):
        """Gets the metric_name of this V2beta1PodsMetricSource.  # noqa: E501

        metricName is the name of the metric in question  # noqa: E501

        :return: The metric_name of this V2beta1PodsMetricSource.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this V2beta1PodsMetricSource.

        metricName is the name of the metric in question  # noqa: E501

        :param metric_name: The metric_name of this V2beta1PodsMetricSource.  # noqa: E501
        :type metric_name: str
        """
        if self.local_vars_configuration.client_side_validation and metric_name is None:  # noqa: E501
            raise ValueError("Invalid value for `metric_name`, must not be `None`")  # noqa: E501

        self._metric_name = metric_name

    @property
    def selector(self):
        """Gets the selector of this V2beta1PodsMetricSource.  # noqa: E501


        :return: The selector of this V2beta1PodsMetricSource.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this V2beta1PodsMetricSource.


        :param selector: The selector of this V2beta1PodsMetricSource.  # noqa: E501
        :type selector: V1LabelSelector
        """

        self._selector = selector

    @property
    def target_average_value(self):
        """Gets the target_average_value of this V2beta1PodsMetricSource.  # noqa: E501

        targetAverageValue is the target value of the average of the metric across all relevant pods (as a quantity)  # noqa: E501

        :return: The target_average_value of this V2beta1PodsMetricSource.  # noqa: E501
        :rtype: str
        """
        return self._target_average_value

    @target_average_value.setter
    def target_average_value(self, target_average_value):
        """Sets the target_average_value of this V2beta1PodsMetricSource.

        targetAverageValue is the target value of the average of the metric across all relevant pods (as a quantity)  # noqa: E501

        :param target_average_value: The target_average_value of this V2beta1PodsMetricSource.  # noqa: E501
        :type target_average_value: str
        """
        if self.local_vars_configuration.client_side_validation and target_average_value is None:  # noqa: E501
            raise ValueError("Invalid value for `target_average_value`, must not be `None`")  # noqa: E501

        self._target_average_value = target_average_value

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
        if not isinstance(other, V2beta1PodsMetricSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2beta1PodsMetricSource):
            return True

        return self.to_dict() != other.to_dict()
