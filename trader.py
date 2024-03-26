import stock

class trader:
    def __init__(self, name):
        self.name = name
        self.stockList = []
        currentMoney = 0.0
    
    def buyStock(self):
        #Lets you add a stock to the surrent list, this input system will likely be changed later
        print("Input stock name:")
        stockName = input()
        print("Input stock price: ")
        stockPrice = input()
        print("Input number of shares: ")
        shares = input()

        newStock = stock(stockName, stockPrice, shares)
        self.stockList.append(newStock)

    def sellStock(self):
        #get stock name
        print("Enter the stock name, price, and shares to sell:")
        stockName = input()

        #Check if stock is on the list
        for x in self.stockList:
            if self.stockList == x:
                #Get the price of the stock
                #add to money
                currentMoney += self.stockList[x].getPrice
                self.stockList.remove(x)
            else:
                print("Not found")

                
            
            
            
        
        
        