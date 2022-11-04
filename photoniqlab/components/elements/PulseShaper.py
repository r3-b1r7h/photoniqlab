# -*- coding: utf-8 -*-

"""Pulse shaper class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class PulseShaper(Element):
    """The class of pulse shaper."""

    def __init__(self, spectral):
        """Create a pulse shaper.
           spectral should be a dict specifying the phase for each mode.
        """
        u = {co(freq): exp(I * phase) * co(freq) for freq, phase in spectral.items()}
        dofs = ['freq']
        Element.__init__(self, 1, dofs, u)
        self.label = '$PulseShaper^{{{}}}$'

