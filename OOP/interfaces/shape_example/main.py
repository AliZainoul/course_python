from circle     import Circle
from rectangle  import Rectangle
from square     import Square
from triangle   import Triangle


def main():
    # Create instances of each shape
    circle      = Circle(radius=5)
    rectangle   = Rectangle(height=4, weight=6)
    square      = Square(side=3)
    triangle    = Triangle(side1=3, side2=4, side3=5)

    # Print details of each shape (calling __str__)
    print("-" * 28 + "Shape Details: via __str__ method" + "-" * 28)
    print(circle)
    print(rectangle)
    print(square)
    print(triangle)

    # Print details of each shape (calling __repr__)
    print("-" * 28 + "Shape Details: via __repr__ method" + "-" * 28)
    print(repr(circle))
    print(repr(rectangle))
    print(repr(square))
    print(repr(triangle))

    

if __name__ == "__main__":
    main()