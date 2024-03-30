class stock:
    def __init__(self, name, price, amt_of_shares):
        self.name = name
        self.price = price
        self.amt_of_shares = amt_of_shares
    
    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    def getShares(self):
        return self.amt_of_shares