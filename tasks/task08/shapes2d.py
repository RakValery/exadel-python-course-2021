#Task 08: Class - inheritance, magic methods
#Implement a set of classes for 2D shapes manipulations
from typing import NamedTuple
import abc
import math 
 
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
    def __init__(self, bottom_left: Point2D, width: float, length: float):
        super().__init__()
        if type(bottom_left) is Point2D and isinstance(width, (int, float)) and isinstance(length, (int, float)) and  \
            width > 0 and length > 0:###
            self.bottom_left = bottom_left
            self.width = width
            self.length = length
        else:
            raise ValueError
    
    def __str__(self):
        return f"Rectangle: bottom_left = {self.bottom_left}, width = {self.width}, length = {self.length}"

    def __contains__(self, point: Point2D):
        if type(point) is Point2D and (self.bottom_left.x <= point.x <= self.bottom_left.x + self.length) and (self.bottom_left.y <= point.y <= self.bottom_left.y + self.width):
            return True
        else: 
            return False
    
    def area(self):
        return self.width * self.length

class Square(Rectangle): #Square - inherits from Rectangle.
    def __init__(self, bottom_left: Point2D, side: float):
        if type(bottom_left) is Point2D and isinstance(side, (int, float)) and  side > 0:
            super().__init__(bottom_left, side, side)
            self.side = side
        else:
            raise ValueError
    
    def __str__(self):
        return f"Square: bottom_left = {self.bottom_left}, side = {self.side}"
    
class Circle(Shape2D): #Circle - inherits from Shape2D. Has arguments like center, radius.
    def __init__(self, center: Point2D, radius: float):# -> None:
        super().__init__()
        if type(center) is Point2D and isinstance(radius, (int, float)) and  radius > 0:
            self.center = center
            self.radius = radius
        else:
            raise ValueError
    
    def __str__(self):
        return f"Circle: center = {self.center}, radius = {self.radius}"

    def __contains__(self, point: Point2D):
        if type(point) is Point2D and math.sqrt((point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2) <= self.radius:
            return True
        else: 
            return False
    
    def area(self):
        return math.pi * (self.radius ** 2)

class Shape2DCollection(Shape2D): #Shape2DCollection* - inherits from Shape2D. 
    """A collection of shapes, stores a list of Shape2D. 
    For Shape2DCollection, area and __contains__ have special meaning:
    area  - is the sum of areas of the stored shapes
    __contains__ - returns True if the point is inside any of the stored shapes."""
    def __init__(self, shapes: list[Shape2D] = []):# -> None:
        super().__init__()
        self.shapes = shapes
    def __str__(self):
        res = ""
        for shape in self.shapes:
            res += str(shape)
        return res
    """def add(self, shape: Shape2D):
        self.shapes.append(shape)"""
    def __contains__(self, point: Point2D):
        if type(point) is Point2D:
            for shape in self.shapes:
                if point in shape:
                    return True
        return False
    
    def area(self):
        res = 0
        for shape in self.shapes:
            res += shape.area()
        return res

