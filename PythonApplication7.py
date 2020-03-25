from tkinter import Tk,Canvas
from keyboard import*
WIDTH=20
HEIGHT=20
SIZE = 15
class Segment(object):
    def __init__(self,x,y, color): 
        self.x = x
        self.y = y
        self.c = c;
        self.shape = c.create_rectangle(self.x*SIZE,self.y*SIZE,(self.x + 1)*SIZE,(self.y+1)*SIZE,fill = color)
#----------------------------------------------------
    def move(self,x,y):
        self.c.move(self.shape, (x- self.x)*SIZE, (y- self.y)*SIZE)
        self.x=x
        self.y=y
    def moveTo(self,segment):
        self.move(segment.x,segment.y)
class Snake:
    direction = (0,1)
    def __init__(self):
        self.segments = [Segment(1,3,"red"),Segment(1,2,"blue"),Segment(1,1,"blue"),Segment(1,0, "blue"),Segment(1,-1, "blue")]
#-----------------------------------------------------
    def getHead(self):
        return self.segments[0]
#-----------------------------------------------------
    def move(self):
        head = self.getHead()
        NewX = head.x+self.direction[0]
        NewY = head.y+self.direction[1]
        if self.canmoveTO(NewX,NewY) == False:
            return
        for index in range(len(self.segments)-1,0,-1):
            self.segments[index].moveTo(self.segments[index-1])
        head.move(head.x+self.direction[0],head.y+self.direction[1])
#----------------------------------------------------
    def canmoveTO(self,x,y):
        if x < 0:
            return False
        if y < 0:
            return False
        if x>WIDTH:
            return False
        if y>HEIGHT:
            return False
        return True
#----------------------------------------------------
    def change_direction(self, key):
        if (key.keysym == "s"):
            self.direction = (0,1)
        if (key.keysym == "w"):
            self.direction = (0,-1)
        if (key.keysym == "a"):
            self.direction = (-1,0)
        if (key.keysym == "d"):
            self.direction = (1,0)
#----------------------------------------------------   
def main():
    snake.move()
    root.after(100, main)
root = Tk()
root.title("Змейка")
c = Canvas(root, width=(WIDTH+1)*SIZE,height=(HEIGHT+1)*SIZE, bg = "green")
c.grid()
c.focus_set()
snake = Snake()
c.bind("<KeyPress>",snake.change_direction)
main()
root.mainloop()
#----------------------------------------------------
