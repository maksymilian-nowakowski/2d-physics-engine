class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector2({self.x}, {self.y})'
    

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Vector2(scalar * self.x, scalar * self.y)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ZeroDivisionError('scalar must not be zero')
        return Vector2(self.x / scalar, self.y / scalar)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def magnitude_squared(self):
        return self.x ** 2 + self.y ** 2

    def normalized(self):
        if self.is_zero():
            raise ZeroDivisionError('vector of magnitude zero cannot be normalized')
        return Vector2(self.x, self.y) / self.magnitude()

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def distance_to(self, other):
        return (other - self).magnitude()

    def copy(self):
        return Vector2(self.x, self.y)

    def is_zero(self):
        return (self.x, self.y) == (0, 0)
