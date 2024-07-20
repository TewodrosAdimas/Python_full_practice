class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return f"area from shape class is: {self.length * self.width}"


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

    def calculate_area(self):
        return f"area from rectangle class is: {self.length * self.width}"
    
rectangle1 = Rectangle(int(5), int(6))

print(rectangle1.calculate_area())