class segment:
    def __init__(self,x,y):
        self.x = x
        self.y = y
class snake:
    segments:[segment(4,1),segment(5,1),segment(6,1)]
    def moveright(self):
        head = segment[0]