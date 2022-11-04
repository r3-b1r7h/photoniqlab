# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab.components.sources.Psi_m import Psi_m
from photoniqlab.path_name_generator import PathNameGenerator
from test.photoniqlab_test import PhotoniqlabTest

class TestPsi_m(PhotoniqlabTest):
    def test__init(self):
        state = Psi_m()
        self.assertEqual(state.get_state(), (1/sqrt(2)) * co(0, 'H') * co(1, 'V') - (1 / sqrt(2)) * co(0, 'V') * co(1, 'H'))
