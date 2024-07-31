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


class V1ResourceAttributes(object):
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
        'group': 'str',
        'name': 'str',
        'namespace': 'str',
        'resource': 'str',
        'subresource': 'str',
        'verb': 'str',
        'version': 'str'
    }

    attribute_map = {
        'group': 'group',
        'name': 'name',
        'namespace': 'namespace',
        'resource': 'resource',
        'subresource': 'subresource',
        'verb': 'verb',
        'version': 'version'
    }

    def __init__(self, group=None, name=None, namespace=None, resource=None, subresource=None, verb=None, version=None, local_vars_configuration=None):  # noqa: E501
        """V1ResourceAttributes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._group = None
        self._name = None
        self._namespace = None
        self._resource = None
        self._subresource = None
        self._verb = None
        self._version = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if resource is not None:
            self.resource = resource
        if subresource is not None:
            self.subresource = subresource
        if verb is not None:
            self.verb = verb
        if version is not None:
            self.version = version

    @property
    def group(self):
        """Gets the group of this V1ResourceAttributes.  # noqa: E501

        Group is the API Group of the Resource.  \"*\" means all.  # noqa: E501

        :return: The group of this V1ResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this V1ResourceAttributes.

        Group is the API Group of the Resource.  \"*\" means all.  # noqa: E501

        :param group: The group of this V1ResourceAttributes.  # noqa: E501
        :type group: str
        """

        self._group = group

    @property
    def name(self):
        """Gets the name of this V1ResourceAttributes.  # noqa: E501

        Name is the name of the resource being requested for a \"get\" or deleted for a \"delete\". \"\" (empty) means all.  # noqa: E501

        :return: The name of this V1ResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1ResourceAttributes.

        Name is the name of the resource being requested for a \"get\" or deleted for a \"delete\". \"\" (empty) means all.  # noqa: E501

        :param name: The name of this V1ResourceAttributes.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this V1ResourceAttributes.  # noqa: E501

        Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces \"\" (empty) is defaulted for LocalSubjectAccessReviews \"\" (empty) is empty for cluster-scoped resources \"\" (empty) means \"all\" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview  # noqa: E501

        :return: The namespace of this V1ResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1ResourceAttributes.

        Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces \"\" (empty) is defaulted for LocalSubjectAccessReviews \"\" (empty) is empty for cluster-scoped resources \"\" (empty) means \"all\" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview  # noqa: E501

        :param namespace: The namespace of this V1ResourceAttributes.  # noqa: E501
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def resource(self):
        """Gets the resource of this V1ResourceAttributes.  # noqa: E501

        Resource is one of the existing resource types.  \"*\" means all.  # noqa: E501

        :return: The resource of this V1ResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this V1ResourceAttributes.

        Resource is one of the existing resource types.  \"*\" means all.  # noqa: E501

        :param resource: The resource of this V1ResourceAttributes.  # noqa: E501
        :type resource: str
        """

        self._resource = resource

    @property
    def subresource(self):
        """Gets the subresource of this V1ResourceAttributes.  # noqa: E501

        Subresource is one of the existing resource types.  \"\" means none.  # noqa: E501

        :return: The subresource of this V1ResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._subresource

    @subresource.setter
    def subresource(self, subresource):
        """Sets the subresource of this V1ResourceAttributes.

        Subresource is one of the existing resource types.  \"\" means none.  # noqa: E501

        :param subresource: The subresource of this V1ResourceAttributes.  # noqa: E501
        :type subresource: str
        """

        self._subresource = subresource

    @property
    def verb(self):
        """Gets the verb of this V1ResourceAttributes.  # noqa: E501

        Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  \"*\" means all.  # noqa: E501

        :return: The verb of this V1ResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """Sets the verb of this V1ResourceAttributes.

        Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  \"*\" means all.  # noqa: E501

        :param verb: The verb of this V1ResourceAttributes.  # noqa: E501
        :type verb: str
        """

        self._verb = verb

    @property
    def version(self):
        """Gets the version of this V1ResourceAttributes.  # noqa: E501

        Version is the API Version of the Resource.  \"*\" means all.  # noqa: E501

        :return: The version of this V1ResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1ResourceAttributes.

        Version is the API Version of the Resource.  \"*\" means all.  # noqa: E501

        :param version: The version of this V1ResourceAttributes.  # noqa: E501
        :type version: str
        """

        self._version = version

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
        if not isinstance(other, V1ResourceAttributes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ResourceAttributes):
            return True

        return self.to_dict() != other.to_dict()
