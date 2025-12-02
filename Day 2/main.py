import sys
import csv


#!/usr/bin/env python3
def part1():
    total = 0
    file = "Day 2/ids.txt"
    file_test = "Day 2/test.txt"
    with open(file, "r") as f:
        first_line = f.readline()
        sets = first_line.split(",")
        for i, row in enumerate(sets):
            ids = row.split("-")
            for id in range(int(ids[0]), int(ids[1]) + 1):
                # print(f"id : {id}")
                # print(f"add: {checkrepeat(id)}")
                # print(f"new total: {total+checkrepeat(id)}")
                total += checkrepeat(id)
    print(total)


def checkrepeat(id):
    if (len(str(id)) % 2) != 0:
        # NOT REPEAT
        return 0
    else:
        id = str(id)
        mid = len(id) // 2  # Integer division to get the middle index
        first_half = id[:mid]
        second_half = id[mid:]
        if first_half == second_half:
            return int(id)
        else:
            return 0


def checkrepeat_n(id):
    id = str(id)
    for iii in range(1, (len(str(id)) // 2) + 1):
        if (len(str(id)) % iii) != 0:
            # NOT REPEAT
            pass
        else:
            chunks = [id[i : i + iii] for i in range(0, len(id), iii)]
            if all(s == chunks[0] for s in chunks):
                return int(id)
            else:
                pass
    return 0


def part2():
    total = 0
    file = "Day 2/ids.txt"
    file_test = "Day 2/test.txt"
    with open(file, "r") as f:
        first_line = f.readline()
        sets = first_line.split(",")
        for i, row in enumerate(sets):
            ids = row.split("-")
            for id in range(int(ids[0]), int(ids[1]) + 1):
                # print(f"id : {id}")
                # print(f"add: {checkrepeat_n(id)}")
                # print(f"new total: {total+checkrepeat_n(id)}")
                total += checkrepeat_n(id)
    print(total)


if __name__ == "__main__":
    part1()
    part2()
