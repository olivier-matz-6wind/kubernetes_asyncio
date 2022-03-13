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


class V1CustomResourceConversion(object):
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
        'strategy': 'str',
        'webhook': 'V1WebhookConversion'
    }

    attribute_map = {
        'strategy': 'strategy',
        'webhook': 'webhook'
    }

    def __init__(self, strategy=None, webhook=None, local_vars_configuration=None):  # noqa: E501
        """V1CustomResourceConversion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._strategy = None
        self._webhook = None
        self.discriminator = None

        self.strategy = strategy
        if webhook is not None:
            self.webhook = webhook

    @property
    def strategy(self):
        """Gets the strategy of this V1CustomResourceConversion.  # noqa: E501

        strategy specifies how custom resources are converted between versions. Allowed values are: - `None`: The converter only change the apiVersion and would not touch any other field in the custom resource. - `Webhook`: API Server will call to an external webhook to do the conversion. Additional information   is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhook to be set.  # noqa: E501

        :return: The strategy of this V1CustomResourceConversion.  # noqa: E501
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """Sets the strategy of this V1CustomResourceConversion.

        strategy specifies how custom resources are converted between versions. Allowed values are: - `None`: The converter only change the apiVersion and would not touch any other field in the custom resource. - `Webhook`: API Server will call to an external webhook to do the conversion. Additional information   is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhook to be set.  # noqa: E501

        :param strategy: The strategy of this V1CustomResourceConversion.  # noqa: E501
        :type strategy: str
        """
        if self.local_vars_configuration.client_side_validation and strategy is None:  # noqa: E501
            raise ValueError("Invalid value for `strategy`, must not be `None`")  # noqa: E501

        self._strategy = strategy

    @property
    def webhook(self):
        """Gets the webhook of this V1CustomResourceConversion.  # noqa: E501


        :return: The webhook of this V1CustomResourceConversion.  # noqa: E501
        :rtype: V1WebhookConversion
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this V1CustomResourceConversion.


        :param webhook: The webhook of this V1CustomResourceConversion.  # noqa: E501
        :type webhook: V1WebhookConversion
        """

        self._webhook = webhook

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
        if not isinstance(other, V1CustomResourceConversion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CustomResourceConversion):
            return True

        return self.to_dict() != other.to_dict()
