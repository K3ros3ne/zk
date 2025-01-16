import math

class Shape():
    def __init__(self, shape_name=None):
        self.shape_name = shape_name
    
    def __str__(self):
        return f'{self.shape_name} shape with area {self.area()}'

    def area(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(shape_name="Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return round(self.width * self.height, 1)

    def __str__(self):
        return f"Rectangle shape with area {self.area()}"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(shape_name="Circle")
        self.radius = radius

    def area(self):
        return round(math.pi * (self.radius ** 2), 1)

    def __str__(self):
        return f"{self.shape_name} with a radius of {self.radius} has an area of {self.area()}"

def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20.0
    assert str(rect) == "Rectangle shape with area 20.0"

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3
    assert str(circle) == "Circle with a radius of 3 has an area of 28.3"

if __name__ == "__main__":
    shape = Shape()
    print(shape)

    rect = Rectangle(4, 5)
    print(rect)

    circle = Circle(3)
    print(circle)
