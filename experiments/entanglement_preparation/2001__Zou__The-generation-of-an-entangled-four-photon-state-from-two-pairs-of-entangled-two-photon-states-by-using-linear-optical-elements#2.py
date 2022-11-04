# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()

epr1 = Photons(2, ['path', 'pol'], sqrt(1/2) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
epr2 = Photons(2, ['path', 'pol'], sqrt(1/2) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))

bs1 = BS()
bs2 = BS()
bs3 = BS()
bs4 = BS()

det = Detectors(4)

expt.add_sources(epr1, epr2)
expt.add_elements(bs1, bs2, bs3, bs4)
expt.add_detectors(det)

epr1.o[0] = bs1.i[0]
epr1.o[1] = bs2.i[0]
epr2.o[0] = bs1.i[1]
epr2.o[1] = bs2.i[1]
bs1.o[0] = bs3.i[1]
bs2.o[1] = bs4.i[0]
bs3.o[0] = det.i[0]
bs3.o[1] = det.i[1]
bs4.o[0] = det.i[2]
bs4.o[1] = det.i[3]

expt.build()
expt.simulate()


