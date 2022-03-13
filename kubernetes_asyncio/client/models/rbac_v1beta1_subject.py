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


class RbacV1beta1Subject(object):
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
        'api_group': 'str',
        'kind': 'str',
        'name': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'api_group': 'apiGroup',
        'kind': 'kind',
        'name': 'name',
        'namespace': 'namespace'
    }

    def __init__(self, api_group=None, kind=None, name=None, namespace=None, local_vars_configuration=None):  # noqa: E501
        """RbacV1beta1Subject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._api_group = None
        self._kind = None
        self._name = None
        self._namespace = None
        self.discriminator = None

        if api_group is not None:
            self.api_group = api_group
        self.kind = kind
        self.name = name
        if namespace is not None:
            self.namespace = namespace

    @property
    def api_group(self):
        """Gets the api_group of this RbacV1beta1Subject.  # noqa: E501

        APIGroup holds the API group of the referenced subject. Defaults to \"\" for ServiceAccount subjects. Defaults to \"rbac.authorization.k8s.io\" for User and Group subjects.  # noqa: E501

        :return: The api_group of this RbacV1beta1Subject.  # noqa: E501
        :rtype: str
        """
        return self._api_group

    @api_group.setter
    def api_group(self, api_group):
        """Sets the api_group of this RbacV1beta1Subject.

        APIGroup holds the API group of the referenced subject. Defaults to \"\" for ServiceAccount subjects. Defaults to \"rbac.authorization.k8s.io\" for User and Group subjects.  # noqa: E501

        :param api_group: The api_group of this RbacV1beta1Subject.  # noqa: E501
        :type api_group: str
        """

        self._api_group = api_group

    @property
    def kind(self):
        """Gets the kind of this RbacV1beta1Subject.  # noqa: E501

        Kind of object being referenced. Values defined by this API group are \"User\", \"Group\", and \"ServiceAccount\". If the Authorizer does not recognized the kind value, the Authorizer should report an error.  # noqa: E501

        :return: The kind of this RbacV1beta1Subject.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this RbacV1beta1Subject.

        Kind of object being referenced. Values defined by this API group are \"User\", \"Group\", and \"ServiceAccount\". If the Authorizer does not recognized the kind value, the Authorizer should report an error.  # noqa: E501

        :param kind: The kind of this RbacV1beta1Subject.  # noqa: E501
        :type kind: str
        """
        if self.local_vars_configuration.client_side_validation and kind is None:  # noqa: E501
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this RbacV1beta1Subject.  # noqa: E501

        Name of the object being referenced.  # noqa: E501

        :return: The name of this RbacV1beta1Subject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RbacV1beta1Subject.

        Name of the object being referenced.  # noqa: E501

        :param name: The name of this RbacV1beta1Subject.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this RbacV1beta1Subject.  # noqa: E501

        Namespace of the referenced object.  If the object kind is non-namespace, such as \"User\" or \"Group\", and this value is not empty the Authorizer should report an error.  # noqa: E501

        :return: The namespace of this RbacV1beta1Subject.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this RbacV1beta1Subject.

        Namespace of the referenced object.  If the object kind is non-namespace, such as \"User\" or \"Group\", and this value is not empty the Authorizer should report an error.  # noqa: E501

        :param namespace: The namespace of this RbacV1beta1Subject.  # noqa: E501
        :type namespace: str
        """

        self._namespace = namespace

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
        if not isinstance(other, RbacV1beta1Subject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RbacV1beta1Subject):
            return True

        return self.to_dict() != other.to_dict()
