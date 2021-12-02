import re

def convert_to_tuples(path):
    with open(path) as input:
        entries = [str(entry.rstrip().replace(" ","")) for entry in input]
        results = [re.compile("([a-zA-Z]+)([0-9]+)").match(entry).groups() for entry in entries]
    return results

def submarine_movement(tuples):
    horizontal_movement = 0
    depth = 0
    for row in (tuples):
        if row[0] == "forward":
            horizontal_movement += int(row[1])
        elif row[0] == "down":
            depth += int(row[1])
        elif row[0] == "up":
            depth -= int(row[1])

    return depth * horizontal_movement

def submarine_movement_2(tuples):
    horizontal_movement = 0
    aim = 0
    depth = 0
    for x in (tuples):
        if x[0] == "forward":
            horizontal_movement += int(x[1])
            depth += int(x[1]) * aim
        elif x[0] == "down":
            aim += int(x[1])
        elif x[0] == "up":
            aim -= int(x[1])

    return depth * horizontal_movement

print(submarine_movement(convert_to_tuples('input.txt')))
print(submarine_movement_2(convert_to_tuples('input.txt')))