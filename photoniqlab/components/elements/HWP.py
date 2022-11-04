# -*- coding: utf-8 -*-

"""Half wave plate class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class HWP(Element):
    """The class of half wave plate.

   The optical axis is arbitrary here.
    """

    def __init__(self, oa):
        """Create a HWP."""
        u = {co('H'): cos(2 * oa).evalf() * co('H') + sin(2 * oa).evalf() * co('V'),
             co('V'): sin(2 * oa).evalf() * co('H') - cos(2 * oa).evalf() * co('V')}
        dofs = ['pol']
        Element.__init__(self, 1, dofs, u)
        self.label = '$HWP$'
        self.param = '$oa={}$'.format(latex(oa))
