# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()
alpha, beta, delta, gamma = symbols('alpha beta delta gamma')
target = Photons(1, ['path', 'pol'], delta * co('p1', 'H') + gamma * co('p1', 'V'))
control = Photons(1, ['path', 'pol'], alpha * co('p1', 'H') + beta * co('p1', 'V'))

hwp_i = HWP(pi/8)
hwp_o = HWP(pi/8)
hwp_comp = HWP(0)
hwp1 = HWP(0.3472 * pi)
hwp2 = HWP(0.3472 * pi)
hwp3 = HWP(0.3472 * pi)
bd1 = BD(3)
bd2 = BD(4, swap=True)
det = Detectors(2)

expt.add_sources(control, target)
expt.add_elements(hwp_i, hwp_o, hwp_comp, hwp1, hwp2, hwp3, bd1, bd2)
expt.add_detectors(det)

target.o[0] = hwp_i.i[0]
hwp_i.o[0] = bd1.i[0]
control.o[0] = bd1.i[1]
bd1.o[0] = hwp1.i[0]
bd1.o[1] = hwp2.i[0]
bd1.o[2] = hwp3.i[0]
hwp1.o[0] = bd2.i[0]
hwp2.o[0] = bd2.i[1]
hwp3.o[0] = bd2.i[2]
bd2.o[1] = hwp_o.i[0]
bd2.o[2] = hwp_comp.i[0]
hwp_comp.o[0] = det.i[0]
hwp_o.o[0] = det.i[1]

expt.build()
expt.simulate()