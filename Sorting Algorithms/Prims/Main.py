from pythonds import Graph
import timeit
from algorithms import Prims
from Stats import Display

graph = Graph()
Display.creategraph(Display, graph)
v = graph.getVertex(1)
testing = 10
exe = 0
exe2 = 0

# Prim 1
for i in range(testing):
    start_time = timeit.default_timer()
    Prims.prim1(Prims, graph, v)
    time = timeit.default_timer() - start_time
    exe += time
average = exe / testing
print("Prim 1 took:", average, 'on average')

'''

# Prim 2
for x in range(testing):
    start_time = timeit.default_timer()
    Prims.prim2(Prims, graph, v)
    time = timeit.default_timer() - start_time
    exe2 += time
average = exe2 / testing
print("Prim 2 took:", average, 'on average')

'''
