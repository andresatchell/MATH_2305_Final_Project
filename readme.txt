About Program 

Definition of  Prim's algorithm

Prims, is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph. 
It finds a tree of that graph which includes every vertex and the total weight of all the edges in the tree is less than or equal to every possible spanning tree. 
Prim's algorithm is faster on dense graphs.

List of Functions
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________

****graph_operations**** 

The graph_operations function interacts with the graph data structure stored within the within in the "data" folder directory "...\MATH_2305_Final_Project\data" as XX.txt file.
Graph_operations is composed of six (6) defined functions: (good_edges, incident_edges, cost, initialize_tree, min_cost_incident_edge, total_cost_of_tree)


good_edges - Returns a list with all avalible edges that will not yeild a cycle edge/path

incident_edges - Returns all posible edges that are not in the tree. Essentially give you next avalible path to the next vertex. '''

cost - Returns the cost of an edge

initialize_tree - Returns an array that is in a workable format for out other functions while ging us a starting point'''
   
min_cost_incident_edge - Returns the edge with the minimum cost or shortest distance simple find the minimum in an array'''

total_cost_of_tree - Returns the total cost/weight of tree as it iterates through each individual edge.


****reading_writing_function****

The reading_writing_function works with numpy to load the stored .txt file input by the user.  The data file is then entered into the empty graph
by iterating through the txt file.  The data contained within the text file is converted into a workable array/tuple/dictionary structure.
The first two numbers in the graph reflects the edges while the third number reflects the weighting of the identified edge.


______________________________________________________________________________________________________________________________________________________________________________________________________
Algorithm

Prims algorithm makes use of the graph_operations and reading_writing_function(s) referenced above.
Prims is utilized to return the minimum sapning tree as well and the total cost of that tree. 
Upon determining a point of initialization Prims identifies available paths and chooses the mininum cost path and interates each edge.
