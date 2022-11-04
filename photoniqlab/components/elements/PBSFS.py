# -*- coding: utf-8 -*-

"""Polarization beam splitter (in FS) class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class PBSFS(Element):
    """The class of polarization beam splitters in FS."""

    def __init__(self):
        """Create a PBS."""
        u = {co('p1', 'H'): Rational(1, 2) * (co('p2', 'H') + co('p2', 'V')) + Rational(1, 2) * (co('p1', 'H') - co('p1', 'V')),
             co('p2', 'H'): Rational(1, 2) * (co('p1', 'H') + co('p1', 'V')) + Rational(1, 2) * (co('p2', 'H') - co('p2', 'V')),
             co('p1', 'V'): Rational(1, 2) * (co('p2', 'H') + co('p2', 'V')) - Rational(1, 2) * (co('p1', 'H') - co('p1', 'V')),
             co('p2', 'V'): Rational(1, 2) * (co('p1', 'H') + co('p1', 'V')) - Rational(1, 2) * (co('p2', 'H') - co('p2', 'V'))}
        dofs = ['path', 'pol']
        Element.__init__(self, 2, dofs, u)
        self.label = '$PBS_{{FS}}^{{{}}}$'
