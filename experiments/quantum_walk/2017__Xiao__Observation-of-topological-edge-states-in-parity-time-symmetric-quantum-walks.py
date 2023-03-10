# -*- coding: utf-8 -*-

from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Detectors, BD, BS, HWP, PBS, POL, PS, QWP

expt = Experiment()
s = Photons(1, ['path', 'pol'], (co('p1', 'H') + I * co('p1', 'V')) / sqrt(2))
# step 1
hwp1 = HWP(pi / 3)
bd1 = BD(2)
hwp21 = HWP(pi / 8)
hwp22 = HWP(pi / 8)
bd2 = BD(3)
# step 2
hwp31 = HWP(pi / 3)
hwp32 = HWP(pi / 3)
hwp33 = HWP(pi / 3)
bd3 = BD(4)
hwp41 = HWP(pi / 8)
hwp42 = HWP(pi / 8)
hwp43 = HWP(pi / 8)
hwp44 = HWP(pi / 8)
bd4 = BD(5)
# step 3
hwp51 = HWP(pi / 3)
hwp52 = HWP(pi / 3)
hwp53 = HWP(pi / 3)
hwp54 = HWP(pi / 3)
hwp55 = HWP(pi / 3)
bd5 = BD(6)
hwp61 = HWP(pi / 8)
hwp62 = HWP(pi / 8)
hwp63 = HWP(pi / 8)
hwp64 = HWP(pi / 8)
hwp65 = HWP(pi / 8)
hwp66 = HWP(pi / 8)
bd6 = BD(7)
# step 4
hwp71 = HWP(pi / 3)
hwp72 = HWP(pi / 3)
hwp73 = HWP(pi / 3)
hwp74 = HWP(pi / 3)
hwp75 = HWP(pi / 3)
hwp76 = HWP(pi / 3)
hwp77 = HWP(pi / 3)
bd7 = BD(8)
hwp81 = HWP(pi / 8)
hwp82 = HWP(pi / 8)
hwp83 = HWP(pi / 8)
hwp84 = HWP(pi / 8)
hwp85 = HWP(pi / 8)
hwp86 = HWP(pi / 8)
hwp87 = HWP(pi / 8)
hwp88 = HWP(pi / 8)
bd8 = BD(9)
# step 5
hwp91 = HWP(pi / 3)
hwp92 = HWP(pi / 3)
hwp93 = HWP(pi / 3)
hwp94 = HWP(pi / 3)
hwp95 = HWP(pi / 3)
hwp96 = HWP(pi / 3)
hwp97 = HWP(pi / 3)
hwp98 = HWP(pi / 3)
hwp99 = HWP(pi / 3)
bd9 = BD(10)
hwp101 = HWP(pi / 8)
hwp102 = HWP(pi / 8)
hwp103 = HWP(pi / 8)
hwp104 = HWP(pi / 8)
hwp105 = HWP(pi / 8)
hwp106 = HWP(pi / 8)
hwp107 = HWP(pi / 8)
hwp108 = HWP(pi / 8)
hwp109 = HWP(pi / 8)
hwp1010 = HWP(pi / 8)
bd10 = BD(11)
# step 6
hwp111 = HWP(pi / 3)
hwp112 = HWP(pi / 3)
hwp113 = HWP(pi / 3)
hwp114 = HWP(pi / 3)
hwp115 = HWP(pi / 3)
hwp116 = HWP(pi / 3)
hwp117 = HWP(pi / 3)
hwp118 = HWP(pi / 3)
hwp119 = HWP(pi / 3)
hwp1110 = HWP(pi / 3)
hwp1111 = HWP(pi / 3)
bd11 = BD(12)
hwp121 = HWP(pi / 8)
hwp122 = HWP(pi / 8)
hwp123 = HWP(pi / 8)
hwp124 = HWP(pi / 8)
hwp125 = HWP(pi / 8)
hwp126 = HWP(pi / 8)
hwp127 = HWP(pi / 8)
hwp128 = HWP(pi / 8)
hwp129 = HWP(pi / 8)
hwp1210 = HWP(pi / 8)
hwp1211 = HWP(pi / 8)
hwp1212 = HWP(pi / 8)
bd12 = BD(13)
expt.add_sources(s)
expt.add_elements(hwp1, hwp21, hwp22, hwp31, hwp32, hwp33, hwp41, hwp42, hwp43, hwp44, hwp51, hwp52, hwp53, hwp54, hwp55, hwp61, hwp62, hwp63, hwp64, hwp65, hwp66, hwp71, hwp72, hwp73, hwp74, hwp75, hwp76, hwp77, hwp81, hwp82, hwp83, hwp84, hwp85, hwp86, hwp87, hwp88, hwp91, hwp92, hwp93, hwp94, hwp95, hwp96, hwp97, hwp98, hwp99, hwp101, hwp102, hwp103, hwp104, hwp105, hwp106, hwp107, hwp108, hwp109, hwp1010, hwp111, hwp112, hwp113, hwp114, hwp115, hwp116, hwp117, hwp118, hwp119, hwp1110, hwp1111, hwp121, hwp122, hwp123, hwp124, hwp125, hwp126, hwp127, hwp128, hwp129, hwp1210, hwp1211, hwp1212, bd1, bd2, bd3, bd4, bd5, bd6, bd7, bd8, bd9, bd10, bd11, bd12)

