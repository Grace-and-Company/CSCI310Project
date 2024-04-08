import yfinance as yf
from datetime import datetime, timedelta

class StockInfo:
    def __init__(self, ticker):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)
    
    def get_historical_data(self):
        end_date = datetime.today().strftime('%Y-%m-%d')
        start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')
        data = self.stock.history(start=start_date, end=end_date)
        return data
    
  

# # Example usage:
# ticker = "AAPL" # For Apple Inc.
# stock_info = StockInfo(ticker)

# # Get historical data from the last year
# historical_data = stock_info.get_historical_data()
# print("Historical Data:")
# print(historical_data)

# # To install python packages:
# type pip install (package name) in the terminal
# Example: pip install yfinance
# example installs yfinance package used in project