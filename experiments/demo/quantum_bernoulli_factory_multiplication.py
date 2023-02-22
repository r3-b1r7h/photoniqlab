# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()

p = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * co('p1', 'H') * co('p2', 'H') + (1 / sqrt(2)) * co('p1', 'V') * co('p2', 'V'))

pbs_1 = PBS()
pbs_2 = PBS()
bs_1 = BS()
bs_2 = BS()

hwp_1t = HWP(pi/4)
qwp_1t = QWP(0)
pol_1t = POL(0)

# h2 == 0
hwp_1r = HWP(pi/2)
qwp_1r = QWP(pi/2)
pol_1r = POL(pi/2)

hwp_2t = HWP(pi/4)
qwp_2t = QWP(0)

# h2 == 0
hwp_2r = HWP(pi/2)
qwp_2r = QWP(pi/2)
X = HWP(pi/4)  # B is X while A == C == I

pol_H = POL(0)
det = Detectors(2)

expt.add_sources(p)
expt.add_elements(pbs_1, pbs_2, bs_1, bs_2, hwp_1t, qwp_1t, pol_1t, hwp_1r, qwp_1r, pol_1r, hwp_2t, qwp_2t, hwp_2r, qwp_2r, X, pol_H)
expt.add_detectors(det)

p.o[0] = pbs_1.i[0]

pbs_1.o[0] = hwp_1r.i[0]
hwp_1r.o[0] = qwp_1r.i[0]
qwp_1r.o[0] = pol_1r.i[0]

pbs_1.o[1] = hwp_1t.i[0]
hwp_1t.o[0] = qwp_1t.i[0]
qwp_1t.o[0] = pol_1t.i[0]

pol_1r.o[0] = bs_1.i[0]
pol_1t.o[0] = bs_1.i[1]

bs_1.o[0] = det.i[0]

p.o[1] = pbs_2.i[0]

pbs_2.o[0] = hwp_2r.i[0]
hwp_2r.o[0] = qwp_2r.i[0]
qwp_2r.o[0] = X.i[0]
X.o[0] = bs_2.i[0]

pbs_2.o[1] = hwp_2t.i[0]
hwp_2t.o[0] = qwp_2t.i[0]
qwp_2t.o[0] = bs_2.i[1]

bs_2.o[0] = pol_H.i[0]
pol_H.o[0] = det.i[1]

expt.build()
expt.simulate()