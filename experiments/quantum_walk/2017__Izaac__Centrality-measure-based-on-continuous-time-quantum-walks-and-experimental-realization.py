# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()
s = Photons(1, ['path', 'pol'], co('p1', 'H'))
hwpa = HWP(pi / 8)
hwpb = HWP(-pi / 8)
hwpc = HWP(pi / 8)

Ru1 = HWP(0)
Ru2 = HWP(N((48.4/180), 2) * pi)
Ru3 = QWP(pi / 2)
Rd1 = HWP(0)
Rd2 = QWP(pi / 8)
Rd3 = QWP(pi / 8)

Lu1 = QWP(pi / 2)
Lu2 = HWP(0)
Lu3 = HWP(N((-3.3/180), 2) * pi)
Ld1 = HWP(pi / 2)
Ld2 = HWP(0)
Ld3 = HWP(N((157.5/180), 2) * pi)

hwp11 = HWP(N((54.1/180), 2) * pi)
hwp12 = HWP(N((54.1/180), 2) * pi)
hwp2 = HWP(N((144.1/180), 2) * pi)
hwp31 = HWP(-pi / 4)
hwp32 = HWP(-pi / 4)
hwp4 = HWP(-pi / 4)
hwp51 = HWP(-pi / 4)
hwp52 = HWP(-pi / 4)
hwp6 = HWP(pi / 4)

bd1 = BD(2, True)
bd2 = BD(3, True)
bd3 = BD(4, True)
expt.add_sources(s)
expt.add_elements(bd1, bd2, bd3, hwpa, hwpb, hwpc, Ru1, Ru2, Ru3, Rd1, Rd2, Rd3, Lu1, Lu2, Lu3, Ld1, Ld2, Ld3, hwp11, hwp12, hwp2, hwp31, hwp32, hwp4, hwp51, hwp52, hwp6)

s.o[0] = hwpa.i[0]
hwpa.o[0] = bd1.i[0]
bd1.o[0] = hwpb.i[0]
bd1.o[1] = hwpc.i[0]
hwpb.o[0] = Ru1.i[0]
Ru1.o[0] = Ru2.i[0]
Ru2.o[0] = Ru3.i[0]
hwpc.o[0] = Rd1.i[0]
Rd1.o[0] = Rd2.i[0]
Rd2.o[0] = Rd3.i[0]
Ru3.o[0] = bd2.i[0]
Rd3.o[0] = bd2.i[1]
bd2.o[0] = hwp11.i[0]
bd2.o[1] = hwp12.i[0]
bd2.o[2] = hwp4.i[0]
hwp11.o[0] = hwp2.i[0]
hwp12.o[0] = hwp51.i[0]
hwp4.o[0] = hwp52.i[0]
hwp2.o[0] = hwp31.i[0]
hwp51.o[0] = hwp32.i[0]
hwp52.o[0] = hwp6.i[0]
hwp31.o[0] = bd3.i[0]
hwp32.o[0] = bd3.i[1]
hwp6.o[0] = bd3.i[2]
bd3.o[1] = Lu1.i[0]
bd3.o[2] = Ld1.i[0]
Lu1.o[0] = Lu2.i[0]
Ld1.o[0] = Ld2.i[0]
Lu2.o[0] = Lu3.i[0]
Ld2.o[0] = Ld3.i[0]

expt.build()
expt.simulate()
