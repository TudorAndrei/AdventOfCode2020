from my_tools import *

a = read_file("../inputs/day5.txt")


# Part1

def binary_partition(string, top, bottom, ticket):
    if len(ticket) == 1:
        return ticket[0]
    half = int(len(ticket)/2)

    if string[0] == top:
        return binary_partition(string[1:], top, bottom, ticket[:half])

    if string[0] == bottom:
        return binary_partition(string[1:], top, bottom, ticket[half:])


def ticket_id(string):
    row_ = binary_partition(string[:7], 'F', 'B', ticket=range(1, 128))
    col = binary_partition(string[-3:], 'L', 'R', ticket=range(0, 8))
    return row_ * 8 + col


tickets = sorted([ticket_id(ticket) for ticket in a])

print("Max is : {}".format(tickets[-1]))
# Part2

all_ticket = range(tickets[0], tickets[-1])

for t in all_ticket[8:-8]:
    if t not in tickets:
        print("My seat is {}".format(t))
        break
