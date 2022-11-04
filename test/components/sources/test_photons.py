# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab.path_name_generator import PathNameGenerator
from photoniqlab.components.sources.photons import Photons
from test.photoniqlab_test import PhotoniqlabTest

class TestPhotons(PhotoniqlabTest):
    def test_init(self):
        state1 = (1 / sqrt(2)) * co('p1', 'H') * co('p2', 'H') + (1 / sqrt(2)) * co('p1', 'V') * co('p2', 'V')
        photons1 = Photons(2, ['path', 'pol'], state1)
        self.assertEqual(photons1.dofs, ['path', 'pol'])
        self.assertEqual(photons1.state, (1 / sqrt(2)) * co(Symbol('p1'), Symbol('H')) * co(Symbol('p2'), Symbol('H')) + (1 / sqrt(2)) * co(Symbol('p1'), Symbol('V')) * co(Symbol('p2'), Symbol('V')))
        state2 = co('H', 'p1', 2, 810) * co('V', 'p2', -1, 405)
        photons2 = Photons(2, ['pol', 'path', 'oam', 'freq'], state2)
        self.assertEqual(photons2.dofs, ['pol', 'path', 'oam', 'freq'])
        self.assertEqual(photons2.state, co(Symbol('H'), Symbol('p1'), Integer(2), Integer(810)) * co(Symbol('V'), Symbol('p2'), Integer(-1), Integer(405)))

    def test_get_state(self):
        state = co('H', 'p1', 2, 810) * co('V', 'p2', -1, 405)
        photons = Photons(2, ['pol', 'path', 'oam', 'freq'], state)
        self.assertEqual(photons.get_state(), co('H', 0, 2, 810) * co('V', 1, -1, 405))



