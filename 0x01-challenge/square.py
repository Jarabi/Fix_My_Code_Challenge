#!/usr/bin/python3
''' Class definition for a square '''


class square():
    '''
    Definition of a square
    '''

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initialization for arguments """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter of square """
        return (self.width * 4)

    def __str__(self):
        """ return string representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
