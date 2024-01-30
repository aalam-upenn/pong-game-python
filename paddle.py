from turtle import Turtle
MOVE_DISTANCE = 25

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.showturtle()

    def up(self):
        if not self.ycor() >= 250:
            self.goto(self.xcor(),self.ycor() + MOVE_DISTANCE)

    def down(self):
        if not self.ycor() <= -230:
            self.goto(self.xcor(),self.ycor() - MOVE_DISTANCE)