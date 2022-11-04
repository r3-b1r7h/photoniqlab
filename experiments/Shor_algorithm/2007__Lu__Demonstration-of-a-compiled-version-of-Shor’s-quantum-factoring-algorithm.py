# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()

p1 = Photons(1, ['path', 'pol'], co('p1', 'H'))
p2 = Photons(1, ['path', 'pol'], co('p1', 'H'))
p3 = Photons(1, ['path', 'pol'], co('p1', 'H'))
p4 = Photons(1, ['path', 'pol'], co('p1', 'H'))

# Hardamard gates
hdmd1 = HWP(pi / 8)
hdmd2 = HWP(pi / 8)
# C-Not gate 1
hwp_cnot1 = HWP(pi / 8)
pbs_cnot1 = PBS()
# C-Not gate 2
hwp_cnot2 = HWP(pi / 8)
pbs_cnot2 = PBS()
# semi-classical QFT
qwp = QWP(pi / 2)
hdmd3 = HWP(pi / 8)
hdmd4 = HWP(pi / 8)
det = Detectors(4)

expt.add_sources(p1, p2, p3, p4)
expt.add_elements(hdmd1, hdmd2, hdmd3, hdmd4, hwp_cnot1, pbs_cnot1, hwp_cnot2, pbs_cnot2, qwp)
expt.add_detectors(det)

p1.o[0] = hdmd1.i[0]
p2.o[0] = hdmd2.i[0]
p3.o[0] = hwp_cnot1.i[0]
hdmd2.o[0] = pbs_cnot1.i[0]
hwp_cnot1.o[0] = pbs_cnot1.i[1]
p4.o[0] = hwp_cnot2.i[0]
pbs_cnot1.o[1] = pbs_cnot2.i[0]
hwp_cnot2.o[0] = pbs_cnot2.i[1]
hdmd1.o[0] = hdmd3.i[0]
pbs_cnot2.o[1] = qwp.i[0]
qwp.o[0] = hdmd4.i[0]

hdmd3.o[0] = det.i[0]
pbs_cnot1.o[0] = det.i[1]
pbs_cnot2.o[0] = det.i[2]
hdmd4.o[0] = det.i[3]

expt.build()
expt.simulate()