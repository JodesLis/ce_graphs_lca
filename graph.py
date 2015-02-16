from pprint import pprint


class Graph(dict):
    def __init__(self, vs=[], es=[]):
        """
        Creates a new graph
        :param vs: list of vertices
        :param es: list of edges
        """
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)

    def add_vertex(self, vertex):
        """
        Adds vertex to graph
        :param vertex: vertex to add
        """
        if vertex not in self:
            self[vertex] = {}

    def add_edge(self, edge):
        """
        Adds edge to graph by adding entry in
        both directions. Will replace an
        existing edge if one exists
        :param edge: edge to add to graph
        """
        v, w = edge
        self[v][w] = edge
        self[w][v] = edge

    def get_edge(self, vertex_1, vertex_2):
        """
        :return: the edge between the two vertexes,
        or None otherwise.
        """
        try:
            return self[vertex_1][vertex_2]
        except:
            return None

    def remove_edge(self, edge):
        """
        Removes all references to edge from graph
        :param edge: Edge to remove
        """
        v, w = edge
        del self[v][w]
        del self[w][v]

    def vertices(self):
        """
        :return: List of vertices in graph
        """
        return self.keys()

    def edges(self):
        """
        :return: List of edges in graph
        """
        out_edges = set()
        for vertex in self.keys():
            for linked in self[vertex].values():
                out_edges.add(linked)
        return list(out_edges)

    def out_vertices(self, vertex):
        """
        :param vertex: Target vertex in graph
        :return: List of connected vertices
        """
        if vertex in self:
            return self[vertex].keys()
        else:
            return []

    def out_edges(self, vertex):
        """
        :param vertex: Vertex in graph
        :return: List of edges connected to vertex
        """
        edges = []
        if vertex in self:
            for linked in self[vertex].values():
                edges.append(linked)
        return edges

    def add_all_edges(self):
        """
        Starting with edgeless graph, connects
        all vertices by adding edges
        """
        for vertex in self.keys():
            for connection in self.keys():
                if vertex != connection:
                    self[vertex][connection] = Edge(vertex, connection)
                    self[connection][vertex] = Edge(connection, vertex)

    def add_regular_edges(self, n=1):
        """
        See page 14 (abs 28)
        Takes edgeless graph and adds edges to
        make every vertex have the same degree
        :n: degree of vertices
        """
        pass


class Vertex(object):
    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__


class Edge(tuple):
    def __new__(cls, start, end):
        """
        Python invokes new to create object, then
        init to initialise the attributes. Here, we're
        using a immutable object so want to override and
        be able to use the parameters to create the object
        :param cls:
        :param start: start vertex
        :param end: end vertex
        :return: new edge tuple
        """
        return tuple.__new__(cls, (start, end))

    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__


# v = Vertex('first vertex')
# w = Vertex('second vertex')
# f = Vertex('third vertex')
# # e = Edge(v, w)
# # edge_2 = Edge(v, f)
# graph = Graph([v, w, f], [])
# pprint(graph)
# print ""
# graph.add_all_edges()
# pprint(graph)

