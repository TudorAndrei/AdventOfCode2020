import my_tools as mt
from itertools import chain

a = mt.read_file("../inputs/day6.txt")

indices = [i for i, x in enumerate(a) if x == '']
pairs = zip(chain([0], indices), chain(indices, [None]))
groups = [a[i:j] for i, j in pairs]


count = 0


for ans in groups:
    ans = "".join(ans)
    ans = [x for x in ans]
    ans = set(ans)
    count += len(ans)

print(count)


# Part 2
alphabet = list(map(chr, range(97, 123)))
count = 0
for ans in groups:
    if ans[0] == '':
        ans = ans[1:]

    for letter in alphabet:
        check = 0
        for a in ans:
            if letter in a:
                check += 1
        if check == len(ans):
            count += 1

print(count)
