# KELAS GRAPH
# Buatlah kelas objek Graph
from collections import defaultdict
class Graph(object):
	def __init__(self):
		self.nodes = set()
		self.edges = defaultdict(list)
		self.distances = {}

	def add_node(self, value):
		self.nodes.add(value)

	def add_edge(self, from_node, to_node, distance):
		self.edges[from_node].append(to_node)
		self.edges[to_node].append(from_node)
		self.distances[(from_node, to_node)] = distance
		self.distances[(to_node, from_node)] = distance

# FUNGSI PENCARIAN RUTE TERCEPAT
# Tulis algoritma disini...
def dijkstra(graph, initial):
	visited = {initial: 0}
	path = {}

	nodes = set(graph.nodes)

	while nodes: 
		min_node = None
		for node in nodes:
			if node in visited:
				if min_node is None:
					min_node = node
				elif visited[node] < visited[min_node]:
					min_node = node
		if min_node is None:
			break

		nodes.remove(min_node)
		current_weight = visited[min_node]

		for edge in graph.edges[min_node]:
			weight = current_weight + graph.distances[(min_node, edge)]
			if edge not in visited or weight < visited[edge]:
				visited[edge] = weight
				path[edge] = min_node

	return visited,path

def shortest(graph,start,end):
	d,p = dijkstra(graph,start)
	path = []
	while 1:
		path.append(end)
		if end == start: break
		end = p[end]
	path.reverse()
	return path

g = Graph();
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_node('G')
g.add_node('S')

g.add_edge('S','B',14)
g.add_edge('S','A',6)
g.add_edge('S','C',10)
g.add_edge('B','A',6)
g.add_edge('B','C',4)
g.add_edge('B','E',15)
g.add_edge('C','F',18)
g.add_edge('A','D',24)
g.add_edge('D','E',4)
g.add_edge('E','F',4)
g.add_edge('F','G',9)
g.add_edge('G','D',9)
g.add_edge('E','G',9)

panjang_lintasan,lintasan = dijkstra(g,'S')
print("Lintasan : ",shortest(g,'S','G'))
print("Panjang Lintasan : ",panjang_lintasan['G'])