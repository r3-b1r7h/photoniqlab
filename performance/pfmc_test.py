# -*- coding: utf-8 -*-
import random as rd
import gc
import numpy as np
import numpy.matlib
import time
from scipy.sparse import rand
from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

f = open("time_photoniqlab","w")

for i in range(1, 5):
	print(i)
	'''
	expt = Experiment()
	p_list = []
	e_list = []
	last_row = []
	for j in range(0, i):
		p_list.append(Photons(1, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') + co('p1', 'V'))))
		hwp = HWP(pi / 6)
		p_list[-1].o[0] = hwp.i[0]
		e_list.append(hwp)
		last_row.append(hwp)
	for k in range(1 - 1):  # Other i - 1 layers
		for j in range(i):  # For each row
			hwp = HWP(pi / 7)
			last_row[j].o[0] = hwp.i[0]
			last_row[j] = hwp
			e_list.append(hwp)
	expt.add_sources(*p_list)
	expt.add_elements(*e_list)
	start_time = time.clock()
	expt.build()
	expt.simulate()
	elapse = time.clock() - start_time
	f.write(str(elapse) + '\n')
	'''
	
	dim = (2*i)**(i)
	v_state = np.array([rd.random() for k in range(dim)])
	u_matrix = rand(dim, dim, density=(1/i)**i)
	#print(u_matrix)
	start_time = time.clock()
	o_state = u_matrix * v_state
	elapse = time.clock() - start_time
	f.write(str(elapse) + '\n')

f = open("time_photoniqlab'","w")

for i in range(1, 5):
	print(i)
	'''
	expt = Experiment()
	p_list = []
	e_list = []
	last_row = []
	for j in range(0, i):
		p_list.append(Photons(1, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') + co('p1', 'V'))))
		hwp = HWP(pi / 6)
		p_list[-1].o[0] = hwp.i[0]
		e_list.append(hwp)
		last_row.append(hwp)
	for k in range(1 - 1):  # Other i - 1 layers
		for j in range(i):  # For each row
			hwp = HWP(pi / 7)
			last_row[j].o[0] = hwp.i[0]
			last_row[j] = hwp
			e_list.append(hwp)
	expt.add_sources(*p_list)
	expt.add_elements(*e_list)
	start_time = time.clock()
	expt.build()
	expt.simulate()
	elapse = time.clock() - start_time
	f.write(str(elapse) + '\n')
	'''
	
	dim = (2*i)**(i)
	v_state = np.array([rd.random() for k in range(dim)])
	u_matrix = rand(dim, dim, density=(1/i)**i)
	#print(u_matrix)
	start_time = time.clock()
	o_state = u_matrix * v_state
	elapse = time.clock() - start_time
	f.write(str(elapse) + '\n')
	if i == 1:
		dim = (2*i)**(i)
		v_state = np.array([rd.random() for k in range(dim)])
		u_matrix = rand(dim, dim, density=(1/i)**i)
		#print(u_matrix)
		start_time = time.clock()
		o_state = u_matrix * v_state
		elapse = time.clock() - start_time
		f.write(str(elapse) + '\n')

