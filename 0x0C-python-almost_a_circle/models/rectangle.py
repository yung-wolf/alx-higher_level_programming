#!/usr/bin/python3

"""
Module: models/rectangle

Holds one class, Rectangle()
"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes object."""

        super().__init__(id)

        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    @property
    def width(self):
        """Return width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Returns height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """Returns the value of `x`."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """Returns the value of `y`."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """Returns the area of rect."""
        return self.__width * self.__height

    def display(self):
        """Prints out rect with `#` key."""
        self.down = self.__y
        self.right = self.__x

        while (self.down != 0):
            print()
            self.down -= 1

        for row in range(self.__height):
            while (self.right != 0):
                print(" ", end="")
                self.right -= 1
            print('#' * self.__width)
            self.right = self.__x

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Updates class Rectangle with args."""

        if args and args != []:
            self.len_args = len(args)
            max_args = 5
            i = 1  # counter

            # validate num of args passed
            if self.len_args > max_args:
                raise TypeError(f'update() takes a max of 5 positional args '
                                f'but {self.len_args} were given')

            for arg in args:
                if i == 1:
                    if type(arg) is not int:
                        raise TypeError('id must be an integer')
                    else:
                        self.id = arg
                elif i == 2:
                    self.width = arg
                elif i == 3:
                    self.height = arg
                elif i == 4:
                    self.x = arg
                elif i == 5:
                    self.y = arg
                i += 1
        else:
            for arg, v in kwargs.items():
                if arg == 'id':
                    self.id = v
                elif arg == 'width':
                    self.width = v
                elif arg == 'height':
                    self.height = v
                elif arg == 'x':
                    self.x = v
                elif arg == 'y':
                    self.y = v
                else:
                    raise TypeError(f'update() got an unexpected keyword '
                                    f'argument: {arg}')

    def to_dictionary(self):
        """Returns dictionary representation of Rectangle object."""
        r_dic = {'id': self.id, 'width': self.width, 'height': self.height,
                 'x': self.x, 'y': self.y}
        return r_dic
