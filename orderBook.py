from typing import List
import yfinance
from Order import * 
#trying to import order by itself causes issues with
#creating the book

class OrderBook:
    def __init__(self):
        self.strategy = None
        self.book: List['Order'] = []
    
    def add_order(self, new_order: Order):
        self.book.append(new_order)

    def matchOrders(self):
        buy_orders = []
        sell_orders = []

        # create lists of orders
        for order in self.book:
            if order.get_price() > 0:
                buy_orders.append(order)
            else:
                sell_orders.append(order)
        
        self.strategy.match_orders(buy_orders, sell_orders)

        self.book.clear()
        self.book.extend(buy_orders)
        self.book.extend(sell_orders)

    def print_order_book(self):
        print("Order Book content...")
        print("ID\tPrice\tQuantity\tOrder Type")
        for order in self.book: 
            order_type_name = "Buy" if order.get_order_type() == "BUY" else "Sell"
            print(f"{order.get_id()}\t{order.get_price()}\t{order.get_quantity()}\t\t{order_type_name}")
        print()

    def set_strategy(self, newStrategy : OrderMatchingStrategy):
        self.strategy = newStrategy