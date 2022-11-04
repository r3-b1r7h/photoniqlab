# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()

a, b = symbols('a b')
p1 = Photons(1, ['path', 'pol'], co('p1', 'V'))
p2 = Photons(1, ['path', 'pol'], a * co('p1', 'H') + b * co('p1', 'V'))
pbs = PBS()
hwp1 = HWP(0.375 * pi)
hwp2 = HWP(pi / 4)
det = Detectors(2)

expt.add_sources(p1, p2)
expt.add_elements(hwp1, hwp2, pbs)
expt.add_detectors(det)

p2.o[0] = pbs.i[0]
p1.o[0] = hwp1.i[0]
hwp1.o[0] = pbs.i[1]
pbs.o[0] = det.i[0]
pbs.o[1] = hwp2.i[0]
hwp2.o[0] = det.i[1]

expt.build()
expt.simulate()
