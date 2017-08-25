# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class PressureSummary(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, nm=None, u=None, v=None, t=None, n=None, lbl=None):
        """
        PressureSummary - a model defined in Swagger

        :param nm: The nm of this PressureSummary.
        :type nm: str
        :param u: The u of this PressureSummary.
        :type u: str
        :param v: The v of this PressureSummary.
        :type v: float
        :param t: The t of this PressureSummary.
        :type t: datetime
        :param n: The n of this PressureSummary.
        :type n: str
        :param lbl: The lbl of this PressureSummary.
        :type lbl: str
        """
        self.swagger_types = {
            'nm': str,
            'u': str,
            'v': float,
            't': datetime,
            'n': str,
            'lbl': str
        }

        self.attribute_map = {
            'nm': 'nm',
            'u': 'u',
            'v': 'v',
            't': 't',
            'n': 'n',
            'lbl': 'lbl'
        }

        self._nm = nm
        self._u = u
        self._v = v
        self._t = t
        self._n = n
        self._lbl = lbl

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PressureSummary of this PressureSummary.
        :rtype: PressureSummary
        """
        return deserialize_model(dikt, cls)

    @property
    def nm(self):
        """
        Gets the nm of this PressureSummary.

        :return: The nm of this PressureSummary.
        :rtype: str
        """
        return self._nm

    @nm.setter
    def nm(self, nm):
        """
        Sets the nm of this PressureSummary.

        :param nm: The nm of this PressureSummary.
        :type nm: str
        """

        self._nm = nm

    @property
    def u(self):
        """
        Gets the u of this PressureSummary.

        :return: The u of this PressureSummary.
        :rtype: str
        """
        return self._u

    @u.setter
    def u(self, u):
        """
        Sets the u of this PressureSummary.

        :param u: The u of this PressureSummary.
        :type u: str
        """

        self._u = u

    @property
    def v(self):
        """
        Gets the v of this PressureSummary.

        :return: The v of this PressureSummary.
        :rtype: float
        """
        return self._v

    @v.setter
    def v(self, v):
        """
        Sets the v of this PressureSummary.

        :param v: The v of this PressureSummary.
        :type v: float
        """

        self._v = v

    @property
    def t(self):
        """
        Gets the t of this PressureSummary.
        the timestamp when the pressure was measured

        :return: The t of this PressureSummary.
        :rtype: datetime
        """
        return self._t

    @t.setter
    def t(self, t):
        """
        Sets the t of this PressureSummary.
        the timestamp when the pressure was measured

        :param t: The t of this PressureSummary.
        :type t: datetime
        """

        self._t = t

    @property
    def n(self):
        """
        Gets the n of this PressureSummary.

        :return: The n of this PressureSummary.
        :rtype: str
        """
        return self._n

    @n.setter
    def n(self, n):
        """
        Sets the n of this PressureSummary.

        :param n: The n of this PressureSummary.
        :type n: str
        """

        self._n = n

    @property
    def lbl(self):
        """
        Gets the lbl of this PressureSummary.

        :return: The lbl of this PressureSummary.
        :rtype: str
        """
        return self._lbl

    @lbl.setter
    def lbl(self, lbl):
        """
        Sets the lbl of this PressureSummary.

        :param lbl: The lbl of this PressureSummary.
        :type lbl: str
        """

        self._lbl = lbl
