# -*- coding: utf-8 -*-

"""Dove prism class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class DP(Element):
    """The class of Dove prism."""
    def __init__(self):
        """Create a DP."""
        u = {co(Wild('l')): I * exp(I * Wild('l') * pi) * co(-Wild('l'))}
        dofs = ['oam']
        Element.__init__(self, 1, dofs, u)
        self.label = '$DP^{{{}}}$'
