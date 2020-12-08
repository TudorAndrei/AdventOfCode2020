import my_tools as mt
from copy import deepcopy


def run_code(input_commands, loop=False, aux_index=False):
    index = 0
    acc = 0
    while index <= len(input_commands) - 1:
        command = input_commands[index][0]
        if index == aux_index:
            if command == "nop":
                command = "jmp"
            elif command == "jmp":
                command = "nop"
        value = int(input_commands[index][1])
        visit = input_commands[index][2]
        if visit == 0:
            if loop:
                return acc
            return 0

        if command == "nop":
            input_commands[index][2] = 0

        if command == "acc":
            acc += value
            input_commands[index][2] = 0

        if command == "jmp":
            input_commands[index][2] = 0
            index += value
            if index != 0:
                continue

        index += 1
    return (acc)


def get_commands(input_):
    commands = []
    for line in input_:
        line = line.split()
        commands.append([line[0], line[1], 1])
    return (commands)


def par1(input_):
    return run_code(get_commands(input_), loop=True)


def par2(input_):
    commands = get_commands(input_)
    for index in range(0, len(commands)):
        if commands[index][0] in ["nop", "jmp"]:
            result = run_code(deepcopy(commands), aux_index=index)
            if result:
                return result
                continue


input_ = mt.read_file("../inputs/day8.txt")
print(par1(input_))
print(par2(input_))
