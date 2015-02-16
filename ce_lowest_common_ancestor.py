import sys


def read_file(filename):
    """
    cleans input data up
    """
    with open(filename, "r") as f_in:
        raw_data = f_in.readlines()
    raw_data = map(lambda s: s.strip().split(" "), raw_data)
    return raw_data


class Graph(dict):
    def __init__(self, vs=[], es=[]):
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)

    def add_vertex(self, vertex):
        if vertex not in self:
            self[vertex] = {}

    def add_edge(self, edge):
        v, w = edge
        self[v][w] = edge
        self[w][v] = edge

    def vertices(self):
        return self.keys()

    def out_vertices(self, vertex):
        return self[vertex].keys()

    def out_edges(self, vertex):
        edges = []
        if vertex in self:
            for linked in self[vertex].values():
                edges.append(linked)
        return edges

    def find_ancestors(self, vertex):
        pass






class Vertex(object):
    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__


class Edge(tuple):
    def __new__(cls, start, end):
        return tuple.__new__(cls, (start, end))

    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__



def make_graph():
    nodes, edges = {}, []
    for node in [30, 8, 52, 3, 20, 10, 29]:
        nodes[node] = Vertex("node_{0}".format(node))
    edges.append(Edge(nodes[30], nodes[8]))
    edges.append(Edge(nodes[30], nodes[52]))
    edges.append(Edge(nodes[8], nodes[3]))
    edges.append(Edge(nodes[8], nodes[20]))
    edges.append(Edge(nodes[20], nodes[10]))
    edges.append(Edge(nodes[20], nodes[29]))
    graph = Graph(nodes.values(), edges)
    return graph, nodes







#test_cases = sys.argv[1]
test_cases = "codeeval.txt"
data = read_file(test_cases)
graph, node_dict = make_graph()
print graph.find_ancestors(node_dict[8])


