from collections import defaultdict


class graph:

    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for connect in self.graph[v]:
            if not visited[connect]:
                self.topologicalSortUtil(connect, visited, stack)
            stack.insert(0, v)

    def topologicalSort(self):
        visited = [False] * self.v
        stack = []

        for i in range(self.v):
            if not visited[i]:
                self.topologicalSortUtil(i,visited,stack)
            print(stack)