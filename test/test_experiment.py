# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
theta = Symbol('theta')
from photoniqlab import Experiment, Photons, Psi_p, Detectors, BD, BS, HWP, PBS, POL, PS, QWP
from photoniqlab.path_name_generator import PathNameGenerator
from photoniqlab.exceptions import PhotoniqlabError
from test.photoniqlab_test import PhotoniqlabTest

class TestExperiment(PhotoniqlabTest):
    def test_init(self):
        experiment = Experiment()
        self.assertEqual(experiment.ele_dofs, ['path'])
        self.assertEqual(experiment.sources, [])
        self.assertEqual(experiment.elements, [])
        self.assertEqual(experiment.detectors, None)
        self.assertEqual(experiment.layers, [])
        self.assertEqual(experiment.result, [])

    def test_extend_ele_dofs(self):
        expt = Experiment()
        expt._Experiment__extend_ele_dofs(['path', 'freq'])
        self.assertEqual(set(expt.ele_dofs), set(['path', 'freq']))
        expt._Experiment__extend_ele_dofs(['oam', 'pol'])
        self.assertEqual(set(expt.ele_dofs), set(['path', 'freq', 'oam', 'pol']))

    def test_add_sources(self):
        expt = Experiment()
        photons = Photons(2, ['path', 'pol'], co('p1', 'H') * co('p2', 'V'))
        bbo = Psi_p()
        expt.add_sources(bbo, photons)
        self.assertEqual(expt.sources, [bbo, photons])

    def test_add_sources_diff_error(self):
        expt = Experiment()
        photons = Photons(2, ['path', 'freq', 'pol'], co('p1', 810, 'H') * co('p2', 405, 'V'))
        bbo = Psi_p()
        with self.assertRaises(PhotoniqlabError):
            expt.add_sources(bbo, photons)

    def test_add_elements(self):
        expt = Experiment()
        hwp = HWP(theta)
        qwp = QWP(0)
        bs = BS()
        expt.add_elements(hwp, qwp, bs)
        self.assertEqual(expt.elements, [hwp, qwp, bs])
        self.assertEqual(set(expt.ele_dofs), set(['path', 'pol']))

    def test_add_detectors(self):
        expt = Experiment()
        detectors = Detectors(4)
        expt.add_detectors(detectors)
        self.assertEqual(expt.detectors, detectors)

    def test_build(self):
        expt = Experiment()
        p1 = Photons(3, ['path', 'pol', 'freq'], (1 / sqrt(2)) * co('p1', 'H', 810) * co('p2', 'H', 810) * co('p3', 'H', 810)
                     + (1 / sqrt(2)) * co('p1', 'V', 405) * co('p2', 'V', 405) * co('p3', 'V', 405))
        p2 = Photons(1, ['path', 'pol', 'freq'], (1 / sqrt(2)) * (co('p1', 'H', 1550) + co('p1', 'V', 1550)))
        hwp1 = HWP(0)
        hwp2 = HWP(pi / 8)
        bs1 = BS()
        bs2 = BS()
        bd1 = BD(3)
        qwp1 = QWP(0)
        pol1 = POL(pi / 4)
        detectors = Detectors(2)

        expt.add_sources(p1, p2)
        expt.add_elements(hwp1, hwp2, bs1, bs2, bd1, qwp1, pol1)
        expt.add_detectors(detectors)

        p1.o[0] = hwp1.i[0]
        p1.o[1] = bs1.i[0]
        p1.o[2] = hwp2.i[0]
        p2.o[0] = bd1.i[1]
        hwp1.o[0] = bs1.i[1]
        hwp2.o[0] = bs2.i[0]
        bs1.o[0] = bs2.i[1]
        bs1.o[1] = bd1.i[0]
        bd1.o[0] = qwp1.i[0]
        bd1.o[1] = pol1.i[0]
        bs2.o[1] = detectors.i[0]
        pol1.o[0] = detectors.i[1]

        expt.build()
        self.assertEqual(expt.layers, [[hwp1, hwp2], [bs1], [bs2, bd1], [qwp1, pol1]])
        self.assertEqual(p1.path, [0, 1, 2])
        self.assertEqual(p2.path, [3])
        self.assertEqual(hwp1.path, [0])
        self.assertEqual(hwp2.path, [2])
        self.assertEqual(bs1.path, [1, 0])
        self.assertEqual(bd1.path, [0, 3, 12])
        self.assertEqual(bs2.path, [2, 1])
        self.assertEqual(pol1.path, [3])
        self.assertEqual(qwp1.path, [0])
        self.assertEqual(detectors.path, [1, 3])

    def test_simulate(self):
        expt = Experiment()
        p1 = Photons(1, ['path', 'pol'], co('p1', 'H'))
        p2 = Photons(1, ['path', 'pol'], co('p1', 'V'))
        hwp = HWP(pi / 4)
        bs = BS()
        p1.o[0] = hwp.i[0]
        hwp.o[0] = bs.i[0]
        p2.o[0] = bs.i[1]
        expt.add_sources(p1, p2)
        expt.add_elements(hwp, bs)
        expt.build()
        res = expt.simulate()
        self.assertEqual(N(res[-1], 4), (1 / 2) * co(0, 'V')**2 - (1 / 2) * co(1, 'V')**2)
