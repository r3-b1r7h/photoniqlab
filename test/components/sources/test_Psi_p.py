# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab.components.sources.Psi_p import Psi_p
from photoniqlab.path_name_generator import PathNameGenerator
from test.photoniqlab_test import PhotoniqlabTest

class TestPsi_p(PhotoniqlabTest):
    def test__init(self):
        state = Psi_p()
        self.assertEqual(state.get_state(), (1/sqrt(2)) * co(0, 'H') * co(1, 'V') + (1 / sqrt(2)) * co(0, 'V') * co(1, 'H'))