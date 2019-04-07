from search import *
from modelagem import *
p1 = robo((10, 10), (50, 50))
p2 = robo((50, 50), (10, 10))
p3 = robo((10, 50), (50, 10))
p4 = robo((50, 10), (10, 50))
p5 = robo((10,10), (10, 50))
p6 = robo((50, 10), (50, 50))
problems = [p2]
searchers = [breadth_first_graph_search, depth_first_graph_search, astar_search]
headers = ['search algorithm', 'sucessors/goal tests/ states generated/ solution']

compare_searchers(problems, headers, searchers)
