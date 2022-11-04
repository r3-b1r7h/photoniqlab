# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, Element, BD, BS, HWP, PBS, POL, PS, QWP

class H2V(Element):
    def __init__(self):
        u = {co('H'): co('V')}
        dofs = ['pol']
        Element.__init__(self, 1, dofs, u)
        self.label = 'H2V'

u, v = symbols('u v')
expt = Experiment()

b = Photons(1, ['pol', 'path'], u * co('H', 'p1') + v * co('V', 'p1'))
r1 = Photons(1, ['pol', 'path'], co('H', 'p1'))
r2 = Photons(1, ['pol', 'path'], co('H', 'p1'))
a = Photons(1, ['pol', 'path'], co('H', 'p1'))

pbs3 = PBS()
pbs4 = PBS()
pbs5 = PBS()
pbs6 = PBS()
pbs66 = PBS()
hwp1 = HWP(pi / 8)
hwp2 = HWP(pi / 8)
hwp3 = HWP(pi / 8)
hwp4 = HWP(pi / 8)
x = HWP(pi / 4)
hdmd = HWP(pi / 8)
h16 = HWP(pi / 16)
h8 = HWP(pi / 8)
pol_a = POL(pi / 4)
v2h = HWP(pi / 4)
h2v = H2V()

hdmd_r2 = HWP(pi / 8)
hdmd_r1 = HWP(pi / 8)
pol_r2 = POL(0)
pol_r1 = POL(0)
det = Detectors(4)
expt.add_sources(b, r1, r2, a)
expt.add_elements(hdmd_r2, hdmd_r1, pol_r2, pol_r1, v2h, h2v, pol_a, h16, h8, pbs3, pbs4, pbs5, pbs6, pbs66, hwp1, hwp2, hwp3, hwp4, hdmd, x)
expt.add_detectors(det)

b.o[0] = hwp1.i[0]
r1.o[0] = hwp2.i[0]
r2.o[0] = hwp3.i[0]
a.o[0] = hwp4.i[0]
hwp1.o[0] = pbs3.i[0]
hwp2.o[0] = pbs3.i[1]
hwp3.o[0] = pbs5.i[0]
hwp4.o[0] = pbs5.i[1]
pbs3.o[1] = pbs4.i[0]
pbs5.o[0] = pbs4.i[1]

pbs3.o[0] = hdmd.i[0]
pbs4.o[0] = x.i[0]

pbs5.o[1] = pbs6.i[0]
pbs6.o[0] = v2h.i[0]
v2h.o[0] = h16.i[0]
pbs6.o[1] = h8.i[0]
h16.o[0] = pbs66.i[0]
h8.o[0] = pbs66.i[1]
pbs66.o[0] = h2v.i[0]

'''h2v.o[0] = det.i[0]
pbs4.o[1] = det.i[1]
hdmd.o[0] = det.i[2]
x.o[0] = det.i[3]'''

h2v.o[0] = pol_a.i[0]
pbs4.o[1] = hdmd_r2.i[0]
x.o[0] = hdmd_r1.i[0]
hdmd_r2.o[0] = pol_r2.i[0]
hdmd_r1.o[0] = pol_r1.i[0]
pol_a.o[0] = det.i[0]
pol_r2.o[0] = det.i[1]
pol_r1.o[0] = det.i[2]
hdmd.o[0] = det.i[3]
expt.build()
expt.simulate()