# -*- coding: utf-8 -*-

"""Bell state: Phi_m"""

from photoniqlab.sympy_widget import *
from photoniqlab.components.sources.photons import Photons

class Phi_m(Photons):
    """Bell state, Phi_m, |HH> - |VV>."""
    def __init__(self):
        """Create a photon source of Phi_m."""
        state = (1 / sqrt(2)) * co('p1', 'H') * co('p2', 'H') - (1 / sqrt(2)) * co('p1', 'V') * co('p2', 'V')
        Photons.__init__(self, 2, ['path', 'pol'], state)
        self.label = '$Phi_m^{{{}}}$'
        self.param = str(state)
