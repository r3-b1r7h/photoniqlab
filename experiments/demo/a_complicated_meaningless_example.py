# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

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
pbs = PBS()
detectors = Detectors(2)

expt.add_sources(p1, p2)
expt.add_elements(hwp1, hwp2, bs1, bs2, bd1, qwp1, pol1, pbs)
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
pol1.o[0] = pbs.i[0]
bs2.o[1] = pbs.i[1]
pbs.o[1] = detectors.i[0]
pbs.o[0] = detectors.i[1]

expt.build()
#pdb.set_trace()
expt.simulate()
