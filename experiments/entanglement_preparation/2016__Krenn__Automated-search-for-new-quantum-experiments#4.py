# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP, Reflection, DP, LI, Hologram

expt = Experiment()
xxx = [co(-i, 'p1') * co(i, 'p2') + co(-i, 'p3') * co(i, 'p4') for i in range(-1, 2)]
state = 0
for item in xxx:
	state += item
spdc = Photons(4, ['oam', 'path'], state**2)
li = LI()
det = Detectors(4)

expt.add_sources(spdc)
expt.add_elements(li)
expt.add_detectors(det)

spdc.o[1] = li.i[0]
spdc.o[2] = li.i[1]
spdc.o[0] = det.i[0]
spdc.o[3] = det.i[1]
li.o[0] = det.i[2]
li.o[1] = det.i[3]

expt.build()
expt.simulate()