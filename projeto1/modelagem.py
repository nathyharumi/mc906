from search import *

XMIN = YMIN = 0
XMAX = YMAX = 60
W1_X = 20
W1_YMIN = 0
W1_YMAX = 40
W2_X = 40
W2_YMIN = 20
W2_YMAX = 60

def up(self, state):
    (X, Y) = state
    return (Y < YMAX - 1) and ((X, Y) != (W2_X, W2_YMIN))

def down(self, state):
    (X, Y) = state
    return (Y > YMIN + 1) and ((X, Y) != (W1_X, W1_YMAX))

def right(self, state):
    (X, Y) = state
    return not(X == W1_X - 1 and Y > W1_YMIN and Y < W1_YMAX) and \
    not(X == W2_X - 1 and Y > W2_YMIN and Y < W2_YMAX) and \
    X < XMAX - 1

def left(self, state):
    (X, Y) = state
    return not(X == W1_X + 1 and Y > W1_YMIN and Y < W1_YMAX) and \
    not(X == W2_X + 1 and Y > W2_YMIN and Y < W2_YMAX) and \
    X < XMIN + 1

class robo(Problem):
    def __init__(self, initial=(10,10), goal=(50,50)):
        self.initial = initial
        self.goal = goal
        self.visited_states = []

    def goal_test(self, state):
        return state == self.goal

    def __repr__(self):
        return "Robo(initial: {}, goal: {})".format(self.initial, self.goal)

    def actions(self, state):
        if up(self, state): yield'go_up'
        if down(self, state): yield'go_down'
        if right(self, state): yield'go_right'
        if left(self, state): yield'go_left'

    def result(self, state, action):
        (X, Y) = state
        if action == 'go_up': return (X, Y+1)
        elif action == 'go_down': return (X, Y-1)
        elif action == 'go_right': return (X+1, Y)
        elif action == 'go_left': return (X-1, Y)

    def h(self, node):
        (X, Y) = node.state
        (GX, GY) = self.goal
        return abs(GX - X) + abs(GY - Y)
