# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab.components.detectors import Detectors
from photoniqlab.path_name_generator import PathNameGenerator
from test.photoniqlab_test import PhotoniqlabTest

class TestDetectors(PhotoniqlabTest):
    def test_init(self):
        detectors = Detectors(2)
        self.assertEqual(detectors.dofs, ['path'])
        self.assertEqual(detectors.coincidence, [1, 1])

    def test_post_select_2_path(self):
        detectors = Detectors(2)
        state1 = co(1, 'H', 810, 3)**2 * co(0, 'V', 405, 2) + co(0, 'V', 810, -1) * co(1, 'H', 405, 1) * co(2, 'V', 1550, 3) + co(3, 'H', 810, -3) * co(0, 'V', 1550, 3)
        output1 = detectors.post_select(state1, ['path', 'pol', 'freq', 'oam'])
        self.assertEqual(output1, co(0, 'V', 810, -1) * co(1, 'H', 405, 1) * co(2, 'V', 1550, 3))
        state2 = co(0, 'H', 810, 3)**2 * co(1, 'V', 405, 2)
        output2 = detectors.post_select(state2, ['path', 'pol', 'freq', 'oam'])
        self.assertEqual(output2, 0)
        state3 = co(2, 'H', 1550, 5) * co(4, 'V', 1550, 5)
        output3 = detectors.post_select(state3, ['path', 'pol', 'freq', 'oam'])
        self.assertEqual(output3, 0)
        state4 = co('V', 0, 5)
        output4 = detectors.post_select(state4, ['pol', 'path', 'oam'])
        self.assertEqual(output4, 0)

    def test_post_select_1_path(self):
        detectors = Detectors(1)
        state = co(0) + co(1) + co(2) * co(3) + co(0)**3*co(8)
        output = detectors.post_select(state, ['path'])
        self.assertEqual(output, co(0))

    def test_post_select_change_coincidence_number(self):
        detectors = Detectors(3)
        detectors.coincidence[0] = 2
        detectors.coincidence[1] = 0
        a = Symbol('a')
        b = Symbol('b')
        state = a * co(0, 'H')**3 * co(2, 'V') + b * co(0, 'V') * co(0, 'H') * co(2, 'H') * co(2, 'V') + a * b * co(0, 'V')**2 * co(2, 'H') * co(3, 'H') + sqrt(3) * co(0, 'H')**2 * co(2, 'H') * co(1, 'H')
        output = detectors.post_select(state, ['path', 'pol'])
        self.assertEqual(output, a * b * co(0, 'V')**2 * co(2, 'H') * co(3, 'H'))
