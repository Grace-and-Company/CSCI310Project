import sys
import StockInfo
import yfinance as yf
from datetime import datetime, timedelta
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QLabel

class StockVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        ticker_label = QLabel("Ticker:")
        self.tickerInput = QLineEdit()
        self.getDataButton = QPushButton("Get Data")
        self.getDataButton.clicked.connect(self.get_stock_data) 

        self.dataTable = QTableWidget()

        layout = QVBoxLayout()
        layout.addWidget(ticker_label)
        layout.addWidget(self.tickerInput)
        layout.addWidget(self.getDataButton)
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

        for row, date in enumerate(data.index):
            date_str = date.strftime('%Y-%m-%d') 
            self.dataTable.setItem(row, 0, QTableWidgetItem(date_str))
            for col, col_name in enumerate(["Open", "High", "Low", "Close", "Volume"]):
                item = QTableWidgetItem(str(data.loc[date, col_name]))
                self.dataTable.setItem(row, col+1, item) 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    visualizer = StockVisualizer()
    visualizer.show()
    sys.exit(app.exec_())
