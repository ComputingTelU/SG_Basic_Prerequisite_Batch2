# KELAS GRAPH
# Buatlah kelas objek Graph
import math


class Graph:

    def __init__(self, vertices, node):
        self.V = vertices
        self.node = graph

    # FUNGSI PENCARIAN RUTE TERCEPAT
    # Tulis algoritma disini...

    def print_path(self, parent, dest):
        j = dest
        while parent[j] != -1:
            print(j,", ")
            j = parent[j]
        print(j)

    def print_solution(self, dist, parent):
        src = 0
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(1, len(dist)):
            self.print_path(parent, i)

    def min_distance(self, dist, queue):
        minimum = math.inf
        min_index = -1
        for i in range(self.V):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    def djikstra(self, src, dest):

        dist = [math.inf] * self.V
        dist[src] = 0

        parent = [-1] * self.V

        queue = []
        for i in range(self.V):
            queue.append(i)

        while queue:
            u = self.min_distance(dist, queue)

            queue.remove(u)

            for i in range(self.V):
                if self.node[u][i] and i in queue:
                    if dist[u] + self.node[u][i] < dist[i]:
                        dist[i] = dist[u] + self.node[u][i]
                        parent[i] = u

        self.print_path(parent, dest)

graph = [
        [0, 6, 14, 10, 0, 0, 0, 0],
        [6, 0, 6, 0, 24, 0, 0, 0],
        [14, 6, 0, 4, 0, 15, 0, 0],
        [10, 0, 4, 0, 18, 0, 0, 0],
        [0, 24, 0, 18, 0, 4, 0, 9],
        [0, 0, 15, 0, 4, 0, 4, 9],
        [0, 0, 0, 0, 0, 4, 0, 9],
        [0, 0, 0, 0, 9, 9, 9, 0]
        ]
g = Graph(8, graph)
g.djikstra(0,7)
