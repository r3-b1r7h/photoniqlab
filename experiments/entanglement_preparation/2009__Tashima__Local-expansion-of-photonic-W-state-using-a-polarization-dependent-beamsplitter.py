# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()
w = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * co('p1', 'H') * co('p2', 'V') + (1 / sqrt(2)) * co('p1', 'V') * co('p2', 'H'))
ancilla = Photons(1, ['path', 'pol'], co('p1', 'H'))
pdbs = PDBS(tH=(5 - sqrt(5)) / 10, tV=(5 + sqrt(5)) / 10)
hwp = HWP(0)
det = Detectors(2)
expt.add_sources(w, ancilla)
expt.add_elements(pdbs, hwp)
expt.add_detectors(det)

w.o[0] = pdbs.i[0]
ancilla.o[0] = pdbs.i[1]
pdbs.o[1] = hwp.i[0]
pdbs.o[0] = det.i[0]
hwp.o[0] = det.i[1]

expt.build()
expt.simulate()