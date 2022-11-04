# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab.components.sources.GHZ import GHZ
from photoniqlab.path_name_generator import PathNameGenerator
from test.photoniqlab_test import PhotoniqlabTest

class TestGHZ(PhotoniqlabTest):
    def test__init(self):
        state = GHZ()
        self.assertEqual(state.get_state(), (1/sqrt(2)) * co(0, 'H') * co(1, 'H') * co(2, 'H') + (1 / sqrt(2)) * co(0, 'V') * co(1, 'V') * co(2, 'V'))
