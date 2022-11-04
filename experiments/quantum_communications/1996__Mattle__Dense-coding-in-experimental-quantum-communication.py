# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()

s = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
qwp1 = QWP(0)
qwp2 = QWP(0)
bs = BS()
pbs1 = PBS()
pbs2 = PBS()
det = Detectors(2)

expt.add_sources(s)
expt.add_elements(qwp1, qwp2, bs, pbs1, pbs2)
expt.add_detectors(det)

s.o[0] = qwp1.i[0]
qwp1.o[0] = qwp2.i[0]
qwp2.o[0] = bs.i[0]
s.o[1] = bs.i[1]
bs.o[0] = pbs1.i[1]
bs.o[1] = pbs2.i[1]
pbs1.o[0] = det.i[0]
pbs2.o[1] = det.i[1]

expt.build()
expt.simulate()