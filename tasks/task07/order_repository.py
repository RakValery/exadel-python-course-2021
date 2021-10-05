#Task 07: OrderRepository
import time
from typing import List
class Good:
    def __init__(self, id:str = "", name: str = "", price = 0):
        self.id = id 
        self.name = name
        self.price = price
    def __str__(self):
        return f"id: {self.id}\tname: {self.name}\tprice: {self.price}"
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Good):
            if self.id == o.id and self.name == o.name and self.price == o.price:
                return True
        return False

class Order:
    def __init__(self, order_id, order_date, client_id, goods: list[Good] = []):
        self.order_id = order_id
        self.order_date = order_date
        self.client_id = client_id
        self.goods = goods
        self.price = 0
        for igood in goods:
            self.price += igood.price
    def __str__(self):
        res = f"order_id: {self.order_id}\torder_date: {time.strftime('%Y-%m-%d_%H:%M.%S',time.gmtime(self.order_date))}\tclient_id: {self.client_id}\tprice: {self.price}\n\tGoods:\n"
        for igood in self.goods:
            res += "\t" + str(igood) + "\n"
        return res
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Order):
            if  self.order_id == o.order_id and \
                self.order_date == o.order_date and \
                self.client_id == o.client_id and \
                self.price == o.price and \
                self.goods == o.goods:
                return True
        return False

class OrderRepository:
    def __init__(self, orders: list[Order] = []):
        self.orders = orders
    def __str__(self):
        res = ""
        for iorder in self.orders:
            res += str(iorder)
        return res
    def add(self, order: Order):
        self.orders.append(order)
    def get(self, order_id): 
        for iorder in self.orders:
            if iorder.order_id == order_id:
                return iorder
        raise ValueError(f"Order with ID={order_id} not found")
    def list(self, n_latest: int = None):
        if n_latest == None:
            return self.orders
        elif (1 > n_latest) or (n_latest > len(self.orders)) or type(n_latest) != int:
            raise ValueError(f"The value {n_latest} must be an integer in the range [1-{len(self.orders)}]")
        else: 
            return self.orders[-n_latest:] # EQ [len(self.orders)-n_latest : len(self.orders)]     [-n_latest:] 
    def delete(self, order_id):
        for iorder in self.orders:
            if iorder.order_id == order_id:
                self.orders.remove(iorder)
                return 0
        raise ValueError(f"Order with ID={order_id} not found")