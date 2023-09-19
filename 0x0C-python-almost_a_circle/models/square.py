#!/usr/bin/python3

"""
Module: models/square

Holds one class, Square()
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Models a square. Inherits from cls Rectangle.

    Attr:
        size (int): size on square (l)
        x (int): x - coordinates
        y (int): y - coordinates
        id (int): id of square object
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Returns size of Square object"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes of object. Takes *args & **kwargs"""
        if args and args != []:
            self.max_args = 4
            self.len_args = len(args)
            i = 1  # counter
            if self.len_args > self.max_args:
                raise TypeError(f'update() takes a max of 4 positional args'
                                f' but {self.len_args} were given')

            for arg in args:
                if i == 1:
                    if type(arg) is not int:
                        raise TypeError('id must be an integer')
                    else:
                        self.id = arg
                elif i == 2:
                    self.size = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        else:  # **kwargs
            for arg, v in kwargs.items():
                if arg == 'id':
                    self.id = v
                elif arg == 'size':
                    self.size = v
                elif arg == 'x':
                    self.x = v
                elif arg == 'y':
                    self.y = v
                else:
                    raise TypeError(f'update() got an unexpected keyword '
                                    f'argument: {arg}')

    def to_dictionary(self):
        """Returns dictionary representation of Square object."""
        sq_dic = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return sq_dic
