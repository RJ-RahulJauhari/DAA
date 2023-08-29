import sys

INF = sys.maxsize
v = 4


def printSol(dist):
    for row in range(v):
        for col in range(v):
            if row == col:
                print(1, end=" ")
            elif dist[row][col] == INF:
                print("INF", end=" ")
            else:
                print(dist[row][col], end=" ")
        print("\n")


def warshall(g):
    dist = [row[:] for row in g]

    for r in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = dist[i][j] or (dist[i][r] and dist[r][j])

    printSol(dist)


graph = [[1, 1, 0, 1],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [0, 0, 0, 1]]

warshall(graph)
