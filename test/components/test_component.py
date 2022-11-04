# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab.components.component import Component
from test.photoniqlab_test import PhotoniqlabTest

class TestComponent(PhotoniqlabTest):
    def test_init(self):
        comp1 = Component(4)
        self.assertEqual(comp1.o, [(None, None), (None, None), (None, None), (None, None)])
        self.assertEqual(comp1.i, [(comp1, 0), (comp1, 1), (comp1, 2), (comp1, 3)])
        self.assertEqual(comp1.path, [0, 1, 2, 3])
        comp2 = Component(5)
        self.assertEqual(comp2.path, [4, 5, 6, 7, 8])

    def test_generate_wild(self):
    	comp = Component(3)
    	self.assertEqual(comp._generate_wild(['pol', 'path', 'oam', 'freq']), co(Wild('pol'), Wild('path'), Wild('oam'), Wild('freq')))
    	self.assertEqual(comp._generate_wild(['oam', 'freq']), co(Wild('oam'), Wild('freq')))
