from my_tools import *

a = read_file("../inputs/day5.txt")


def row(string, ticket=range(0, 128)):
    #print(string, ticket)
    if len(ticket) == 1:
        return ticket[0]

    half = int(len(ticket)/2)

    if string[0] == 'F':
        return row(string[1:], ticket[:half])

    if string[0] == 'B':
        return row(string[1:], ticket[half:])


def column(string, col=range(0, 8)):
    x = [y for y in col]
    #print("String: {} \nx is {}".format(string, x))
    half = int(len(x) / 2)

    if len(x) == 1:
        return x

    if string[0] == 'L':
        return column(string[1:], col[:half])

    if string[0] == 'R':
        return column(string[1:], col[half:])


def ticket_id(string):
    row_ = row(string[:7])
    col = column(string[-3:])[0]
    # print(string)
    #print(row_, col)
    return row_ * 8 + col


tickets = []
for ticket in a:
    tickets.append(ticket_id(ticket))

seats = sorted(tickets)
print("Max is : {}".format(seats[-1]))
all_ticket = range(seats[0], seats[-1])

for t in all_ticket[8:-8]:
    if t not in tickets:
        print("My seat is {}".format(t))
        break
