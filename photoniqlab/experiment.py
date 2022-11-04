# -*- coding: utf-8 -*-

from copy import deepcopy

from photoniqlab.sympy_widget import *
from photoniqlab.components.detectors import Detectors
from photoniqlab.exceptions import PhotoniqlabError

"""The Experiment class. """

class Experiment:
    """The experiment you want to simulate.

    Everything in the experiment(photon source, elements and detectors) is in this class.
    You just need to create them and connect them to each others like what you do on your laboratory bench.

    Attributes:
        dofs: Degree of freedoms encoded in this experiment. Smartly generated.
        sources: All photon sources are considered as components here.
        elements: All elements that apply transformation to the photons.
        detectors: The post select system realized by photon number detector.
        layers: Each layer is a column of elements here.
        result: The simulation result after each layer in the experiment.
        post_selected_result: The post selected result when the detectors exist.
    """

    def __init__(self):
        """Create the experiment."""
        self.ele_dofs = ['path']  # The path dof is implicitly declared
        self.sources = []
        self.elements = []
        self.detectors = None
        self.layers = []
        self.result = []
        self.post_selected_result = None

        self.__all_paths = []  # All path (in number form) in the experiment
        self.__path_mapping = {}  # A dict that maps a path to a name in str

    def __extend_ele_dofs(self, dofs):
        """Extend the total dofs of the experiment."""
        total_dofs = set(self.ele_dofs)
        tmp_dofs = dofs
        total_dofs = total_dofs.union(set(tmp_dofs))
        total_dofs = list(total_dofs)
        self.ele_dofs = total_dofs

    def add_sources(self, *sources):
        """Add the photon sources as one component of current experiment."""
        tmp_dofs = sources[0].dofs
        for src in sources:
            if set(src.dofs) != set(tmp_dofs):
                raise PhotoniqlabError("The dofs of the sources are different.")
        self.sources.extend(sources)

    def add_elements(self, *elements):
        """Add elements of current experiment."""
        for ele in elements:
            self.__extend_ele_dofs(ele.dofs)
        self.elements.extend(elements)

    def add_detectors(self, detectors):
        """Add the post select system realized by photon number detectors."""
        self.detectors = detectors

    def build(self):
        """Build the experiment components as a matrix."""
        # Check whether the dofs of sources equal to all used dofs in the experiment.
        # When it is less, sometimes it can not work (e.g. photon only has path information
        # meets a PBS).
        for dof in self.ele_dofs:
            if dof not in self.sources[0].dofs:
                raise PhotoniqlabError("The dofs of the photon sources are not sufficient. Information of {} is needed.".format(dof))
        self.total_dofs = self.sources[0].dofs

        all_comps = deepcopy(self.sources)
        all_comps.extend(self.elements)
        if self.detectors != None:
            all_comps.append(self.detectors)
        for i in range(len(all_comps)):
            all_comps[i].id = i  # The id for each component is its index in all_comps

        def elim(cur_comp):
           for succ, path_num in cur_comp.o:
                if (succ != None or path_num != None):
                    if ais[succ.id] == 1:
                        ais[succ.id] = 2
                    elim(succ)
        # Layerize. Each round we collect the successors of the current layer,
        # and eliminate the components of them that are not immediate successors.
        cur_layer = deepcopy(self.sources)  # The first layer is sources
        ais = [0 for i in range(len(all_comps))]
        while len(cur_layer) != 0:  # Finished when no more successors (to be tested).
            ais = [0 for i in range(len(all_comps))]
            next_layer = []
            for comp in cur_layer:
                for succ, path_num in comp.o:
                    if (succ != None or path_num != None) and not isinstance(succ, Detectors):  # Detectors not considered here
                        ais[succ.id] = 1
            for i in range(len(all_comps)):
                if ais[i] != 0:
                    cur_comp = all_comps[i]
                    '''for succ, path_num in cur_comp.o:
                        if (succ != None or path_num != None) and ais[succ.id] == 1:
                            ais[succ.id] = 2'''
                    elim(cur_comp)
            for i in range(len(all_comps)):
                if ais[i] == 1:
                    next_layer.append(all_comps[i])
            if len(next_layer) != 0:
                self.layers.append(next_layer)
            cur_layer = next_layer

        # Here we give the path information row to row. This must be done after layerizing.
        for row in [self.sources] + self.layers:  # Consider the sources are in a layer
            for comp in row:
                for i in range(len(comp.o)):
                    succ, path_num = comp.o[i]
                    if succ != None or path_num != None:  # Only consider the connected ports
                        succ.path[path_num] = comp.path[i]

        # Todo: when some components are not scanned, raise an error or warnning?

        # Create the mapping from path name in number form to string form
        all_paths = set([])
        for src in self.sources:
            all_paths = all_paths.union(set(src.path))
            #print(src.path)
        for ele in self.elements:
            all_paths = all_paths.union(set(ele.path))
            #print(ele.path)
        self.__all_paths = list(all_paths)
        self.__all_paths.sort()

        # TODO: sort the paths to reduce twists.
        
        for i in range(len(self.__all_paths)):
            tail_length = i // 26  # if a to z are not enough, we add a pri and recycle from a to z.
            char = chr(i % 26 + ord('a'))
            cur_str_name = char
            for i in range(tail_length):
                cur_str_name += '\''
            # cur_str_name += '$'
            self.__path_mapping[self.__all_paths[i]] = cur_str_name

        return

    def draw(self):
        """Draw the built experiment components by matplotlib."""
        from photoniqlab.visualization.experiment_drawer import ExperimentDrawer
        from photoniqlab.visualization.state_drawer import StateDrawer
        experiment_drawer = ExperimentDrawer(self, self.__all_paths, self.__path_mapping)
        experiment_drawer.draw()
        state_drawer = StateDrawer(self.result, self.post_selected_result, self.__path_mapping, self.total_dofs)
        state_drawer.draw()

    def simulate(self):
        """Simulate the experiment and get the result post-selected by the detectors."""

        # Prepare the initial state generated by the photon sources
        state = 1
        for src in self.sources:
            state *= src.get_state()
        self.result.append(state)  # Save the initial state in the result
        print("\n----------------------------------------")
        print("Initial state:")
        print(self.__visualize(state))

        # Simulate the evolution layer by layer
        for i in range(len(self.layers)):
            layer = self.layers[i]
            #print(layer)
            u = {}
            for ele in layer:
                u.update(ele.get_u(self.total_dofs))
            #print(u)
            state = self.__s_replace(state, u)
            state = expand(state)
            self.result.append(state)
            print("----------------------------------------")
            print("After layer {}:".format(str(i)))
            print(self.__visualize(state))

        # If the post-selecting system exists
        if self.detectors != None:
            state = self.detectors.post_select(state, self.total_dofs)
            self.post_selected_result = state
            print("----------------------------------------")
            print("After post-selection:")
            print(self.__visualize(state))
        print("----------------------------------------")
        self.draw()

        return self.result

    def __s_replace(self, state, u):
        """
        Do a lot of transformation simutaneously. Necessary, for example, PBS.
        Inspired by the method 'replace' of sympy.core.basic.Basic.
        """
        def co_replace(expr):
            for query, value in u.items():
                result = expr.match(query)
                if result or result == {}:
                    new = value.subs(result)
                    if new is not None and new != expr:
                        expr = new
                    break
            return expr
        rv = bottom_up(state, co_replace)
        return rv

    def __cut_off(self, state, precision=4):
        """Chop the term including variable with small coeffecient."""
        def chop(expr):
            return expr.n(n=precision, chop=True) 
        rv = bottom_up(state, chop, atoms=True)
        return rv

    def __visualize(self, state):
        """Tranform the result to fock state form."""
        return self.__cut_off(state)

def bottom_up(rv, F, atoms=False, nonbasic=False):
        """Modified from the function 'bottom_up' in sympy.simplify.simplify."""

        # Here I fixed a bug of Sympy. When H + V through a HWP(pi / 8),
        # The substituions happen on H and V respectively, but
        # the origin implementation of this function will substitude 
        # the generated H again, because Add(H) is just a H.
        # So, I simplified the function.
        try:
            if rv.args:
                if rv.func == co:
                    rv = F(rv)
                else:
                    args = tuple([bottom_up(a, F, atoms, nonbasic)
                        for a in rv.args])
                    if args != rv.args:
                        rv = rv.func(*args)
                    #rv = F(rv)
            elif atoms:
                rv = F(rv)
        except AttributeError:
            if nonbasic:
                try:
                    rv = F(rv)
                except TypeError:
                    pass
        return rv