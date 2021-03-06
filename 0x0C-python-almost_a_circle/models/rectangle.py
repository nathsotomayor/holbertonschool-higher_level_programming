#!/usr/bin/python3
""" Creates a Rectangle class inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ Defines Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializing constructor """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Rectangle width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set value to rectangle width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Rectangle height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set value to rectangle height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Rectangle 'x' attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set value to rectangle 'x' """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Rectangle 'y' attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set value to rectangle 'y' """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Public method that computes the Rectangle area """
        rect_area = self.__width * self.__height
        return rect_area

    def display(self):
        """ Displays the rectangle with '#' character taking care x and y """
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            for m in range(self.__x):
                print(" ", end="")
            for n in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ Representation of the Rectangle """
        return "[Rectangle] ({}) {}/{} - {}/"\
               "{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Method to assigns an argument to each attribute of class """
        if args:
            for attr in range(len(args)):
                if attr == 0:
                    self.id = args[attr]
                if attr == 1:
                    self.__width = args[attr]
                if attr == 2:
                    self.__height = args[attr]
                if attr == 3:
                    self.__x = args[attr]
                if attr == 4:
                    self.__y = args[attr]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """ Dictionary representation of Rectangle class """
        key_attr = ["id", "width", "height", "x", "y"]
        dict_rect = {}
        for key in key_attr:
            dict_rect[key] = getattr(self, key)
        return dict_rect
