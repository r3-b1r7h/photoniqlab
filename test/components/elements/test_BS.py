# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab.components.elements.BS import BS
from photoniqlab.path_name_generator import PathNameGenerator
from test.photoniqlab_test import PhotoniqlabTest

class TestBS(PhotoniqlabTest):
    def test_init(self):
        bs = BS()
        all_dofs = ['oam', 'freq', 'path', 'pol']
        self.assertEqual(bs.get_u(all_dofs),
                         {co(Wild('oam'), Wild('freq'), 0, Wild('pol')):
                          N(1 / sqrt(2)) * co(Wild('oam'), Wild('freq'), 0, Wild('pol')) + N(1 / sqrt(2)) * co(Wild('oam'), Wild('freq'), 1, Wild('pol')),
                          co(Wild('oam'), Wild('freq'), 1, Wild('pol')):
                          N(1 / sqrt(2)) * co(Wild('oam'), Wild('freq'), 0, Wild('pol')) - N(1 / sqrt(2)) * co(Wild('oam'), Wild('freq'), 1, Wild('pol'))})
