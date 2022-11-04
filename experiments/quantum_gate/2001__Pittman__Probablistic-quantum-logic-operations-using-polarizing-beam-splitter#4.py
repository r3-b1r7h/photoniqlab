# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PBSFS, POL, PS, QWP

expt = Experiment()

alpha, beta = symbols('alpha beta')

p_in = Photons(1, ['path', 'pol'], alpha * co('p1', 'H') + beta * co('p1', 'V'))
phi_m = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * co('p1', 'H') * co('p2', 'H') + (1 / sqrt(2)) * co('p1', 'V') * co('p2', 'V'))
pbs = PBS()
pbs_fs = PBSFS()
det = Detectors(3)

expt.add_sources(p_in, phi_m)
expt.add_elements(pbs, pbs_fs)
expt.add_detectors(det)

p_in.o[0] = pbs.i[0]
phi_m.o[0] = pbs.i[1]
pbs.o[0] = pbs_fs.i[1]
phi_m.o[1] = det.i[0]
pbs.o[1] = det.i[1]
pbs_fs.o[0] = det.i[2]

expt.build()
expt.simulate()