from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

RIGHT_PAD_POSITIONS = (383, 0)
LEFT_PAD_POSITIONS = (-390, 0)

pong_screen = Screen()
pong_screen.setup(width=800, height=600)
pong_screen.bgcolor("black")
pong_screen.title("Asif's Pong Game 2022")
pong_screen.tracer(0)

right_player = pong_screen.textinput(title = "Name", prompt = "Enter the right paddle player name: ")
left_player = pong_screen.textinput(title = "Name", prompt = "Enter the left paddle player name: ")


paddle_right = Paddle(RIGHT_PAD_POSITIONS)
paddle_left = Paddle(LEFT_PAD_POSITIONS)
game_ball = Ball()
right_scoreboard = Scoreboard([100,265], right_player)
left_scoreboard = Scoreboard([-100,265], left_player)

pong_screen.listen()
pong_screen.onkey(fun=paddle_right.up, key="Up")
pong_screen.onkey(fun=paddle_right.down, key="Down")
pong_screen.onkey(fun=paddle_left.up, key="w")
pong_screen.onkey(fun=paddle_left.down, key="s")

#red line in the middle
# x_coordinate = Turtle()
# x_coordinate.penup()
# x_coordinate.color("red")
# x_coordinate.hideturtle()
# x_coordinate.goto(0,300)
# x_coordinate.setheading(270)
#
# for i in range(600):
#     x_coordinate.pendown()
#     x_coordinate.forward(10)
#     x_coordinate.penup()
#     x_coordinate.forward(25)



game_on = True

while game_on:
    pong_screen.update()
    time.sleep(0.1)
    game_ball.move_ball()
    game_ball.paddle_bounce(paddle_left)
    game_ball.paddle_bounce(paddle_right)

    if game_ball.xcor() >= 393:
        game_ball.reset_position()
        left_scoreboard.update_score()

        if left_scoreboard.player_score == 5:
            left_scoreboard.game_over()
            game_on = False

    if game_ball.xcor() <= -400:
        game_ball.reset_position()
        right_scoreboard.update_score()

        if right_scoreboard.player_score == 5:
            right_scoreboard.game_over()
            game_on = False







pong_screen.exitonclick()