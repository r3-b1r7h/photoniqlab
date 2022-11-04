# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PBSFS, POL, PS, QWP

expt = Experiment()

alpha, beta = symbols('alpha beta')
delta, gamma = symbols('delta gamma')

control = Photons(1, ['path', 'pol'], alpha * co('p1', 'H') + beta * co('p1', 'V'))
target = Photons(1, ['path', 'pol'], delta * co('p1', 'H') + gamma * co('p1', 'V'))
phi_m = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * co('p1', 'H') * co('p2', 'H') + (1 / sqrt(2)) * co('p1', 'V') * co('p2', 'V'))
pbs = PBS()
pol_f = POL(pi / 4)
pbs_fs = PBSFS()
pol_h = POL(0)
det = Detectors(4)
expt.add_sources(control, target, phi_m)
expt.add_elements(pbs, pol_f, pbs_fs, pol_h)
expt.add_detectors(det)

control.o[0] = pbs.i[0]
phi_m.o[0] = pbs.i[1]
phi_m.o[1] = pbs_fs.i[0]
target.o[0] = pbs_fs.i[1]
pbs.o[0] = pol_f.i[0]
pbs_fs.o[1] = pol_h.i[0]
pol_f.o[0] = det.i[0]
pbs.o[1] = det.i[1]
pbs_fs.o[0] = det.i[2]
pol_h.o[0] = det.i[3]

expt.build()
expt.simulate()
