from modelagem import *
p1 = robot((10, 10), (50, 50))
p2 = robot((50, 50), (10, 10))
p3 = robot((10, 50), (50, 10))
p4 = robot((50, 10), (10, 50))
p5 = robot((10,10), (10, 50))
p6 = robot((50, 10), (50, 50))
problems = [p1, p2, p3, p4, p5, p6]
searchers = [breadth_first_graph_search, depth_first_graph_search, astar_search]
headers = ['search algorithm', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6']

f = open("data.txt", "w+")
for p in problems:
    f.write(str(p) + "\n")
    result_1 = breadth_first_graph_search(p)
    f.write("  breadth first graph search stats: \n    Path cost: ")
    f.write(str(result_1.path_cost))
    result_2 = depth_first_graph_search(p)
    f.write("\n\n  depth first graph search stats: \n    Path cost: ")
    f.write(str(result_2.path_cost))
    result_3 = astar_search(p)
    f.write("\n\n  A* search stats: \n    Path cost: ")
    f.write(str(result_1.path_cost) + "\n\n\n")
f.close()
#compare_searchers(problems, headers, searchers)
