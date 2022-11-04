# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()
s = Photons(1, ['path', 'pol'], co('p1', 'H'))
hwp1 = HWP(pi / 8)
bd1 = BD(2)
hwp21 = HWP(pi / 8)
hwp22 = HWP(pi / 8)
bd2 = BD(3)
hwp31 = HWP(pi / 8)
hwp32 = HWP(pi / 8)
hwp33 = HWP(pi / 8)
bd3 = BD(4)
hwp41 = HWP(pi / 8)
hwp42 = HWP(pi / 8)
hwp43 = HWP(pi / 8)
hwp44 = HWP(pi / 8)
bd4 = BD(5)

expt.add_sources(s)
expt.add_elements(hwp1, hwp21, hwp22, hwp31, hwp32, hwp33, hwp41, hwp42, hwp43, hwp44, bd1, bd2, bd3, bd4)

s.o[0] = hwp1.i[0]
hwp1.o[0] = bd1.i[0]
bd1.o[0] = hwp21.i[0]
bd1.o[1] = hwp22.i[0]
hwp21.o[0] = bd2.i[0]
hwp22.o[0] = bd2.i[1]
bd2.o[0] = hwp31.i[0]
bd2.o[1] = hwp32.i[0]
bd2.o[2] = hwp33.i[0]
hwp31.o[0] = bd3.i[0]
hwp32.o[0] = bd3.i[1]
hwp33.o[0] = bd3.i[2]
bd3.o[0] = hwp41.i[0]
bd3.o[1] = hwp42.i[0]
bd3.o[2] = hwp43.i[0]
bd3.o[3] = hwp44.i[0]
hwp41.o[0] = bd4.i[0]
hwp42.o[0] = bd4.i[1]
hwp43.o[0] = bd4.i[2]
hwp44.o[0] = bd4.i[3]

expt.build()
expt.simulate()