# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.element import Element
from photoniqlab.path_name_generator import PathNameGenerator
from test.photoniqlab_test import PhotoniqlabTest

class TestElement(PhotoniqlabTest):
    def test_init(self):
        u = {co('p1', 'H'): co('p2', 'H'), co('p2', 'H'): co('p1', 'H')}
        ele = Element(2, ['path', 'pol'], u)
        self.assertEqual(ele.dofs, ['path', 'pol'])
        self.assertEqual(ele.u, u)

    def test_get_u_ordinary(self):
        u = {co('p1', 'H'): co('p2', 'H'), co('p2', 'H'): co('p1', 'H')}
        ele = Element(2, ['path', 'pol'], u)
        all_dofs = ['pol', 'freq', 'oam', 'path']
        complete_u = ele.get_u(all_dofs)
        self.assertEqual(complete_u, {co('H', Wild('freq'), Wild('oam'), 0): co('H', Wild('freq'), Wild('oam'), 1),
                                      co('H', Wild('freq'), Wild('oam'), 1): co('H', Wild('freq'), Wild('oam'), 0)})

    def test_get_u_omit_path(self):
        u = {co('H', -1): sqrt(2) * co('H', 2) + sqrt(2) * co('V', 1),
             co('V', -1): Symbol('a') * co('H', 3) + Symbol('b') * I * co('V', 9)}
        ele = Element(1, ['pol', 'oam'], u)
        all_dofs = ['path', 'oam', 'pol', 'freq']
        complete_u = ele.get_u(all_dofs)
        self.assertEqual(complete_u, {co(0, -1, 'H', Wild('freq')): sqrt(2) * co(0, 2, 'H', Wild('freq')) + sqrt(2) * co(0, 1, 'V', Wild('freq')),
                                      co(0, -1, 'V', Wild('freq')): Symbol('a') * co(0, 3, 'H', Wild('freq')) + Symbol('b') * I * co(0, 9, 'V', Wild('freq'))})

    def test_get_u_wildcard(self):
        w = Wild('w')
        u = {co(w, 'p1'): co(w + 1, 'p2'), co(w, 'p2'): co(w - 1, 'p1')}
        ele = Element(2, ['oam', 'path'], u)
        all_dofs = ['path', 'oam', 'pol']
        complete_u = ele.get_u(all_dofs)
        self.assertEqual(complete_u, {co(0, w, Wild('pol')): co(1, w + 1, Wild('pol')),
                                      co(1, w, Wild('pol')): co(0, w - 1, Wild('pol'))})

