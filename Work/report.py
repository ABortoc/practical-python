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

def print_report(report):
    headers = ('Names', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {f"${price:0.2f}":>10s} {change:>10.2f}')
        
def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)
    
portfolio_report('Data\portfolio.csv', 'Data\prices.csv')