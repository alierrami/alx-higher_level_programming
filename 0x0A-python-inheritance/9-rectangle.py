#!/usr/bin/python3
"""Contains the class BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class with public instance methods area and integer_validator"""

    def __init__(self, width, height):
        """initialization"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculate area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """custom str method for print the rectangle"""

        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
