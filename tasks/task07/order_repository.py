#Task 07: OrderRepository
class Good:
    def __init__(self, id, name = "", price = 0):
        self.id = id 
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_id, order_date, client_id, goods: list[Good] = []):
        self.order_id = order_id
        self.order_date = order_date
        self.client_id = client_id
        self.goods = goods
        price=0
        for igood in goods:
            price += igood.price

class OrderRepository:
    def __init__(self, orders: list[Order] = []):
        self.orders = orders
 
    def add(self, order: Order): # - add order
        self.orders.append(order)
        return 0

    def get(self, order_id): # -> Order - get one order by its id
        for iorder in self.orders:
            if iorder.order_id == order_id:
                return iorder
        return f"Order with ID={order_id} not found"

    def list(self, n_latest: int = None): # -> List[Order] - get n_latest orders or all orders if n_latest is None
        if n_latest == None:
            n = len(self.orders)
            return self.orders
        elif n_latest > len(self.orders):
            return f"{n_latest} more then count of Orders"
        elif n_latest < 1:
            return f"{n_latest} less then 1"
        else: 
            return self.orders[len(self.orders) - n_latest-1:]

    def delete(self, order_id):
        for iorder in self.orders:
            if iorder.order_id == order_id:
                self.orders.remove(iorder)
                return 0
        return f"Order with ID={order_id} not found"
