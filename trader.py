import stock

class trader:
    def __init__(self, name):
        self.name = name
        self.stockList = []
        currentMoney = 0.0
    
    def buyStock(self):
        self.stockList.append(stock)

    def sellStock(self):
        print("Enter the stock name to sell:")
        stockName = input()
        self.stockList.remove(stockName)