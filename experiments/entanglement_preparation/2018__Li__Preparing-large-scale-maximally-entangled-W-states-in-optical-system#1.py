# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()
wa = Photons(3, ['path', 'pol'], (1 / sqrt(3)) * (co('p1', 'H') * co('p2', 'H') * co('p3', 'V') + co('p1', 'H') * co('p2', 'V') * co('p3', 'H') + co('p1', 'V') * co('p2', 'H') * co('p3', 'H')))
wb = Photons(3, ['path', 'pol'], (1 / sqrt(3)) * (co('p1', 'H') * co('p2', 'H') * co('p3', 'V') + co('p1', 'H') * co('p2', 'V') * co('p3', 'H') + co('p1', 'V') * co('p2', 'H') * co('p3', 'H')))
ancilla = Photons(1, ['path', 'pol'], co('p1', 'H'))

pdbs1 = PDBS(tH=(5 + sqrt(5)) / 10, tV=(5 - sqrt(5)) / 10)
pdbs2 = PDBS(tH=(5 + sqrt(5)) / 10, tV=(5 - sqrt(5)) / 10)
pbs = PBS()
det = Detectors(7)
expt.add_sources(wa, wb, ancilla)
expt.add_elements(pdbs1, pdbs2, pbs)
expt.add_detectors(det)

ancilla.o[0] = pdbs1.i[0]
wa.o[0] = pdbs1.i[1]
pdbs1.o[1] = pdbs2.i[0]
wb.o[0] = pdbs2.i[1]
pdbs2.o[1] = pbs.i[0]
pdbs1.o[0] = det.i[0]
pdbs2.o[0] = det.i[1]
pbs.o[0] = det.i[2]
wa.o[1] = det.i[3]
wa.o[2] = det.i[4]
wb.o[1] = det.i[5]
wb.o[2] = det.i[6]

expt.build()
expt.simulate()