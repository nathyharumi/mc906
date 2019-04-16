##
# Nathália Harumi Kuromiya - RA 175188
# Assignment 1
#
# This file is responsible for executing the problem to get statistics and
# compare searchers.
##

from modeling import *

p1 = robot((10, 10), (50, 50))
p2 = robot((50, 50), (10, 10))
p3 = robot((10, 50), (50, 10))
p4 = robot((50, 10), (10, 50))
p5 = robot((10,10), (10, 50))
p6 = robot((50, 10), (50, 50))

problems = [p1, p2, p3, p4, p5, p6]
searchers = [breadth_first_graph_search, depth_first_graph_search, astar_search]
headers = ['search algorithm', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6']

for p in problems:
    print(p, "\n")
    result_1 = breadth_first_graph_search(p)
    print("  BFS path cost: ", str(result_1.path_cost), "\n")
    result_2 = depth_first_graph_search(p)
    print("  DFS path cost: ", str(result_2.path_cost), "\n")
    result_3 = astar_search(p)
    print("  A* path cost: ", str(result_3.path_cost) + "\n\n")

compare_searchers(problems, headers, searchers)
