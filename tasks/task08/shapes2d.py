#Task 08: Class - inheritance, magic methods
#Implement a set of classes for 2D shapes manipulations
from typing import List, NamedTuple
import abc
import math 
 
class Point2D(NamedTuple):
    x: float
    y: float
 
    def __str__(self) -> str:
        return f"({self.x}, {self.y})" 
 
class Shape2D(abc.ABC):
    @property
    @abc.abstractmethod
    def area(self) -> float:
        raise NotImplementedError
 
    @abc.abstractmethod
    def __contains__(self, point: Point2D) -> bool:
        raise NotImplementedError
 
    @abc.abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError

class Rectangle(Shape2D): #Rectangle - inherits from Shape2D. Has arguments like bottom_left, width, length.
    def __init__(self, bottom_left: Point2D, width: float, length: float) -> None:
        super().__init__()
        self.bottom_left = bottom_left
        self.width = width
        self.length = length 
            
    @property
    def bottom_left(self) -> float:
        return self._bottom_left
    @bottom_left.setter
    def bottom_left(self, bottom_left) -> None:
        if type(bottom_left) != Point2D:
            raise ValueError("Type of bottom left point must be Point2D")
        self._bottom_left = bottom_left

    @property
    def width(self) -> float:
        return self._width
    @width.setter
    def width(self, width) -> None:
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Width must be Int or Float positive number")
        self._width = width
    
    @property
    def length(self) -> float:
        return self._length
    @length.setter
    def length(self, length) -> None:
        if not isinstance(length, (int, float)) or length <= 0:
            raise ValueError("Length must be Int or Float positive number")
        self._length = length

    def __str__(self) -> str:
        return f"Rectangle: bottom_left = {self.bottom_left}, width = {self.width}, length = {self.length}"

    def __contains__(self, point: Point2D) -> bool:
        if type(point) is Point2D and \
            (self.bottom_left.x <= point.x <= self.bottom_left.x + self.length) and \
            (self.bottom_left.y <= point.y <= self.bottom_left.y + self.width):
            return True
        else: 
            return False
    
    @property
    def area(self) -> float:
        return self.width * self.length

class Square(Rectangle): #Square - inherits from Rectangle.
    def __init__(self, bottom_left: Point2D, side: float) -> None:
        self.side = side
        super().__init__(bottom_left, side, side)

    @property
    def side(self) -> float:
        return self.width
    @side.setter
    def side(self, side) -> None:
        if not isinstance(side, (int, float)) or side <= 0:
            raise ValueError("Side must be Int or Float positive number")
        self.width = side 
        self.length = side  

    def __str__(self) -> str:
        return f"Square: bottom_left = {self.bottom_left}, side = {self.side}"
    
class Circle(Shape2D): #Circle - inherits from Shape2D. Has arguments like center, radius.
    def __init__(self, center: Point2D, radius: float) -> None:
        super().__init__()
        self.center = center
        self.radius = radius
    
    @property
    def radius(self) -> float:
        return self._radius
    @radius.setter
    def radius(self, radius) -> None:
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be Int or Float positive number")
        self._radius = radius
    
    @property
    def center(self) -> float:
        return self._center
    @center.setter
    def center(self, center) -> None:
        if type(center) != Point2D:
            raise ValueError("Type of center point must be Point2D")
        self._center = center

    def __str__(self) -> str:
        return f"Circle: center = {self.center}, radius = {self.radius}"

    def __contains__(self, point: Point2D) -> bool:
        if type(point) is Point2D and math.sqrt((point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2) <= self.radius:
            return True
        else: 
            return False
    
    @property
    def area(self) -> float:
        return math.pi * (self.radius ** 2)

class Shape2DCollection(Shape2D): #Shape2DCollection* - inherits from Shape2D. 
    def __init__(self, shapes: list[Shape2D] = []) -> None:
        super().__init__()
        self.shapes = shapes

    @property
    def shapes(self) -> list:
        return self._shapes
    @shapes.setter
    def shapes(self, shapes) -> None:
        if type(shapes) != list:
            raise ValueError(f"Type of Shape2DCollection parameter must be List of Shape2D")
        for shape in shapes:
            if not isinstance(shape, Shape2D):
                raise ValueError(f"Type of collection item must be Shape2D")
        self._shapes = shapes

    def __str__(self) -> str:
        res = f"Collection has {len(self.shapes)} shapes:"
        for shape in self.shapes:
            res += "\n" + str(shape)
        return res

    def __contains__(self, point: Point2D) -> bool:
        if type(point) is Point2D:
            for shape in self.shapes:
                if point in shape:
                    return True
        return False
    
    @property
    def area(self) -> float:
        res = 0
        for shape in self.shapes:
            res += shape.area
        return res