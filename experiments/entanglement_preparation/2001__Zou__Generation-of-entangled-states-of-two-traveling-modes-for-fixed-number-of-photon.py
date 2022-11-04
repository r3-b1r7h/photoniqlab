# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()

p1 = Photons(2, ['path'], co('p1') * co('p2'))
ancila1 = Photons(1, ['path'], co('p1'))
ancila2 = Photons(1, ['path'], co('p1'))

bs1 = BS()
bs2 = BS()
bs3 = BS()
bs4 = BS(eta=2/3)

det = Detectors(2)
det.coincidence[0] = 0
det.coincidence[1] = 0

expt.add_sources(p1, ancila1, ancila2)
expt.add_elements(bs1, bs2, bs3, bs4)
expt.add_detectors(det)

p1.o[0] = bs1.i[0]
p1.o[1] = bs1.i[1]
bs1.o[0] = bs2.i[1]
bs1.o[1] = bs3.i[0]
ancila1.o[0] = bs2.i[0]
ancila2.o[0] = bs3.i[1]
bs2.o[1] = bs4.i[0]
bs3.o[0] = bs4.i[1]
bs2.o[0] = det.i[0]
bs3.o[1] = det.i[1]

expt.build()
expt.simulate()
