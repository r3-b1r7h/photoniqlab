# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()
s1 = Photons(2, ['pol', 'path'], (co('H', 'p1') * co('V', 'p2') + co('V', 'p1') * co('H', 'p2')) / sqrt(2))
s2 = Photons(2, ['pol', 'path'], (co('H', 'p1') * co('V', 'p2') + co('V', 'p1') * co('H', 'p2')) / sqrt(2))
bs = BS()
det = Detectors(4)

expt.add_sources(s1, s2)
expt.add_elements(bs)
expt.add_detectors(det)

s1.o[1] = bs.i[0]
s2.o[0] = bs.i[1]
s1.o[0] = det.i[0]
bs.o[0] = det.i[1]
bs.o[1] = det.i[2]
s2.o[1] = det.i[3]

expt.build()
expt.simulate()