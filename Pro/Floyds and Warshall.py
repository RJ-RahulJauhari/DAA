class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.g = [[0 for col in range(vertices)] for row in range(vertices)]

    def floyd(self):
        dist = [row[:] for row in self.g]

        for k in range(self.v):
            for j in range(self.v):
                for i in range(self.v):
                    dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
        self.printSol(dist)

    def warshall(self):
        reach = [row[:] for row in self.g]

        for k in range(self.v):
            for j in range(self.v):
                for i in range(self.v):
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
        self.printSol(reach)

    def printSol(self,g):
        for i in range(self.v):
            for j in range(self.v):
                print(g[i][j], end=" ")
        print()

g = Graph(4)
INF = 99999999999
G = [[0, 5, INF, INF],
     [50, 0, 15, 5],
     [30, INF, 0, 15],
     [15, INF, 5, 0]]

graph = [[1, 1, 0, 1],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [0, 0, 0, 1]]
g.g = graph
g.warshall()
