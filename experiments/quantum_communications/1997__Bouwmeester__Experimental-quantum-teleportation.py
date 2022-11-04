# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()
p = Photons(1, ['pol', 'path'], (co('H', 'p1') + co('V', 'p1')) / sqrt(2))
epr = Photons(2, ['pol', 'path'], (co('H', 'p1') * co('V', 'p2') + co('V', 'p1') * co('H', 'p2')) / sqrt(2))
bs = BS()
det = Detectors(3)

expt.add_sources(p, epr)
expt.add_elements(bs)
expt.add_detectors(det)

p.o[0] = bs.i[0]
epr.o[0] = bs.i[1]
bs.o[0] = det.i[0]
bs.o[1] = det.i[1]
epr.o[1] = det.i[2]

expt.build()
expt.simulate()