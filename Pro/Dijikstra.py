import sys


class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.g = [[0 for col in range(vertices)] for row in range(vertices)]

    def getMinNode(self, dist, visited):
        min = sys.maxsize
        min_index = None
        for i in range(self.v):
            if not visited[i] and dist[i] < min:
                min = dist[i]
                min_index = i
        return min_index

    def dijikstra(self, src):

        dist = [sys.maxsize] * self.v
        visited = [False] * self.v
        dist[src] = 0

        for node in range(self.v):
            min_node = self.getMinNode(dist, visited)
            visited[min_node] = True

            for to in range(self.v):
                cost = self.g[min_node][to]
                if cost > 0 and (not visited[to]) and dist[to] > dist[min_node] + cost:
                    dist[to] = dist[min_node] + cost
        print(dist)

g = Graph(9)
g.g =      [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijikstra(0)


