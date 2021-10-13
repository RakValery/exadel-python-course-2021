#tests for Task 08: Class - inheritance, magic methods
import unittest 
from shapes2d import Point2D, Rectangle, Circle, Square, Shape2DCollection

class TestShapes2D(unittest.TestCase):
    def setUp(self):    #before start    
        self.point1 = Point2D(-1, -2)
        self.point2 = Point2D(2, -2)
        self.point3 = Point2D(2, -3)
        self.point4 = Point2D(-4, -5)
        self.rect = Rectangle(self.point1, 6, 4)
        self.sqr = Square(self.point3, 2)
        self.crcl = Circle(self.point1, 3)
        self.shapes = Shape2DCollection([self.rect, self.sqr, self.crcl])

    def test_area_rect(self): # OK
        self.assertEqual(self.rect.area(), 24)
    def test_area_sqr(self): # OK
        self.assertEqual(self.sqr.area(), 4)
    def test_area_crcl(self): # OK
        self.assertEqual(self.crcl.area(), 28.274333882308138)
    def test_area_shapes(self): # OK
        self.assertEqual(self.shapes.area(), 56.27433388230814)

    def test_cont_rect(self): # OK
        self.assertTrue(self.point2 in self.rect)
    def test_cont_sqr(self): # OK
        self.assertTrue(self.point2 in self.sqr)
    def test_cont_crcl(self): # OK
        self.assertTrue(self.point2 in self.crcl)
    def test_cont_shapes(self): # OK
        self.assertTrue(self.point2 in self.shapes)

    def test_ncont_rect(self): # OK
        self.assertFalse(self.point4 in self.rect)
    def test_ncont_sqr(self): # OK
        self.assertFalse(self.point4 in self.sqr)
    def test_ncont_crcl(self): # OK
        self.assertFalse(self.point4 in self.crcl)
    def test_ncont_shapes(self): # OK
        self.assertFalse(self.point4 in self.shapes)    

if __name__ == '__main__':  
    unittest.main()
