# -*- coding: utf-8 -*-

import unittest

from photoniqlab.sympy_widget import *
from photoniqlab.path_name_generator import PathNameGenerator

class PhotoniqlabTest(unittest.TestCase):
    def setUp(self):
        PathNameGenerator.path_name = -1

    def tearDown(self):
        pass