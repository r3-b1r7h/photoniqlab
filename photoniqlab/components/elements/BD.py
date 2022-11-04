# -*- coding: utf-8 -*-

"""Beam displacer class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class BD(Element):
    """The class of beam displacer on multi-path.

    You can specify the path number and whether the roles of H and V are swapped.
    """

    def __init__(self, path_num=2, swap=False):
        """Create a BD."""
        self.swap = swap
        if swap:
            u = {co('p' + str(i + 1), 'H'): co('p' + str(i + 2), 'H') for i in range(0, path_num - 1)}
        else:
            u = {co('p' + str(i + 1), 'V'): co('p' + str(i + 2), 'V') for i in range(0, path_num - 1)}
        self.swap = swap
        dofs = ['path', 'pol']
        Element.__init__(self, path_num, dofs, u)
        self.label = '$BD^{{{}}}$'
        if swap:
            self.param = '$V pass$'
        else:
            self.param = '$H pass$'
