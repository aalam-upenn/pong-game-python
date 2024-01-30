from turtle import Turtle
from random import randint, choice

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.distance_x = 10
        self.distance_y = 10

    def move_ball(self):
        new_x = self.xcor() + self.distance_x
        new_y = self.ycor() + self.distance_y
        self.goto(new_x, new_y)
        if self.ycor() >= 280 or self.ycor() <= -275:
            self.bounce()

    def bounce(self):
        self.distance_y *= -1

    def paddle_bounce(self, paddle):
        if (self.xcor() > 356 and self.distance(paddle) < 50) or (self.xcor() < -363 and self.distance(paddle) < 50):
            self.distance_x *= -1.1

    def reset_position(self):
        self.home()
        self.distance_x /= (self.distance_x/10)
        self.distance_x *= -1
        self.distance_y /= (self.distance_y/10)
        self.distance_y *= -1