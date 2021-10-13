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
        self.assertEqual(self.rect.area, 24)
    def test_area_sqr(self): # OK
        self.assertEqual(self.sqr.area, 4)
    def test_area_crcl(self): # OK
        self.assertEqual(self.crcl.area, 28.274333882308138)
    def test_area_shapes(self): # OK
        self.assertEqual(self.shapes.area, 56.27433388230814)

    def test_cont_rect(self): # OK
        self.assertTrue(self.point2 in self.rect)
    def test_cont_sqr(self): # OK
        self.assertTrue(self.point2 in self.sqr)
    def test_cont_crcl(self): # OK
        self.assertTrue(self.point2 in self.crcl)
    def test_cont_shapes(self): # OK
        self.assertTrue(self.point2 in self.shapes)

    def test_ncont_rect(self): # False
        self.assertFalse(self.point4 in self.rect)
    def test_ncont_sqr(self): # False
        self.assertFalse(self.point4 in self.sqr)
    def test_ncont_crcl(self): # False
        self.assertFalse(self.point4 in self.crcl)
    def test_ncont_shapes(self): # False
        self.assertFalse(self.point4 in self.shapes)    

    def test_init_rect(self): # OK
        with self.assertRaisesRegex(ValueError, "Type of bottom left point must be Point2D"):
            Rectangle({"a": 2, "b": 6}, 5, 9)
        with self.assertRaisesRegex(ValueError, "Width must be Int or Float positive number"):
            Rectangle(self.point4, "5", 9)
        with self.assertRaisesRegex(ValueError, "Length must be Int or Float positive number"):
            Rectangle(self.point4, 5, "9")
    def test_init_sqr(self): # OK
        with self.assertRaisesRegex(ValueError, "Type of bottom left point must be Point2D"):
            Square({"a": 2, "b": 6}, 5)
        with self.assertRaisesRegex(ValueError, "Side must be Int or Float positive number"):
            Square(self.point4, "5")
    def test_init_crcl(self): # OK
        with self.assertRaisesRegex(ValueError, "Type of center point must be Point2D"):
            Circle({"a": 2, "b": 6}, 5)
        with self.assertRaisesRegex(ValueError, "Radius must be Int or Float positive number"):
            Circle(self.point4, "5")        
    def test_init_shapes(self): # OK
        with self.assertRaisesRegex(ValueError, "Type of Shape2DCollection parameter must be List of Shape2D"):
            Shape2DCollection(self.point3)
        with self.assertRaisesRegex(ValueError, "Type of collection item must be Shape2D"):
            Shape2DCollection([self.rect, self.point3, self.crcl])

if __name__ == '__main__':  
    unittest.main()
