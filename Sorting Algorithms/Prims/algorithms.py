from pythonds.graphs.priorityQueue import PriorityQueue
import sys


class Prims:
    def prim1(self, graph, v):
        queue = PriorityQueue()
        for i in graph:
            i.setDistance(sys.maxsize)
            i.setPred(None)
        v.setDistance(0)
        queue.buildHeap([(i.getDistance(), i) for i in graph])
        while not queue.isEmpty():
            current = queue.delMin()
            for vertex in current.getConnections():
                weight = current.getWeight(vertex)
                if vertex in queue and weight < vertex.getDistance():
                    vertex.setPred(current)
                    vertex.setDistance(weight)
                    queue.decreaseKey(vertex, weight)
'''
    def prim2(self, graph, v):
        matrix = {}
        for l, i in graph.vertices.items():
            matrix[l] = {}
            for vertex in i.getConnections():
                matrix[l][vertex.getId()] = i.getWeight(vertex)
        remaining = list(matrix)
        current = v.getId()
        remaining.remove(v.getId())
        while len(remaining) > 0:
            edge = list(matrix[current])
            smallest = sys.maxsize
            vert = None
            for i in edge:
                if matrix[current][i] < smallest:
                    smallest = matrix[current][i]
                    vert = i
            current = vert
            remaining.remove(current)

'''
