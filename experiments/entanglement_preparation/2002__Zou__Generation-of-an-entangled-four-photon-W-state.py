# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()

epr = Photons(2, ['path', 'pol'], sqrt(1/2) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
ancilla1 = Photons(1, ['path', 'pol'], co('p1', 'H'))
ancilla2 = Photons(1, ['path', 'pol'], co('p1', 'H'))

pbs1 = PBS()
pbs2 = PBS()
pbs3 = PBS()
pbs4 = PBS()

bs1 = BS(eta=1/3)
bs2 = BS(eta=1/3)
bs3 = BS()
bs4 = BS()

det = Detectors(4)

expt.add_sources(epr, ancilla1, ancilla2)
expt.add_elements(pbs1, pbs2, pbs3, pbs4, bs1, bs2, bs3, bs4)
expt.add_detectors(det)

epr.o[0] = pbs1.i[1]
epr.o[1] = pbs2.i[1]
ancilla1.o[0] = bs1.i[1]
ancilla2.o[0] = bs2.i[1]
pbs1.o[0] = bs1.i[0]
pbs2.o[0] = bs2.i[0]
pbs1.o[1] = pbs3.i[1]
pbs2.o[1] = pbs4.i[1]
bs1.o[0] = pbs3.i[0]
bs2.o[0] = pbs4.i[0]
pbs3.o[1] = bs3.i[1]
pbs4.o[1] = bs4.i[1]
bs3.o[0] = det.i[0]
bs3.o[1] = det.i[1]
bs4.o[0] = det.i[2]
bs4.o[1] = det.i[3]

expt.build()
expt.simulate()
