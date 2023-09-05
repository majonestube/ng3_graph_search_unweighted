import numpy as np
import matplotlib.pyplot as plt


def read_maze_text(maze_file_path):
    """ Read text file defining a maze 
    
    # Arguments:
    maze_file_path      String or pathlib.Path with text file path

    # Returns:
    maze_text           List with each text line, newline characters removed
    """
    with open(maze_file_path) as file:
        lines = []
        for line in file:
            lines.append(line.rstrip())
    return lines


def maze_text_to_graph(maze_text):
    """ Parse maze text and return graph as dict
    
    # Arguments:
    maze_text   List of maze text lines. 
                Walls in the maze are indicated with '#' symbols.
                Any other symbol is interpreted as open space (a node).
                A "wall" of '#'s surrounding the maze is assumed.
                The maze is assumed to be rectangular (each text 
                line is assumed to be equally long).

    graph:      A dict containing nodes and edges in the graph.
                The keys in the dict are 2-element tuples (y,x),
                where y and x are integers indicating node position.
                Position follows standard matrix / image indexing,
                with upper left corner being origo, x axis pointing 
                from left to right, and y axis pointing from top to bottom.
                The values in the dict are lists with neighbor nodes,
                which are also identified with (y,x) tuples.

    # Example:
    maze:       #####
                #...#
                #.###
                #####
    maze_text:  ['#####','#...#','#.###','#####']
    graph:     {(1, 1): [(2, 1), (1, 2)],
                (1, 2): [(1, 1), (1, 3)],
                (1, 3): [(1, 2)],
                (2, 1): [(1, 1)]}
    """
    graph = {}
    for i,line in enumerate(maze_text):
        for j,char in enumerate(line):
            if char != '#':                                                 # If maze tile is not blocked
                graph[(i,j)] = []                                           # Add tile (node) to graph dict
                if maze_text[i][j-1] != '#':                                # If valid node to the west
                    graph[(i,j)].append((i,j-1))    
                if maze_text[i+1][j] != '#':                                # If valid node to the south
                    graph[(i,j)].append((i+1,j))    
                if maze_text[i][j+1] != '#':                                # If valid node to the east
                    graph[(i,j)].append((i,j+1))   
                if maze_text[i-1][j] != '#':                                # If valid node to the north
                    graph[(i,j)].append((i-1,j))
    return graph


def maze_text_to_matrix(maze_text):
    """ Convert maze text into 2D matrix 
    
    # Arguments:
    maze_text   List of maze text lines. See parse_maze_text()

    # Returns:
    grid        NumPy 2D matrix with 0's indicating walls and 1's 
                indicating open space (nodes)

    # Notes:
    For easy visualization of a maze, plot the 2D matrix as an image.
    Example:
        grid = maze_text_to_matrix(['#####','#...#','#.###','#...#','#####'])
        import matplotlib.pyplot
        matplotlib.pyplot.imshow(grid)  # Show as image
    """
    n_rows = len(maze_text)
    n_cols = len(maze_text[0])
    grid = np.zeros((n_rows,n_cols),dtype=int)
    for i,line in enumerate(maze_text):
        for j,char in enumerate(line):
            if char == '#':
                grid[i,j] = 0
            else:
                grid[i,j] = 1
    return grid


def plot_maze_edges(edges):
    """ Plot edges between maze nodes as arrows

    # Arguments:
    edges:      Dict, key = (from) node, value = list of (to) nodes
    """
    for node in edges.keys():
        for neighbor in edges[node]:
            y0,x0 = node
            y,x = neighbor
            dy,dx = y-y0, x-x0
            plt.arrow(x=x0,y=y0,dx=0.8*dx,dy=0.8*dy,head_width=0.1)


def plot_visited(visited):
    """ Plot text labels indicating the order in which nodes are visited """
    for i,node in enumerate(visited):
        y,x = node
        plt.text(s=int(i),y=y,x=x)


def plot_came_from(came_from):
    """ Plot arrows indicating "came from" edges
    
    # Arguments:
    came_from   Dict, key = node, value = previous node (during graph traversal)
    """
    for node, neighbor in came_from.items():
        y0,x0 = node
        y,x = neighbor
        dy,dx = y-y0, x-x0
        plt.arrow(x=x0,y=y0,dx=0.8*dx,dy=0.8*dy,head_width=0.1)

def plot_path(path):
    for i in range(len(path)-1):
        y0,x0 = path[i]
        y,x = path[i+1]
        dy,dx = y-y0, x-x0
        plt.arrow(x=x0,y=y0,dx=0.8*dx,dy=0.8*dy,head_width=0.1)
