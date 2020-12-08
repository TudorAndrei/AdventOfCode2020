import my_tools as mt
import regex as re


bags = '(\d\ \w*\ \w*)'


def parser(input_string):
    # this function returns a dictionary
    # name { name: size, name:size, ... }
    string = input_string.split("bag")
    bag_name = string[0:1][0]
    bag_name = bag_name.strip()
    contents = re.findall(bags, input_string)
    result = {}
    # list of dicts
    for element in contents:
        result.update(
            {" ".join(element.split(" ")[1:]).strip(): element.split(" ")[0]})

    return {bag_name: result}


def calculator(kb, item):
    kb.pop(item)
    empty = []
    for x in kb:
        if kb[x] == {}:
            empty.append(x)

    for x in empty:
        kb.pop(x)

    has_item = set()
    for x in kb:
        if item in list(kb[x].keys()):
            has_item.add(x)
            print(x)

    for x in has_item:
        kb.pop(x)

    limit = 100
    while kb and limit:
        to_remove = 0
        for x in kb:
            out = any(check in kb[x] for check in has_item)
            if out:
                has_item.add(x)
            else:
                limit += -1

        for x in has_item:
            try:
                kb.pop(x)
            except:
                continue
        print(len(has_item))


def depth_calc(kb, item):
    print(item)
    print(kb[item])
    if kb[item] == {}:
        return 1
    result = 0
    for x in kb[item]:

        value = depth_calc(kb, x)
        if value == 1:
            aux = int(kb[item][x]) * value
        else:
            aux = int(kb[item][x]) * value + int(kb[item][x])
        result = result + aux

    return result


lists = mt.read_file("../inputs/day7.txt")
test_text = mt.read_file("../inputs/test7.txt")
test_text2 = mt.read_file("../inputs/test7_2.txt")

input_ = lists

aux = [parser(x) for x in input_]
ex2 = {}
for a in aux:
    ex2.update(a)

item = "shiny gold"
print(depth_calc(ex2, item))

# calculator(ex2, item2)
