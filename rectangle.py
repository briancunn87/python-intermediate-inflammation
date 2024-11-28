class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def get_area(self):
    return self.width * self.height

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def get_area(self):
    import math

    return math.pi * self.radius * self.radius 

my_circle = Circle(10)
my_rectangle = rectangle(5,3)
my_shapes = [my_circle,my_rectangle]
total_area = sum(shape.get_area for shape in my_shapes)
