# portfolio.py

class Portfolio:
    def __init__(self, holdings) -> None:
        self._holdings = holdings
        
    def __iter__(self) -> iter:
        return self._holdings.__iter__()
    
    def __len__(self) -> int:
        return len(self._holdings)
    
    def __getitem__(self, index):
        return self._holdings[index]
    
    def __contains__(self, name):
        return any([elem.name == name for elem in self._holdings])
        
    @property
    def total_cost(self) -> float:
        return sum([elem.cost for elem in self._holdings])
    
    def tabulate_shares(self) -> int:
        from collections import Counter
        total_shares = Counter()
        for elem in self._holdings:
            total_shares[elem.name] += elem.shares
        return total_shares