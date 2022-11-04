# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.POL import POL
from photoniqlab.path_name_generator import PathNameGenerator
from test.photoniqlab_test import PhotoniqlabTest

class TestPOL(PhotoniqlabTest):
    def test_get_u(self):
        theta = Symbol('theta')
        pol = POL(theta)
        all_dofs = ['oam', 'freq', 'path', 'pol']
        self.assertEqual(pol.get_u(all_dofs),
                         {co(Wild('oam'), Wild('freq'), 0, 'H'):
                           cos(theta)**2 * co(Wild('oam'), Wild('freq'), 0, 'H')
                          + cos(theta) * sin(theta) * co(Wild('oam'), Wild('freq'), 0, 'V'),
                          co(Wild('oam'), Wild('freq'), 0, 'V'):
                          cos(theta) * sin(theta) * co(Wild('oam'), Wild('freq'), 0, 'H')
                          + sin(theta)**2 * co(Wild('oam'), Wild('freq'), 0, 'V')})
