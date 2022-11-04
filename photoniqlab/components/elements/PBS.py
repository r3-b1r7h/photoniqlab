# -*- coding: utf-8 -*-

"""Polarization beam splitter class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class PBS(Element):
    """The class of polarization beam splitters."""

    def __init__(self):
        """Create a PBS."""
        u = {co('p1', 'H'): co('p2', 'H'), co('p2', 'H'): co('p1', 'H')}
        dofs = ['path', 'pol']
        Element.__init__(self, 2, dofs, u)
        self.label = '$PBS^{{{}}}$'
