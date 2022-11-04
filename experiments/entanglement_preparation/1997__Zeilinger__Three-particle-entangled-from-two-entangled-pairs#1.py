# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()

a = Photons(4, ['path'], (1 / sqrt(2)) * co('p1') * co('p4') + (1 / sqrt(2)) * co('p2') * co('p3'))
b = Photons(4, ['path'], (1 / sqrt(2)) * co('p1') * co('p4') + (1 / sqrt(2)) * co('p2') * co('p3'))
bs = BS()
det = Detectors(2)
det.coincidence[1] = 0
expt.add_sources(a, b)
expt.add_elements(bs)
expt.add_detectors(det)

a.o[3] = bs.i[0]
b.o[0] = bs.i[1]
bs.o[0] = det.i[0]
bs.o[1] = det.i[1]

expt.build()
expt.simulate()
