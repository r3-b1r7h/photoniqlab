# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.QWP import QWP
from photoniqlab.path_name_generator import PathNameGenerator
from test.photoniqlab_test import PhotoniqlabTest

class TestQWP(PhotoniqlabTest):
    def test_init(self):
        theta = Symbol('theta')
        qwp = QWP(theta)
        all_dofs = ['oam', 'path', 'pol']
        self.assertEqual(qwp.get_u(all_dofs), {co(Wild('oam'), 0, 'H'):
                                               (cos(theta)**2 + I * sin(theta)**2) * co(Wild('oam'), 0, 'H')
                                               + ((1 - I) * sin(theta) * cos(theta)) * co(Wild('oam'), 0, 'V'),
                                               co(Wild('oam'), 0, 'V'):
                                               ((1 - I) * sin(theta) * cos(theta)) * co(Wild('oam'), 0, 'H')
                                               + (sin(theta)**2 + I * cos(theta)**2) * co(Wild('oam'), 0, 'V')})

