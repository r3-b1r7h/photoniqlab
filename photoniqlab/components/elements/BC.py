# -*- coding: utf-8 -*-

"""Birefringent compensator class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class BC(Element):
    """The class of birefringent compensator.

    Inducing a phase phi between H and V.
    """

    def __init__(self, phi):
        """Create a phase shifter."""
        u = {co('V'): exp(I * phi) * co('V')}
        dofs = ['pol']
        Element.__init__(self, 1, dofs, u)
        self.label = '$BC$'
        self.param = '$\\phi={}$'.format(latex(phi))