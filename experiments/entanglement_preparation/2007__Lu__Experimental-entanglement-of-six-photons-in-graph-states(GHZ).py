# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()
epr1 = Photons(2, ['path', 'pol'], co('p1', 'H') * co('p2', 'H') / sqrt(2) + co('p1', 'V') * co('p2', 'V') / sqrt(2))
epr2 = Photons(2, ['path', 'pol'], co('p1', 'H') * co('p2', 'H') / sqrt(2) + co('p1', 'V') * co('p2', 'V') / sqrt(2))
epr3 = Photons(2, ['path', 'pol'], co('p1', 'H') * co('p2', 'H') / sqrt(2) + co('p1', 'V') * co('p2', 'V') / sqrt(2))
pbs1 = PBS()
pbs2 = PBS()
det = Detectors(6)
expt.add_sources(epr1, epr2, epr3)
expt.add_elements(pbs1, pbs2)
expt.add_detectors(det)
epr1.o[1] = pbs1.i[0]
epr2.o[0] = pbs1.i[1]
epr2.o[1] = pbs2.i[0]
epr3.o[0] = pbs2.i[1]
epr1.o[0] = det.i[0]
pbs1.o[0] = det.i[1]
pbs1.o[1] = det.i[2]
pbs2.o[0] = det.i[3]
pbs2.o[1] = det.i[4]
epr3.o[1] = det.i[5]
expt.build()
expt.simulate()