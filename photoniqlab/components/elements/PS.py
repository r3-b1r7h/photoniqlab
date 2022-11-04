# -*- coding: utf-8 -*-

"""Phase shifter class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class PS(Element):
    """The class of phase shifter.

    You can specify phi (the phase delay) for a phase shifter.
    """

    def __init__(self, phi):
        """Create a phase shifter."""

        # co() is not valid for windows!!

        u = {co('p1'): exp(I * phi) * co('p1')}
        dofs = ['path']
        Element.__init__(self, 1, dofs, u)
        self.label = '$PS$'
        self.param = '$\\phi={}'.format(latex(phi))