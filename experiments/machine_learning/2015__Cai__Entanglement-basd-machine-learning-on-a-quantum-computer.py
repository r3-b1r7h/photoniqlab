# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()

s1 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
s2 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
pbsf = PBS()
hwpf1 = HWP(pi / 4)
hwpf2 = HWP(pi / 4)
pbs0 = PBS()
hwp0 = HWP(-0.1476 * pi)
pbs1 = PBS()
hwp1_0 = HWP(0)
hwp1_1 = HWP(pi / 2)
bs1 = BS()
pbs2 = PBS()
hwp2_0 = HWP(0)
hwp2_1 = HWP(pi / 2)
bs2 = BS()
pbs3 = PBS()
hwp3_0 = HWP(0)
hwp3_1 = HWP(pi / 2)
bs3 = BS()
det = Detectors(4)
expt.add_sources(s1, s2)
expt.add_elements(pbsf, hwpf1, hwpf2, pbs0, hwp0, pbs1, hwp1_0, hwp1_1, bs1, pbs2, hwp2_0, hwp2_1, bs2, pbs3, hwp3_0, hwp3_1, bs3)
expt.add_detectors(det)

s1.o[0] = hwpf1.i[0]
s1.o[1] = pbsf.i[0]
s2.o[0] = pbsf.i[1]
s2.o[1] = hwpf2.i[0]

hwpf1.o[0] = hwp0.i[0]
hwp0.o[0] = pbs0.i[0]

pbsf.o[0] = pbs1.i[0]
pbs1.o[0] = hwp1_1.i[0]
pbs1.o[1] = hwp1_0.i[0]
hwp1_1.o[0] = bs1.i[0]
hwp1_0.o[0] = bs1.i[1]

pbsf.o[1] = pbs2.i[0]
pbs2.o[0] = hwp2_1.i[0]
pbs2.o[1] = hwp2_0.i[0]
hwp2_1.o[0] = bs2.i[0]
hwp2_0.o[0] = bs2.i[1]

hwpf2.o[0] = pbs3.i[0]
pbs3.o[0] = hwp3_1.i[0]
pbs3.o[1] = hwp3_0.i[0]
hwp3_1.o[0] = bs3.i[0]
hwp3_0.o[0] = bs3.i[1]

pbs0.o[1] = det.i[0]
bs1.o[0] = det.i[1]
bs2.o[0] = det.i[2]
bs3.o[0] = det.i[3]

expt.build()
expt.simulate()

