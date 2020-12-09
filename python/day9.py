import my_tools as mt
from copy import deepcopy
import os


input_ = mt.read_file("../inputs/day9.txt")
test_ = mt.read_file("../inputs/test9.txt")
# print(test_)


def checker(list_, item):
    #print("Preable is {}".format(list_))
    for i in list_:
        value = abs(item - i)
        print("{} - {} = {}".format(item, i, abs(item-i)))
        if value in list_ and value != item:
            return 0
    for i in list_:
        value = abs(item - i)
        print("{} - {} = {}".format(item, i, value))
    return value


def part1(input_, preamble=5):
    input_ = [int(x) for x in input_]
    for i in range(len(input_) - preamble):
        print("INDEX:", i)
        i += preamble
        result = checker(input_[i-preamble:i], input_[i])
        # print(result)
        if result == 0:
            continue
        else:
            return input_[i]


# print(part1(input_, 25))


def checker2(list_, item):
    print(list_)
    invalid = checker(list_, item)
    for index in range(len(list_)):
        cont_list = list_[index:]
        cont_list.append(item)
        value = sum(cont_list)
        if value == invalid:
            continue
        else:
            return min(cont_list) + max(cont_list)

    return 0


def part2(input_, preamble=5):
    input_ = [int(x) for x in input_]

    for i in range(len(input_) - preamble):
        print("INDEX:", i)
        i += preamble
        result = checker2(input_[i-preamble:i], input_[i])
        print(result)
        if result != 0:
            return result
        else:
            continue


print(part2(test_, preamble=5))
print(part2(input_, preamble=25))
