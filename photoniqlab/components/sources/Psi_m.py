# -*- coding: utf-8 -*-

"""Bell state: Psi_m"""

from photoniqlab.sympy_widget import *
from photoniqlab.components.sources.photons import Photons

class Psi_m(Photons):
    """Bell state, Psi_m, |HV> - |VH>."""
    def __init__(self):
        """Create a photon source of Psi_m."""
        state = (1 / sqrt(2)) * co('p1', 'H') * co('p2', 'V') - (1 / sqrt(2)) * co('p1', 'V') * co('p2', 'H')
        Photons.__init__(self, 2, ['path', 'pol'], state)
        self.label = '$Psi_m^{{{}}}$'
        self.param = str(state)
