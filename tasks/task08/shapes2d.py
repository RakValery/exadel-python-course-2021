#Task 08: Class - inheritance, magic methods
#Implement a set of classes for 2D shapes manipulations
from typing import NamedTuple
import abc
 
 
class Point2D(NamedTuple):
    """
    A point in 2-dimensional space.
    Implemented as NamedTuple (so it is immutable), but simple class can be used instead.
    """
    x: float
    y: float
 
    def __str__(self):
        return f"({self.x}, {self.y})"
 
 
class Shape2D(abc.ABC):
    """
    An abstract shape in 2-dimensional space. Examples of 2D shapes are rectangle, circle, etc.
    """
 
    @property
    @abc.abstractmethod
    def area(self):# -> float:
        """Area of the shape."""
        raise NotImplementedError
 
    @abc.abstractmethod
    def __contains__(self, point: Point2D):# -> bool:
        """Check if the point is inside the shape.
        Support semantics like `if point in shape`"""
        raise NotImplementedError
 
    @abc.abstractmethod
    def __str__(self):# -> str:
        """Get string representation of the shape."""
        raise NotImplementedError

class Rectangle(Shape2D): #Rectangle - inherits from Shape2D. Has arguments like bottom_left, width, length.
    pass

class Square(Shape2D): #Square - inherits from Rectangle.
    pass
class Circle(Shape2D): #Circle - inherits from Shape2D. Has arguments like center, radius.
    pass
class Shape2DCollection(Shape2D): #Shape2DCollection* - inherits from Shape2D. 
    """A collection of shapes, stores a list of Shape2D. 
    For Shape2DCollection, area and __contains__ have special meaning:
    area  - is the sum of areas of the stored shapes
    __contains__ - returns True if the point is inside any of the stored shapes."""
    pass


var = Point2D(5, 6)
print(var.x)