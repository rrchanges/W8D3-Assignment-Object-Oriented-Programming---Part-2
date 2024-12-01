import math

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color,filled)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius
    
    def get_perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self,color, filled, width, height):
        super().__init__(color,filled)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
class Triangle(Shape):
    def __init__(self, color, filled, side1, side2, side3):
        super().__init__(color, filled)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    def get_perimeter(self):
        return self.side1 + self.side2 +self.side3
    
circle = Circle('red', True, 5)
rectangle = Rectangle('blue', False, 4, 6)
triangle = Triangle("green", True, 3, 4, 5)

shapes = [circle, rectangle, triangle]

for shape in shapes:
    print(f"Area: {shape.get_area()}")
    print(f"Perimeter: {shape.get_perimeter()}")

tolerance = 0.00001

assert circle.get_area() == 78.53981633974483
assert circle.get_perimeter() == 31.41592653589793

assert rectangle.get_area() == 24
assert rectangle.get_perimeter() == 20

assert triangle.get_area() == 6
assert triangle.get_perimeter() == 12

print("All tests passed!")