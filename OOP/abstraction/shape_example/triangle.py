import cmath
from shape import Shape

class Triangle(Shape):
    """
    Triangle class representing a triangle shape.
    Implements triangle inequality theorem validation and Heron's formula for area calculation.
    """
    def __init__(self, side1: float, side2: float, side3: float, name: str = "Triangle", color: str = "Blue"):
        """
        Initialize a triangle with three sides.
        
        Args:
            side1 (float): Length of first side
            side2 (float): Length of second side
            side3 (float): Length of third side
            name (str): Name of the shape (default: "Triangle")
            color (str): Color of the shape (default: "Blue")
            
        Raises:
            ValueError: If any side is non-positive or if sides don't satisfy triangle inequality theorem
        """
        super().__init__(name, color)
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("All sides must be positive numbers.")
        
        # Triangle inequality theorem: sum of any two sides must be greater than the third side
        if (side1 + side2 <= side3) or (side2 + side3 <= side1) or (side1 + side3 <= side2):
            raise ValueError("Given sides do not form a valid triangle (violates triangle inequality theorem)")
            
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self) -> float:
        """
        Calculate the area of the triangle using Heron's formula.
        
        Returns:
            float: Area of the triangle
        """
        # Semi-perimeter
        s = (self.side1 + self.side2 + self.side3) / 2
        # Heron's formula
        area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        return area
    
    def perimeter(self) -> float:
        """
        Calculate the perimeter of the triangle.
        
        Returns:
            float: Perimeter of the triangle
        """
        return self.side1 + self.side2 + self.side3
    
    def __str__(self) -> str:
        return f"Triangle with sides {self.side1}, {self.side2}, {self.side3} and area {self.area()}"
    
    def __repr__(self) -> str:
        return f"(id = {id(self)}, sides = [{self.side1}, {self.side2}, {self.side3}], area = {self.area()})"
