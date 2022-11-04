# -*- coding: utf-8 -*-

"""Parent for all elements here."""

from photoniqlab.sympy_widget import *
from photoniqlab.components.component import Component

class Element(Component):
    """The base class for all elements.

    All elements are defined by inherent this class and specify the U. The user can also define new elements by the same method.
    The dofs used in the element and responding unitary transformation are included here.

    Attributes:
        dofs: Degree of freedoms used. Now we will smartly collect all.
        u: The unitary transformation for this component.
    """

    def __init__(self, path_num, dofs, u):
        """Create a element."""
        Component.__init__(self, path_num)
        self.dofs = dofs
        self.u = u

    def get_u(self, total_dofs):
        """Get the specified unitary transformation of this component.

        This method is very smart as the user don't need to specified
        information on all dofs. Only necessary information is needed
        and we fill the information on other dofs by wildcard automatically.

        """

        # Fill other dofs with wildcards
        complete_u = {}
        for trans in self.u.items():

            # Keep the gived information of the dofs of the elements, while left the position of other dofs as
            # wild card (even though the information it self is a wildcard).
            query = trans[0].replace(self._generate_wild(self.dofs), self._generate_wild(total_dofs))
            value = trans[1].replace(self._generate_wild(self.dofs), self._generate_wild(total_dofs))

            # Convert the local information of each element to a global view and a easier-computing form.
            # If path information is omitted by the 1 path element, the position for path will be Wild('path').
            # Otherwise, it will be 'pi'...
            if 'path' not in self.dofs:
                if len(self.path) == 1:

                    # Actually, the 1-path elements are not path-information-free. They work just on single path.
                    query = query.subs(Wild('path'), self.path[0])
                    value = value.subs(Wild('path'), self.path[0])
                else:
                    raise PhotoniqlabError('Only 1 path elements can omit the path information.')
            else:
                for i in range(0, len(self.path)):
                    query = query.subs(Symbol('p' + str(i + 1)), self.path[i])
                    value = value.subs(Symbol('p' + str(i + 1)), self.path[i])
            complete_u[query] = value
        return complete_u
