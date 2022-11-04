# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()
alpha = Symbol('alpha')
theta, phi, omega = symbols('theta phi omega')
a, b, c = symbols('a b c')
p1 = Photons(1, ['path', 'pol'], alpha * co('p1', 'H'))
epr = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * co('p1', 'H') * co('p2', 'V') + (1 / sqrt(2)) * co('p1', 'V') * co('p2', 'H'))
hwp1 = HWP(pi / 8)
hwp2 = HWP(pi / 4)
pbs = PBS()
bc1 = BC(theta)
bc2 = BC(phi)
bc3 = BC(omega)
det = Detectors(3)
expt.add_sources(p1, epr)
expt.add_elements(hwp1, hwp2, pbs, bc1, bc2, bc3)
expt.add_detectors(det)
p1.o[0] = hwp1.i[0]
epr.o[1] = hwp2.i[0]
hwp1.o[0] = pbs.i[0]
epr.o[0] = pbs.i[1]
pbs.o[0] = bc1.i[0]
pbs.o[1] = bc2.i[0]
hwp2.o[0] = bc3.i[0]
bc1.o[0] = det.i[0]
bc2.o[0] = det.i[1]
bc3.o[0] = det.i[2]
expt.build()
expt.simulate()