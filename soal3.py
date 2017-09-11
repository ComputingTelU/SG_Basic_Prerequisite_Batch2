# KELAS GRAPH
# Buatlah kelas objek Graph
class Graph(object):

	def __init__(self, graph_dict=None):
	    if graph_dict == None:
	        graph_dict = {}
	    self.__graph_dict = graph_dict

	def getVertices(self):
	    #mengembalikan semua vertex pada graf
	    return list(self.__graph_dict.keys())

	def getEdges(self):
	    #mengembalikan semua sisi pada graf
	    return self.__generate_edges()

	def add_vertex(self, vertex):
	    if vertex not in self.__graph_dict:
	        self.__graph_dict[vertex] = []

	def add_edge(self, edge):
	    edge = set(edge)
	    (vertex1, vertex2) = tuple(edge)
	    if vertex1 in self.__graph_dict:
	        self.__graph_dict[vertex1].append(vertex2)
	    else:
	        self.__graph_dict[vertex1] = [vertex2]

	def __generate_edges(self):
	    #menghasilkan semua sisi pada graf
	    edges = []
	    for vertex in self.__graph_dict:
	        for neighbour in self.__graph_dict[vertex]:
	            if {neighbour, vertex} not in edges:
	                edges.append({vertex, neighbour})
	    return edges

	def __str__(self):
	    res = "vertices: "
	    for k in self.__graph_dict:
	        res += str(k) + " "
	    res += "\nedges: "
	    for edge in self.__generate_edges():
	        res += str(edge) + " "
	    return res

	def __getitem__(self,vertex):
		return self.__graph_dict[vertex]

# FUNGSI PENCARIAN RUTE TERCEPAT
# Tulis algoritma disini...
