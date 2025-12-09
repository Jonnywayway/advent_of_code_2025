from tqdm import tqdm
import pandas as pd


def part1():
    df = pd.read_csv("Day 6/homework.txt", sep="\s+", header=None)
    df_numbers = df.iloc[:-1].astype(int)  # First 3 rows (numeric data)
    df_operators = df.iloc[-1:]
    col_products = df_numbers.loc[:, (df_operators == "*").iloc[0]].apply(
        lambda row: row.prod(), axis=0
    )
    col_add = df_numbers.loc[:, (df_operators == "+").iloc[0]].apply(
        lambda row: row.sum(), axis=0
    )
    print(col_add.sum() + col_products.sum())
    return col_add.sum() + col_products.sum()


def part2():

    with open("Day 6/homework.txt", "r") as f:
        input_text = f.read()

    lines = input_text.strip().split("\n")
    max_width = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_width) for line in lines]
    operator_line = padded_lines[-1]
    number_lines = padded_lines[:-1]

    problems = []
    for col in range(max_width - 1, -1, -1):
        op = operator_line[col]
        if op not in ["+", "*"]:
            continue

        numbers = []
        for row in number_lines:
            if col < len(row) and row[col].strip():
                digit = row[col]
                if digit.isdigit():
                    numbers.append(digit)

        if numbers:
            number = int("".join(numbers))
            problems.append((op, [number]))

    problems = []
    current_numbers = []

    for col in range(max_width - 1, -1, -1):
        op = operator_line[col]
        digits = []
        for row in number_lines:
            if col < len(row):
                ch = row[col]
                if ch.isdigit():
                    digits.append(ch)

        if digits:
            num = int("".join(digits))
            current_numbers.append(num)

        if op in ["+", "*"]:
            if current_numbers:
                problems.append((op, current_numbers[::-1]))
                current_numbers = []

    results = []
    for op, nums in problems:
        if op == "+":
            result = sum(nums)
        else:  # op == '*'
            result = 1
            for n in nums:
                result *= n
        results.append(result)
        print(f"{' {op} '.join(map(str, nums))} = {result}")

    grand_total = sum(results)
    print(f"\nGrand Total: {grand_total}")
    return grand_total


if __name__ == "__main__":
    part1()
    part2()
