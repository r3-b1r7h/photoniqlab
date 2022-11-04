# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()
p = Photons(1, ['pol', 'path'], co('H', 'p1'))
hwp1 = HWP(pi / 8)
qwp1 = QWP(0)
s1 = BD(2)
hwp2_1 = HWP(pi / 8)
hwp2_2 = HWP(pi / 8)
s2 = BD(3)
hwp3_1 = HWP(pi / 8)
hwp3_2 = HWP(pi / 8)
hwp3_3 = HWP(pi / 8)
s3 = BD(4)
hwp4_1 = HWP(pi / 8)
hwp4_2 = HWP(pi / 8)
hwp4_3 = HWP(pi / 8)
hwp4_4 = HWP(pi / 8)
s4 = BD(5)
hwp5_1 = HWP(pi / 8)
hwp5_2 = HWP(pi / 8)
hwp5_3 = HWP(pi / 8)
hwp5_4 = HWP(pi / 8)
hwp5_5 = HWP(pi / 8)
s5 = BD(6)
hwp6_1 = HWP(pi / 8)
hwp6_2 = HWP(pi / 8)
hwp6_3 = HWP(pi / 8)
hwp6_4 = HWP(pi / 8)
hwp6_5 = HWP(pi / 8)
hwp6_6 = HWP(pi / 8)
s6 = BD(7)

expt.add_sources(p)
expt.add_elements(hwp1, qwp1, s1, hwp2_1, hwp2_2, s2, hwp3_1, hwp3_2, hwp3_3, s3, hwp4_1, hwp4_2, hwp4_3, hwp4_4, s4, hwp5_1, hwp5_2, hwp5_3, hwp5_4, hwp5_5, s5, hwp6_1, hwp6_2, hwp6_3, hwp6_4, hwp6_5, hwp6_6, s6)

p.o[0] = hwp1.i[0]
hwp1.o[0] = qwp1.i[0]
qwp1.o[0] = s1.i[0]
s1.o[0] = hwp2_1.i[0]
s1.o[1] = hwp2_2.i[0]
hwp2_1.o[0] = s2.i[0]
hwp2_2.o[0] = s2.i[1]
s2.o[0] = hwp3_1.i[0]
s2.o[1] = hwp3_2.i[0]
s2.o[2] = hwp3_3.i[0]
hwp3_1.o[0] = s3.i[0]
hwp3_2.o[0] = s3.i[1]
hwp3_3.o[0] = s3.i[2]
s3.o[0] = hwp4_1.i[0]
s3.o[1] = hwp4_2.i[0]
s3.o[2] = hwp4_3.i[0]
s3.o[3] = hwp4_4.i[0]
hwp4_1.o[0] = s4.i[0]
hwp4_2.o[0] = s4.i[1]
hwp4_3.o[0] = s4.i[2]
hwp4_4.o[0] = s4.i[3]
s4.o[0] = hwp5_1.i[0]
s4.o[1] = hwp5_2.i[0]
s4.o[2] = hwp5_3.i[0]
s4.o[3] = hwp5_4.i[0]
s4.o[4] = hwp5_5.i[0]
hwp5_1.o[0] = s5.i[0]
hwp5_2.o[0] = s5.i[1]
hwp5_3.o[0] = s5.i[2]
hwp5_4.o[0] = s5.i[3]
hwp5_5.o[0] = s5.i[4]
s5.o[0] = hwp6_1.i[0]
s5.o[1] = hwp6_2.i[0]
s5.o[2] = hwp6_3.i[0]
s5.o[3] = hwp6_4.i[0]
s5.o[4] = hwp6_5.i[0]
s5.o[5] = hwp6_6.i[0]
hwp6_1.o[0] = s6.i[0]
hwp6_2.o[0] = s6.i[1]
hwp6_3.o[0] = s6.i[2]
hwp6_4.o[0] = s6.i[3]
hwp6_5.o[0] = s6.i[4]
hwp6_6.o[0] = s6.i[5]

expt.build()
expt.simulate()