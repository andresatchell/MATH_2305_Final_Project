from algorithms.prims_algorithms import Prims
from functions.reading_writing_function import get_graph
from functions.graph_operations import *
import os

os.system("cls") # used to clear the console on windows machines

Graph = get_graph('FinalG') 

#starting_point = int( input(f' {Graph[0]} \n Pick a vertex. :')) 
starting_point = 0

minimum_spanning_tree = Prims(Graph, starting_point)

cost_of_tree = total_cost_of_tree(Graph, minimum_spanning_tree)

vertices, edges = minimum_spanning_tree


print (f'''\n The minimun spanining tree 
 Vetices: {vertices}, total: {len(vertices)}
 Edges : {edges}, total: {len(edges)} 
 Total cost of the tree: {total_cost_of_tree(Graph, minimum_spanning_tree)} ''')

