# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.HWP import HWP
from photoniqlab.path_name_generator import PathNameGenerator
from test.photoniqlab_test import PhotoniqlabTest

class TestHWP(PhotoniqlabTest):
    def test_init(self):
        theta = Symbol('theta')
        hwp = HWP(theta)
        all_dofs = ['path', 'pol']
        self.assertEqual(hwp.get_u(all_dofs), {co(0, 'H'): cos(2 * theta) * co(0, 'H') + sin(2 * theta) * co(0, 'V'),
                                               co(0, 'V'): sin(2 * theta) * co(0, 'H') - cos(2 * theta) * co(0, 'V')})

