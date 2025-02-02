# pcost.py
#
# Exercise 1.27
from report import read_portfolio

def portfolio_cost(filename) -> float:
    portfolio = read_portfolio(filename)
    return portfolio.total_cost

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} portfoliofile')
    
    filename = argv[1]
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':    
    import sys
    main(sys.argv)