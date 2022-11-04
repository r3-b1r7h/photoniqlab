# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()

a, b, c, d = symbols('a b c d')
entangled = Photons(4, ['path', 'pol'], 0.5 * co('p1', 'H') * co('p2', 'H') * co('p3', 'H') * co('p4', 'H')
                    + 0.5 * co('p1', 'H') * co('p2', 'H') * co('p3', 'V') * co('p4', 'V')
                    + 0.5 * co('p1', 'V') * co('p2', 'V') * co('p3', 'V') * co('p4', 'H')
                    + 0.5 * co('p1', 'V') * co('p2', 'V') * co('p3', 'H') * co('p4', 'V'))
control = Photons(1, ['path', 'pol'], a * co('p1', 'H') + b * co('p1', 'V'))
target = Photons(1, ['path', 'pol'], c * co('p1', 'H') + d * co('p1', 'V'))

pbs1 = PBS()
pbs2 = PBS()
pol1 = POL(pi / 4)
pol2 = POL(pi / 4)
pol3 = POL(pi / 4)
pol4 = POL(pi / 4)

det = Detectors(4)

expt.add_sources(entangled, control, target)
expt.add_elements(pbs1, pbs2, pol1, pol2, pol3, pol4)
expt.add_detectors(det)

entangled.o[0] = pbs1.i[1]
entangled.o[3] = pbs2.i[0]
control.o[0] = pbs1.i[0]
target.o[0] = pbs2.i[1]
pbs1.o[0] = pol1.i[0]
pbs1.o[1] = pol2.i[0]
#entangled.o[1] = det.i[2]
#entangled.o[2] = det.i[3]
pbs2.o[0] = pol3.i[0]
pbs2.o[1] = pol4.i[0]
pol1.o[0] = det.i[0]
pol2.o[0] = det.i[1]
pol3.o[0] = det.i[2]
pol4.o[0] = det.i[3]

expt.build()
expt.simulate()