import sys


#!/usr/bin/env python3
def part1():
    with open("Day 1/dial.txt", "r") as f:
        current_pos = 50
        count = 0
        for line in f:
            if line[0] == "R":
                value = int(line[1:])
            elif line[0] == "L":
                value = -int(line[1:])
            new_pos = fix_pos(current_pos, value)
            if new_pos == 0:
                count += 1
            current_pos = new_pos
    print(count)


def fix_pos(current_pos, value):
    reduced = (current_pos + value) % 100
    if reduced < 0:
        reduced = reduced + 100
    return reduced


def part2():
    with open("Day 1/dial.txt", "r") as f:
        current_pos = 50
        count = 0
        for line in f:
            if line[0] == "R":
                value = int(line[1:])
            elif line[0] == "L":
                value = -int(line[1:])
            total_value = value + current_pos
            if total_value < 0 and current_pos != 0:
                count += 1
            if total_value == 0 and abs(total_value) < 100:
                count += 1
            count += abs(total_value) // 100
            new_pos = fix_pos(current_pos, value)
            # print(f"new pos : {new_pos}")
            # print(f"new total: {total_value}")
            # print(f"count total: {count}")
            current_pos = new_pos

    print(count)


if __name__ == "__main__":
    part1()
    part2()


# too low 6299
# too high 7151
