import random
from turtle import Turtle

turtle_colors = [
    "lawn green", "dark green", "burlywood", "white", "red", "saddle brown",
    "lime green", "yellow", "cyan", "navy", "olive", "dark khaki", 
    "olive drab", "dark goldenrod"
]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.refresh([])  

    def refresh(self, snake_segments):
        while True:
            # Safe width limits (-13 to 13)
            random_x = random.randint(-13, 13) * 20
            # Safe height limits: Upper constraint capped at 10 to keep away from the scoreboard area
            random_y = random.randint(-13, 10) * 20
            
            # Distance array lookup loop mapping
            overlapping = any(seg.distance(random_x, random_y) < 15 for seg in snake_segments)
            
            if not overlapping:
                self.color(random.choice(turtle_colors))
                self.goto(random_x, random_y)
                break

