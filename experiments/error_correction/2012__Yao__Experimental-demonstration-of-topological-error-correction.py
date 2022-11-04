# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP, PDBS

expt = Experiment()

s1 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'H') + co('p1', 'V') * co('p2', 'V')))
s2 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'H') + co('p1', 'V') * co('p2', 'V')))
s3 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'H') + co('p1', 'V') * co('p2', 'V')))
s4 = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'H') + co('p1', 'V') * co('p2', 'V')))

pbs1 = PBS()
pbs2 = PBS()
pdbs1 = PDBS(tH=1, tV=1/3)
pdbs2 = PDBS(tH=1/3, tV=1)
pdbs3 = PDBS(tH=1/3, tV=1)

det = Detectors(8)

expt.add_sources(s1, s2, s3, s4)
expt.add_elements(pbs1, pbs2, pdbs1, pdbs2, pdbs3)
expt.add_detectors(det)

s1.o[0] = pbs1.i[0]
s2.o[0] = pbs1.i[1]
s3.o[0] = pdbs1.i[0]
s4.o[0] = pdbs1.i[1]
pdbs1.o[0] = pdbs2.i[1]
pdbs1.o[1] = pdbs3.i[0]
pbs1.o[1] = pbs2.i[0]
pdbs2.o[0] = pbs2.i[1]
s1.o[1] = det.i[0]
s2.o[1] = det.i[1]
s3.o[1] = det.i[2]
s4.o[1] = det.i[3]
pbs1.o[0] = det.i[4]
pbs2.o[0] = det.i[5]
pbs2.o[1] = det.i[6]
pdbs3.o[1] = det.i[7]

expt.build()
expt.simulate()