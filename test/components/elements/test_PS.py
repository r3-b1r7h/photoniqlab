# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.PS import PS
from photoniqlab.path_name_generator import PathNameGenerator
from test.photoniqlab_test import PhotoniqlabTest

class TestPS(PhotoniqlabTest):
    def test_get_u(self):
        phi = Symbol('phi')
        ps = PS(phi)
        all_dofs = ['freq', 'path', 'pol']
        self.assertEqual(ps.get_u(all_dofs), {co(Wild('freq'), 0, Wild('pol')): exp(I * phi) * co(Wild('freq'), 0, Wild('pol'))})
