"""
Link: www.adventofcode.com/2020/day/3
"""

import argparse
import csv
from functools import reduce
import re


def count_trees_hit_2(terrain_file, slopes):
    with open(terrain_file, 'r') as terrain:
        lines = terrain.readlines()
        
        max_height = len(lines)
        max_width = len(lines[0].strip()) # Assumes each line is of equal length

        multiplier = 1

        for slope in slopes:
            (x_incr, y_incr) = slope

            x = x_incr
            y = y_incr
            
            trees_hit = 0

            while y < max_height:
                line = lines[y].strip()
                cell = line[x]
            
                if cell == "#":
                    trees_hit += 1
                
                x = (x + x_incr) % max_width
                y += y_incr

            if trees_hit:
                multiplier *= trees_hit

        return multiplier


def count_trees_hit_1(terrain_file, slope):
    with open(terrain_file, 'r') as terrain:
        lines = terrain.readlines()
        
        max_height = len(lines)
        max_width = len(lines[0].strip()) # Assumes each line is of equal length

        (x, y) = slope
        
        trees_hit = 0

        while y < max_height:
            line = lines[y].strip()
            cell = line[x]
        
            if cell == "#":
                trees_hit += 1
            
            x = (x + 3) % max_width
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

    print("Part 1: ", count_trees_hit_1(terrain_file, (3,1)))
    print("Part 2: ", count_trees_hit_2(terrain_file, [(1,1), (3,1), (5,1), (7,1), (1,2)]))
