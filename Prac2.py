from collections import defaultdict


class Graph:

    def __init__(self, verticies):
        self.v = verticies
        self.g = defaultdict(list)

    def addEdge(self, u, v):
        self.g[u].append(v)

    def TopoLogicalUtil(self, v, visited, stack):
        visited[v] = True

        for i in self.g[v]:
            if not visited[i]:
                self.TopoLogicalUtil(i, visited, stack)
        stack.insert(0, v)

    def TopoLogicalSort(self):

        visited = [False]*self.v
        stack = []

        for i in range(self.v):
            if not visited[i]:
                self.TopoLogicalUtil(i,visited,stack)
        print(stack)


g= Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

g.TopoLogicalSort()