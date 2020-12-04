from my_tools import read_file

a = read_file("../inputs/day4.txt")
test = read_file("../inputs/test4.txt")


def separat(l):
    new_l = []
    aux = []
    for a in l:
        aux.append(a)
        if not a:
            new_l.append(aux)
            aux = []

    return new_l


required_fiels = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def solve1(file):

    # print(separat(a))
    b = separat(file)
    required_fiels = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

    valid = 0

    c = [" ".join(x) for x in b]

    valid = 0
    for passport in c:
        field = sorted([x.split(":")[0]
                        for x in passport.split(" ")][:-1])
        try:
            field.remove("cid")
        except:
            pass

        check = 1

        for x, y in zip(required_fiels, field):
            if x != y:
                check = 0
                break

        print("F: {} \nR: {} \nC: {}\n\n".format(field, required_fiels, check))
        valid += check
    return valid


def valid_filed(field):
    value = field[1]
    field = field[0]

    if field == "byr" and (1920 <= int(value) <= 2002):
        return True
    if field == "iyr" and (2010 <= int(value) <= 2020):
        return True
    if field == "eyr" and (2010 <= int(value) <= 2030):
        return True
    if field == "hgt":
        if value == '':
            return False
        unit = value[-2:]
        value = value[0:-2]
        try:
            aux = int(value)
        except:
            return False
        if unit == "cm" and (150 <= int(value) <= 193):
            return True
        if unit == "in" and (59 <= int(value) <= 76):
            return True
    if field == "hcl" and value[0] == "#":
        return value[1:].isalnum()
    eyecl = ['amb', 'blu', 'brn', 'gry', 'hzl', 'oth']
    if field == "ecl" and (value in eyecl):
        return True
    if field == 'pid' and (len(value) == 9 and value.isnumeric()):
        return True
    if field == 'cid':
        return True

    return False


def solve2(file):
    # print(separat(a))
    b = separat(file)
    valid = 0
    c = [" ".join(x) for x in b]

    valid = 0
    for passport in c:
        fields = sorted([x.split(":")
                         for x in passport.split(" ")][:-1])
        if len(fields) < 7:
            continue

        check = [valid_filed(x) for x in fields]
        # print("Field: {} \n check {} \nvalid {} \n\n".format(
        #    fields, check, sum(check)))
        if sum(check) in [7, 8]:
            valid += 1
    return valid


print(solve2(a))
