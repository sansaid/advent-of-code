"""
Link: www.adventofcode.com/2020/day/2
"""

import argparse
import csv
from functools import reduce
import re


def count_letters(letter, string):
    return len(re.findall(letter, string))


def is_password_valid_1(_range, letter, string):
    (_min, _max) = list(map(int, _range.split("-")))

    letter_count = count_letters(letter, string)

    if letter_count > _max or letter_count < _min:
        return 0
    
    return 1


def is_password_valid_2(_range, letter, string):
    (fi, si) = list(map(int, _range.split("-")))
    stripped_string = string.strip()

    fi_letter = stripped_string[fi-1]
    si_letter = stripped_string[si-1]

    if (letter == fi_letter) != (letter == si_letter):
        return 1
    
    return 0


def get_valid_passwords_1(file):
    valid_passwords = 0

    with open(file, 'r') as passwords_file:
        lines = passwords_file.readlines()

        for line in lines:
            (policy, password) = line.split(":")
            (_range, letter) = policy.split(" ")
            valid_passwords += is_password_valid_1(_range, letter, password)
    
    return valid_passwords
    

def get_valid_passwords_2(file):
    valid_passwords = 0

    with open(file, 'r') as passwords_file:
        lines = passwords_file.readlines()

        for line in lines:
            (policy, password) = line.split(":")
            (_range, letter) = policy.split(" ")
            valid_passwords += is_password_valid_2(_range, letter, password)
    
    return valid_passwords


if __name__ == "__main__":
    # Initialise argument parser
    prog = argparse.ArgumentParser()

    # Define arguments
    prog.add_argument("--file", "-f",
            help="File containing list of expenses. Must be in CSV format with one column. Each row in the column represents one expense.")

    # Parse argument
    args = prog.parse_args()

    passwords_file = args.file

    print("Part 1: ", get_valid_passwords_1(passwords_file))
    print("Part 2: ", get_valid_passwords_2(passwords_file))
