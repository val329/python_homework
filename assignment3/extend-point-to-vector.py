# Task 5
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y  # equality

    def __str__(self):
        return f"Point: ({self.x}, {self.y})"  # string representation

    def euc_distance(self, other):
        return math.dist(self, other)  # Euclidian distance to another point


class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return f"Vector: ({self.x}, {self.y})"  # string representation

    def __add__(self):          # overriding addition
        return self.x + self.y


print(f"Point: {Point.__dict__}")  # prints attributes and methods for the class
print(f"Vector: {Vector.__dict__}")  # prints attributes and methods for the class
