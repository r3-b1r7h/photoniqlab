# -*- coding: utf-8 -*-

"""Electro-Optic Phase Modulator class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class EOM(Element):
    """The class of EOM."""

    def __init__(self, delta, phi_t, bandwidth=50):
        """Create a EOM.
           phi_t should be a function from 0 to 1 / delta.
        """
        p = 1 / delta
        u = {co(Wild('freq')): sum([integrate(exp(I * phi_t) * exp(-I * 2 * pi * i * Symbol('t') / p), (Symbol('t'), 0, p)).evalf(chop=True) / p * co(Wild('freq') + i * delta) for i in range(-bandwidth, bandwidth + 1)])}
        dofs = ['freq']
        Element.__init__(self, 1, dofs, u)
        self.label = '$EOM^{{{}}}$'

