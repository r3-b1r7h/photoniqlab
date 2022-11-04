# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()
alpha, beta = symbols('alpha beta')
s = Photons(1, ['path', 'pol'], alpha * co('p1', 'H') + beta * co('p1', 'V'))
epr1 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'H') + co('p1', 'V') * co('p2', 'V')))
epr2 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'H') + co('p1', 'V') * co('p2', 'V')))
pbs1 = PBS()
pbs2 = PBS()
pol1 = POL(pi / 4)
pol2 = POL(pi / 4)
pol3 = POL(pi / 4)
pol4 = POL(pi / 4)
det = Detectors(5)
expt.add_sources(s, epr1, epr2)
expt.add_elements(pbs1, pbs2, pol1, pol2, pol3, pol4)
expt.add_detectors(det)

s.o[0] = pbs1.i[0]
epr1.o[0] = pbs1.i[1]
epr1.o[1] = pbs2.i[0]
epr2.o[0] = pbs2.i[1]
pbs1.o[0] = pol1.i[0]
pbs1.o[1] = pol2.i[0]
pbs2.o[0] = det.i[0]
pbs2.o[1] = pol3.i[0]
epr2.o[1] = pol4.i[0]
pol1.o[0] = det.i[1]
pol2.o[0] = det.i[2]
pol3.o[0] = det.i[3]
pol4.o[0] = det.i[4]

expt.build()
expt.simulate()