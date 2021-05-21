#!/usr/bin/python3
"""Create class for rectangle."""


class Rectangle:
    """Create constructor for with and height."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """class defenicion"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Proprty to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter to set it"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property height to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter height to retrieve it"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Function that calculates the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Function that calculates the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Function that calculates the __str__ of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ''
        rect_print = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rect_print += '{}'.format(self.print_symbol)
            rect_print += '\n'
        return rect_print[:-1]

    def __repr__(self):
        """reprecent __repr__ for print rectangle"""
        eval = "Rectangle({}, {})".format(self.__width, self.__height)
        return eval

    def __del__(self):
        """Print text for del instancia"""
        print("Bye rectangle...")
        Rectangle.number_of_instances += -1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static bigger_or_equal by rect_1 and rect_2"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
