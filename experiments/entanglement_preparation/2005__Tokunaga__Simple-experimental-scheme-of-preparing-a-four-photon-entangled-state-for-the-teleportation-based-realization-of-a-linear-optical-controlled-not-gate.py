# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()
epr = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * co('p1', 'H') * co('p2', 'H') + (1 / sqrt(2)) * co('p1', 'V') * co('p2', 'V'))
p1 = Photons(1, ['path', 'pol'], (1 / sqrt(2)) * co('p1', 'H') + (1 / sqrt(2)) * co('p1', 'V'))
p2 = Photons(1, ['path', 'pol'], (1 / sqrt(2)) * co('p1', 'H') + (1 / sqrt(2)) * co('p1', 'V'))
pbs1 = PBS()
pbs2 = PBS()
hwp1 = HWP(pi / 8)
hwp2 = HWP(pi / 8)
hwp3 = HWP(pi / 8)
det = Detectors(4)
expt.add_sources(epr, p1, p2)
expt.add_elements(pbs1, pbs2, hwp1, hwp2, hwp3)
expt.add_detectors(det)

epr.o[0] = hwp1.i[0]
epr.o[1] = pbs1.i[0]
p1.o[0] = pbs1.i[1]
pbs1.o[0] = hwp2.i[0]
pbs1.o[1] = hwp3.i[0]
hwp3.o[0] = pbs2.i[0]
p2.o[0] = pbs2.i[1]
hwp1.o[0] = det.i[0]
hwp2.o[0] = det.i[1]
pbs2.o[0] = det.i[2]
pbs2.o[1] = det.i[3]

expt.build()
expt.simulate()