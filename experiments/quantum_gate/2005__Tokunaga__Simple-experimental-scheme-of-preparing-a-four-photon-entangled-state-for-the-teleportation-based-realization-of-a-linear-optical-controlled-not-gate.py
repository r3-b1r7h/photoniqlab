# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Element, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

alpha, beta = symbols('alpha beta')
delta, gamma = symbols('delta gamma')

class TMaker(Element):
    def __init__(self):
        u = {co('H'): alpha * co('H') + beta * co('V')}
        dofs = ['pol']
        Element.__init__(self, 1, dofs, u)
        self.label = 'CMaker'

class CMaker(Element):
    def __init__(self):
        u = {co('H'): delta * co('H') + gamma * co('V')}
        dofs = ['pol']
        Element.__init__(self, 1, dofs, u)
        self.label = 'TMaker'

expt = Experiment()
x = Photons(4, ['path', 'pol'], 0.5 * ((co('p1', 'H') * co('p2', 'H') + co('p1', 'V') * co('p2', 'V')) * co('p3', 'H') * co('p4', 'H') + (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')) * co('p3', 'V') * co('p4', 'V')))
pbs_l = PBS()
pbs_r = PBS()
pbs_1 = PBS()
pbs_2 = PBS()
pbs_3 = PBS()
pbs_4 = PBS()
hwp1 = HWP(pi / 4)
hwp2 = HWP(pi / 4)
hwp3 = HWP(pi / 4)
hwp4 = HWP(pi / 4)
bs_l = BS()
bs_r = BS()
cmaker1 = CMaker()
cmaker2 = CMaker()
tmaker1 = TMaker()
tmaker2 = TMaker()
det = Detectors(4)
expt.add_sources(x)
expt.add_elements(pbs_l, pbs_r, pbs_1, pbs_2, pbs_3, pbs_4, hwp1, hwp2, hwp3, hwp4, bs_l, bs_r, cmaker1, cmaker2, tmaker1, tmaker2)
expt.add_detectors(det)

x.o[0] = pbs_l.i[0]
x.o[3] = pbs_r.i[0]
pbs_l.o[0] = hwp1.i[0]
pbs_r.o[0] = hwp3.i[0]
pbs_l.o[1] = tmaker1.i[0]
hwp1.o[0] = tmaker2.i[0]
pbs_r.o[1] = cmaker1.i[0]
hwp3.o[0] = cmaker2.i[0]
tmaker2.o[0] = hwp2.i[0]
cmaker2.o[0] = hwp4.i[0]
tmaker1.o[0] = bs_l.i[0]
hwp2.o[0] = bs_l.i[1]
cmaker1.o[0] = bs_r.i[0]
hwp4.o[0] = bs_r.i[1]
bs_l.o[0] = pbs_1.i[0]
bs_l.o[1] = pbs_2.i[0]
bs_r.o[0] = pbs_3.i[0]
bs_r.o[1] = pbs_4.i[0]
pbs_1.o[1] = det.i[0]
pbs_3.o[1] = det.i[1]
x.o[1] = det.i[2]
x.o[2] = det.i[3]

expt.build()
expt.simulate()