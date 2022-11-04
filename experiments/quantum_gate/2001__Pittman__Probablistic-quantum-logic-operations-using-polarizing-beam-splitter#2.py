# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PBSFS, POL, PS, QWP

expt = Experiment()

a, b = symbols('a b')

p1 = Photons(1, ['path', 'pol'], a * co('p1', 'H') + b * co('p1', 'V'))
p2 = Photons(1, ['path', 'pol'], (1/sqrt(2)) * (co('p1', 'H') + co('p1', 'V')))

pbs = PBS()
pbsfs = PBSFS()

det = Detectors(2)

expt.add_sources(p1, p2)
expt.add_elements(pbs, pbsfs)
expt.add_detectors(det)

p1.o[0] = pbs.i[0]
p2.o[0] = pbs.i[1]
pbs.o[0] = pbsfs.i[1]

pbsfs.o[0] = det.i[0]
pbs.o[1] = det.i[1]

expt.build()
expt.simulate()