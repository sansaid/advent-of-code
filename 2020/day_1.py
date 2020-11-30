"""
Link: www.adventofcode.com/2020/day/1
"""

import argparse
import csv
from functools import reduce


def get_expenses(file_name):
    expenses = []
    
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file)
        expenses.extend([row for row in reader])

    return expenses


def expense_sum_2(expense_list, total):
    def to_int(x):
        if type(x) is str:
            return int(x)
        elif type(x) is list:
            return int(x[0])
        else:
            return x

    sorted_expenses = sorted(list(map(to_int, expense_list)))
    
    bottom_index = 0
    top_index = len(sorted_expenses) - 1

    while bottom_index < top_index:
        _sum = sorted_expenses[bottom_index] + sorted_expenses[top_index]

        if _sum < total:
            bottom_index += 1
        elif _sum > total:
            top_index -= 1
        elif _sum == total:
            return [sorted_expenses[bottom_index], sorted_expenses[top_index]]

    return None


def expense_sum_3(expense_list, total):
    sorted_expenses = sorted(list(map(lambda x: int(x[0]), expense_list)))
    
    last_index = len(sorted_expenses) - 1

    for i in range(0, last_index):
        num = sorted_expenses[i]
        if len(sorted_expenses[i+1:]) > 2:
            num_list = expense_sum_2(sorted_expenses[i+1:], total-num)
            
            if num_list:
                num_list.append(num)
                _sum = sum(num_list)

                if _sum == total:
                    return num_list
        else:
            return None


def multiply_all(multiply_list):
    return reduce(lambda x, y: x*y, multiply_list)
    

if __name__ == "__main__":
    # Initialise argument parser
    prog = argparse.ArgumentParser()

    # Define arguments
    prog.add_argument("--file", "-f",
            help="File containing list of expenses. Must be in CSV format with one column. Each row in the column represents one expense.")
    prog.add_argument("--total", "-t",
            type=int,
            help="The total sum of the expenses")

    # Parse argument
    args = prog.parse_args()

    expenses_file = args.file
    total = args.total

    expenses = get_expenses(expenses_file)

    print("Part 1: ", multiply_all(expense_sum_2(expenses,total)))
    print("Part 2: ", multiply_all(expense_sum_3(expenses,total)))
