# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP, Reflection, DP, LI, Hologram, EOM, PulseShaper

expt = Experiment()
omega0 = 193600
delta = 25

a, b, c, d, t = symbols('a b c d t')
#p = Photons(1, ['freq', 'path'], a * co(omega0, 'p1') * co(omega0 + 7 * delta, 'p1') + b * co(omega0, 'p1') * co(omega0 + 8 * delta, 'p1') + c * co(omega0 + 6 * delta, 'p1') * co(omega0 + 7 * delta, 'p1') + d * co(omega0 + 6 * delta, 'p1') * co(omega0 + 8 * delta, 'p1'))
p = Photons(1, ['freq', 'path'], co(omega0, 'p1') * co(omega0 + 1 * delta, 'p1'))

eom1 = EOM(delta=delta, phi_t=0.8169*sin(50 * pi * t), bandwidth=13)
shaper = PulseShaper({omega0 + i * delta: pi for i in range(1, 13)})
eom2 = EOM(delta=delta, phi_t=-0.8169*sin(50 * pi * t), bandwidth=13)

expt.add_sources(p)
expt.add_elements(eom1, shaper, eom2)

p.o[0] = eom1.i[0]
eom1.o[0] = shaper.i[0]
shaper.o[0] = eom2.i[0]

expt.build()
expt.simulate()

# - 0.4879 |00> + 0.4879 |11>