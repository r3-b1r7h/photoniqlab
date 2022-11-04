# -*- coding: utf-8 -*-

"""Visualize the state after each layer and the output state of the experiment."""

import re
from matplotlib import patches
from matplotlib import pyplot
# -*- coding: utf-8 -*-
from photoniqlab.sympy_widget import *

class StateDrawer:
    def __init__(self, result, post_selected_result, path_mapping, total_dofs):
        self.init = result[0]
        self.intermediate = result[1:]
        self.post_selected_result = post_selected_result

        self.total_dofs = total_dofs
        self.path_mapping = path_mapping

    def draw(self):
        with open('Degrees of freedom','w') as file_object:
            dofs_str = ''
            for dof in self.total_dofs:
                dofs_str += dof
                dofs_str += ', '
            dofs_str = dofs_str.rstrip(' ')
            dofs_str = dofs_str.rstrip(',')
            file_object.write(dofs_str)

        init_state = self.statelize(self.init)
        pyplot.savefig('./init_state.pdf', quality=100, dpi='figure', bbox_inches='tight')
        for i in range(len(self.intermediate)):
            cur_state = self.statelize(self.intermediate[i])
            pyplot.savefig('./after_layer{}.pdf'.format(i), quality=100, dpi='figure', bbox_inches='tight')
        if self.post_selected_result != None:
            post_state = self.statelize(self.post_selected_result)
            pyplot.savefig('./post_selected.pdf', quality=100, dpi='figure', bbox_inches='tight')

    def statelize(self, co_poly):
        mapping_wild = self.__generate_mapping_wild(self.total_dofs, self.path_mapping)

        # Here we don't need to consider the requirement for instantaneous, because each mapping are isolated...
        for query, value in mapping_wild.items():
            co_poly = co_poly.replace(query, value)

        state = latex(co_poly)
        #print('origin state:\n', state)
        state = re.sub(r'\\operatorname{co}{\\left \((\S*) \\right \)}', r'\\left\|1 \\right \\rangle_{\1}', state)
        #print('replaced state1:\n', state)
        state = re.sub(r'\\operatorname{co}\^{(\S*)}{\\left \((\S*) \\right \)}', r'\\left\|\1 \\right \\rangle_{\2}', state)
        #print('replaced state2:\n', state)

        state_figure = pyplot.figure(figsize=[5, 5])
        ax = state_figure.add_subplot(111)
        ax.axis('off')
        ax.set_aspect('equal')
        ax.tick_params(labelbottom=False, labeltop=False,
                       labelleft=False, labelright=False)
        ax.text(0.5, 0.5, '${}$'.format(state), clip_on=False, ha='center', va='center')
        return state

    def __generate_mapping_wild(self, dofs, path_mapping):
        wild_str = 'co('
        for dof in dofs:
            wild_str += 'Wild(\'' + dof + '\'),'
        wild_str.rstrip(',')
        wild_str += (')')
        wild = sympify(wild_str)

        mapping_wild = {}
        for key, val in path_mapping.items():
            origin = 'co('
            target = 'co('
            for dof in dofs:
                if dof == 'path':
                    origin += str(key)
                    origin += ','
                    target += val
                    target += ','
                else:
                    origin += 'Wild(\'' + dof + '\'),'
                    target += 'Wild(\'' + dof + '\'),'

            origin = origin.rstrip(',')
            target = target.rstrip(',')
            origin += (')')
            target += (')')
            origin_wild = sympify(origin)
            target_wild = sympify(target)
            mapping_wild.update({origin_wild: target_wild})
        return mapping_wild

