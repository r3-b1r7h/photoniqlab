# PhotoniQLAB

PhotoniQLAB is an open-source object-oriented Python framework for simulating photonic quantum information processing (PQIP) experiments.

The directory structure of the project is shown as follows.

```bash
photoniqlab
 ©À©¤experiments.............................Usage cases covering various fields
 ©À©¤performance.............................Code for performance tests
 ©À©¤photoniqlab.............................Source code of PhotoniQLAB
 ©¸©¤test....................................Code for unit tests
```
## Instructions

### Installation

You can install our package by the following command.
```bash
pip3 install photoniqlab-1.0.tar.gz
```

### Usage

To get started with PhotoniQLAB to simulate a PQIP experiment, you need to create a Python script, e.g. `yourscript.py`, and describe the target PQIP experiment according to the step-by-step tutorial shown in our manuscript. Here we suppose the target PQIP experiment is for 4-photon entangled state generation.

The PhotoniQLAB code is shown as follows.

```python
# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC

expt = Experiment()
a = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
b = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * (co('p1', 'H') * co('p2', 'V') + co('p1', 'V') * co('p2', 'H')))
pbs = PBS()
det = Detectors(4)
expt.add_sources(a, b)
expt.add_elements(pbs)
expt.add_detectors(det)

a.o[0] = pbs.i[0]
b.o[0] = pbs.i[1]
a.o[1] = det.i[0]
b.o[1] = det.i[1]
pbs.o[0] = det.i[2]
pbs.o[1] = det.i[3]

expt.build()
expt.simulate()
```

You can run the Python script to conduct the simulation by the following command.
```bash
python yourscript.py
```

After the simulation process finished, you can get some output pdf files containing the simulation results. The content of each file is described by the following table.

| File name | Description                    |
| ------------- | ------------------------------ |
| `init_state.pdf` | The initial state of the network |
| `after_layerX.pdf`   | The quantum state after X layers |
| `post_selected.pdf`   | The quantum state after post selection |
| `experiment.pdf`   | The schemadic diagram of the network |