# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()
state_in = Photons(2, ['path', 'pol'], 0.5 * (co('p1', 'H') * co('p2', 'V') - co('p1', 'V') * co('p2', 'H')) * (co('p1', 'H') * co('p2', 'V') - co('p1', 'V') * co('p2', 'H')))
hwp = HWP(3 * pi / 8)
pbs1 = PBS()
pbs2 = PBS()
bs = BS()
det = Detectors(4)
expt.add_sources(state_in)
expt.add_elements(hwp, pbs1, pbs2, bs)
expt.add_detectors(det)

state_in.o[0] = pbs1.i[1]
pbs1.o[1] = hwp.i[0]
hwp.o[0] = pbs2.i[0]
state_in.o[1] = bs.i[0]
bs.o[0] = pbs2.i[1]
pbs1.o[0] = det.i[0]
pbs2.o[0] = det.i[1]
pbs2.o[1] = det.i[2]
bs.o[1] = det.i[3]

expt.build()
expt.simulate()