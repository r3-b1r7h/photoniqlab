# -*- coding: utf-8 -*-

"""Beam splitter class."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element

class BS(Element):
    """The class of beam splitters.

    You can specify theta and phi for a BS.
    """

    def __init__(self, eta=1/2, oam=False):
        """Create a BS."""

        # TODO: User can specify the theta, phi. Read KLM.

        #u = {co('p1'): 1/sqrt(2) * co('p1') + 1/sqrt(2) * co('p2'),
        #     co('p2'): 1/sqrt(2) * co('p1') - 1/sqrt(2) * co('p2')}
        if not oam:
            u = {co('p1'): sqrt(eta) * co('p1') + sqrt(1 - eta) * co('p2'),
                co('p2'): sqrt(1 - eta) * co('p1') - sqrt(eta) * co('p2')}

            dofs = ['path']
        else:
            u = {co(Wild('l'), 'p1'): (sqrt(2)) * (co(Wild('l'), 'p2') + I * co(-Wild('l'), 'p1')),
                 co(Wild('l'), 'p2'): (sqrt(2)) * (co(Wild('l'), 'p1') + I * co(-Wild('l'), 'p2'))}
            dofs = ['oam', 'path']
        Element.__init__(self, 2, dofs, u)
        self.label = '$BS^{{{}}}$'

