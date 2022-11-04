# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()

p1 = Photons(1, ['path'], co('p1'))
p2 = Photons(1, ['path'], co('p1'))

bs = BS()

expt.add_sources(p1, p2)
expt.add_elements(bs)

p1.o[0] = bs.i[0]
p2.o[0] = bs.i[1]

expt.build()
expt.simulate()
