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


class V1alpha1ClusterTrustBundleSpec(object):
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
        'signer_name': 'str',
        'trust_bundle': 'str'
    }

    attribute_map = {
        'signer_name': 'signerName',
        'trust_bundle': 'trustBundle'
    }

    def __init__(self, signer_name=None, trust_bundle=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ClusterTrustBundleSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default()
        self.local_vars_configuration = local_vars_configuration

        self._signer_name = None
        self._trust_bundle = None
        self.discriminator = None

        if signer_name is not None:
            self.signer_name = signer_name
        self.trust_bundle = trust_bundle

    @property
    def signer_name(self):
        """Gets the signer_name of this V1alpha1ClusterTrustBundleSpec.  # noqa: E501

        signerName indicates the associated signer, if any.  In order to create or update a ClusterTrustBundle that sets signerName, you must have the following cluster-scoped permission: group=certificates.k8s.io resource=signers resourceName=<the signer name> verb=attest.  If signerName is not empty, then the ClusterTrustBundle object must be named with the signer name as a prefix (translating slashes to colons). For example, for the signer name `example.com/foo`, valid ClusterTrustBundle object names include `example.com:foo:abc` and `example.com:foo:v1`.  If signerName is empty, then the ClusterTrustBundle object's name must not have such a prefix.  List/watch requests for ClusterTrustBundles can filter on this field using a `spec.signerName=NAME` field selector.  # noqa: E501

        :return: The signer_name of this V1alpha1ClusterTrustBundleSpec.  # noqa: E501
        :rtype: str
        """
        return self._signer_name

    @signer_name.setter
    def signer_name(self, signer_name):
        """Sets the signer_name of this V1alpha1ClusterTrustBundleSpec.

        signerName indicates the associated signer, if any.  In order to create or update a ClusterTrustBundle that sets signerName, you must have the following cluster-scoped permission: group=certificates.k8s.io resource=signers resourceName=<the signer name> verb=attest.  If signerName is not empty, then the ClusterTrustBundle object must be named with the signer name as a prefix (translating slashes to colons). For example, for the signer name `example.com/foo`, valid ClusterTrustBundle object names include `example.com:foo:abc` and `example.com:foo:v1`.  If signerName is empty, then the ClusterTrustBundle object's name must not have such a prefix.  List/watch requests for ClusterTrustBundles can filter on this field using a `spec.signerName=NAME` field selector.  # noqa: E501

        :param signer_name: The signer_name of this V1alpha1ClusterTrustBundleSpec.  # noqa: E501
        :type signer_name: str
        """

        self._signer_name = signer_name

    @property
    def trust_bundle(self):
        """Gets the trust_bundle of this V1alpha1ClusterTrustBundleSpec.  # noqa: E501

        trustBundle contains the individual X.509 trust anchors for this bundle, as PEM bundle of PEM-wrapped, DER-formatted X.509 certificates.  The data must consist only of PEM certificate blocks that parse as valid X.509 certificates.  Each certificate must include a basic constraints extension with the CA bit set.  The API server will reject objects that contain duplicate certificates, or that use PEM block headers.  Users of ClusterTrustBundles, including Kubelet, are free to reorder and deduplicate certificate blocks in this file according to their own logic, as well as to drop PEM block headers and inter-block data.  # noqa: E501

        :return: The trust_bundle of this V1alpha1ClusterTrustBundleSpec.  # noqa: E501
        :rtype: str
        """
        return self._trust_bundle

    @trust_bundle.setter
    def trust_bundle(self, trust_bundle):
        """Sets the trust_bundle of this V1alpha1ClusterTrustBundleSpec.

        trustBundle contains the individual X.509 trust anchors for this bundle, as PEM bundle of PEM-wrapped, DER-formatted X.509 certificates.  The data must consist only of PEM certificate blocks that parse as valid X.509 certificates.  Each certificate must include a basic constraints extension with the CA bit set.  The API server will reject objects that contain duplicate certificates, or that use PEM block headers.  Users of ClusterTrustBundles, including Kubelet, are free to reorder and deduplicate certificate blocks in this file according to their own logic, as well as to drop PEM block headers and inter-block data.  # noqa: E501

        :param trust_bundle: The trust_bundle of this V1alpha1ClusterTrustBundleSpec.  # noqa: E501
        :type trust_bundle: str
        """
        if self.local_vars_configuration.client_side_validation and trust_bundle is None:  # noqa: E501
            raise ValueError("Invalid value for `trust_bundle`, must not be `None`")  # noqa: E501

        self._trust_bundle = trust_bundle

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
        if not isinstance(other, V1alpha1ClusterTrustBundleSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ClusterTrustBundleSpec):
            return True

        return self.to_dict() != other.to_dict()
