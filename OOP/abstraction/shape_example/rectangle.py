from shape import Shape

class Rectangle(Shape):
    
    def __init__(self, height: float, weight: float, name: str = "Rectangle", color: str = "Blue"):
        super().__init__(name, color)
        if height <= 0 or weight <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        if height == weight:
            raise ValueError("Weight and height must not be equal (use Square class for squares).")

        self.height_member = height
        self.weight_member = weight

    def area(self) -> float:
        return (self.height_member * self.weight_member)
    
    def perimeter(self) -> float:
        return  (2 * (self.height_member + self.weight_member)) 
    
    def __str__(self) -> str:
        return f"Rectangle with height {self.height_member}, weight {self.weight_member} and area {self.area()}"
    
    def __repr__(self) -> str:
        return f"(id = {id(self)}, w,h = {(self.weight_member, self.height_member)}, area = {self.area()})"
