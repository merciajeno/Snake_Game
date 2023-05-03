from turtle import Turtle, Screen
positions=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
         def __init__(self):
             self.score=0
             self.segments=[]
             self.ctr=0
             self.create_snake()

         def extend(self):
             self.add_segment(self.segments[-1].position())


         def create_snake(self):
             for pos in positions:
                 self.add_segment(pos)

         def add_segment(self,position):
             new_segment = Turtle(shape="square")
             new_segment.penup()
             new_segment.color("white")
             new_segment.goto(position)
             self.segments.append(new_segment)

         def move(self):
             for seg in range(len(self.segments)-1, 0, -1):
                 new_x=self.segments[seg-1].xcor()
                 new_y=self.segments[seg-1].ycor()
                 self.segments[seg].goto(new_x,new_y)
             self.segments[0].fd(20)

         def left(self):
             if self.segments[0].heading()!=RIGHT:
               self.segments[0].setheading(LEFT)


         def right(self):
             if self.segments[0].heading() !=LEFT:
               self.segments[0].setheading(RIGHT)


         def up(self):
             if self.segments[0].heading()!=DOWN:
               self.segments[0].setheading(UP)


         def down(self):
             if self.segments[0].heading()!=UP:
                self.segments[0].setheading(DOWN)



