# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.BD import BD
from photoniqlab.path_name_generator import PathNameGenerator
from test.photoniqlab_test import PhotoniqlabTest

class TestBD(PhotoniqlabTest):
    def test_get_u_ordinary(self):
        bd = BD(3)
        all_dofs = ['path', 'pol']
        self.assertEqual(bd.get_u(all_dofs),
                         {co(0, 'V'):
                          co(1, 'V'),
                          co(1, 'V'):
                          co(2, 'V')})

    def test_get_u_swap(self):
        bd = BD(3, swap=True)
        all_dofs = ['pol', 'path']
        self.assertEqual(bd.get_u(all_dofs),
                         {co('H', 0):
                          co('H', 1),
                          co('H', 1):
                          co('H', 2)})
