class Parallelogram():

    def __init__(self, wight, lenght):
        self.wight = wight
        self.lenght = lenght

    def get_area(self):
        return f'Area of parallelogram {self.wight * self.lenght} cm2'

class Square (Parallelogram):

    def __init__(self, side_square):
        self.side_square = side_square
    def get_area(self):
            return f'Area of square {self.side_square**2} cm2'





p1 = Parallelogram(10, 5)
p2 = Parallelogram(2, 2.2)
p3 = Square(5.2)
print(p3.get_area())