#tests for Task 07: OrderRepository
import order_repository, unittest
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

class TestOrdRep(unittest.TestCase):
    def setUp(self):
        self.rep = order_repository.OrderRepository([order1, order2, order3, order4, order5])
    def test_add(self): 
        self.rep.add(order4)
        self.assertEqual(self.rep.orders, [order1, order2, order3, order4, order5, order4])
    def test_get(self):
        self.assertEqual(order5, self.rep.get("o659360132")) #Order5
    def test_list3(self):
        self.assertTrue(self.rep.list(3) == [order3, order4, order5]) #Last 3 orders
    def test_listall(self):
        self.assertTrue(self.rep.list() == [order1, order2, order3, order4, order5]) #All orders 
    def test_del(self):
        self.rep.delete("o576023242")# delete order4
        self.assertEqual(self.rep.orders, [order1, order2, order3, order5])
    def test_listfalse(self): #Argument of list() out of range
        try:
            self.rep.list(-5)
        except ValueError as mes:
            self.assertTrue(str(mes) == "The value -5 must be an integer in the range [1-5]")
    def test_getfalse(self): #order4 was deleted - raise ValueError
        try:
            self.rep.get("o57602355642")
        except ValueError as mes:
            self.assertTrue(str(mes) == "Order with ID=o57602355642 not found")

if __name__ == '__main__':  
    unittest.main()
