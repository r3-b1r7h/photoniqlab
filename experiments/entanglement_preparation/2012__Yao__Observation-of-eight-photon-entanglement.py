# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()
epr1 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
epr2 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
epr3 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
epr4 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
hwp1 = HWP(pi / 4)
hwp2 = HWP(pi / 4)
hwp3 = HWP(pi / 4)
hwp4 = HWP(pi / 4)
pbs1 = PBS()
pbs2 = PBS()
pbs3 = PBS()
pbs_epr1 = PBS()
pbs_epr2 = PBS()
pbs_epr3 = PBS()
pbs_epr4 = PBS()
det = Detectors(8)
expt.add_sources(epr1, epr2, epr3, epr4)
expt.add_elements(hwp1, hwp2, hwp3, hwp4, pbs1, pbs2, pbs3, pbs_epr1, pbs_epr2, pbs_epr3, pbs_epr4)
expt.add_detectors(det)

epr1.o[0] = hwp1.i[0]
hwp1.o[0] = pbs_epr1.i[0]
epr1.o[1] = pbs_epr1.i[1]
epr2.o[0] = hwp2.i[0]
hwp2.o[0] = pbs_epr2.i[0]
epr2.o[1] = pbs_epr2.i[1]
epr3.o[0] = hwp3.i[0]
hwp3.o[0] = pbs_epr3.i[0]
epr3.o[1] = pbs_epr3.i[1]
epr4.o[0] = hwp4.i[0]
hwp4.o[0] = pbs_epr4.i[0]
epr4.o[1] = pbs_epr4.i[1]
pbs_epr1.o[0] = pbs1.i[0]
pbs_epr2.o[0] = pbs1.i[1]
pbs_epr3.o[0] = pbs2.i[0]
pbs_epr4.o[0] = pbs2.i[1]
pbs1.o[0] = pbs3.i[0]
pbs2.o[1] = pbs3.i[1]
pbs_epr1.o[1] = det.i[0]
pbs_epr2.o[1] = det.i[1]
pbs_epr3.o[1] = det.i[2]
pbs_epr4.o[1] = det.i[3]
pbs1.o[1] = det.i[4]
pbs2.o[0] = det.i[5]
pbs3.o[0] = det.i[6]
pbs3.o[1] = det.i[7]

expt.build()
expt.simulate()
