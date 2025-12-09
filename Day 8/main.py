from tqdm import tqdm
import pandas as pd
from scipy.spatial import KDTree
import numpy as np


def part1():
    df = pd.read_csv("Day 8/wires.txt", header=None)
    array_of_points = df.to_numpy()
    tree = KDTree(array_of_points)
    df[4] = None
    conn_count = {}
    wire_count = 0
    for idx, each_row in enumerate(array_of_points):
        # check if already connected
        if df.loc[idx, 4] == None:
            distance, index = tree.query(each_row, k=2)
            print(distance)
            print(index)
            if df[4][index[1]] == None:
                # make new wire
                conn_count[wire_count] = 2
                df.loc[[index[1]], [4]] = wire_count
                df.loc[[index[0]], [4]] = wire_count
                wire_count += 1
            else:
                if df.loc[index[1], 4] is None:
                    wire = df.loc[index[0], 4]
                    onereal = False
                elif df.loc[index[0], 4] is None:
                    wire = df.loc[index[1], 4]
                    onereal = True
                else:
                    wire = max(df.loc[index[1], 4], df.loc[index[0], 4])
                print(conn_count)
                print(df.loc[index[1], 4])
                print(df.loc[index[0], 4])
                print(wire)
                print(wire_count)
                conn_count[wire] += 1
                if onereal:
                    df.loc[index[1], 4] = df.loc[index[0], 4]
                else:
                    df.loc[index[0], 4] = df.loc[index[1], 4]
    dict_vals = list(conn_count.values())
    dict_vals.sort()
    print()
    print(dict_vals[-1] * dict_vals[-2] * dict_vals[-3])
    # print(wire_count)
    # print(conn_count)

    return


def part2():
    return


if __name__ == "__main__":
    part1()
    part2()
