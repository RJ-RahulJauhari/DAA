import sys

v = 4
INF = sys.maxsize


def floyd(g):
    dist = [row[:] for row in g]
    for r in range(v):
        for j in range(v):
            for i in range(v):
                dist[i][j] = min(dist[i][j],dist[i][r] + dist[r][j])
    sol(dist)


def sol(dist):
    for i in range(v):
        for j in range(v):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j],end=" ")
        print(" ")


G = [[0, 5, INF, INF],
     [50, 0, 15, 5],
     [30, INF, 0, 15],
     [15, INF, 5, 0]]


floyd(G)

