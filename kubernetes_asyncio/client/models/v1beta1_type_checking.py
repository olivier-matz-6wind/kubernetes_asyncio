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


class V1beta1TypeChecking(object):
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
        'expression_warnings': 'list[V1beta1ExpressionWarning]'
    }

    attribute_map = {
        'expression_warnings': 'expressionWarnings'
    }

    def __init__(self, expression_warnings=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1TypeChecking - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._expression_warnings = None
        self.discriminator = None

        if expression_warnings is not None:
            self.expression_warnings = expression_warnings

    @property
    def expression_warnings(self):
        """Gets the expression_warnings of this V1beta1TypeChecking.  # noqa: E501

        The type checking warnings for each expression.  # noqa: E501

        :return: The expression_warnings of this V1beta1TypeChecking.  # noqa: E501
        :rtype: list[V1beta1ExpressionWarning]
        """
        return self._expression_warnings

    @expression_warnings.setter
    def expression_warnings(self, expression_warnings):
        """Sets the expression_warnings of this V1beta1TypeChecking.

        The type checking warnings for each expression.  # noqa: E501

        :param expression_warnings: The expression_warnings of this V1beta1TypeChecking.  # noqa: E501
        :type expression_warnings: list[V1beta1ExpressionWarning]
        """

        self._expression_warnings = expression_warnings

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
        if not isinstance(other, V1beta1TypeChecking):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1TypeChecking):
            return True

        return self.to_dict() != other.to_dict()
