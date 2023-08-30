from collections import defaultdict

class Graph:

    def __init__(self,verticies):
        self.v = verticies
        self.g = defaultdict(list)

    def addEdge(self,u,v):
        self.g[u].append(v)

    def TopologicalUtil(self,v,visited,stack):
        visited[v] = True
        for i in self.g[v]:
            if not visited[i]:
                self.TopologicalUtil(i,visited,stack)
        stack.insert(0,v)

    def TopoLogicalSort(self):
        stack = []
        visited = [False]*self.v

        for i in range(self.v):
            if not visited[i]:
                self.TopologicalUtil(i,visited,stack)
        print(stack)


g= Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 3)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)


g.TopoLogicalSort()

