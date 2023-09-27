#!/usr/bin/python3
"square"


class Square:
    "representation"

    def __init__(self, size=0):
        "initialization"
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        "public instance methode that return area"
        return self.__size ** 2
