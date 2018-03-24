NODE, EDGE, ATTR = range(3)

NODE_NAME, NODE_ATTR = 1, 2
EDGE_SRC, EDGE_DST, EDGE_ATTR = 1, 2, 3
ATTR_NAME, ATTR_VAL = 1, 2

TYPE_INDEX = 0
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
            type, *params = element

            # Raise error if type is unknown
            if type not in [NODE, EDGE, ATTR]:
                raise ValueError("Unknown element")
            # Raise an error if the number of parameters is incorrect
            elif len(params) != correct_num_of_parameters[type]:
                raise ValueError("Malformed input")

            # Otherwise, add it to the graph
            if type == NODE:
                self.nodes.append(Node(element[NODE_NAME], element[NODE_ATTR]))
            elif type == EDGE:
                self.edges.append(Edge(element[EDGE_SRC], element[EDGE_DST], element[EDGE_ATTR]))
            elif type == ATTR:
                self.attrs[element[ATTR_NAME]] = element[ATTR_VAL]
