#!C:\Users\OP\AppData\Local\Programs\Python\Python312\python.exe

from models.base import Base


class Rectangle(Base):
    """Class that defines properties of Rectangle.

     Attributes:
        width (int): width of rectangle.
        height (int): height of rectangle.
        x (int): x.
        y (int): y.
"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates new instances of rectangle.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): Identity number of rectangle. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """ width getter """
            return self.__width

        @width.setter
        def width(self, value):
            """ width setter """
            if type(value) is not int:
                raise TypeError("widht must be integer")
            if value <=0:
                raise ValueError("width must be positive")
            self.__width

            @property
        def height(self):
            """ height getter """
            return self.__height

        @height.setter
        def height(self, value):
            """ height setter """
            if type(value) is not int:
                raise TypeError("height must be integer")
            if value <=0:
                raise ValueError("height must be positive")
            self.__height

        @property
        def x(self):
            """ x getter """
            return self.__x

        @x.setter
        def x(self, value):
            """ x setter """
            if type(value) is not int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """ y getter """
            return self.__y

        @y.setter
        def y(self, value):
            """ y setter """
            if type(value) is not int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

