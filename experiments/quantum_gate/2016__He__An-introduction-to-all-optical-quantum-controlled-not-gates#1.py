# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()

a, b = symbols('a b')
p1 = Photons(1, ['path', 'pol'], co('p1', 'H'))
p2 = Photons(1, ['path', 'pol'], a * co('p1', 'H') + b * co('p1', 'V'))
pbs = PBS()
hwp = HWP(pi / 8)
detectors = Detectors(2)

expt.add_sources(p1, p2)
expt.add_elements(hwp, pbs)
expt.add_detectors(detectors)

p2.o[0] = pbs.i[0]
p1.o[0] = hwp.i[0]
hwp.o[0] = pbs.i[1]
pbs.o[0] = detectors.i[0]
pbs.o[1] = detectors.i[1]

expt.build()
expt.simulate()
