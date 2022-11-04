# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.PBS import PBS
from photoniqlab.path_name_generator import PathNameGenerator
from test.photoniqlab_test import PhotoniqlabTest

class TestPBS(PhotoniqlabTest):
    def test_get_u(self): 
        pbs = PBS()
        all_dofs = ['freq', 'path', 'pol']
        self.assertEqual(pbs.get_u(all_dofs),
                         {co(Wild('freq'), 0, 'H'):
                          co(Wild('freq'), 1, 'H'),
                          co(Wild('freq'), 1, 'H'):
                          co(Wild('freq'), 0, 'H')})
