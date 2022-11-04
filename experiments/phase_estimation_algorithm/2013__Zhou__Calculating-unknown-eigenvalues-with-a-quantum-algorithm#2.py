# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()

s = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
pbs = PBS()
bs = BS(0.5)
hwp_h = HWP(pi / 8)
hwp_v = HWP(3 * pi / 8)
qwp_h = QWP(0)
qwp_v = QWP(0)

uhhwp1 = HWP(0)
uhhwp2 = HWP(pi / 4)
uhhwp3 = HWP(0)
uhhwp4 = HWP(pi / 4)

qwp_r1 = QWP(-pi / 4)
hwp_r = HWP(0)
qwp_r2 = QWP(-pi / 4)
hwp_c = HWP(pi / 8)
pbs_c = PBS()

det = Detectors(2)

expt.add_sources(s)
expt.add_elements(pbs, bs, hwp_h, hwp_v, qwp_h, qwp_v, uhhwp1, uhhwp2, uhhwp3, uhhwp4, qwp_r1, hwp_r, qwp_r2, hwp_c, pbs_c)
expt.add_detectors(det)

s.o[0] = qwp_r1.i[0]
qwp_r1.o[0] = hwp_r.i[0]
hwp_r.o[0] = qwp_r2.i[0]
qwp_r2.o[0] = hwp_c.i[0]
hwp_c.o[0] = pbs_c.i[0]
pbs_c.o[1] = det.i[0]

s.o[1] = pbs.i[0]
pbs.o[1] = hwp_h.i[0]
pbs.o[0] = hwp_v.i[0]
hwp_h.o[0] = qwp_h.i[0]
hwp_v.o[0] = qwp_v.i[0]
qwp_h.o[0] = uhhwp1.i[0]
uhhwp1.o[0] = uhhwp2.i[0]
uhhwp2.o[0] = uhhwp3.i[0]
uhhwp3.o[0] = uhhwp4.i[0]

qwp_v.o[0] = bs.i[0]
uhhwp4.o[0] = bs.i[1]
bs.o[0] = det.i[1]

expt.build()
expt.simulate()