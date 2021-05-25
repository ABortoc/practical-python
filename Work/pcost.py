# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0
    
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row_num, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                num_shares = int(record['shares'])
                price = float(record['price'])
                total_cost += num_shares * price
            except ValueError:
                print(f'Row {row_num}: Bad row: {row}')
    
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)