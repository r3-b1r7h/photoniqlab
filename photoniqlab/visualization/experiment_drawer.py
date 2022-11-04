# -*- coding: utf-8 -*-

"""Experiment visualization by matplotlib."""

import numpy as np
from matplotlib import patches
import matplotlib.lines as lines
from matplotlib import pyplot

#from photoniqlab.sympy_widget import *
from photoniqlab import Experiment, Photons, Element, Detectors, BD, BS, HWP, PBS, PDBS, PBSFS, POL, PS, QWP, BC, Reflection, LI, Hologram, DP, EOM, PulseShaper
from photoniqlab.exceptions import PhotoniqlabError

COL_WIDTH = 6
ROW_HEIGHT = 3
COMP_SIZE = 2
DOT_RADIUS = 0.05

TEXT_ORDER = 100
COMP_ORDER = 99
BLOCKER_ORDER = 98
class ExperimentDrawer:
    def __init__(self, experiment, all_paths, path_mapping):
        self.__experiment = experiment
        self.__sources = experiment.sources
        self.__layers = experiment.layers
        self.__detectors = experiment.detectors
        self.__result = experiment.result
        self.__dofs = experiment.total_dofs
        # Detectors must in these paths...
        self.__all_paths = all_paths
        self.__path_mapping = path_mapping
        self.figure = pyplot.figure(figsize=[10,10])
        self.figure.patch.set_facecolor(color='white')
        self.ax = self.figure.add_subplot(111)
        self.ax.axis('off')
        self.ax.set_aspect('equal')
        self.ax.tick_params(labelbottom=False, labeltop=False,
                            labelleft=False, labelright=False)

        self.__styles_cycle = [['dodgerblue', 2, 50], ['lightsalmon', 6, 49], ['lightgreen', 10, 48], ['darkgray', 0.5, 0]]

    '''def __draw_component(self, comp, tmp_x, pos_occupied):
        cur_y_max = 0
        cur_y_min = 100000000
        tmp_y = 0
        cur_patches = []
        for i in range(len(comp.path)):
            for j in range(len(self.__all_paths)):
                if self.__all_paths[j] == comp.path[i]:
                    tmp_y = j
                    cur_port = None
                    if isinstance(comp, Photons):
                        cur_port = self.__draw_photon(i, comp.label, comp.param, tmp_x, tmp_y)
                        cur_patches.append(cur_port)
                    elif isinstance(comp, Element):
                        cur_port = self.__draw_element(i, comp.label, comp.param, tmp_x, tmp_y)
                        cur_patches.append(cur_port)
                    elif isinstance(comp, Detectors):
                        cur_port = self.__draw_detector(i, comp.coincidence[i], tmp_x, tmp_y)
                        cur_patches.append(cur_port)
                    self.ax.add_patch(cur_port)
                    if tmp_y > cur_y_max:
                        cur_y_max = tmp_y
                    if tmp_y < cur_y_min:
                        cur_y_min = tmp_y
        style_index = 0
        for i in range(cur_y_min, cur_y_max + 1):
            if pos_occupied[i] >= style_index:
                style_index = pos_occupied[i] + 1
        style_index %= len(self.__styles_cycle)
        for i in range(cur_y_min, cur_y_max + 1):
            pos_occupied[i] = style_index
        for patch in cur_patches:
            patch.set_ec(self.__styles_cycle[style_index][0])
            patch.set_fc('white')
        self.__draw_line(tmp_x, tmp_x, cur_y_min, cur_y_max, style_index)

    def __draw_photon(self, index, label, param, tmp_x, tmp_y):
        tri = patches.RegularPolygon(xy=(tmp_x * COL_WIDTH, tmp_y * ROW_HEIGHT),
                                      numVertices=3, radius= COMP_SIZE * 0.8, orientation=-np.pi / 2,
                                      linewidth=2, zorder=COMP_ORDER)
        self.ax.text(tmp_x * COL_WIDTH, tmp_y * ROW_HEIGHT, label.format(str(index)), ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)
        #if index == 0:
        #    self.ax.text(tmp_x * COL_WIDTH, tmp_y * ROW_HEIGHT - 0.8 * COMP_SIZE, param, ha='center', va='center', clip_on=True, zorder=TEXT_ORDER)

        return tri

    def __draw_element(self, index, label, param, tmp_x, tmp_y):
        box = patches.Rectangle(xy=(tmp_x * COL_WIDTH  - 0.5 * COMP_SIZE, tmp_y * ROW_HEIGHT - 0.5 * COMP_SIZE),
                                width=COMP_SIZE, height=COMP_SIZE, linewidth=2, zorder=COMP_ORDER)
        self.ax.text(tmp_x * COL_WIDTH, tmp_y * ROW_HEIGHT, label.format(str(index)), ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)
        if index == 0:
            self.ax.text(tmp_x * COL_WIDTH, tmp_y * ROW_HEIGHT - 0.8 * COMP_SIZE, param, ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)

        return box

    def __draw_detector(self, index, co_num, tmp_x, tmp_y):
        tri = patches.RegularPolygon(xy=(tmp_x * COL_WIDTH, tmp_y * ROW_HEIGHT),
                                      numVertices=3, radius= COMP_SIZE * 0.8, orientation=np.pi / 2,
                                      linewidth=2, zorder=COMP_ORDER)
        self.ax.text(tmp_x * COL_WIDTH, tmp_y * ROW_HEIGHT, str(co_num), ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)

        return tri

    def __draw_line(self, x_min, x_max, y_min, y_max, style_index):
        cur_color, cur_width, cur_z = self.__styles_cycle[style_index]
        self.ax.plot([x_min * COL_WIDTH, x_max * COL_WIDTH], [y_min * ROW_HEIGHT, y_max * ROW_HEIGHT],
                     color = cur_color,
                     linewidth = cur_width,
                     linestyle = 'solid',
                     zorder = cur_z)
    '''
    def draw(self):
        tmp_x = 0
        pos_occupied = [-1 for p in self.__all_paths]
        for src in self.__sources:
            #self.__draw_component(src, tmp_x, pos_occupied)
            #print(list(map(self.__all_paths.index, src.path)))
            self.__draw_source(0, list(map(self.__all_paths.index, src.path)))
        tmp_x += 1
        for layer in self.__layers:
            self.__draw_index(tmp_x)
            pos_occupied = [-1 for p in self.__all_paths]
            num_big_ele = 0  # recording the number of big elements in the layer to avoid the unclear input/output ports...
            for ele in layer:
                #self.__draw_component(ele, tmp_x, pos_occupied)
                if isinstance(ele, HWP):
                    self.__draw_HWP(tmp_x, self.__all_paths.index(ele.path[0]), ele.param)
                elif isinstance(ele, QWP):
                    self.__draw_QWP(tmp_x, self.__all_paths.index(ele.path[0]), ele.param)
                elif isinstance(ele, POL):
                    self.__draw_POL(tmp_x, self.__all_paths.index(ele.path[0]), ele.param)
                elif isinstance(ele, BC):
                    self.__draw_BC(tmp_x, self.__all_paths.index(ele.path[0]), ele.param)
                elif isinstance(ele, Reflection):
                    self.__draw_Reflection(tmp_x, self.__all_paths.index(ele.path[0]), ele.param)
                elif isinstance(ele, Hologram):
                    self.__draw_Holo(tmp_x, self.__all_paths.index(ele.path[0]), ele.param)
                elif isinstance(ele, EOM):
                    self.__draw_EOM(tmp_x, self.__all_paths.index(ele.path[0]), ele.param)
                elif isinstance(ele, PulseShaper):
                    self.__draw_Pulse_Shaper(tmp_x, self.__all_paths.index(ele.path[0]), ele.param)
                elif isinstance(ele, DP):
                    self.__draw_DP(tmp_x, self.__all_paths.index(ele.path[0]), ele.param)
                elif isinstance(ele, PBS):
                    self.__draw_PBS(tmp_x, self.__all_paths.index(ele.path[0]), self.__all_paths.index(ele.path[1]), num_big_ele)
                    num_big_ele += 1
                elif isinstance(ele, PDBS):
                    self.__draw_PDBS(tmp_x, self.__all_paths.index(ele.path[0]), self.__all_paths.index(ele.path[1]), num_big_ele)
                    num_big_ele += 1
                elif isinstance(ele, PBSFS):
                    self.__draw_PBSFS(tmp_x, self.__all_paths.index(ele.path[0]), self.__all_paths.index(ele.path[1]), num_big_ele)
                    num_big_ele += 1
                elif isinstance(ele, BS):
                    self.__draw_BS(tmp_x, self.__all_paths.index(ele.path[0]), self.__all_paths.index(ele.path[1]), num_big_ele)
                    num_big_ele += 1
                elif isinstance(ele, LI):
                    self.__draw_LI(tmp_x, self.__all_paths.index(ele.path[0]), self.__all_paths.index(ele.path[1]), num_big_ele)
                    num_big_ele += 1
                elif isinstance(ele, BD):
                    self.__draw_BD(tmp_x, list(map(self.__all_paths.index, ele.path)), ele.swap)
                else:
                    self.__draw_Custom(tmp_x, self.__all_paths.index(ele.path[0]), ele.label)
            tmp_x += 1
        if self.__detectors != None:
            #print('det')
            #print(self.__all_paths)
            #print(self.__all_paths.index)
            #print(self.__detectors.path)
            self.__draw_detectors(tmp_x, list(map(self.__all_paths.index, self.__detectors.path)), self.__detectors.coincidence)
            #self.__draw_component(self.__detectors, tmp_x, [-1 for p in self.__all_paths])

        # Draw the path lines and the path names
        for i in range(len(self.__all_paths)):
            self.ax.text(0 * COL_WIDTH, (i + 0.2) * ROW_HEIGHT, self.__path_mapping[self.__all_paths[i]], size='x-large', ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)
            self.__draw_line(0, tmp_x, i, i, -1)

        # Draw the light
        for i in range(len(self.__result)):
            bright_paths = self.__get_bright_paths(self.__result[i])
            for path in bright_paths:
                #print(path)
                shine = lines.Line2D([i * COL_WIDTH, (i + 1) * COL_WIDTH], [self.__all_paths.index(path) * ROW_HEIGHT, self.__all_paths.index(path) * ROW_HEIGHT],
                                     lw=2, color='red', axes=self.ax, zorder=2)
                self.ax.add_line(shine)

        #pyplot.show()
        pyplot.savefig('./experiment.pdf', quality=100, dpi='figure', bbox_inches='tight')
    def __draw_source(self, x, ys):
        len_ys = len(ys)
        sum_y = 0
        for y in ys:
            sum_y += y
        mid_y = sum_y / len_ys
        src_icon = patches.Arrow((x - 0.5) * COL_WIDTH, mid_y * ROW_HEIGHT, 0.25 * COL_WIDTH, 0, color='red')
        self.ax.add_patch(src_icon)
        for y in ys:
            seb = lines.Line2D([(x - 0.25) * COL_WIDTH, x * COL_WIDTH], [mid_y * ROW_HEIGHT, y * ROW_HEIGHT],
                                                       lw=2, color='red', axes=self.ax)
            self.ax.add_line(seb)

    def __draw_index(self, x):
        self.ax.text(x * COL_WIDTH  - 0 * COMP_SIZE, - 1.5 * COMP_SIZE, x - 1, ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)

    def __draw_HWP(self, x, y0, param):
        hwp_icon = patches.Rectangle(xy=(x * COL_WIDTH  - 0.25 * COMP_SIZE, y0 * ROW_HEIGHT - 0.5 * COMP_SIZE),
                                     width=COMP_SIZE / 2, height=COMP_SIZE, color='dodgerblue', zorder=COMP_ORDER)
        self.ax.text(x * COL_WIDTH  - 0 * COMP_SIZE, y0 * ROW_HEIGHT - 0.7 * COMP_SIZE, param, ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)
        self.ax.add_patch(hwp_icon)

    def __draw_Custom(self, x, y0, label):
        custom_icon = patches.Rectangle(xy=(x * COL_WIDTH  - 0.25 * COMP_SIZE, y0 * ROW_HEIGHT - 0.5 * COMP_SIZE),
                                     width=COMP_SIZE / 2, height=COMP_SIZE, ec='dodgerblue', fc='white', zorder=COMP_ORDER)
        self.ax.text(x * COL_WIDTH  - 0 * COMP_SIZE, y0 * ROW_HEIGHT + 0.7 * COMP_SIZE, label, ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)
        self.ax.add_patch(custom_icon)

    def __draw_QWP(self, x, y0, param):
        qwp_icon = patches.Rectangle(xy=(x * COL_WIDTH  - 0.25 * COMP_SIZE, y0 * ROW_HEIGHT - 0.5 * COMP_SIZE),
                                                                  width=COMP_SIZE / 2, height=COMP_SIZE, color='hotpink', zorder=COMP_ORDER)
        self.ax.text(x * COL_WIDTH  - 0 * COMP_SIZE, y0 * ROW_HEIGHT - 0.7 * COMP_SIZE, param, ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)
        self.ax.add_patch(qwp_icon)

    def __draw_POL(self, x, y0, param):
        pol_icon = patches.Rectangle(xy=(x * COL_WIDTH  - 0.25 * COMP_SIZE, y0 * ROW_HEIGHT - 0.5 * COMP_SIZE),
                                                                  width=COMP_SIZE / 2, height=COMP_SIZE, color='lightgreen', zorder=COMP_ORDER)
        self.ax.text(x * COL_WIDTH  - 0 * COMP_SIZE, y0 * ROW_HEIGHT - 0.7 * COMP_SIZE, param, ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)

        self.ax.add_patch(pol_icon)

    def __draw_BC(self, x, y0, param):
        pol_icon = patches.Rectangle(xy=(x * COL_WIDTH  - 0.25 * COMP_SIZE, y0 * ROW_HEIGHT - 0.5 * COMP_SIZE),
                                                                  width=COMP_SIZE / 2, height=COMP_SIZE, color='lightsalmon', zorder=COMP_ORDER)
        self.ax.text(x * COL_WIDTH  - 0 * COMP_SIZE, y0 * ROW_HEIGHT - 0.7 * COMP_SIZE, param, ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)

        self.ax.add_patch(pol_icon)

    def __draw_Reflection(self, x, y0, param):
        ref_icon = patches.Rectangle(xy=(x * COL_WIDTH  - 0.25 * COMP_SIZE, y0 * ROW_HEIGHT - 0.5 * COMP_SIZE),
                                                                  width=COMP_SIZE / 2, height=COMP_SIZE, color='gray', zorder=COMP_ORDER)
        self.ax.text(x * COL_WIDTH  - 0 * COMP_SIZE, y0 * ROW_HEIGHT - 0.7 * COMP_SIZE, param, ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)

        self.ax.add_patch(ref_icon)

    def __draw_Holo(self, x, y0, param):
        holo_icon = patches.Rectangle(xy=(x * COL_WIDTH  - 0.25 * COMP_SIZE, y0 * ROW_HEIGHT - 0.5 * COMP_SIZE),
                                                                  width=COMP_SIZE / 2, height=COMP_SIZE, color='purple', zorder=COMP_ORDER)
        self.ax.text(x * COL_WIDTH  - 0 * COMP_SIZE, y0 * ROW_HEIGHT - 0.7 * COMP_SIZE, param, ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)

        self.ax.add_patch(holo_icon)

    def __draw_EOM(self, x, y0, param):
        eom_icon = patches.Rectangle(xy=(x * COL_WIDTH  - 0.25 * COMP_SIZE, y0 * ROW_HEIGHT - 0.5 * COMP_SIZE),
                                                                  width=COMP_SIZE / 2, height=COMP_SIZE, color='bisque', zorder=COMP_ORDER)
        self.ax.text(x * COL_WIDTH  - 0 * COMP_SIZE, y0 * ROW_HEIGHT - 0.7 * COMP_SIZE, param, ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)

        self.ax.add_patch(eom_icon)

    def __draw_Pulse_Shaper(self, x, y0, param):
        ps_icon = patches.Rectangle(xy=(x * COL_WIDTH  - 0.25 * COMP_SIZE, y0 * ROW_HEIGHT - 0.5 * COMP_SIZE),
                                                                  width=COMP_SIZE / 2, height=COMP_SIZE, color='lightsteelblue', zorder=COMP_ORDER)
        self.ax.text(x * COL_WIDTH  - 0 * COMP_SIZE, y0 * ROW_HEIGHT - 0.7 * COMP_SIZE, param, ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)

        self.ax.add_patch(ps_icon)

    def __draw_DP(self, x, y0, param):
        dp_icon = patches.Rectangle(xy=(x * COL_WIDTH  - 0.25 * COMP_SIZE, y0 * ROW_HEIGHT - 0.5 * COMP_SIZE),
                                                                  width=COMP_SIZE / 2, height=COMP_SIZE, color='yellow', zorder=COMP_ORDER)
        self.ax.text(x * COL_WIDTH  - 0 * COMP_SIZE, y0 * ROW_HEIGHT - 0.7 * COMP_SIZE, param, ha='center', va='center', clip_on=False, zorder=TEXT_ORDER)

        self.ax.add_patch(dp_icon)

    def __draw_PBS(self, x, y0, y1, sty):
        y_min = min(y0, y1)
        y_max = max(y0, y1)

        pbs_icon = patches.RegularPolygon(xy=(x * COL_WIDTH, (y_min + 0.5) * ROW_HEIGHT),
                                          numVertices=4, radius=COMP_SIZE / 2, color='dodgerblue', zorder=COMP_ORDER)
        self.ax.add_patch(pbs_icon)
        lpie = lines.Line2D([x * COL_WIDTH + ROW_HEIGHT / 2, x * COL_WIDTH - ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_min * ROW_HEIGHT],
                                               lw=2, color='darkgrey', axes=self.ax)
        lna = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_min * ROW_HEIGHT],
                                               lw=2, color='darkgrey', axes=self.ax)
        lad_l = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH - ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                                lw=2, color='darkgrey', axes=self.ax)
        lad_r = lines.Line2D([x * COL_WIDTH + ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                                lw=2, color='darkgrey', axes=self.ax)
        blocker_min = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [y_min * ROW_HEIGHT, y_min * ROW_HEIGHT],
                                   lw=4, color='white', axes=self.ax, zorder=BLOCKER_ORDER)
        blocker_max = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [y_max * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                   lw=4, color='white', axes=self.ax, zorder=BLOCKER_ORDER)
        self.ax.add_line(blocker_min)
        self.ax.add_line(blocker_max)
        self.ax.add_line(lpie)
        self.ax.add_line(lna)
        self.ax.add_line(lad_l)
        self.ax.add_line(lad_r)
        if sty == 0:
            dot_min_l = patches.Circle(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_min * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
            dot_min_r = patches.Circle(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_min * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
            dot_max_l = patches.Circle(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_max * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
            dot_max_r = patches.Circle(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_max * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
        else:
            dot_min_l = patches.RegularPolygon(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_min * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)
            dot_min_r = patches.RegularPolygon(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_min * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)
            dot_max_l = patches.RegularPolygon(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_max * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)
            dot_max_r = patches.RegularPolygon(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_max * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)

        self.ax.add_patch(dot_min_l)
        self.ax.add_patch(dot_min_r)
        self.ax.add_patch(dot_max_l)
        self.ax.add_patch(dot_max_r)
        dash = lines.Line2D([x * COL_WIDTH - 0.45 * COMP_SIZE, x * COL_WIDTH + 0.45 * COMP_SIZE], [(y_min + 0.5) * ROW_HEIGHT, (y_min + 0.5) * ROW_HEIGHT],
                            lw=2, ls='-', color='black', axes=self.ax, zorder=COMP_ORDER + 1, solid_capstyle='round')
        self.ax.add_line(dash)

    def __draw_LI(self, x, y0, y1, sty):
        y_min = min(y0, y1)
        y_max = max(y0, y1)

        pbs_icon = patches.RegularPolygon(xy=(x * COL_WIDTH, (y_min + 0.5) * ROW_HEIGHT),
                                          numVertices=4, radius=COMP_SIZE / 2, color='grey', zorder=COMP_ORDER)
        self.ax.add_patch(pbs_icon)
        lpie = lines.Line2D([x * COL_WIDTH + ROW_HEIGHT / 2, x * COL_WIDTH - ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_min * ROW_HEIGHT],
                                               lw=2, color='darkgrey', axes=self.ax)
        lna = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_min * ROW_HEIGHT],
                                               lw=2, color='darkgrey', axes=self.ax)
        lad_l = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH - ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                                lw=2, color='darkgrey', axes=self.ax)
        lad_r = lines.Line2D([x * COL_WIDTH + ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                                lw=2, color='darkgrey', axes=self.ax)
        blocker_min = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [y_min * ROW_HEIGHT, y_min * ROW_HEIGHT],
                                   lw=4, color='white', axes=self.ax, zorder=BLOCKER_ORDER)
        blocker_max = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [y_max * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                   lw=4, color='white', axes=self.ax, zorder=BLOCKER_ORDER)
        self.ax.add_line(blocker_min)
        self.ax.add_line(blocker_max)
        self.ax.add_line(lpie)
        self.ax.add_line(lna)
        self.ax.add_line(lad_l)
        self.ax.add_line(lad_r)
        if sty == 0:
            dot_min_l = patches.Circle(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_min * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
            dot_min_r = patches.Circle(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_min * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
            dot_max_l = patches.Circle(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_max * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
            dot_max_r = patches.Circle(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_max * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
        else:
            dot_min_l = patches.RegularPolygon(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_min * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)
            dot_min_r = patches.RegularPolygon(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_min * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)
            dot_max_l = patches.RegularPolygon(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_max * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)
            dot_max_r = patches.RegularPolygon(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_max * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)

        self.ax.add_patch(dot_min_l)
        self.ax.add_patch(dot_min_r)
        self.ax.add_patch(dot_max_l)
        self.ax.add_patch(dot_max_r)
        dash = lines.Line2D([x * COL_WIDTH - 0.45 * COMP_SIZE, x * COL_WIDTH + 0.45 * COMP_SIZE], [(y_min + 0.5) * ROW_HEIGHT, (y_min + 0.5) * ROW_HEIGHT],
                            lw=2, ls='-', color='black', axes=self.ax, zorder=COMP_ORDER + 1, solid_capstyle='round')
        self.ax.add_line(dash)
    
    def __draw_PDBS(self, x, y0, y1, sty):
        y_min = min(y0, y1)
        y_max = max(y0, y1)

        pbs_icon = patches.RegularPolygon(xy=(x * COL_WIDTH, (y_min + 0.5) * ROW_HEIGHT),
                                          numVertices=4, radius=COMP_SIZE / 2, color='violet', zorder=COMP_ORDER)
        self.ax.add_patch(pbs_icon)
        lpie = lines.Line2D([x * COL_WIDTH + ROW_HEIGHT / 2, x * COL_WIDTH - ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_min * ROW_HEIGHT],
                                               lw=2, color='darkgrey', axes=self.ax)
        lna = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_min * ROW_HEIGHT],
                                               lw=2, color='darkgrey', axes=self.ax)
        lad_l = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH - ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                                lw=2, color='darkgrey', axes=self.ax)
        lad_r = lines.Line2D([x * COL_WIDTH + ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                                lw=2, color='darkgrey', axes=self.ax)
        blocker_min = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [y_min * ROW_HEIGHT, y_min * ROW_HEIGHT],
                                   lw=4, color='white', axes=self.ax, zorder=BLOCKER_ORDER)
        blocker_max = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [y_max * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                   lw=4, color='white', axes=self.ax, zorder=BLOCKER_ORDER)
        self.ax.add_line(blocker_min)
        self.ax.add_line(blocker_max)
        self.ax.add_line(lpie)
        self.ax.add_line(lna)
        self.ax.add_line(lad_l)
        self.ax.add_line(lad_r)
        if sty == 0:
            dot_min_l = patches.Circle(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_min * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
            dot_min_r = patches.Circle(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_min * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
            dot_max_l = patches.Circle(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_max * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
            dot_max_r = patches.Circle(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_max * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
        else:
            dot_min_l = patches.RegularPolygon(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_min * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)
            dot_min_r = patches.RegularPolygon(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_min * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)
            dot_max_l = patches.RegularPolygon(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_max * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)
            dot_max_r = patches.RegularPolygon(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_max * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)

        self.ax.add_patch(dot_min_l)
        self.ax.add_patch(dot_min_r)
        self.ax.add_patch(dot_max_l)
        self.ax.add_patch(dot_max_r)
        dash = lines.Line2D([x * COL_WIDTH - 0.45 * COMP_SIZE, x * COL_WIDTH + 0.45 * COMP_SIZE], [(y_min + 0.5) * ROW_HEIGHT, (y_min + 0.5) * ROW_HEIGHT],
                            lw=2, ls='-', color='black', axes=self.ax, zorder=COMP_ORDER + 1, solid_capstyle='round')
        self.ax.add_line(dash)

    def __draw_PBSFS(self, x, y0, y1, sty):
        y_min = min(y0, y1)
        y_max = max(y0, y1)

        pbs_icon = patches.RegularPolygon(xy=(x * COL_WIDTH, (y_min + 0.5) * ROW_HEIGHT),
                                          numVertices=4, radius=COMP_SIZE / 2, color='dodgerblue', zorder=COMP_ORDER)
        self.ax.add_patch(pbs_icon)
        lpie = lines.Line2D([x * COL_WIDTH + ROW_HEIGHT / 2, x * COL_WIDTH - ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_min * ROW_HEIGHT],
                                               lw=2, color='darkgrey', axes=self.ax)
        lna = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_min * ROW_HEIGHT],
                                               lw=2, color='darkgrey', axes=self.ax)
        lad_l = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH - ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                                lw=2, color='darkgrey', axes=self.ax)
        lad_r = lines.Line2D([x * COL_WIDTH + ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                                lw=2, color='darkgrey', axes=self.ax)
        blocker_min = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [y_min * ROW_HEIGHT, y_min * ROW_HEIGHT],
                                   lw=4, color='white', axes=self.ax, zorder=BLOCKER_ORDER)
        blocker_max = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [y_max * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                   lw=4, color='white', axes=self.ax, zorder=BLOCKER_ORDER)
        self.ax.add_line(blocker_min)
        self.ax.add_line(blocker_max)
        self.ax.add_line(lpie)
        self.ax.add_line(lna)
        self.ax.add_line(lad_l)
        self.ax.add_line(lad_r)
        if sty == 0:
            dot_min_l = patches.Circle(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_min * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
            dot_min_r = patches.Circle(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_min * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
            dot_max_l = patches.Circle(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_max * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
            dot_max_r = patches.Circle(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_max * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
        else:
            dot_min_l = patches.RegularPolygon(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_min * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)
            dot_min_r = patches.RegularPolygon(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_min * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)
            dot_max_l = patches.RegularPolygon(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_max * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)
            dot_max_r = patches.RegularPolygon(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_max * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)

        self.ax.add_patch(dot_min_l)
        self.ax.add_patch(dot_min_r)
        self.ax.add_patch(dot_max_l)
        self.ax.add_patch(dot_max_r)
        dash = lines.Line2D([x * COL_WIDTH - 0.45 * COMP_SIZE, x * COL_WIDTH + 0.45 * COMP_SIZE], [(y_min + 0.5) * ROW_HEIGHT, (y_min + 0.5) * ROW_HEIGHT],
                            lw=2, ls='-', color='black', axes=self.ax, zorder=COMP_ORDER + 1, solid_capstyle='round')
        fs_circ = patches.Circle(xy=(x * COL_WIDTH, (y_min + 0.5) * ROW_HEIGHT), radius = COMP_SIZE / 3, fc=None, fill=False, ec='black', zorder=COMP_ORDER)
        self.ax.add_patch(fs_circ)
        self.ax.add_line(dash)

    def __draw_BS(self, x, y0, y1, sty):
        y_min = min(y0, y1)
        y_max = max(y0, y1)

        bs_icon = patches.Rectangle(xy=(x * COL_WIDTH  - 0.5 * COMP_SIZE, (y_min + 0.5) * ROW_HEIGHT - 0.125 * COMP_SIZE),
                                                                width=COMP_SIZE, height=COMP_SIZE / 4, color='dodgerblue', zorder=COMP_ORDER)
        self.ax.add_patch(bs_icon)
        lpie = lines.Line2D([x * COL_WIDTH + ROW_HEIGHT / 2, x * COL_WIDTH - ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_min * ROW_HEIGHT],
                                               lw=2, color='darkgrey', axes=self.ax)
        lna = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_min * ROW_HEIGHT],
                                               lw=2, color='darkgrey', axes=self.ax)
        lad_l = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH - ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                                lw=2, color='darkgrey', axes=self.ax)
        lad_r = lines.Line2D([x * COL_WIDTH + ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [(y_min + 1) * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                                lw=2, color='darkgrey', axes=self.ax)
        blocker_min = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [y_min * ROW_HEIGHT, y_min * ROW_HEIGHT],
                                   lw=4, color='white', axes=self.ax, zorder=BLOCKER_ORDER)
        blocker_max = lines.Line2D([x * COL_WIDTH - ROW_HEIGHT / 2, x * COL_WIDTH + ROW_HEIGHT / 2], [y_max * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                   lw=4, color='white', axes=self.ax, zorder=BLOCKER_ORDER)
        self.ax.add_line(blocker_min)
        self.ax.add_line(blocker_max)
        if sty == 0:
            dot_min_l = patches.Circle(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_min * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
            dot_min_r = patches.Circle(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_min * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
            dot_max_l = patches.Circle(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_max * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
            dot_max_r = patches.Circle(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_max * ROW_HEIGHT), radius = DOT_RADIUS, color='black', zorder=COMP_ORDER)
        else:
            dot_min_l = patches.RegularPolygon(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_min * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)
            dot_min_r = patches.RegularPolygon(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_min * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)
            dot_max_l = patches.RegularPolygon(xy=(x * COL_WIDTH - ROW_HEIGHT / 2, y_max * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)
            dot_max_r = patches.RegularPolygon(xy=(x * COL_WIDTH + ROW_HEIGHT / 2, y_max * ROW_HEIGHT), numVertices=sty + 2, radius=DOT_RADIUS * 2, color='black', zorder=COMP_ORDER)

        self.ax.add_patch(dot_min_l)
        self.ax.add_patch(dot_min_r)
        self.ax.add_patch(dot_max_l)
        self.ax.add_patch(dot_max_r)
        
        if y0 < y1:
            dash = lines.Line2D([x * COL_WIDTH - 0.48 * COMP_SIZE, x * COL_WIDTH + 0.48 * COMP_SIZE], [(y_min + 0.5) * ROW_HEIGHT + 0.2 * COMP_SIZE, (y_min + 0.5) * ROW_HEIGHT + 0.2 * COMP_SIZE],
                                lw=3, ls='--', color='grey', axes=self.ax, zorder=COMP_ORDER)
        else:
            dash = lines.Line2D([x * COL_WIDTH - 0.48 * COMP_SIZE, x * COL_WIDTH + 0.48 * COMP_SIZE], [(y_min + 0.5) * ROW_HEIGHT - 0.2 * COMP_SIZE, (y_min + 0.5) * ROW_HEIGHT - 0.2 * COMP_SIZE],
                                lw=3, ls='--', color='grey', axes=self.ax, zorder=COMP_ORDER)
        self.ax.add_line(dash)

        self.ax.add_line(lpie)
        self.ax.add_line(lna)
        self.ax.add_line(lad_l)
        self.ax.add_line(lad_r)


    def __draw_BD(self, x, ys, swap):
        for i in range(len(ys) - 1):
            y0 = ys[i]
            y1 = ys[i + 1]

            ar0 = patches.Arrow((x - 0.25) * COL_WIDTH, y0 * ROW_HEIGHT, COL_WIDTH / 4, 0, alpha=0.7, color='dodgerblue' if swap == False else 'red', width=0.5, zorder=COMP_ORDER)
            ar1 = patches.Arrow((x - 0.25) * COL_WIDTH, y0 * ROW_HEIGHT, COL_WIDTH / 4, (y1 - y0) * ROW_HEIGHT, alpha=0.7, color='red' if swap == False else 'dodgerblue', width=0.5, zorder=COMP_ORDER)

            self.ax.add_patch(ar0)
            self.ax.add_patch(ar1)
        
    def __draw_line(self, x_min, x_max, y_min, y_max, style_index):
        cur_color, cur_width, cur_z = self.__styles_cycle[style_index]
        self.ax.plot([x_min * COL_WIDTH, x_max * COL_WIDTH], [y_min * ROW_HEIGHT, y_max * ROW_HEIGHT],
                                  color = cur_color,
                                  linewidth = cur_width,
                                  linestyle = 'solid',
                                  zorder = cur_z)

    def __draw_detectors(self, x, ys, cs):
        y_min = min(ys)
        y_max = max(ys)
        len_ys = len(ys)
        for i in range(len_ys):
            y = ys[i]
            c = cs[i]
            det_icon = patches.Wedge(center=(x * COL_WIDTH, y * ROW_HEIGHT), theta1=-90, theta2=90, r= COMP_SIZE / 4, label=c)

            self.ax.text((x + 0.02) * COL_WIDTH, y * ROW_HEIGHT, c, ha='center', va='center', clip_on=False, zorder=TEXT_ORDER, color='white')
            self.ax.add_patch(det_icon)
            det_line = lines.Line2D([x * COL_WIDTH, (x + 0.25) * COL_WIDTH], [y * ROW_HEIGHT, y * ROW_HEIGHT])
            self.ax.add_line(det_line)
        merge_line = lines.Line2D([(x + 0.25) * COL_WIDTH, (x + 0.25) * COL_WIDTH], [y_max * ROW_HEIGHT, y_min * ROW_HEIGHT])
        self.ax.add_line(merge_line)
    
    def __get_bright_paths(self, state):
        from photoniqlab.sympy_widget import Wild, sympify, Function, co
        wild_str = 'co('
        for dof in self.__dofs:
            wild_str += ('Wild(\'' + dof + '\')')
            wild_str += ','
        wild_str = wild_str.rstrip(',')
        wild_str += ')'
        #print(wild_str)
        wild_expr = sympify(wild_str)
        bright_paths = []
        all_co = state.atoms(co)
        for aco in all_co:
            #print(aco, aco.match(wild_expr))
            path = aco.match(wild_expr)[Wild('path')]
            bright_paths.append(path)
        bright_paths = list(set(bright_paths))
        #print('bright paths:')
        #print(bright_paths)
        return bright_paths


