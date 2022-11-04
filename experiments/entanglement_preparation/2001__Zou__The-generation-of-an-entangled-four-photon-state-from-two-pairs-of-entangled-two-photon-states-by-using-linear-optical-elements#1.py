# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Psi_p, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()

epr1 = Psi_p()
epr2 = Psi_p()

bs1 = BS()
bs2 = BS()
#bs3 = BS()
#bs4 = BS()

det = Detectors(2)
det.coincidence[0] = 0
det.coincidence[1] = 0

expt.add_sources(epr1, epr2)
expt.add_elements(bs1, bs2)
expt.add_detectors(det)

epr1.o[0] = bs1.i[0]
epr1.o[1] = bs2.i[0]
epr2.o[0] = bs1.i[1]
epr2.o[1] = bs2.i[1]
'''bs1.o[0] = bs3.i[1]
bs2.o[1] = bs4.i[0]
bs3.o[0] = det.i[0]
bs3.o[1] = det.i[1]
bs4.o[0] = det.i[2]
bs4.o[1] = det.i[3]'''

bs1.o[0] = det.i[0]
bs2.o[1] = det.i[1]

expt.build()
expt.simulate()


