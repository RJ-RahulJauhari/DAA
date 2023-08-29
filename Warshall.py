from collections import defaultdict

class graph:
    def __init__(self,verticies):
        self.v = verticies

    def printSolution(self,reach):
        print("Following matrix transitive closure of the given graph")
        for i in range(self.v):
            for j in range(self.v):
                if i==j:
                    print("%7d\t"%(1))
                else:
                    print("%7d\t"%(reach[i][j]))

    def transitiveClosure(self,graph):
        reach = [i[:] for i in graph]

        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
        self.printSolution(reach)

g= graph(4)
graph = [[1, 1, 0, 1],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [0, 0, 0, 1]]

g.transitiveClosure(graph)