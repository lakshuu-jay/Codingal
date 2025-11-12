from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

class Square(Polygon):
    def __init__(self, side):
        self._side = side

    def area(self):
        return self._side ** 2

class Triangle(Polygon):
    def __init__(self, base, height):
        self._base = base
        self._height = height

    def area(self):
        return 0.5 * self._base * self._height

polygons = [
    Rectangle(5, 10),
    Square(6),
    Triangle(8, 4)
]

for s in polygons:
    print(s.area())