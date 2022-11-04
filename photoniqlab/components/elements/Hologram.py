# -*- coding: utf-8 -*-

"""Hologram class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class Hologram(Element):
    """The class of Hologram."""
    def __init__(self, n):
        """Create a Hologram."""
        u = {co(Wild('oam')): co(Wild('oam') + n)}
        dofs = ['oam']
        Element.__init__(self, 1, dofs, u)
        self.label = '$DP^{{{}}}$'
        self.param = str(n)
