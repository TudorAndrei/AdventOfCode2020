from tools import read_file


a = read_file('inputs/day2.txt')
b = [x.split() for x in a]

# TODO: part1 of the exercise


def check(l):
    interval = [int(x)-1 for x in l[0].split("-")]
    string = l[2]
    letter = l[1][0]
    return((string[interval[0]] == letter and string[interval[1]] != letter)
           or (string[interval[1]] == letter and string[interval[0]] != letter))


count2 = [check(x) for x in b]
print(sum(count2))
