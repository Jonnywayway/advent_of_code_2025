from tqdm import tqdm
import pandas as pd


def part1(file):
    prev_row = None
    current_row = None
    split_count = 0
    with open(file, "r") as f:
        for line in tqdm(f):
            current_row = list(line.rstrip("\n"))
            # print(prev_row)
            # print(current_row)
            if prev_row == None:
                prev_row = current_row
                continue

            for idx, val in enumerate(current_row):
                if current_row[idx] == "^" and prev_row[idx] == "|":
                    current_row[idx - 1] = "|"
                    current_row[idx + 1] = "|"
                    split_count += 1
                if prev_row[idx] == "S":
                    current_row[idx] = "|"
                if prev_row[idx] == "|" and current_row[idx] != "^":
                    current_row[idx] = "|"
            print(current_row)
            prev_row = current_row
    print(split_count)


def part2(file):
    with open(file, "r") as f:
        grid = [list(line.rstrip("\n")) for line in f]

    rows = len(grid)
    cols = len(grid[0])
    # breakpoint()

    start_col = None
    for col in range(cols):
        if grid[0][col] == "S":
            start_col = col
            break

    timelines = [0] * cols
    timelines[start_col] = 1  # Start with 1 timeline

    # Process each row
    for row in range(1, rows):
        next_timelines = [0] * cols

        for col in range(cols):
            if timelines[col] > 0:
                if grid[row][col] == "^":
                    if col - 1 >= 0:
                        next_timelines[col - 1] += timelines[col]
                    if col + 1 < cols:
                        next_timelines[col + 1] += timelines[col]
                else:
                    next_timelines[col] += timelines[col]

        timelines = next_timelines

    # Total timelines is the sum of all active timelines at the bottom
    print(sum(timelines))


if __name__ == "__main__":
    file = "Day 7/test.txt"
    file = "Day 7/beam.txt"
    part1(file)
    part2(file)
