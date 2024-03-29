##
# Nathália Harumi Kuromiya - RA 175188
# Assignment 1
#
# This file is responsible for modeling the problem, including the state
# format, the initial and goal state, the path cost, the goal test, the 
# actions, the result and the heristic functions
##

from search import *
from grid import *

class robot(Problem):
    def __init__(self, initial=(10,10), goal=(50,50)):
        self.initial = initial
        self.goal = goal

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        if action == 'go_up' or action == 'go_down' or action == 'go_right' or \
        action == 'go_left':
            return c + 1
        else:
            return c + 2**(1/2)

    def __repr__(self):
        return "Robot(initial: {}, goal: {})".format(self.initial, self.goal)

    def actions(self, state):
        if self.up(state): yield'go_up'
        if self.down(state): yield'go_down'
        if self.right(state): yield'go_right'
        if self.left(state): yield'go_left'
        #diagonals
        (X, Y) = state
        if self.up((X+1, Y)) and self.right((X, Y+1)): yield'go_upright'
        if self.up((X-1, Y)) and self.left((X, Y+1)): yield'go_upleft'
        if self.down((X+1, Y)) and self.right((X, Y-1)): yield'go_downright'
        if self.down((X-1, Y)) and self.left((X, Y-1)): yield'go_downleft'

    def result(self, state, action):
        (X, Y) = state
        global matrix
        matrix[y_converter(Y)][X] = 1
        if action == 'go_up': return (X, Y+1)
        elif action == 'go_down': return (X, Y-1)
        elif action == 'go_right': return (X+1, Y)
        elif action == 'go_left': return (X-1, Y)
        elif action == 'go_upright': return (X+1, Y+1)
        elif action == 'go_upleft': return (X-1, Y+1)
        elif action == 'go_downright': return (X+1, Y-1)
        elif action == 'go_downleft': return (X-1, Y-1)

    def h(self, node):
        (X, Y) = node.state
        (GX, GY) = self.goal

        ## 100 times Manhattan Heuristic Function
        return 100*(abs(GX - X) + abs(GY - Y))

        ## Straight-line distance
        #return ((X - GX)**2 + (Y - GY)**2)**(1/2)

    # these functions define if its possible to go to a specific direction
    def up(self, state):
        (X, Y) = state
        return (Y < YMAX - 2) and ((X, Y) != (W2_X, W2_YMIN))

    def down(self, state):
        (X, Y) = state
        return (Y > YMIN + 1) and ((X, Y) != (W1_X, W1_YMAX))

    def right(self, state):
        (X, Y) = state
        return not(X == W1_X - 1 and Y > W1_YMIN and Y < W1_YMAX) and \
        not(X == W2_X - 1 and Y > W2_YMIN and Y < W2_YMAX) and \
        X < XMAX - 2

    def left(self, state):
        (X, Y) = state
        return not(X == W1_X + 1 and Y > W1_YMIN and Y < W1_YMAX) and \
        not(X == W2_X + 1 and Y > W2_YMIN and Y < W2_YMAX) and \
        X > XMIN + 1
