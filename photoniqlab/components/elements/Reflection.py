# -*- coding: utf-8 -*-

"""Reflection class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class Reflection(Element):
    """The class of Reflection."""

    def __init__(self):
        """Create a BD."""

        u = {co(Wild('oam')): I * co(-Wild('oam'))}

        dofs = ['oam']
        Element.__init__(self, 1, dofs, u)
        self.label = '$Reflection^{{{}}}$'
