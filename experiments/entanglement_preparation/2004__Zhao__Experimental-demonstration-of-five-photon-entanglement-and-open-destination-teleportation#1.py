# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()
s = Photons(1, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') + co('p1', 'V')))
epr1 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'H') + co('p1', 'V') * co('p2', 'V')))
epr2 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'H') + co('p1', 'V') * co('p2', 'V')))
pbs1 = PBS()
pbs2 = PBS()
det = Detectors(5)
expt.add_sources(s, epr1, epr2)
expt.add_elements(pbs1, pbs2)
expt.add_detectors(det)

s.o[0] = pbs1.i[0]
epr1.o[0] = pbs1.i[1]
epr1.o[1] = pbs2.i[0]
epr2.o[0] = pbs2.i[1]
pbs1.o[0] = det.i[0]
pbs1.o[1] = det.i[1]
pbs2.o[0] = det.i[2]
pbs2.o[1] = det.i[3]
epr2.o[1] = det.i[4]

expt.build()
expt.simulate()
