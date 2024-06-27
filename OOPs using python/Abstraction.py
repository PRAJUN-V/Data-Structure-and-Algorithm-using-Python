# abc module is used to implement abstraction in python

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Trying to instantiate Shape will raise an error
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

# Instantiate the concrete classes
rectangle = Rectangle(3, 4)
circle = Circle(5)

print(f"Rectangle area: {rectangle.area()}")  # Output: Rectangle area: 12
print(f"Rectangle perimeter: {rectangle.perimeter()}")  # Output: Rectangle perimeter: 14

print(f"Circle area: {circle.area()}")  # Output: Circle area: 78.53975
print(f"Circle perimeter: {circle.perimeter()}")  # Output: Circle perimeter: 31.4159

