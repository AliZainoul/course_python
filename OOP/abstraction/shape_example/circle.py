import cmath
from shape import Shape

class Circle(Shape):
    def __init__(self, radius: float, name: str = "Circle", color: str = "Red"):
        super().__init__(name, color)
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius_member = radius

    def area(self) -> float:
        return (cmath.pi * (self.radius_member ** 2))
    
    def perimeter(self) -> float:
        return (2 * cmath.pi * (self.radius_member))
    
    def __str__(self) -> str:
        return f"Circle with radius {self.radius_member} and area {self.area()}"
    
    def __repr__(self) -> str:
        return f"(id = {id(self)}, radius = {self.radius_member}, area = {self.area()})"
