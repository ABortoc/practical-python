# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename) -> list:
    portfolio = []
    
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            holding = {}
            holding['name'] = row[0]
            holding['shares'] = int(row[1])
            holding['price'] = float(row[2])
            portfolio.append(holding)
    
    return portfolio

def read_prices(filename) -> dict:
    prices = {}
    
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        for row in rows:
            if row != []:
                prices[row[0]] = float(row[1])
            else:
                continue
            
    return prices

portfolio = read_portfolio('Work\Data\portfolio.csv')
prices = read_prices('Work\Data\prices.csv')
current_portfolio_value = 0
stock_gain_loss = {}

for holding in portfolio:
    current_portfolio_value += holding['shares'] * prices[holding['name']]
    current_value = holding['shares'] * prices[holding['name']]
    original_value = holding['shares'] * holding['price']
    if holding['name'] in stock_gain_loss:
        stock_gain_loss[holding['name']] = stock_gain_loss[holding['name']] + (current_value - original_value)
    else:
        stock_gain_loss[holding['name']] = current_value - original_value
    
print(f'Portfolio value: {current_portfolio_value}')
print(stock_gain_loss)