# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()
a = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
b = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
pbs = PBS()
det = Detectors(4)
expt.add_sources(a, b)
expt.add_elements(pbs)
expt.add_detectors(det)

a.o[0] = pbs.i[0]
b.o[0] = pbs.i[1]
a.o[1] = det.i[0]
b.o[1] = det.i[1]
pbs.o[0] = det.i[2]
pbs.o[1] = det.i[3]

expt.build()
expt.simulate()