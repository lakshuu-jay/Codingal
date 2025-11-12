from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

rectangle = Rectangle(4, 5)
print("Rectangle area:", rectangle.calculate_area())

square = Square(3)
print("Square area:", square.calculate_area())

triangle = Triangle(6, 2)
print("Triangle area:", triangle.calculate_area())