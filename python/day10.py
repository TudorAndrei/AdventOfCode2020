from my_tools import *
import numpy as np


def getAdjacentSeats(input_, i, j):
    adj_seat = []
    # L,R, U,D
    try:
        adj_seat.append(input_[i + 1, j])
    except:
        pass
    try:
        adj_seat.append(input_[i - 1, j])
    except:
        pass
    try:
        adj_seat.append(input_[i, j + 1])
    except:
        pass
    try:
        adj_seat.append(input_[i, j - 1])
    except:
        pass

    # Diagonal
    try:
        adj_seat.append(input_[i - 1, j - 1])
    except:
        pass
    try:
        adj_seat.append(input_[i + 1, j - 1])
    except:
        pass
    try:
        adj_seat.append(input_[i + 1, j + 1])
    except:
        pass
    try:
        adj_seat.append(input_[i - 1, j + 1])
    except:
        pass
    return adj_seat


def update(matrix, changes):
    for change in changes:


def check_seats(input_):
    generations = 0
    change = True
    while change:
        check = False
        generations += 1
        print(input_)
        to_chage = []
        for i in range(input_.shape[0]):
            for j in range(input_.shape[1]):
                if input_[i, j] == ".":
                    continue
                adj_seat = getAdjacentSeats(input_, i, j)
                if input_[i, j] == "L" and "#" not in adj_seat:
                    to_chage.append((i, j, '#'))
                if input_[i, j] == "#" and adj_seat.count("#") > 3:
                    to_chage.append((i, j, "L"))
        input_ = update(input_, to_chage)
    print(generations)
    return input_


a = read_file("../inputs/day10.txt")
a = read_file("../inputs/test10.txt")

l2 = []
for line in a:
    l2.append([x for x in line])

b = np.array(l2)

arr = check_seats(b)
print(arr)
exit()
print(sum(np.char.count(arr, "#")))
