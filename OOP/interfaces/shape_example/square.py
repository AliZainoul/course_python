from shape import Shape

class Square(Shape):
    def __init__(self, side: float):
        if side <= 0 :
            raise ValueError("Side must be positive numbers.")
        self.side_member = side

    def area(self) -> float:
        return (self.side_member ** 2)
    
    def perimeter(self) -> float:
        return  (4 * self.side_member)
    
    def __str__(self) -> str:
        return f"Square with side {self.side_member}, and area {self.area()}"
    
    def __repr__(self) -> str:
        return f"(id = {id(self)}, side = {(self.side_member,self.side_member)}, area = {self.area()})"
