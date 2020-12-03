"""
Link: www.adventofcode.com/2020/day/2
"""

import argparse
import csv
from functools import reduce
import re


def count_letters(letter, string):
    return len(re.findall(letter, string))


def is_password_invalid(_range, letter, string):
    (_min, _max) = list(map(int, _range.split("-")))

    letter_count = count_letters(letter, string)

    if letter_count > _max or letter_count < _min:
        return 1
    
    return 0


def get_valid_passwords(file):
    invalid_passwords = 0

    with open(file, 'r') as passwords_file:
        lines = passwords_file.readlines()

        for line in lines:
            (policy, password) = line.split(":")
            (_range, letter) = policy.split(" ")
            invalid_passwords += is_password_invalid(_range, letter, password)
    
    return invalid_passwords
        

if __name__ == "__main__":
    # Initialise argument parser
    prog = argparse.ArgumentParser()

    # Define arguments
    prog.add_argument("--file", "-f",
            help="File containing list of expenses. Must be in CSV format with one column. Each row in the column represents one expense.")

    # Parse argument
    args = prog.parse_args()

    passwords_file = args.file

    valid_passwords = get_valid_passwords(passwords_file)

    print("Part 1: ", valid_passwords)
