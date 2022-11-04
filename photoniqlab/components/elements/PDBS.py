# -*- coding: utf-8 -*-

"""Polarization dependent beam splitter class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class PDBS(Element):
    """The class of polarization dependence beam splitter."""

    def __init__(self, tH=2/3, tV = 1/3):
        """Create a PDBS."""
        u = {co('p1', 'H'): sqrt(1 - tH) * co('p1', 'H') + sqrt(tH) * co('p2', 'H'),
             co('p2', 'H'): sqrt(1 - tH) * co('p2', 'H') - sqrt(tH) * co('p1', 'H'),
             co('p1', 'V'): sqrt(1 - tV) * co('p1', 'V') + sqrt(tV) * co('p2', 'V'),
             co('p2', 'V'): sqrt(1 - tV) * co('p2', 'V') - sqrt(tV) * co('p1', 'V')}
        dofs = ['path', 'pol']
        Element.__init__(self, 2, dofs, u)