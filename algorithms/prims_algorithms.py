from functions.graph_operations import min_cost_incident_edge, incident_edges, initialize_tree, cost, GE


def Prims(Graph, Starting_point):
    '''Returns the minimum sapning tree as well and the total cost of that tree. 
    Return format ( [[],()] )
    
    '''

    Tree = initialize_tree(Starting_point)


    #while (len(Tree[0]) = len(Graph[0])):                          #while the length of the tree's vertices is not the same lenght of the graph's vertices than do the operation 
   
    avalible_paths = GE(Graph, Tree)

    a = len(avalible_paths
    
    
    )
    while (len(avalible_paths) != 0 ):                          #while the length of the tree's vertices is not the same lenght of the graph's vertices than do the operation 


        avalible_paths = GE(Graph, Tree)          
        path_to_take = min_cost_incident_edge(Graph, Tree)


       
        for path in avalible_paths:
            for vertex in path:

                if (vertex not in Tree[0]) and ( path == path_to_take) :  #Only allows for the smallest path to be taken and adds that path/edge to our working tree  
                    Tree[1].append(path)
                    Tree[0].append(vertex)
                    print (Tree)
                    path_to_take = min_cost_incident_edge(Graph, Tree)
        avalible_paths = GE(Graph, Tree)

    return Tree

