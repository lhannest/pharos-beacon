# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.beacon_concept_detail import BeaconConceptDetail  # noqa: F401,E501
from swagger_server import util


class BeaconConceptWithDetails(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, type: str=None, synonyms: List[str]=None, definition: str=None, details: List[BeaconConceptDetail]=None):  # noqa: E501
        """BeaconConceptWithDetails - a model defined in Swagger

        :param id: The id of this BeaconConceptWithDetails.  # noqa: E501
        :type id: str
        :param name: The name of this BeaconConceptWithDetails.  # noqa: E501
        :type name: str
        :param type: The type of this BeaconConceptWithDetails.  # noqa: E501
        :type type: str
        :param synonyms: The synonyms of this BeaconConceptWithDetails.  # noqa: E501
        :type synonyms: List[str]
        :param definition: The definition of this BeaconConceptWithDetails.  # noqa: E501
        :type definition: str
        :param details: The details of this BeaconConceptWithDetails.  # noqa: E501
        :type details: List[BeaconConceptDetail]
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'type': str,
            'synonyms': List[str],
            'definition': str,
            'details': List[BeaconConceptDetail]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'synonyms': 'synonyms',
            'definition': 'definition',
            'details': 'details'
        }

        self._id = id
        self._name = name
        self._type = type
        self._synonyms = synonyms
        self._definition = definition
        self._details = details

    @classmethod
    def from_dict(cls, dikt) -> 'BeaconConceptWithDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BeaconConceptWithDetails of this BeaconConceptWithDetails.  # noqa: E501
        :rtype: BeaconConceptWithDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this BeaconConceptWithDetails.

        local object identifier for the concept in the specified knowledge source database   # noqa: E501

        :return: The id of this BeaconConceptWithDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this BeaconConceptWithDetails.

        local object identifier for the concept in the specified knowledge source database   # noqa: E501

        :param id: The id of this BeaconConceptWithDetails.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this BeaconConceptWithDetails.

        canonical human readable name of the concept   # noqa: E501

        :return: The name of this BeaconConceptWithDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this BeaconConceptWithDetails.

        canonical human readable name of the concept   # noqa: E501

        :param name: The name of this BeaconConceptWithDetails.
        :type name: str
        """

        self._name = name

    @property
    def type(self) -> str:
        """Gets the type of this BeaconConceptWithDetails.

        concept semantic type   # noqa: E501

        :return: The type of this BeaconConceptWithDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this BeaconConceptWithDetails.

        concept semantic type   # noqa: E501

        :param type: The type of this BeaconConceptWithDetails.
        :type type: str
        """

        self._type = type

    @property
    def synonyms(self) -> List[str]:
        """Gets the synonyms of this BeaconConceptWithDetails.

        list of synonyms for concept   # noqa: E501

        :return: The synonyms of this BeaconConceptWithDetails.
        :rtype: List[str]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms: List[str]):
        """Sets the synonyms of this BeaconConceptWithDetails.

        list of synonyms for concept   # noqa: E501

        :param synonyms: The synonyms of this BeaconConceptWithDetails.
        :type synonyms: List[str]
        """

        self._synonyms = synonyms

    @property
    def definition(self) -> str:
        """Gets the definition of this BeaconConceptWithDetails.

        concept definition   # noqa: E501

        :return: The definition of this BeaconConceptWithDetails.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition: str):
        """Sets the definition of this BeaconConceptWithDetails.

        concept definition   # noqa: E501

        :param definition: The definition of this BeaconConceptWithDetails.
        :type definition: str
        """

        self._definition = definition

    @property
    def details(self) -> List[BeaconConceptDetail]:
        """Gets the details of this BeaconConceptWithDetails.


        :return: The details of this BeaconConceptWithDetails.
        :rtype: List[BeaconConceptDetail]
        """
        return self._details

    @details.setter
    def details(self, details: List[BeaconConceptDetail]):
        """Sets the details of this BeaconConceptWithDetails.


        :param details: The details of this BeaconConceptWithDetails.
        :type details: List[BeaconConceptDetail]
        """

        self._details = details
