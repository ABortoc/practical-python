# report.py
#
# Exercise 2.4
from fileparse import parse_csv
import stock
import tableformat

def read_portfolio(filename) -> list:
    with open(filename) as lines:
        portfolio_dicts = parse_csv(lines, col_select=['name','shares','price'], types=[str,int,float], silence_errors=False)
    
    portfolio = [stock.Stock(item['name'], item['shares'], item['price']) for item in portfolio_dicts]
    return portfolio

def read_prices(filename) -> dict:
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str,float], has_headers=False))

def make_report(portfolio, prices) -> list:
    stock_price_change = []
    
    for item in portfolio:
        price_change = prices[item.name] - item.price
        stock_price_change.append((item.name, item.shares, prices[item.name] ,price_change))
        
    return stock_price_change

def print_report(report, formatter):
    formatter.headings(['Name','Shares','Price','Change'])

    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)
        
def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    
    report = make_report(portfolio, prices)
    
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
    
def main(argv):
    if len(argv) < 3 and len(argv) > 5:
        raise SystemExit(f'Usage: {argv[0]} portfile pricefile')
    if len(argv) == 3:
        portfolio_report(argv[1], argv[2])
    else:
        portfolio_report(argv[1], argv[2], argv[3])

if __name__ == '__main__':    
    import sys
    main(sys.argv)