NODE, EDGE, ATTR = range(3)

correct_num_of_parameters = {NODE: 2, EDGE: 3, ATTR: 2}


class Node(object):
    def __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    func_list = [Node, Edge]

    def __init__(self, data=[]):
        self.nodes = []
        self.edges = []
        self.attrs = {}

        # Loop through each element in the graph
        for element in data:

            # If the element only has 0 or 1 element, then it is improper
            if len(element) < 2:
                raise TypeError("Improper element")

            # Get the type of the element, and the parameters
            element_type, *params = element

            # Raise error if type is unknown
            if element_type not in [NODE, EDGE, ATTR]:
                raise ValueError("Unknown element")
            # Raise an error if the number of parameters is incorrect
            elif len(params) != correct_num_of_parameters[element_type]:
                raise ValueError("Incorrect number of parameters")

            # Otherwise, add it to the graph
            if element_type == NODE:
                self.nodes.append(Node(*params))
            elif element_type == EDGE:
                self.edges.append(Edge(*params))
            elif element_type == ATTR:
                attr_name, value = params
                self.attrs[attr_name] = value
