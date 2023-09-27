#!/usr/bin/python3
"classe square"


class Square:
    "class with attribue size"

    def __init__(self, size=0):
        "inisialization"
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
