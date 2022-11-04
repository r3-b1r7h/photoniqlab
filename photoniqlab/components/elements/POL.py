# -*- coding: utf-8 -*-

"""Polarizer class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class POL(Element):
    """The class of polarizer.

   The optical axis is arbitrary here too.
    """

    def __init__(self, oa):
        """Create a HWP."""
        u = {co('H'): cos(oa)**2 * co('H') + cos(oa) * sin(oa) * co('V'),
             co('V'): cos(oa) * sin(oa) * co('H') + sin(oa)**2 * co('V')}
        dofs = ['pol']
        Element.__init__(self, 1, dofs, u)
        self.label = '$POL$'
        self.param = '$oa={}$'.format(latex(oa))