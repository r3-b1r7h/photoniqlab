# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PBSFS, POL, PS, QWP

expt = Experiment()

alpha, beta = symbols('alpha beta')

control = Photons(1, ['path', 'pol'], co('p1', 'V'))
target = Photons(1, ['path', 'pol'], alpha * co('p1', 'H') + beta * co('p1', 'V'))

pbs_fs = PBSFS()
pbs = PBS()
det = Detectors(2)

expt.add_sources(control, target)
expt.add_elements(pbs_fs, pbs)
expt.add_detectors(det)

control.o[0] = pbs_fs.i[0]
target.o[0] = pbs_fs.i[1]
pbs_fs.o[1] = pbs.i[0]
pbs_fs.o[0] = det.i[0]
pbs.o[1] = det.i[1]

expt.build()
expt.simulate()