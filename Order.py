from datetime import datetime
import yfinance as yf #not really used but i wish to when the other classes has been forged
from abc import ABC, abstractmethod
from typing import List, Tuple
import enum


#TODO:
# modify classes to use the yfinance module

class OrderType(enum.Enum):
    BUY = 1
    SELL = 2

class Order:
    def __init__(self, id : int, price : float, quantity : int):
        self.id = id
        self.price = price
        self.quantity = quantity
        
        # this probably could be something else
        # maybe isocalender()
        # sets time stamp of order to current date
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
    
    def set_order_type(self, order_type):
        self.order_type = order_type

    #reduces quantity of order by amount
    def reduce_quantity(self, amount: int):
        if(amount > 0 and amount <= self.quantity):
            self.quantity -= amount
            print("Quantity has been reduced by {amount}")
        else:
            return "Amount out of range."

# MarketOrder and LimitOrder just inherit the Order class,
# but the order type is their respective type (lol)
class MarketOrder(Order):
    def __init__(self, trader_id, price, quantity):
        super().__init__(trader_id, price, quantity)
        self.order_type = "Market Order"
    def get_order_type(self) -> str:
        return super().get_order_type()

class LimitOrder(Order):
    def __init__(self, trader_id, price, quantity):
        super().__init__(trader_id, price, quantity)
        self.order_type = "Limit Order"
    def get_order_type(self) -> str:
        return super().get_order_type()

class OrderFactory(ABC):
    @abstractmethod
    def create_order(self, trader_id: int, price: float, quantity: int):
        pass

class MarketOrderFactory(OrderFactory):
    def create_order(self, trader_id: int, price: float, quantity: int):
        return MarketOrder(trader_id, price, quantity)

class LimitOrderFactory(OrderFactory):
    def create_order(self, trader_id: int, price: float, quantity: int):
        return LimitOrder(trader_id, price, quantity)

## the tuple for sell_orders represents two lists. one for the reamining buy orders and the other is for the remaining sell orders
class OrderMatchingStrategy(ABC):
    @abstractmethod
    def match_orders(self, buy_orders: List[Order], sell_orders: List[Order]) -> Tuple[List[Order], List[Order]]:
        pass