from tools import *

a = read_file("inputs/day1.txt")

b = [int(x) for x in a.split()]


def part1(b):
    for x in b:
        for y in b:
            if x != y and x+y == 2020:
                print(x*y)
                return


def part2(b):
    for x in b:
        for y in b:
            for z in b:
                if x != y != z and x+y+z == 2020:
                    print(x*y*z)
                    return


part1(b)
part2(b)
