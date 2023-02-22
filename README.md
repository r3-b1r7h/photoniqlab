# PhotoniQLAB

PhotoniQLAB is an open-source object-oriented Python framework for simulating photonic quantum information processing (PQIP) experiments.

The directory structure of the project is shown as follows.

```
- photoniqlab
-- experiments.......Usage cases covering various fields
-- performance.......Code for performance tests
-- photoniqlab.......Source code of PhotoniQLAB
-- test..............Code for unit tests
```

## Installation

You can install our package by the following command under a Python 3.6 environment.

```bash
pip install -e .
```

## Usage

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

### Quantum Bernoulli factory PQIP experiment

The experiment setup of the quantum Bernoulli factory (multiplication operation) PQIP implementation (see <https://doi.org/10.1088/2058-9565/ac2061>) is shown as follows.

![quantum Bernoulli factory PQIP experiment](2023-02-21-16-59-00.png)

The PhotoniQLAB code for simulate this experiment is shown as follows.

```python
# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()

p = Photons(2, ['path', 'pol'], (1 / sqrt(2)) * co('p1', 'H') * co('p2', 'H') + (1 / sqrt(2)) * co('p1', 'V') * co('p2', 'V'))

pbs_1 = PBS()
pbs_2 = PBS()
bs_1 = BS()
bs_2 = BS()

hwp_1t = HWP(pi/4)
qwp_1t = QWP(0)
pol_1t = POL(0)

# h2 == 0
hwp_1r = HWP(pi/2)
qwp_1r = QWP(pi/2)
pol_1r = POL(pi/2)

hwp_2t = HWP(pi/4)
qwp_2t = QWP(0)

# h2 == 0
hwp_2r = HWP(pi/2)
qwp_2r = QWP(pi/2)
X = HWP(pi/4)  # B is X while A == C == I

pol_H = POL(0)
det = Detectors(2)

expt.add_sources(p)
expt.add_elements(pbs_1, pbs_2, bs_1, bs_2, hwp_1t, qwp_1t, pol_1t, hwp_1r, qwp_1r, pol_1r, hwp_2t, qwp_2t, hwp_2r, qwp_2r, X, pol_H)
expt.add_detectors(det)

p.o[0] = pbs_1.i[0]

pbs_1.o[0] = hwp_1r.i[0]
hwp_1r.o[0] = qwp_1r.i[0]
qwp_1r.o[0] = pol_1r.i[0]

pbs_1.o[1] = hwp_1t.i[0]
hwp_1t.o[0] = qwp_1t.i[0]
qwp_1t.o[0] = pol_1t.i[0]

pol_1r.o[0] = bs_1.i[0]
pol_1t.o[0] = bs_1.i[1]

bs_1.o[0] = det.i[0]

p.o[1] = pbs_2.i[0]

pbs_2.o[0] = hwp_2r.i[0]
hwp_2r.o[0] = qwp_2r.i[0]
qwp_2r.o[0] = X.i[0]
X.o[0] = bs_2.i[0]

pbs_2.o[1] = hwp_2t.i[0]
hwp_2t.o[0] = qwp_2t.i[0]
qwp_2t.o[0] = bs_2.i[1]

bs_2.o[0] = pol_H.i[0]
pol_H.o[0] = det.i[1]

expt.build()
expt.simulate()
```

PhotoniQLAB draws a schematic diagram of the experiment setup to help you debug your description.

![quantum Bernoulli factory PhotoniQLAB diagram](2023-02-22-15-07-32.png)

PhotoniQLAB outputs the final quantum state of this experiment into a PDF file by the representation of creative operators, from which we can verify $\ket{h_1, 0}$ has been turned into $\ket{h_1 \cdot 0}$.

![final state](2023-02-22-15-09-50.png)

## Citation

If PhotoniQLAB helps you in your research, please cite our paper:

```
@article{Wu_2021,
doi = {10.1088/2058-9565/abc1ba},
url = {https://dx.doi.org/10.1088/2058-9565/abc1ba},
year = {2021},
month = {jan},
publisher = {IOP Publishing},
volume = {6},
number = {2},
pages = {024001},
author = {Zhihao Wu and Junjie Wu and Anqi Huang},
title = {PhotoniQLAB: a framework for simulating photonic quantum information processing experiments},
journal = {Quantum Science and Technology}
}
```

## License

This project is under apache 2.0 license.
