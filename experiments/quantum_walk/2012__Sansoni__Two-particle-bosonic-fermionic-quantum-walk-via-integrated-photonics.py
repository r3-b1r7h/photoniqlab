# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()
s = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
bs_array = [BS() for i in range(0, 10)]

expt.add_sources(s)
expt.add_elements(*bs_array)

s.o[0] = bs_array[0].i[0]
s.o[1] = bs_array[0].i[1]
bs_array[0].o[0] = bs_array[1].i[1]
bs_array[0].o[1] = bs_array[2].i[0]
bs_array[1].o[0] = bs_array[3].i[1]
bs_array[1].o[1] = bs_array[4].i[0]
bs_array[2].o[0] = bs_array[4].i[1]
bs_array[2].o[1] = bs_array[5].i[0]
bs_array[3].o[0] = bs_array[6].i[1]
bs_array[3].o[1] = bs_array[7].i[0]
bs_array[4].o[0] = bs_array[7].i[1]
bs_array[4].o[1] = bs_array[8].i[0]
bs_array[5].o[0] = bs_array[8].i[1]
bs_array[5].o[1] = bs_array[9].i[0]

expt.build()
expt.simulate()