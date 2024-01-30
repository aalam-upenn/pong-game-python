from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self, position, name):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.player_score = 0
        self.player_name = name
        self.show_score()

    def show_score(self):
        self.write(f"{self.player_name}: {self.player_score} ", False, align="center", font=('Arial', 24, 'normal'))

    def update_score(self):
        self.player_score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over! {self.player_name} wins!", False, align=ALIGNMENT, font=FONT)

