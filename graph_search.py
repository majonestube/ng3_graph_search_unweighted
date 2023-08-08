

def breadth_first_traverse(graph,start_node):
    """ Traverse a graph breadth-first
    
    # Arguments:
    graph:      Adjacency list as dictionary;
                    key = node name
                    value = iterable (e.g. list) with neighbor node names 
                Every node should have a key in the graph dict, 
                even if it has no neighbors.
    start_node: Start node (valid key in graph)

    # Returns:
    came_from:  Dictionary where key = node, value = previous node during traversal.
                If node B was discovered from node A, came_from[B] == A.
                The dict includes the start node, came_from[start_node] == None.
                The keys in the came_from dict also acts as a 
                list of all the nodes that have been discovered.
    """
    pass


def path_backtrack(start_node,end_node,came_from):
    """ Construct path from start to end node based on previous traversal 
    
    # Arguments:
    start_node:     Start node (unique identifier)
    end_node:       End node (unique identifier)
                    end_node must be present as a key in came_from
                    (i.e. it is reachable from start_node) 
    came_from:      Dict from previous traversal - see breadth_first_traverse()
                    key = node, value = previous node

    # Returns:
    path:           List, starting with start_node and ending with end_node,
                    containing all nodes on the path taken from start to end     
    """
    pass


def get_reachable_nodes(graph,start_node):
    """ Determine which nodes in a graph are reachable from a given start node

    # Arguments:
    graph:      Adjacency list as dictionary;
                    key = node name
                    value = iterable (e.g. list) with neighbor node names 
                Every node should have a key in the graph dict, 
                even if it has no neighbors.
    start_node: Start node (valid key in graph)
    
    # Returns:
    reachable_nodes:    A set (using set data type) of all the nodes
                        that are reachable from the start node.
    """
    pass


def breadth_first_search(graph,start_node,end_node):
    """ Search a graph for a single node breadth-first
    
    # Arguments:
    graph:      Adjacency list as dictionary;
                    key = node name
                    value = iterable (e.g. list) with neighbor node names 
                Every node should have a key in the graph dict, 
                even if it has no neighbors.
    start_node: Start node (valid key in graph)
    end_node:   End node (valid key in graph)

    # Returns:
    came_from:  Dictionary where key = node, value = previous node during search.
                If node B was discovered from node A, came_from[B] == A.
                The dict includes the start node, came_from[start_node] == None.
                The keys in the came_from dict also acts as a 
                list of all the nodes that have been discovered.
    path:       List, starting with start_node and ending with end_node,
                containing all nodes on the path taken from start to end
                If the end node is not reachable from the start node,
                path = None.
    """
    pass
