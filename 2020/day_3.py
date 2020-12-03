"""
Link: www.adventofcode.com/2020/day/3
"""

import argparse
import csv
from functools import reduce
import re


def count_trees_hit_1(terrain_file):
    with open(terrain_file, 'r') as terrain:
        lines = terrain.readlines()
        
        max_height = len(lines)
        max_width = len(lines[0]) # Assumes each line is of equal length

        x = 3
        y = 1
        
        trees_hit = 0

        while x < max_height and y < max_width:         
            if lines[x][y] == "#":
                trees_hit += 1
            
            x += 3
            y += 1

        return trees_hit


if __name__ == "__main__":
    # Initialise argument parser
    prog = argparse.ArgumentParser()

    # Define arguments
    prog.add_argument("--file", "-f",
            help="File containing input.")

    # Parse argument
    args = prog.parse_args()

    terrain_file = args.file

    print("Part 1: ", count_trees_hit_1(terrain_file))
    # print("Part 2: ", count_trees_hit_2(passwords_file))
