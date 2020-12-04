from tools import *
import numpy as np


a = read_file("inputs/day3.txt")

l2 = []
for line in a:
    l2.append([x for x in line])

b = np.array(l2)
count = 0


def search(matrix, right, down):
    x = y = count = 0

    while 1:
        x += down
        y = (y + right) % matrix.shape[1]

        count += 1 if matrix[x, y] == "#" else 0

        if x == matrix.shape[0] - 1:
            return count


directions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

result = 1
for d in directions:
    result *= search(b, d[0], d[1])

print(result)
