import sys
import threading
import StockInfo
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QInputDialog
from PyQt5.QtCore import QObject, pyqtSignal
from concurrent.futures import ThreadPoolExecutor
from trader import *


class StockVisualizer(QWidget):
    summary = ""
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        ticker_label = QLabel("Ticker:")
        
        self.tickerInput = QLineEdit()
        self.getDataButton = QPushButton("Get Data")
        self.stockName = QLabel("Stock Name: ")
        self.stockNameInput = QLineEdit()
        self.amount = QLabel("Amount: ")
        self.stockAmountInput = QLineEdit()
        self.buyStockButton = QPushButton("Buy")
        self.buyStockLabel = QLabel("Summary of Costs")
        self.getDataButton.clicked.connect(self.get_stock_data) 
        self.buyStockButton.clicked.connect(self.buy_multiple)
        self.dataTable = QTableWidget()
    
        layout = QVBoxLayout()
        layout.addWidget(ticker_label)
        layout.addWidget(self.tickerInput)
        layout.addWidget(self.getDataButton)
        layout.addWidget(self.stockName)
        layout.addWidget(self.stockNameInput)
        layout.addWidget(self.amount)
        layout.addWidget(self.stockAmountInput)
        layout.addWidget(self.buyStockButton)
        layout.addWidget(self.buyStockLabel)
        layout.addWidget(self.dataTable)

        self.setLayout(layout)

        self.setWindowTitle("Stock Data Visualizer")

    def get_stock_data(self):
        ticker = self.tickerInput.text()
        stock_info = StockInfo.StockInfo(ticker)
        historical_data = stock_info.get_historical_data()

        self.update_table(historical_data)

    def update_table(self, data):
        # Assuming you want columns for Date, Open, High, Low, Close, Volume
        self.dataTable.setRowCount(len(data))
        self.dataTable.setColumnCount(6)
        self.dataTable.setHorizontalHeaderLabels(["Date", "Open", "High", "Low", "Close", "Volume"])

        xAxis = []
        yAxis = []
        i = 0
        for row, date in enumerate(data.index):
            date_str = date.strftime('%Y-%m-%d') 

             #Use date as x, close as y: to be used in a price over time graph
            xAxis.append(date)
            yAxis.append(data['Close'][i])
            i+=1

            self.dataTable.setItem(row, 0, QTableWidgetItem(date_str))
            for col, col_name in enumerate(["Open", "High", "Low", "Close", "Volume"]):
                item = QTableWidgetItem(str(data.loc[date, col_name]))
               
                self.dataTable.setItem(row, col+1, item) 
        
        #Creates and shows a price over time graph
        fig = go.Figure([go.Scatter(x=xAxis, y=yAxis)])
        fig.show()

    def buy_one_stock(self, s, a):

        stock = yf.Ticker(s)
        closing = stock.history(period='1D')['Close'].iloc[0]
        cost = (float(closing) *float(a)) 
        self.summary += "{} shares of {} will cost ${:0.2f}\n".format(a, s, cost) 
    def buy_multiple(self):
        self.summary = ""
        stocksToBuy = self.stockNameInput.text().split(" ")
        amounts = self.stockAmountInput.text().split(" ")
        stocks_and_amounts = {stock: amount for stock, amount in zip(stocksToBuy, amounts)}
        threads = []
        for s, a in stocks_and_amounts.items():
            thread = threading.Thread(target=self.buy_one_stock, args=(s, a))
            threads.append(thread)
        
        for t in threads:
            t.start()

        for t in threads:
            t.join()
        
       

        self.buyStockLabel.setText(self.summary)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    visualizer = StockVisualizer()
    executor = ThreadPoolExecutor(max_workers=3)
    executor.submit(visualizer.show())
    executor.submit(visualizer.show())
    executor.submit(visualizer.show())
        

    executor.shutdown(wait = False)
      
        
    
    
    sys.exit(app.exec_())
