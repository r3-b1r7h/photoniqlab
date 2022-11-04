# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()
epr1 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'H') + co('p1', 'V') * co('p2', 'V')))
epr2 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'H') + co('p1', 'V') * co('p2', 'V')))
epr3 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'H') + co('p1', 'V') * co('p2', 'V')))
pbs = PBS()
pdbs1 = PDBS(tH=1, tV=1/3)
pdbs2 = PDBS(tH=1/3, tV=1)
pdbs3 = PDBS(tH=1/3, tV=1)
pdbs4 = PDBS(tH=1, tV=1/3)
pdbs5 = PDBS(tH=1/3, tV=1)
pdbs6 = PDBS(tH=1/3, tV=1)
hdmd1 = HWP(pi / 8)
hdmd2 = HWP(pi / 8)
hdmd3 = HWP(pi / 8)
hdmd4 = HWP(pi / 8)
det = Detectors(6)
expt.add_sources(epr1, epr2, epr3)
expt.add_elements(pbs, pdbs1, pdbs2, pdbs3, pdbs4, pdbs5, pdbs6, hdmd1, hdmd2, hdmd3, hdmd4)
expt.add_detectors(det)

epr1.o[0] = pbs.i[0]
epr2.o[0] = pbs.i[1]
pbs.o[1] = hdmd1.i[0]
hdmd1.o[0] = pdbs1.i[0]
epr3.o[0] = pdbs1.i[1]
pdbs1.o[0] = pdbs2.i[0]
pdbs1.o[1] = pdbs3.i[0]
pdbs3.o[1] = hdmd3.i[0]
pbs.o[0] = hdmd2.i[0]
hdmd2.o[0] = pdbs4.i[0]
epr3.o[1] = pdbs4.i[1]
pdbs4.o[0] = pdbs5.i[0]
pdbs4.o[1] = pdbs6.i[0]
pdbs6.o[1] = hdmd4.i[0]
epr1.o[1] = det.i[0]
epr2.o[1] = det.i[1]
pdbs2.o[1] = det.i[2]
pdbs5.o[1] = det.i[3]
hdmd3.o[0] = det.i[4]
hdmd4.o[0] = det.i[5]

expt.build()
expt.simulate()