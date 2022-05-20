# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.22.6
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


class V1CronJobStatus(object):
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
        'active': 'list[V1ObjectReference]',
        'last_schedule_time': 'datetime',
        'last_successful_time': 'datetime'
    }

    attribute_map = {
        'active': 'active',
        'last_schedule_time': 'lastScheduleTime',
        'last_successful_time': 'lastSuccessfulTime'
    }

    def __init__(self, active=None, last_schedule_time=None, last_successful_time=None, local_vars_configuration=None):  # noqa: E501
        """V1CronJobStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._active = None
        self._last_schedule_time = None
        self._last_successful_time = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if last_schedule_time is not None:
            self.last_schedule_time = last_schedule_time
        if last_successful_time is not None:
            self.last_successful_time = last_successful_time

    @property
    def active(self):
        """Gets the active of this V1CronJobStatus.  # noqa: E501

        A list of pointers to currently running jobs.  # noqa: E501

        :return: The active of this V1CronJobStatus.  # noqa: E501
        :rtype: list[V1ObjectReference]
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this V1CronJobStatus.

        A list of pointers to currently running jobs.  # noqa: E501

        :param active: The active of this V1CronJobStatus.  # noqa: E501
        :type active: list[V1ObjectReference]
        """

        self._active = active

    @property
    def last_schedule_time(self):
        """Gets the last_schedule_time of this V1CronJobStatus.  # noqa: E501

        Information when was the last time the job was successfully scheduled.  # noqa: E501

        :return: The last_schedule_time of this V1CronJobStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_schedule_time

    @last_schedule_time.setter
    def last_schedule_time(self, last_schedule_time):
        """Sets the last_schedule_time of this V1CronJobStatus.

        Information when was the last time the job was successfully scheduled.  # noqa: E501

        :param last_schedule_time: The last_schedule_time of this V1CronJobStatus.  # noqa: E501
        :type last_schedule_time: datetime
        """

        self._last_schedule_time = last_schedule_time

    @property
    def last_successful_time(self):
        """Gets the last_successful_time of this V1CronJobStatus.  # noqa: E501

        Information when was the last time the job successfully completed.  # noqa: E501

        :return: The last_successful_time of this V1CronJobStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_successful_time

    @last_successful_time.setter
    def last_successful_time(self, last_successful_time):
        """Sets the last_successful_time of this V1CronJobStatus.

        Information when was the last time the job successfully completed.  # noqa: E501

        :param last_successful_time: The last_successful_time of this V1CronJobStatus.  # noqa: E501
        :type last_successful_time: datetime
        """

        self._last_successful_time = last_successful_time

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
        if not isinstance(other, V1CronJobStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CronJobStatus):
            return True

        return self.to_dict() != other.to_dict()