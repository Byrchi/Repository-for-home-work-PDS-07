##############_Task_01####################
class Auto():

    def __init__(self, brand, color, engine_capacity):
        self.brand = brand
        self.color = color
        self.engine_capacity = engine_capacity

    def go_fovard (self):
        return 'go_fovard'

    def go_back(self):
        return 'go_back'

class Sedan(Auto):

    def move_left(self):
        return 'move_left'

    def move_right(self):
        return 'move_right'

golf = Auto('vw', 'black', 2.0)
mondeo = Auto('ford', 'green', 1.8)
astra = Sedan('opel', 'yelow', 2.4)

print(golf.go_fovard())
print(astra.move_right())