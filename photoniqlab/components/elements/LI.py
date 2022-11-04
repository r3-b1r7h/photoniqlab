# -*- coding: utf-8 -*-

"""OAM parity sorter class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class LI(Element):
    """The class of OAM parity sorter."""

    def __init__(self):
        """Create a LI."""
        u = {co(Wild('oam'), 'p1'): cos(Wild('oam') * pi / 2)**2 * co(Wild('oam'), 'p1') + I * sin(Wild('oam') * pi / 2)**2 * co(-Wild('oam'), 'p2'),
             co(Wild('oam'), 'p2'): -cos(Wild('oam') * pi / 2)**2 * co(Wild('oam'), 'p2') + I * sin(Wild('oam') * pi / 2)**2 * co(-Wild('oam'), 'p1')}
        dofs = ['oam', 'path']
        Element.__init__(self, 2, dofs, u)
        self.label = '$LI^{{{}}}$'

