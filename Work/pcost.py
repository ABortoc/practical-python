# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    sum = 0
    
    with open(filename, 'rt') as file:
        for line in file:
            row = line.split(',')
            if row[1].isalpha() is False and row[2][:-1].isalpha() is False:
                try:
                    sum += int(row[1]) * float(row[2][:-1])
                except ValueError:
                    print('Invalid input')
    
    return sum

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)