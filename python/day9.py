import my_tools as mt
from copy import deepcopy
import os


input_ = mt.read_file("../inputs/day9.txt")
test_ = mt.read_file("../inputs/test9.txt")
# print(test_)


def checker(list_, item):
    #print("Preable is {}".format(list_))
    # print(list_)
    for i in list_:
        value = abs(item - i)
        #print("{} - {} = {}".format(item, i, abs(item-i)))
        if value in list_ and value != item:
            return 0
    for i in list_:
        value = abs(item - i)
        #print("{} - {} = {}".format(item, i, value))
    return value


def getInvalidNumber(input_, preamble=5):
    input_ = [int(x) for x in input_]
    for i in range(len(input_) - preamble):
        #print("INDEX:", i)
        i += preamble
        result = checker(input_[i-preamble:i], input_[i])
        # print(result)
        if result == 0:
            continue
        else:
            return input_[i]


# print(part1(input_, 25))


def getInvalidSum(list_, invalid):

    for index in range(1, len(list_)):
        for start in range(index):
            contiguous_set = list_[start:index]
            if sum(contiguous_set) == invalid:
                return sorted(contiguous_set)[0] + sorted(contiguous_set)[-1]
    return 0


def part2(input_, preamble=5):
    input_ = [int(x) for x in input_]
    invalid = getInvalidNumber(input_, preamble)
    return getInvalidSum(input_, invalid)


print(part2(input_, preamble=5))
print(part2(input_, preamble=25))
