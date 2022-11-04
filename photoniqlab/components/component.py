# -*- coding: utf-8 -*-

"""Basic abstract class for components of PQIP networks."""

import re

from photoniqlab.sympy_widget import *
from photoniqlab.path_name_generator import PathNameGenerator
from photoniqlab.exceptions import PhotoniqlabError

class Component:
    """The base class for photon, elements, detectors.

    All component classes in the experiment are children of this class.
    It contains the information of path name and the connection, which
    are common in all component.

    Attributes:
        o: A list for all immediate successors of the component.
        i: A list for reference of the input port.
        path: A list of path names of all ports.
        label: A label for visualization
        param: The parameters for visualization
    """

    def __init__(self, path_num):
        """Create a component."""
        self.o = [(None, None) for i in range(0, path_num)]
        self.i = [(self, i) for i in range(0, path_num)]
        self.path = [PathNameGenerator.new_path_name() for i in range(0, path_num)]

        self.label = '?'
        self.param = ''

    def _extract_dofs(self, state):
        """Extract the dofs used in the co of the state."""
        tmp_co = list(state.atoms(co))[0]  # Get a co in the state to analyse
        co_info = tmp_co.args
        local_dofs = []
        for info in co_info:
            if info == 'H' or info == 'V':
                self.__add_dof(local_dofs, 'pol')
            elif re.search(r'path\d', info):
                self.__add_dof(local_dofs, 'path')
            elif re.search(r'\dHz', info):
                self.__add_dof(local_dofs, 'freq')
            elif re.search(r'\+\d', info) or re.search(r'-\d', info):
                self.__add_dof(local_dofs, 'oam')
        return local_dofs

    def __add_dof(self, local_dofs, dof):
        if dof not in local_dofs:
            local_dofs.append(dof)
        else:
            raise PhotoniqlabError('Information repeats in the co.')

    def _generate_wild(self, dofs):
        """Generate a co-wildcard for a dofs list."""
        wild_str = 'co('
        for dof in dofs:
            wild_str += 'Wild(\'' + dof + '\'),'
        wild_str.rstrip(',')
        wild_str += (')')
        wild = sympify(wild_str)
        return wild
