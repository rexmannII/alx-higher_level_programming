#!/usr/bin/python3
'''Module for a Rectangle class.'''




class Rectangle:
    '''This class defines a simple rectangle.'''

    number_of_instances = 0
    '''print: The number of active instances.'''

    print_symbol = '#'
    '''type: Print symbol, can be any type.'''

    def __init__(self, width=0, height=0):
        '''Constructor.

        Args:
            width: The width of rectangle.
            height: The height of rectangle.
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1


    @property
    def width(self):
        '''Property for the width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for the private instance attribute width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''getter for the private instance attribute height

        Raises:
            TypeError: If height is not an integer.
            ValueErroe: If height is less than 0.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for the private instance attribute height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''returns the area of the rectangle'''
        return self.width * self.height

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """returns string representation of the rectangle"""
        if not self.width or not self.height:
            return ""
        return ((st(self.print_symbol) * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        '''Returns formal string Representation...'''
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        '''Called at instance deletion.'''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_oequal(rect_1, rect_2):
        '''Returns the bigger of two rectangles.

        Args:
            rec_1: The first rectangle.
            rect_2: The second rectangle.
        Raises:
            TypeError: If rect_1, rect_2 are not instance of Rectangle.
        Returns:
            The rectangle with the larger area.
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rec_2.area() > rect_1.area():
            return rect_2
        return rect_1
