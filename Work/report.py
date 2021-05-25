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
            record = dict(zip(headers, row))
            holding = {}
            holding['name'] = record['name']
            holding['shares'] = int(record['shares'])
            holding['price'] = float(record['price'])
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

def make_report(portfolio, prices) -> list:
    stock_price_change = []
    
    for item in portfolio:
        price_change = prices[item['name']] - item['price']
        stock_price_change.append((item['name'], item['shares'], prices[item['name']] ,price_change))
        
    return stock_price_change

portfolio = read_portfolio('Data\portfoliodate.csv')
prices = read_prices('Data\prices.csv')

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

# print(f'Portfolio value: {current_portfolio_value}')
# print('Difference with the original investment:',sum(stock_gain_loss.values()))

report = make_report(portfolio, prices)
headers = ('Names', 'Shares', 'Price', 'Change')
sign = '$'
 
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {f"${price:0.2f}":>10s} {change:>10.2f}')