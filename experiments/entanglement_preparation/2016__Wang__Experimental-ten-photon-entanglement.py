# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()
epr1 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
epr2 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
epr3 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
epr4 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
epr5 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
hwp1 = HWP(pi / 4)
hwp2 = HWP(pi / 4)
hwp3 = HWP(pi / 4)
hwp4 = HWP(pi / 4)
hwp5 = HWP(pi / 4)
pbs1 = PBS()
pbs2 = PBS()
pbs3 = PBS()
pbs4 = PBS()
det = Detectors(10)
expt.add_sources(epr1, epr2, epr3, epr4, epr5)
expt.add_elements(pbs1, pbs2, pbs3, pbs4, hwp1, hwp2, hwp3, hwp4, hwp5)
expt.add_detectors(det)

epr1.o[0] = hwp1.i[0]
epr2.o[0] = hwp2.i[0]
epr3.o[0] = hwp3.i[0]
epr4.o[0] = hwp4.i[0]
hwp1.o[0] = pbs1.i[0]
hwp2.o[0] = pbs1.i[1]
hwp3.o[0] = pbs2.i[0]
hwp4.o[0] = pbs2.i[1]
pbs1.o[1] = pbs3.i[0]
pbs2.o[0] = pbs3.i[1]
pbs2.o[1] = pbs4.i[0]
epr5.o[0] = hwp5.i[0]
hwp5.o[0] = pbs4.i[1]
epr1.o[1] = det.i[0]
pbs1.o[0] = det.i[1]
epr2.o[1] = det.i[2]
pbs3.o[0] = det.i[3]
pbs3.o[1] = det.i[4]
epr3.o[1] = det.i[5]
epr4.o[1] = det.i[6]
epr5.o[1] = det.i[7]
pbs4.o[0] = det.i[8]
pbs4.o[1] = det.i[9]

expt.build()
expt.simulate()