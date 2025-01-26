import math

class Shape:
    """Base class for all shapes."""
    def area(self):
        """Method to calculate the area of the shape. Must be overridden by derived classes."""
        raise NotImplementedError("The area() method must be overridden in derived classes.")

class Rectangle(Shape):
    """Derived class representing a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of a rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Derived class representing a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates the area of a circle."""
        return math.pi * self.radius ** 2
