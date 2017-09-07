# KELAS GRAPH
# Buatlah kelas objek Graph

# FUNGSI PENCARIAN RUTE TERCEPAT
# Tulis algoritma disini...
#Graph tidak berarah dan tidak berbobot
class Graph():
	vertex = []
	edge = {}
			
	def addVertex(self, nama):
		if nama not in  self.vertex:
			self.vertex.append(nama)
	
	def addEdge(self, v1, v2, w):
		if v1 and v2 in self.vertex:
			if (v1, v2) not in self.edge:
				self.edge[(v1, v2)] = int(w)
			
	def showVertex(self):
		print("VERTEX : ", end="")
		for v in self.vertex:
			if v == self.vertex[len(self.vertex)-1]:
				print(v)
			else:
				print(v, end=", ")
	
	def showEdge(self):
		print("EDGE   : ")
		for e in self.edge:
			print("       :", e, "Bobot :",self.edge[e])
		
	def showGraph(self):
		self.showVertex()
		self.showEdge()
		print("\n\n")

	def Djikstra(self, Start, End):
		Dist = {}
		D = {}
		Q = self.vertex
		for k in self.vertex:
			Dist[k] = "~";
			print(k, ":", Dist[k])
		
		Dist[Start] = 0;

			
		
		
		
		
			
	

G = Graph()
G.addVertex("S")
G.addVertex("A")
G.addVertex("B")
G.addVertex("C")
G.addVertex("D")
G.addVertex("E")
G.addVertex("F")
G.addVertex("G")

G.addEdge("S","A",6)
G.addEdge("S","B",14)
G.addEdge("S","C",10)
G.addEdge("A","B",6)
G.addEdge("A","D",24)
G.addEdge("B","C",4)
G.addEdge("B","E",15)
G.addEdge("C","F",18)
G.addEdge("D","E",4)
G.addEdge("D","G",9)
G.addEdge("E","F",4)
G.addEdge("E","G",9)

G.showGraph()
G.Djikstra("S", "G")
