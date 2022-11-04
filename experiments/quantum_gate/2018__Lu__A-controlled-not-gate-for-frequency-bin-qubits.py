# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP, Reflection, DP, LI, Hologram, EOM, PulseShaper

expt = Experiment()
omega0 = 193450
delta = 25

a, b, c, d, t = symbols('a b c d t')
#p = Photons(1, ['freq', 'path'], a * co(omega0, 'p1') * co(omega0 + 7 * delta, 'p1') + b * co(omega0, 'p1') * co(omega0 + 8 * delta, 'p1') + c * co(omega0 + 6 * delta, 'p1') * co(omega0 + 7 * delta, 'p1') + d * co(omega0 + 6 * delta, 'p1') * co(omega0 + 8 * delta, 'p1'))
p = Photons(1, ['freq', 'path'], co(omega0 + 6 * delta, 'p1') * co(omega0 + 8 * delta, 'p1'))

eom1 = EOM(delta=delta, phi_t=-2*sin(50 * pi * t), bandwidth=13)
print(eom1.get_u(['freq']))
shaper = PulseShaper({omega0 - 7 * delta: -0.0786 * pi, omega0 - 6 * delta: -0.07583 * pi, omega0 - 4 * delta: -0.0562 * pi, omega0 - 3 * delta: -0.1292 * pi, omega0 - 2 * delta: -0.1686 * pi, omega0 - delta: -0.185 * pi, omega0: -0.185 * pi, omega0 + delta: 0.309 * pi, omega0 + 2 * delta: 0.7864 * pi, omega0 + 3 * delta: 0.5336 * pi, omega0 + 4 * delta: 0.2106 * pi, omega0 + 5 * delta: -0.4915 * pi, omega0 + 6 * delta: -0.4634 * pi, omega0 + 7 * delta: 0.2528 * pi, omega0 + 8 * delta: 0.1826 * pi, omega0 + 9 * delta: -0.6039 * pi, omega0 + 10 * delta: -0.3932 * pi, omega0 + 11 * delta: -0.2303 * pi, omega0 + 12 * delta: -0.1686 * pi, omega0 + 13 * delta: -0.1264 * pi})
print(shaper.get_u(['freq']))
eom2 = EOM(delta=delta, phi_t=2*sin(50 * pi * t), bandwidth=13)

expt.add_sources(p)
expt.add_elements(eom1, shaper, eom2)

p.o[0] = eom1.i[0]
eom1.o[0] = shaper.i[0]
shaper.o[0] = eom2.i[0]

expt.build()
expt.simulate()

# -0.134228006922019 + 0.16362845319646*I |10>