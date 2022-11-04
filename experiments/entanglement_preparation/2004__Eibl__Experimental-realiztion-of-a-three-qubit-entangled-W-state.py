# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()
four_p = Photons(2, ['path', 'pol'], 0.5 * co('p1', 'H') * co('p2', 'H') * co('p1', 'H') * co('p2', 'H')
                 + 0.5 * co('p1', 'V') * co('p2', 'V') * co('p1', 'V') * co('p2', 'V')
                 + (1 / sqrt(2)) * co('p1', 'H') * co('p2', 'H') * co('p1', 'V') * co('p2', 'V'))

pbs = PBS()
pdbs = PDBS()
bs1 = BS()
bs2 = BS()
det = Detectors(4)
expt.add_sources(four_p)
expt.add_elements(pbs, pdbs, bs1, bs2)
expt.add_detectors(det)

four_p.o[0] = pdbs.i[1]
four_p.o[1] = pbs.i[0]
pdbs.o[1] = bs1.i[0]
pbs.o[1] = bs1.i[1]
bs1.o[0] = bs2.i[1]
pdbs.o[0] = det.i[0]
pbs.o[0] = det.i[1]
bs2.o[0] = det.i[2]
bs2.o[1] = det.i[3]

expt.build()
expt.simulate()