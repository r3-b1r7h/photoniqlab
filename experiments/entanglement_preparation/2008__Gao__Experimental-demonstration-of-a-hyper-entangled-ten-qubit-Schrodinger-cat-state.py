# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Psi_p, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()

bbo1 = Psi_p()
bbo2 = Psi_p()
ancilla = Photons(1, ['path', 'pol'], co('p1', 'H'))

pbs1 = PBS()
pbs2 = PBS()
hwp = HWP(pi / 8)

det = Detectors(5)

expt.add_sources(bbo1, bbo2, ancilla)
expt.add_elements(pbs1, pbs2, hwp)
expt.add_detectors(det)

ancilla.o[0] = hwp.i[0]
bbo1.o[0] = pbs1.i[0]
bbo2.o[0] = pbs1.i[1]
pbs1.o[1] = pbs2.i[0]
hwp.o[0] = pbs2.i[1]
bbo1.o[1] = det.i[0]
bbo2.o[1] = det.i[1]
pbs1.o[0] = det.i[2]
pbs2.o[0] = det.i[3]
pbs2.o[1] = det.i[4]

expt.build()
expt.simulate()
