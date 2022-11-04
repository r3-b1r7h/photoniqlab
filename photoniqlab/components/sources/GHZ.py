# -*- coding: utf-8 -*-

"""GHZ state."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.sources.photons import Photons

class GHZ(Photons):
    """GHZ state, |HHH> + |VVV>."""
    def __init__(self):
        """Create a photon source of GHZ state."""
        state = (1 / sqrt(2)) * co('p1', 'H') * co('p2', 'H') * co('p3', 'H') + (1 / sqrt(2)) * co('p1', 'V') * co('p2', 'V') * co('p3', 'V')
        Photons.__init__(self, 3, ['path', 'pol'], state)
        self.label = '$GHZ^{{{}}}$'
        self.param = str(state)