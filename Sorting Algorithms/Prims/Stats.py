class Display:
    def creategraph(self, graph):
        file = open('C_10_50.mis', 'r')
        newFile = file.read().split("\n")
        file.close()
        f = newFile[0].split()
        for i in range(1, int(f[2])):
            graph.addVertex(i)
        for i in range(1, len(newFile)-1):
            edge = newFile[i].split()
            edge[1] = int(edge[1])
            edge[2] = int(edge[2])
            graph.addEdge(edge[1], edge[2], ((edge[1]+edge[2]) % 200 + 1))
