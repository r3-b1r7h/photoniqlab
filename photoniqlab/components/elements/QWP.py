# -*- coding: utf-8 -*-

"""Quarter wave plate class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class QWP(Element):
    """The class of quarter wave plate.

   The optical axis is also arbitrary here.
    """

    def __init__(self, oa):
        """Create a QWP."""
        u = {co('H'): (cos(oa)**2 + I * sin(oa)**2) * co('H') + ((1 - I) * sin(oa) * cos(oa)) * co('V'),
             co('V'): ((1 - I) * sin(oa) * cos(oa)) * co('H') + (sin(oa)**2 + I * cos(oa)**2) * co('V')}
        dofs = ['pol']
        Element.__init__(self, 1, dofs, u)
        self.label = '$QWP$'
        self.param = '$oa={}$'.format(latex(oa))