import numpy as np

# grid dimensions and walls
XMIN = YMIN = 0
XMAX = YMAX = 60
W1_X = 20
W1_YMIN = 0
W1_YMAX = 40
W2_X = 40
W2_YMIN = 20
W2_YMAX = 60

def y_converter(y):
    return abs(y - YMAX + 1)

# for graphic purposes
matrix = np.zeros((YMAX,XMAX))

# build the external walls
for i in range(YMIN,YMAX):
    matrix[YMIN][i] = 5
    matrix[YMAX-1][i] = 5
for i in range (XMIN, XMAX):
    matrix[i][XMIN] = 5
    matrix[i][XMAX-1] = 5
# build the internal walls (obstacles)
for i in range(0, 40):
    matrix[y_converter(W1_YMIN + i)][W1_X] = 5
    matrix[y_converter(W2_YMIN + i)][W2_X] = 5

def print_grid(filename):
    f = open(filename, "w+")
    for line in range(YMIN,YMAX):
        for column in range(XMIN,XMAX):
            f.write(str(int(matrix[line][column])))
            f.write(" ")
        f.write("\n")
    f.close()
