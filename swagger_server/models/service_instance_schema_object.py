# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.schema_parameters import SchemaParameters
from swagger_server import util


class ServiceInstanceSchemaObject(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, create: SchemaParameters=None, update: SchemaParameters=None):  # noqa: E501
        """ServiceInstanceSchemaObject - a model defined in Swagger

        :param create: The create of this ServiceInstanceSchemaObject.  # noqa: E501
        :type create: SchemaParameters
        :param update: The update of this ServiceInstanceSchemaObject.  # noqa: E501
        :type update: SchemaParameters
        """
        self.swagger_types = {
            'create': SchemaParameters,
            'update': SchemaParameters
        }

        self.attribute_map = {
            'create': 'create',
            'update': 'update'
        }

        self._create = create
        self._update = update

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceInstanceSchemaObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceInstanceSchemaObject of this ServiceInstanceSchemaObject.  # noqa: E501
        :rtype: ServiceInstanceSchemaObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def create(self) -> SchemaParameters:
        """Gets the create of this ServiceInstanceSchemaObject.


        :return: The create of this ServiceInstanceSchemaObject.
        :rtype: SchemaParameters
        """
        return self._create

    @create.setter
    def create(self, create: SchemaParameters):
        """Sets the create of this ServiceInstanceSchemaObject.


        :param create: The create of this ServiceInstanceSchemaObject.
        :type create: SchemaParameters
        """

        self._create = create

    @property
    def update(self) -> SchemaParameters:
        """Gets the update of this ServiceInstanceSchemaObject.


        :return: The update of this ServiceInstanceSchemaObject.
        :rtype: SchemaParameters
        """
        return self._update

    @update.setter
    def update(self, update: SchemaParameters):
        """Sets the update of this ServiceInstanceSchemaObject.


        :param update: The update of this ServiceInstanceSchemaObject.
        :type update: SchemaParameters
        """

        self._update = update
