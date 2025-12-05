import sys
import csv


#!/usr/bin/env python3
def part1():
    total = 0
    with open("Day 3/ids.txt", "r") as f:
        for line in f:
            cleaned_line = line.rstrip("\n")
            largest = cleaned_line[0]
            largest_index = 0
            for i, digit in enumerate(cleaned_line[:-1]):
                if digit > largest:
                    largest = digit
                    largest_index = i
            if largest_index == len(cleaned_line) - 1:
                print(1)
            second_larg = cleaned_line[largest_index + 1]
            for jjj, digit in enumerate(cleaned_line[largest_index + 1 :]):
                if digit > second_larg:
                    second_larg = digit
            # print(largest)
            # print(second_larg)
            # print("------------")
            total += int(largest + second_larg)
    print(total)


def reduce_batt_list(batlist, size):
    cur_best = ["0"] * size
    n = len(batlist)
    for i in range(n):
        for j in range(size):
            # for each position in the target, see if we can improve it.
            # we can only improve it if there are enough characters left
            # in the full line to fill the remaining positions.
            # If so, update the current best and reset all subsequent
            # positions to '0' to allow for future filling.
            if batlist[i] > cur_best[j] and n - i >= size - j:
                cur_best[j] = batlist[i]
                for k in range(j + 1, size):
                    cur_best[k] = "0"
                break
    return int("".join(cur_best))


def part2():
    total = 0
    with open("Day 3/ids.txt", "r") as f:
        for line in f:
            batt_array = []
            cleaned_line = line.rstrip("\n")
            total += reduce_batt_list(cleaned_line, 12)
    print(total)


if __name__ == "__main__":
    part1()
    part2()

    # 167090045807433 too low
    # 169349762274117
    # 1670900458074331 too high
