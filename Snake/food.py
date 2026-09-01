from turtle import Turtle
import random

turtle_colors = ['lawn green','dark green', 'burlywood', 'white', 'red', "saddle brown", "lime green", "yellow", "cyan",
"navy", "olive", 'dark khaki', "olive drab", "dark goldenrod"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.turtle_color = ''
        self.shape("turtle")
        self.penup()
        #self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.turtle_color = random.choice(turtle_colors)
        self.color(self.turtle_color)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.turtle_color = random.choice(turtle_colors)
        self.color(self.turtle_color)
        random_x = random.randint(-270,270)
        random_y = random.randint(-270,270)
        self.goto(random_x, random_y)

