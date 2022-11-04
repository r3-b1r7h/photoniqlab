# -*- coding: utf-8 -*-

"""Parent class for any photon source."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.component import Component

class Photons(Component):
    """Base class for photon source.

    The photon source is also modeled as a component in Photoniqlab. You could selected the wanted DOF.
    You just need to connect it to other passive elements like what you do on your laboratory bench.

    Attributes:
        dofs: The used dofs in the this source.
        state: The state of this photon source.
    """

    def __init__(self, photons_num, dofs, state):
        """Create a photon source."""
        Component.__init__(self, photons_num)
        self.dofs = dofs
        self.state = state
        # TODO need to tranform to a state in latex
        self.label = '$Photon^{{{}}}$'
        self.param = str(self.state)

    def get_state(self):
        """Get the state of the photon sources.

        The dofs expanding process is invalid for photons, because informations on other dofs are unkonow.
        So, dofs of each sources should be same, and this dofs will be the template of the elements.
        """

        # TODO The trivial expanding for exchange the position of dofs should be valid.

        state = self.state
        for i in range(0, len(self.path)):
            state = state.subs(Symbol('p' + str(i + 1)), self.path[i])
        return state
