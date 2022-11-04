# -*- coding: utf-8 -*-

"""Class for the photon number detector."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.component import Component

class Detectors(Component):
    """Class for the photon number detector.

    You can configurate the photon number on each path to trigger the coincidence count.
    In experiment, the photon number is usually 1 because only SPAD is widely implemented.

    Attributes:
        dofs: The used dofs in the this detector.
        coincidence: The photon number on each path to trigger a coincidence count.
    """

    def __init__(self, path_num):
        """Create a detector."""
        Component.__init__(self, path_num)
        self.dofs = ['path']  # Only the path dof is used for detectors
        self.coincidence = [1 for i in range(0, path_num)]

    def post_select(self, state, total_dofs):
        """Post select the state."""
        post_state = Integer(0)

        # If sum of multiple terms
        if state.func == Add:
            all_terms = state.args
            for term in all_terms:
                #print(term)
                if self.__live(term, total_dofs):
                    #print('live!!')
                    post_state += term

        # If single term include several co or single co
        else:
            #print(state)
            if self.__live(state, total_dofs):
                #print('live!!')
                post_state += state

        return post_state

    def __live(self, term, total_dofs):
        """Check whether the single term lives for the post select (Actually, a projection)."""
        co_num = {path: 0 for path in self.path}  # Record the number of co on each mode

        # If this term is multiple of many factors
        if term.func == Mul:
            all_factors = term.args
            for factor in all_factors:
                if factor.has(co): # The coefficient in front of the co will be ignored
                    num, path = self.__extract_num_on_path(factor, total_dofs)
                    if path not in co_num:
                        co_num.update({path: num})
                    else:
                        co_num[path] += num

        # If the term is single Pow factor
        elif term.func == Pow or term.func == co:
            if term.has(co):
                num, path = self.__extract_num_on_path(term, total_dofs)
                if path not in co_num:
                    co_num.update({path: num})
                else:
                    co_num[path] += num

        # Other situation...May be an error
        else:
            raise PhotoniqlabError("This form of the term has not been considered when check a single term for post selection.")

        #print(co_num)
        # Check whether the term will live
        flag = True
        for i in range(len(self.path)):
            if co_num[self.path[i]] != self.coincidence[i]:
                flag = False
                break

        return flag

    def __extract_num_on_path(self, factor, total_dofs):
        """Extract the photon number on the path of current factor (either pow or co is ok)."""
        co_wild = self._generate_wild(total_dofs)  # Wild card for a co under the total dofs. Info on each dof is named by the dof
        factor_info = factor.match(Pow(co_wild, Wild('n')))
        num = factor_info[Wild('n')]
        path = factor_info[Wild('path')]
        return num, path
