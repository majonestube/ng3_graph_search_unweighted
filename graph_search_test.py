import graph_tools as gt
import graph_search as gs

#------------------------
# Breadth-first traverse
#------------------------
def test_bft_linked_list(): # 2p
    graph = {'A':['B'],'B':['A','C'],'C':['B']}
    came_from = gs.breadth_first_traverse(graph,'A')
    assert came_from == {'A':None,'B':'A','C':'B'}

def test_bft_3way_maze(): # 2p
    maze_text = gt.read_maze_text('mazes/maze_3way.txt')
    graph = gt.maze_text_to_graph(maze_text)
    came_from = gs.breadth_first_traverse(graph,(1,3))
    assert came_from[(1,2)] == (1,3)    # Correct previous node
    assert came_from[(3,4)] == (3,3)    # Correct previous node

def test_bft_empty_room(): # 2p
    # Start in middle of empty room. Nodes at middle of each wall should come from node closest to start node
    graph = gt.maze_text_to_graph(gt.read_maze_text('mazes/maze_empty_room.txt'))
    came_from = gs.breadth_first_traverse(graph,(3,3))
    assert came_from[(1,3)] == (2,3)    
    assert came_from[(3,1)] == (3,2)
    assert came_from[(3,5)] == (3,4)
    assert came_from[(5,3)] == (4,3)


#-------------------
# Path backtracking
#-------------------
def test_path_backtrack(): # 3p
    came_from = {'A':None,'B':'A','C':'A','D':'C'}
    assert gs.path_backtrack('A','B',came_from) == ['A','B']
    assert gs.path_backtrack('A','D',came_from) == ['A','C','D']
    assert gs.path_backtrack('A','A',came_from) == ['A']


#-----------------
# Reachable nodes
#-----------------
def test_get_reachable_nodes_linked_list(): # 1p
    graph = {'A':['B'],'B':['C'],'C':[]}  # A -> B -> C
    assert {'A','B','C'} == gs.get_reachable_nodes(graph,'A')
    assert {'B','C'} == gs.get_reachable_nodes(graph,'B')
    assert {'C'} == gs.get_reachable_nodes(graph,'C')

def test_get_reachable_nodes_maze(): # 2p
    graph = gt.maze_text_to_graph(gt.read_maze_text('mazes/maze_disconnected.txt'))
    assert {(1,4),(2,4),(3,4),(3,3)} == gs.get_reachable_nodes(graph,(3,3))    

def test_get_reachable_nodes_digraph(): # 2p
    graph = {1:[2,3,4],2:[5,6,7],3:[4],4:[],5:[8],6:[],7:[9],8:[7],9:[]}
    assert {1,2,3,4,5,6,7,8,9} == gs.get_reachable_nodes(graph,1)
    assert {2,5,6,7,8,9} == gs.get_reachable_nodes(graph,2)
    assert {5,7,8,9} == gs.get_reachable_nodes(graph,5)
    assert {3,4} == gs.get_reachable_nodes(graph,3)
    assert {6} == gs.get_reachable_nodes(graph,6)


#----------------------
# Breadth-first search
#----------------------
def test_bfs_linked_list(): # 2p
    graph = {'A':['B'],'B':['A','C'],'C':['B']}
    came_from, path = gs.breadth_first_search(graph,'A','C')
    assert came_from == {'A':None,'B':'A','C':'B'}
    assert path == ['A','B','C']
    came_from, path = gs.breadth_first_search(graph,'B','A')
    assert came_from == {'B':None,'A':'B','C':'B'}
    assert path == ['B','A']
    came_from, path = gs.breadth_first_search(graph,'C','C')
    assert came_from == {'C':None}
    assert path == ['C']

def test_bfs_3way_maze(): # 2p
    maze_text = gt.read_maze_text('mazes/maze_3way.txt')
    graph = gt.maze_text_to_graph(maze_text)
    came_from, path = gs.breadth_first_search(graph,(1,3),(3,4))
    # All nodes closer than end node should have been visited
    for node in [(1,3),(1,2),(2,3),(1,4),(1,1),(3,3),(1,5)]:
        assert node in came_from
    # Check correct path between start and end
    assert path == [(1,3),(2,3),(3,3),(3,4)]

def test_bfs_empty_room(): # 2p
    graph = gt.maze_text_to_graph(gt.read_maze_text('mazes/maze_empty_room.txt'))
    # Start in upper left corner, go down
    came_from,path = gs.breadth_first_search(graph,(1,1),(4,1))
    for node in [(1,1),(1,2),(2,1),(1,3),(2,2),(3,1)]:
        assert node in came_from
    assert path == [(1,1),(2,1),(3,1),(4,1)]  
    assert len(came_from) <= 10

    # Start and end not on same vertical and horizontal level
    _,path = gs.breadth_first_search(graph,(4,5),(2,1))
    assert len(path) == 7

def test_bfs_disconnected(): # 2p
    graph = gt.maze_text_to_graph(gt.read_maze_text('mazes/maze_disconnected.txt'))
    came_from,path = gs.breadth_first_search(graph,(1,1),(3,3))
    for node in [(1,1),(1,2),(2,1),(3,1)]:
        assert node in came_from
    assert path is None