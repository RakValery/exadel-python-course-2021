#tests for Task 07: OrderRepository
import order_repository, unittest

rep = None

good1 = order_repository.Good("g166236777","PC", 1250)
good2 = order_repository.Good("g369675104","Monitor", 320)
good3 = order_repository.Good("g648146674","Keyboard", 8)
good4 = order_repository.Good("g161204239","Mouse", 5)
good5 = order_repository.Good("g109405973","Headset", 95)

order1 = order_repository.Order("o587621180", 1633329707.78067, "c897700372", [good1, good2, good3, good4, good5])
order2 = order_repository.Order("o882997576", 1633334339.7806716, "c178728546", [good3, good4, good5])
order3 = order_repository.Order("o1529240891", 1633279617.780672, "c1580546929", [good1, good4, good5])
order4 = order_repository.Order("o576023242", 1633332617.7806726, "c289241534", [good1, good2, good3, good4])
order5 = order_repository.Order("o659360132", 1633334578.780673, "c633521705", [good1, good3, good4, good5])

rep = order_repository.OrderRepository()

rep.add(order1)
rep.add(order2)
rep.add(order3)
rep.add(order4)
rep.add(order5)

class TestOrdRep(unittest.TestCase):
    def setUp(self):
        self.rep = None
        self.rep1 = None

    def test_add(self):  
        self.rep1 = None
        self.rep1 = order_repository.OrderRepository()
        self.rep1.add(order1)
        self.rep1.add(order2)
        self.rep1.add(order3)
        self.rep1.add(order4)
        self.rep1.add(order5)
        print(self.rep1)
        self.assertEqual(self.rep1.orders, [order1, order2, order3, order4, order5])
        #del self.rep1

    def test_del(self):
        self.rep = rep
        self.rep.delete("o576023242")# delete order4
        self.assertEqual(self.rep.orders, [order1, order2, order3, order5])
        #del self.rep
 
    def test_get(self):
        self.rep = rep
        self.assertEqual(order5, self.rep.get("o659360132")) #Order5
        #del self.rep


    def test_list3(self):
        self.rep = rep
        print(self.rep, self.rep.list(3), sep="\n")
        self.assertEqual(self.rep.list(3), [order3, order4, order5]) #Last 3 orders
        #del self.rep 
 

    def test_listnone(self):
        self.rep = rep
        self.assertEqual(self.rep.list(), [order1, order2, order3, order4, order5]) #All orders 
        #del self.rep


if __name__ == '__main__':  
    unittest.main()
    

"""


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
    if str(mes) == "The value -5 must be an integer in the range [1-4]":
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

"""