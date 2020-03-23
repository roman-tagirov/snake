from tkinter import Tk,Canvas
WIDTH=800
HEIGHT=600
from tkinter import Tk,Canvas
WIDTH=800
HEIGHT=600
SIZE = 15
class Segment(object):
    def __init__(self,x,y,c): 
        self.x = x
        self.y = y
        self.c = c;
        self.shape = c.create_rectangle(self.x*SIZE,self.y*SIZE,(self.x + 1)*SIZE,(self.y+1)*SIZE,fill = "blue")

    def move(self,x, y):
        self.c.move(self.shape, (x- self.x)*SIZE, (y- self.y)*SIZE)
        self.x=x
        self.y=y
class Snake:
    def __init__(self,c):
        self.c = c 
        self.segments = [Segment(1,3,c),Segment(1,2,c),Segment(1,1,c)]
    def move(self):
        #for index in range(len(self.segments)-1):
        #  s = self.segments[index]
        #  self.segments[index+1].x = s.x
        #  self.segments[index+1].y = s.y
        self.segments[1].move(self.segments[1].x,self.segments[1].y+1)
def main():
    snake.move()
    root.after(100, main)
root = Tk()
root.title("Змейка")
c = Canvas(root, width=WIDTH,height=HEIGHT, bg = "green")
c.grid()
c.focus_set()
snake = Snake(c)
main()
root.mainloop()
