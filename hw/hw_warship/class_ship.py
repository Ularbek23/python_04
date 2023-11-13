from class_sea import Sea
class Ship:
    is_alive = True

    def __init__(self, y, x):
        self.y = y
        self.x = x
    
    def __repr__(self):
        if self.is_alive:
            return "s"
        else:
            return " "