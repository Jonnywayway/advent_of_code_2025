import cv2
import numpy as np


def read_pattern_to_array(file):
    with open(file, "r") as f:
        lines = f.readlines()
    lines = [line.rstrip() for line in lines if line.strip()]
    data = []
    for line in lines:
        row = [1 if char == "@" else 0 for char in line]
        data.append(row)

    return np.array(data, dtype=np.float32)


def part1():
    paper_file = "Day 4/paper.txt"
    paper_array = read_pattern_to_array(paper_file)
    mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.float32)
    convolved_paper = cv2.filter2D(
        paper_array, -1, mask, borderType=cv2.BORDER_CONSTANT
    )
    count = sum(convolved_paper[paper_array == 1] < 4)
    print(count)


def part2():
    paper_file = "Day 4/paper.txt"
    paper_array = read_pattern_to_array(paper_file)
    total = 0
    count = None
    while count != 0:
        mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.float32)
        convolved_paper = cv2.filter2D(
            paper_array, -1, mask, borderType=cv2.BORDER_CONSTANT
        )
        count = int(sum(convolved_paper[paper_array == 1] < 4))
        total += count
        paper_array[convolved_paper < 4] = 0
    print(total)


if __name__ == "__main__":
    part1()
    part2()