s.o[0] = hwp1.i[0]
hwp1.o[0] = bd1.i[0]
bd1.o[0] = hwp21.i[0]
bd1.o[1] = hwp22.i[0]
hwp21.o[0] = bd2.i[0]
hwp22.o[0] = bd2.i[1]
bd2.o[0] = hwp31.i[0]
bd2.o[1] = hwp32.i[0]
bd2.o[2] = hwp33.i[0]
hwp31.o[0] = bd3.i[0]
hwp32.o[0] = bd3.i[1]
hwp33.o[0] = bd3.i[2]
bd3.o[0] = hwp41.i[0]
bd3.o[1] = hwp42.i[0]
bd3.o[2] = hwp43.i[0]
bd3.o[3] = hwp44.i[0]
hwp41.o[0] = bd4.i[0]
hwp42.o[0] = bd4.i[1]
hwp43.o[0] = bd4.i[2]
hwp44.o[0] = bd4.i[3]
bd4.o[0] = hwp51.i[0]
bd4.o[1] = hwp52.i[0]
bd4.o[2] = hwp53.i[0]
bd4.o[3] = hwp54.i[0]
bd4.o[4] = hwp55.i[0]
hwp51.o[0] = bd5.i[0]
hwp52.o[0] = bd5.i[1]
hwp53.o[0] = bd5.i[2]
hwp54.o[0] = bd5.i[3]
hwp55.o[0] = bd5.i[4]
bd5.o[0] = hwp61.i[0]
bd5.o[1] = hwp62.i[0]
bd5.o[2] = hwp63.i[0]
bd5.o[3] = hwp64.i[0]
bd5.o[4] = hwp65.i[0]
bd5.o[5] = hwp66.i[0]
hwp61.o[0] = bd6.i[0]
hwp62.o[0] = bd6.i[1]
hwp63.o[0] = bd6.i[2]
hwp64.o[0] = bd6.i[3]
hwp65.o[0] = bd6.i[4]
hwp66.o[0] = bd6.i[5]
bd6.o[0] = hwp71.i[0]
bd6.o[1] = hwp72.i[0]
bd6.o[2] = hwp73.i[0]
bd6.o[3] = hwp74.i[0]
bd6.o[4] = hwp75.i[0]
bd6.o[5] = hwp76.i[0]
bd6.o[6] = hwp77.i[0]
hwp71.o[0] = bd7.i[0]
hwp72.o[0] = bd7.i[1]
hwp73.o[0] = bd7.i[2]
hwp74.o[0] = bd7.i[3]
hwp75.o[0] = bd7.i[4]
hwp76.o[0] = bd7.i[5]
hwp77.o[0] = bd7.i[6]
bd7.o[0] = hwp81.i[0]
bd7.o[1] = hwp82.i[0]
bd7.o[2] = hwp83.i[0]
bd7.o[3] = hwp84.i[0]
bd7.o[4] = hwp85.i[0]
bd7.o[5] = hwp86.i[0]
bd7.o[6] = hwp87.i[0]
bd7.o[7] = hwp88.i[0]
hwp81.o[0] = bd8.i[0]
hwp82.o[0] = bd8.i[1]
hwp83.o[0] = bd8.i[2]
hwp84.o[0] = bd8.i[3]
hwp85.o[0] = bd8.i[4]
hwp86.o[0] = bd8.i[5]
hwp87.o[0] = bd8.i[6]
hwp88.o[0] = bd8.i[7]
bd8.o[0] = hwp91.i[0]
bd8.o[1] = hwp92.i[0]
bd8.o[2] = hwp93.i[0]
bd8.o[3] = hwp94.i[0]
bd8.o[4] = hwp95.i[0]
bd8.o[5] = hwp96.i[0]
bd8.o[6] = hwp97.i[0]
bd8.o[7] = hwp98.i[0]
bd8.o[8] = hwp99.i[0]
hwp91.o[0] = bd9.i[0]
hwp92.o[0] = bd9.i[1]
hwp93.o[0] = bd9.i[2]
hwp94.o[0] = bd9.i[3]
hwp95.o[0] = bd9.i[4]
hwp96.o[0] = bd9.i[5]
hwp97.o[0] = bd9.i[6]
hwp98.o[0] = bd9.i[7]
hwp99.o[0] = bd9.i[8]
bd9.o[0] = hwp101.i[0]
bd9.o[1] = hwp102.i[0]
bd9.o[2] = hwp103.i[0]
bd9.o[3] = hwp104.i[0]
bd9.o[4] = hwp105.i[0]
bd9.o[5] = hwp106.i[0]
bd9.o[6] = hwp107.i[0]
bd9.o[7] = hwp108.i[0]
bd9.o[8] = hwp109.i[0]
bd9.o[9] = hwp1010.i[0]
hwp101.o[0] = bd10.i[0]
hwp102.o[0] = bd10.i[1]
hwp103.o[0] = bd10.i[2]
hwp104.o[0] = bd10.i[3]
hwp105.o[0] = bd10.i[4]
hwp106.o[0] = bd10.i[5]
hwp107.o[0] = bd10.i[6]
hwp108.o[0] = bd10.i[7]
hwp109.o[0] = bd10.i[8]
hwp1010.o[0] = bd10.i[9]
bd10.o[0] = hwp111.i[0]
bd10.o[1] = hwp112.i[0]
bd10.o[2] = hwp113.i[0]
bd10.o[3] = hwp114.i[0]
bd10.o[4] = hwp115.i[0]
bd10.o[5] = hwp116.i[0]
bd10.o[6] = hwp117.i[0]
bd10.o[7] = hwp118.i[0]
bd10.o[8] = hwp119.i[0]
bd10.o[9] = hwp1110.i[0]
bd10.o[10] = hwp1111.i[0]
hwp111.o[0] = bd11.i[0]
hwp112.o[0] = bd11.i[1]
hwp113.o[0] = bd11.i[2]
hwp114.o[0] = bd11.i[3]
hwp115.o[0] = bd11.i[4]
hwp116.o[0] = bd11.i[5]
hwp117.o[0] = bd11.i[6]
hwp118.o[0] = bd11.i[7]
hwp119.o[0] = bd11.i[8]
hwp1110.o[0] = bd11.i[9]
hwp1111.o[0] = bd11.i[10]
bd11.o[0] = hwp121.i[0]
bd11.o[1] = hwp122.i[0]
bd11.o[2] = hwp123.i[0]
bd11.o[3] = hwp124.i[0]
bd11.o[4] = hwp125.i[0]
bd11.o[5] = hwp126.i[0]
bd11.o[6] = hwp127.i[0]
bd11.o[7] = hwp128.i[0]
bd11.o[8] = hwp129.i[0]
bd11.o[9] = hwp1210.i[0]
bd11.o[10] = hwp1211.i[0]
bd11.o[11] = hwp1212.i[0]
hwp121.o[0] = bd12.i[0]
hwp122.o[0] = bd12.i[1]
hwp123.o[0] = bd12.i[2]
hwp124.o[0] = bd12.i[3]
hwp125.o[0] = bd12.i[4]
hwp126.o[0] = bd12.i[5]
hwp127.o[0] = bd12.i[6]
hwp128.o[0] = bd12.i[7]
hwp129.o[0] = bd12.i[8]
hwp1210.o[0] = bd12.i[9]
hwp1211.o[0] = bd12.i[10]
hwp1212.o[0] = bd12.i[11]

expt.build()
expt.simulate()