import sys


class Graph():

    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]


    def printSolution(self,dist):
        print("The distance from the source to the vertex is: ")
        for node in range(self.v):
            print("Vertex ",node," --distance--> ",dist[node])


    def minDistance(self,dist,visited):

        min = sys.maxsize
        min_node = None
        for node in range(self.v):
            if dist[node] < min and visited[node] == False:
                min = dist[node]
                min_node = node
        return min_node

    def dijikstra(self,src):

        dist = [sys.maxsize]*self.v
        dist[src] = 0
        visited = [False]*self.v

        for node in range(self.v):
            min_node = self.minDistance(dist,visited)
            visited[min_node] = True
            for to in range(self.v):
                cost = self.graph[min_node][to]
                if cost > 0 and (visited[to] == False) and dist[to] > dist[min_node] + cost:
                    dist[to] = dist[min_node] + cost

        self.printSolution(dist)

g = Graph(9)

g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
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