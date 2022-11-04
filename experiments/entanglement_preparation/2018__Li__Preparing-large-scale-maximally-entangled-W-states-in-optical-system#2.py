# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()
wa = Photons(3, ['path', 'pol'], (1 / sqrt(3)) * (co('p1', 'H') * co('p2', 'H') * co('p3', 'V') + co('p1', 'H') * co('p2', 'V') * co('p3', 'H') + co('p1', 'V') * co('p2', 'H') * co('p3', 'H')))
wb = Photons(3, ['path', 'pol'], (1 / sqrt(3)) * (co('p1', 'H') * co('p2', 'H') * co('p3', 'V') + co('p1', 'H') * co('p2', 'V') * co('p3', 'H') + co('p1', 'V') * co('p2', 'H') * co('p3', 'H')))
wc = Photons(3, ['path', 'pol'], (1 / sqrt(3)) * (co('p1', 'H') * co('p2', 'H') * co('p3', 'V') + co('p1', 'H') * co('p2', 'V') * co('p3', 'H') + co('p1', 'V') * co('p2', 'H') * co('p3', 'H')))
ancilla = Photons(1, ['path', 'pol'], co('p1', 'H'))

pdbs1 = PDBS(tH=(5 + sqrt(5)) / 10, tV=(5 - sqrt(5)) / 10)
pdbs2 = PDBS(tH=(5 + sqrt(5)) / 10, tV=(5 - sqrt(5)) / 10)
pdbs3 = PDBS(tH=(5 + sqrt(5)) / 10, tV=(5 - sqrt(5)) / 10)
pbs1 = PBS()
pbs2 = PBS()
det = Detectors(10)
expt.add_sources(wa, wb, wc, ancilla)
expt.add_elements(pdbs1, pdbs2, pdbs3, pbs1, pbs2)
expt.add_detectors(det)

ancilla.o[0] = pdbs1.i[0]
wa.o[0] = pdbs1.i[1]
pdbs1.o[1] = pdbs2.i[0]
wb.o[0] = pdbs2.i[1]
pdbs2.o[1] = pdbs3.i[0]
wc.o[0] = pdbs3.i[1]
pdbs2.o[0] = pbs1.i[0]
pdbs3.o[0] = pbs2.i[0]
wa.o[1] = det.i[0]
wa.o[2] = det.i[1]
wb.o[1] = det.i[2]
wb.o[2] = det.i[3]
wc.o[1] = det.i[4]
wc.o[2] = det.i[5]
pdbs1.o[0] = det.i[6]
pbs1.o[0] = det.i[7]
pbs2.o[0] = det.i[8]
pdbs3.o[1] = det.i[9]
expt.build()
expt.simulate()