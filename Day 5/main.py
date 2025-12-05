from tqdm import tqdm


def part1():
    paper_file = "Day 5/food.txt"
    items = False
    low_array = []
    high_array = []
    good_items = set()
    good_cand = []
    fresh_count = 0
    with open(paper_file, "r") as f:
        for line in tqdm(f):
            cleaned_line = line.rstrip("\n")
            print(cleaned_line)
            if cleaned_line == "":
                items = True
                continue
            if items == False:
                ids = cleaned_line.split("-")
                low_array = low_array + [int(ids[0])]
                high_array = high_array + [int(ids[1])]
            else:
                for iii in range(len(low_array)):
                    if (
                        int(cleaned_line) >= low_array[iii]
                        and int(cleaned_line) <= high_array[iii]
                    ):
                        fresh_count += 1
                        break
    print(fresh_count)


def part2():
    paper_file = "Day 5/test.txt"
    items = False
    pairs_array = []
    with open(paper_file, "r") as f:
        for line in tqdm(f):
            cleaned_line = line.rstrip("\n")
            print(cleaned_line)
            if cleaned_line == "":
                items = True
                continue
            if items == False:
                ids = cleaned_line.split("-")
                pairs_array.append([int(ids[0]), int(ids[1])])
                pairs_array.sort()
                merged = []

            else:
                for start, end in pairs_array:
                    if merged and start <= merged[-1][1] + 1:
                        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
                    else:
                        merged.append((start, end))
                    print(merged)
                total = sum(end - start + 1 for start, end in merged)
                print(total)
                return


if __name__ == "__main__":
    # part1()
    part2()
