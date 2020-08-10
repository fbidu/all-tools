"""
Pointy points
"""


class Point:
    """
    The point class defines a three dimensional vector with coordinates x, y and z.
    """

    def __init__(self, x, y, z):

        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        x_1, y_1, z_1 = self
        x_2, y_2, z_2 = other
        return Point(x_1 + x_2, y_1 + y_2, z_1 + z_2)

    def __sub__(self, other):
        x_1, y_1, z_1 = self
        x_2, y_2, z_2 = other
        return Point(x_1 - x_2, y_1 - y_2, z_1 - z_2)

    def __mul__(self, scale):
        return Point(self.x * scale, self.y * scale, self.z * scale)

    def __rmul__(self, scale):
        return self.__mul__(scale)

    def __eq__(self, other):
        """Returns true if every coordinate of the current point is equal
        to the coordinates of the other point"""
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
