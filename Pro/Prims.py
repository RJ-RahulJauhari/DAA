import sys

INF = sys.maxsize

g = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

N = 5
no_edges = 0

selected_nodes = [0]*N
selected_nodes[0] = True

while no_edges < N-1:

    minimum = INF
    s = 0
    d = 0

    for node in range(N):
        if selected_nodes[node]:
            for connect in range(N):
                if (not selected_nodes[connect]) and g[node][connect]:
                    if minimum > g[node][connect]:
                        minimum = g[node][connect]
                        s = node
                        d = connect
    print(s, " connects to ", d, " Weight: ", g[s][d], '\n')
    no_edges += 1
    selected_nodes[d] = True

