# report.py
#
# Exercise 2.4
from fileparse import parse_csv

def read_portfolio(filename) -> list:
    with open(filename) as lines:
        return parse_csv(lines, col_select=['name','shares','price'], types=[str,int,float], silence_errors=False)

def read_prices(filename) -> dict:
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str,float], has_headers=False))

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
    
def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} portfile pricefile')
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':    
    import sys
    main(sys.argv)