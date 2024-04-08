from datetime import datetime, timedelta
import FirstTry.StockInfo as si
import yfinance as yf

class Order:
    def __init__(self, id : int, price : float, quantity : int):
        self.id = id
        self.price = price
        self.quantity = quantity
        
        # this probably could be something else
        # maybe isocalender()
        self.timestamp = datetime.today()

        self.order_type = None
    
    def get_id(self) -> int:
        return self.id

    def get_quantity(self) -> int:
        return self.quantity
    
    def get_price(self) -> float:
        return self.price
    
    def get_timestamp(self) -> float:
        return self.timestamp
    
    def get_order_type(self) -> str:
        return self.order_type
    
    def set_order_type(self, new_order_type: str):
        self.order_type = new_order_type

    def reduce_quantity(self, amount: int):
        return 0

# TODO:
# implement MarketOrder, LimitOrder, OrderFactory, etc
'''
class MarketOrder(Order):
    def __init__():
        return "what"

class LimitOrder(Order):
    def __init__():
        return "what"
'''