from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.score = 0
        self.goto(x=0, y=260)
        self.update_scorebaord()
        self.hideturtle()

    def update_scorebaord(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.color('red')
        self.write(f"GAME OVER", align=ALIGNMENT, font=("Times New Roman", 30, 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scorebaord()        