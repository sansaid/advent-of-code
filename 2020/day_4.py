"""
Link: www.adventofcode.com/2020/day/3
"""

import argparse
import csv
from functools import reduce
import re

def get_missing_fields(passport, required):
    print(passport)
    entries = passport.strip().split(" ")
    fields = list(map(lambda x: x.split(":")[0], entries))
    print(fields)

    missing_fields = [r for r in required if r not in fields]
    print(missing_fields)

    return missing_fields


def get_invalid_fields(passport):
    validation = {
        "byr": lambda x: re.match(r"^\d{4}$", x) and int(x) <= 2002 and int(x) >= 1920,
        "iyr": lambda x: re.match(r"^\d{4}$", x) and int(x) <= 2020 and int(x) >= 2010,
        "eyr": lambda x: re.match(r"^\d{4}$", x) and int(x) <= 2030 and int(x) >= 2020,
        "hgt": lambda x: re.match(r"^\d{4}$", x) and int(x) <= 2020 and int(x) >= 2010,
        "hcl":
        "ecl":
        "pid":
    }


def get_valid_passports_1(passports_file):
    with open(passports_file, 'r') as passports_reader:
        valid_passports = 0

        passport = ""

        for line in passports_reader:
            passport += " " + line.strip()

            if line == "\n":
                if not get_missing_fields(passport, ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
                    valid_passports += 1
                
                passport = ""

    return valid_passports


def get_valid_passports_2(passports_file):
    with open(passports_file, 'r') as passports_reader:
        valid_passports = 0

        passport = ""

        for line in passports_reader:
            passport += " " + line.strip()

            if line == "\n":
                missing_fields = get_missing_fields(passport, ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
                invalid_values = get_invalid_fields(passport)

                if not missing_fields and not invalid_values:
                    valid_passports += 1
                
                passport = ""

    return valid_passports


if __name__ == "__main__":
    # Initialise argument parser
    prog = argparse.ArgumentParser()

    # Define arguments
    prog.add_argument("--file", "-f",
            help="File containing input.")

    # Parse argument
    args = prog.parse_args()

    passports_file = args.file

    print("Part 1: ", get_valid_passports_1(passports_file))
    # print("Part 2: ", count_trees_hit_2(terrain_file, [(1,1), (3,1), (5,1), (7,1), (1,2)]))
