# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    sum = 0
    
    # with open(filename, 'rt') as file:
    #     for line in file:
    #         row = line.split(',')
    #         if row[1].isalpha() is False and row[2][:-1].isalpha() is False:
    #             try:
    #                 sum += int(row[1]) * float(row[2][:-1])
    #             except ValueError:
    #                 print('Invalid input')
    
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            try:
                sum += int(row[1]) * float(row[2])
            except ValueError:
                print('Invalid value')
    
    return sum

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)