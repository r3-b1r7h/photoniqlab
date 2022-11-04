# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()

p1 = Photons(1, ['pol', 'path'], co('H', 'p1') * co('H', 'p1') * co('V', 'p1') * co('V', 'p1'))

bs1 = BS()
bs2 = BS()
bs3 = BS()
pbs = PBS()

det = Detectors(4)

expt.add_sources(p1)
expt.add_elements(bs1, bs2, bs3, pbs)
expt.add_detectors(det)

p1.o[0] = bs1.i[0]
bs1.o[0] = bs2.i[1]
bs1.o[1] = bs3.i[0]
bs2.o[0] = pbs.i[0]
pbs.o[0] = det.i[0]
bs2.o[1] = det.i[1]
bs3.o[0] = det.i[2]
bs3.o[1] = det.i[3]

expt.build()
expt.simulate()

