#Task 07: OrderRepository
import time
class Good:
    def __init__(self, id:str = "", name: str = "", price = 0):
        self.id = id 
        self.name = name
        self.price = price
    def __str__(self):
        return f"id: {self.id}\tname: {self.name}\tprice: {self.price}"

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
        return 0

    def get(self, order_id): 
        for iorder in self.orders:
            if iorder.order_id == order_id:
                return iorder
        raise ValueError(f"Order with ID={order_id} not found")

    def list(self, n_latest: int = 0):
        if n_latest == 0:
            return self.orders
        elif (0 > n_latest) or (n_latest > len(self.orders)) or type(n_latest) != int:
            raise ValueError(f"The value {n_latest} must be an integer in the range [0-{len(self.orders)}]")
        else: 
            return self.orders[len(self.orders)-n_latest : len(self.orders)]

    def delete(self, order_id):
        for iorder in self.orders:
            if iorder.order_id == order_id:
                self.orders.remove(iorder)
                return 0
        return f"Order with ID={order_id} not found"

good1 = Good("g166236777","PC", 1250)
good2 = Good("g369675104","Monitor", 320)
good3 = Good("g648146674","Keyboard", 8)
good4 = Good("g161204239","Mouse", 5)
good5 = Good("g109405973","Headset", 95)

order1 = Order("o587621180", time.time() - 5456, "c897700372", [good1, good2, good3, good4, good5])
order2 = Order("o882997576", time.time() - 824, "c178728546", [good3, good4, good5])
order3 = Order("o1529240891", time.time() - 55546, "c1580546929", [good1, good4, good5])
order4 = Order("o576023242", time.time() - 2546, "c289241534", [good1, good2, good3, good4])
order5 = Order("o659360132", time.time() - 585, "c633521705", [good1, good3, good4, good5])

rep = OrderRepository()
rep.add(order1)
rep.add(order2)
rep.add(order3)
rep.add(order4)
rep.add(order5)

#OK
print("*OrderRepository after adding 5 orders:\n", rep)

#OK
rep.delete("o576023242") #4
print("*OrderRepository after deleting order4:\n", rep)


#OK
print("*Order5:\n", rep.get("o659360132")) #5

#OK
print("*List last 3 orders:")
for iorder in rep.list(3):
    print(iorder)

#OK
print("*List ALL orders:")
for iorder in rep.list():
    print(iorder)

#Argument of list() out of range
res = False
try:
   for iorder in rep.list(-5):
        print(iorder)
except ValueError as mes:
    if str(mes) == "The value -5 must be an integer in the range [0-4]":
        res = True
        print("*List last -5 orders - ValueError:", mes)
assert res

#order4 was deleted - raise ValueError
res = False
try:
   print(rep.get("o576023242"))
except ValueError as mes:
    if str(mes) == "Order with ID=o576023242 not found":
        res = True
        print("*Get deleted order - ValueError:", mes)
assert res