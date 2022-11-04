# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP, Reflection, DP, LI, Hologram, EOM, PulseShaper

expt = Experiment()

s1 = Photons(2, ['pol', 'path'], (1 / sqrt(2)) * (co('H', 'p1') * co('H', 'p2') + co('V', 'p2') * co('V', 'p2')))
s2 = Photons(2, ['pol', 'path'], (1 / sqrt(2)) * (co('H', 'p1') * co('H', 'p2') + co('V', 'p2') * co('V', 'p2')))

pbs0 = PBS()
pol = POL(pi / 4)

bs_a = BS()
hwp_a = HWP(pi / 8)
qwp_a = QWP(pi / 4)
pbs1_a = PBS()
pbs2_a = PBS()
bs_b = BS()
hwp_b = HWP(pi / 8)
qwp_b = QWP(pi / 4)
pbs1_b = PBS()
pbs2_b = PBS()
bs_c = BS()
hwp_c = HWP(pi / 8)
qwp_c = QWP(pi / 4)
pbs1_c = PBS()
pbs2_c = PBS()
det = Detectors(4)

expt.add_sources(s1, s2)
expt.add_elements(pbs0, pol, bs_a, hwp_a, qwp_a, pbs1_a, pbs2_a, bs_b, hwp_b, qwp_b, pbs1_b, pbs2_b, bs_c, hwp_c, qwp_c, pbs1_c, pbs2_c)
expt.add_detectors(det)

s1.o[0] = pbs0.i[0]
s2.o[0] = pbs0.i[1]
pbs0.o[0] = pol.i[0]
pol.o[0] = det.i[0]

s1.o[1] = bs_a.i[1]
bs_a.o[0] = hwp_a.i[0]
bs_a.o[1] = qwp_a.i[0]
hwp_a.o[0] = pbs1_a.i[0]
qwp_a.o[0] = pbs2_a.i[0]
pbs1_a.o[1] = det.i[1]

s2.o[1] = bs_b.i[1]
bs_b.o[0] = hwp_b.i[0]
bs_b.o[1] = qwp_b.i[0]
hwp_b.o[0] = pbs1_b.i[0]
qwp_b.o[0] = pbs2_b.i[0]
pbs1_b.o[1] = det.i[2]

pbs0.o[1] = bs_c.i[1]
bs_c.o[0] = hwp_c.i[0]
bs_c.o[1] = qwp_c.i[0]
hwp_c.o[0] = pbs1_c.i[0]
qwp_c.o[0] = pbs2_c.i[0]
pbs1_c.o[1] = det.i[3]

expt.build()
expt.simulate()