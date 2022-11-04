# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP, Reflection, DP

expt = Experiment()
spdc = Photons(4, ['oam', 'pol', 'path'], (co(0, 'H', 'p1') * co(0, 'H', 'p2') + co(1, 'H', 'p1') * co(-1, 'H', 'p2') + co(-1, 'H', 'p1') * co(1, 'H', 'p2')) * (co(0, 'H', 'p3') * co(0, 'H', 'p4') + co(1, 'H', 'p3') * co(-1, 'H', 'p4') + co(-1, 'H', 'p3') * co(1, 'H', 'p4')))
bs1 = BS(oam=True)
ref1 = Reflection()
dp = DP()
ref2 = Reflection()
ref3 = Reflection()
bs2 = BS(oam=True)
det = Detectors(4)

expt.add_sources(spdc)
expt.add_elements(bs1, bs2, ref1, ref2, ref3, dp)
expt.add_detectors(det)

spdc.o[1] = bs1.i[0]
spdc.o[2] = bs1.i[1]
bs1.o[0] = ref1.i[0]
ref1.o[0] = dp.i[0]
bs1.o[1] = ref2.i[0]
ref2.o[0] = ref3.i[0]
dp.o[0] = bs2.i[0]
ref3.o[0] = bs2.i[1]
spdc.o[0] = det.i[0]
spdc.o[3] = det.i[1]
bs2.o[0] = det.i[2]
bs2.o[1] = det.i[3]

expt.build()
expt.simulate()