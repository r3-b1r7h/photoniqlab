# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()

p1 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * co('p1', 'H') * co('p2', 'V') + (1 / sqrt(2)) * co('p1', 'V') * co('p2', 'H'))
p2 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * co('p1', 'H') * co('p2', 'V') + (1 / sqrt(2)) * co('p1', 'V') * co('p2', 'H'))

pbs1 = PBS()
pbs2 = PBS()
pbs3 = PBS()
bs = BS()
hwp = HWP(pi / 4)
det = Detectors(4)
expt.add_sources(p1, p2)
expt.add_elements(pbs1, pbs2, pbs3, bs, hwp)
expt.add_detectors(det)

p1.o[1] = pbs1.i[0]
p2.o[1] = pbs2.i[0]
pbs1.o[1] = bs.i[0]
pbs2.o[1] = bs.i[1]
pbs1.o[0] = hwp.i[0]
hwp.o[0] = pbs3.i[0]
pbs2.o[0] = pbs3.i[1]
p1.o[0] = det.i[0]
pbs3.o[1] = det.i[1]
bs.o[0] = det.i[2]
p2.o[0] = det.i[3]

expt.build()
expt.simulate()