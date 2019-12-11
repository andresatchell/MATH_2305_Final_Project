from algorithms.prims_algorithms import Prims
import numpy as np
import os
from functions.reading_writing_function import get_graph
from functions.graph_operations import *

os.system("cls") # used to clear the console on windows machines


#File = input(' Input name of file that cotians the graph. :')




Graph = get_graph('FinalG') 

T = ([0, 2, 1, 9, 4, 5, 6, 3, 11, 7, 8], [(0, 2), (1, 2), (2, 9), (1, 4), (4, 5), (2, 6), (4, 3), (3, 11), (5, 7), (7, 8)])


a = incident_edges(Graph, T)
c = min_cost_incident_edge(Graph, T)



b=[]

for  i in a:
    b.append(cost(Graph, i))


print (T)
print (a)
print (b)
print (c)


