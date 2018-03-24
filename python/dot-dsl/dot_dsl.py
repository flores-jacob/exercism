NODE, EDGE, ATTR = range(3)

TYPE = 0

NODE_NAME, NODE_ATTR = 1, 2

EDGE_SRC, EDGE_DST, EDGE_ATTR = 1, 2, 3

ATTR_NAME, ATTR_VAL = 1, 2


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
    def __init__(self, data=[]):
        self.nodes = []
        self.edges = []
        self.attrs = {}

        for element in data:
            if element[TYPE] == NODE:
                self.nodes.append(Node(element[NODE_NAME], element[NODE_ATTR]))
            elif element[TYPE] == EDGE:
                self.edges.append(Edge(element[EDGE_SRC], element[EDGE_DST], element[EDGE_ATTR]))
            elif element[TYPE] == ATTR:
                self.attrs[element[ATTR_NAME]] = element[ATTR_VAL]
