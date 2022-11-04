# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()
# Creating the photon sources, passive elements and detectors.
p1 = Photons(1, ['path', 'pol'], sqrt(1/2) * (co('p1', 'H') + co('p1', 'V')))
p2 = Photons(1, ['path', 'pol'], sqrt(1/2) * (co('p1', 'H') + co('p1', 'V')))
p3 = Photons(1, ['path', 'pol'], sqrt(1/2) * (co('p1', 'H') + co('p1', 'V')))
p4 = Photons(1, ['path', 'pol'], sqrt(1/2) * (co('p1', 'H') + co('p1', 'V')))
pbs1 = PBS()
pbs2 = PBS()
pbs3 = PBS()
det = Detectors(4)
# Adding the components to exp.
expt.add_sources(p1, p2, p3, p4)
expt.add_elements(pbs1, pbs2, pbs3)
expt.add_detectors(det)
p1.o[0] = pbs1.i[0]
p2.o[0] = pbs1.i[1]
p3.o[0] = pbs2.i[0]
p4.o[0] = pbs2.i[1]
pbs1.o[1] = pbs3.i[0]
pbs2.o[0] = pbs3.i[1]
pbs1.o[0] = det.i[0]
pbs3.o[0] = det.i[1]
pbs3.o[1] = det.i[2]
pbs2.o[1] = det.i[3]
expt.build()
expt.simulate()