#!/usr/bin/python3

"""Square Class.

This module contains a class that defines a square.

Usage Example:

    Square = __import__('4-square').Square

    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
"""


class Square:
    """Defines the blueprint of a square.

    Attribute:
        size: An integer indicating the size of the square object.
    """

    def __init__(self, size=0):
        """An object constructor method.

        Initiatilizes Square with size.

        Arg:
            size: A integer representing object size.
                  Has a default value of 0.
        """
        self.__size = size

    @property
    def size(self):
        """Gets the size private attribute value.

        Returns:
            The size private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size private attribute value.

        Validates the assignment of the size private attribute.

        Arg:
            value: the value to be set.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """A public object method.

        Returns:
            The current square area
        """
        return self.__size**2
