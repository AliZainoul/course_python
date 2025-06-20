"""
module Shape
This module defines an abstract base class for geometric shapes.
It provides a structure for implementing various geometric shapes with methods to calculate area and perimeter.
"""
from abc import ABC , abstractmethod

class Shape(ABC):
    """Abstract base class for geometric shapes.
    This class defines the basic structure and methods that all shapes must implement.
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass