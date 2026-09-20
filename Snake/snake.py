from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("arrow")
        self.head.color("spring green")
        self.current_direction = RIGHT 
        self.input_locked = False  # Handles rapid keystrokes buffer bugs

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            
        self.head.forward(MOVE_DISTANCE)
        self.current_direction = self.head.heading() 
        self.input_locked = False  # Reset input lock buffer post frame render

    def up(self):
        if self.current_direction != DOWN and not self.input_locked:
            self.head.setheading(UP)
            self.input_locked = True

    def down(self):
        if self.current_direction != UP and not self.input_locked:
            self.head.setheading(DOWN)
            self.input_locked = True

    def left(self):
        if self.current_direction != RIGHT and not self.input_locked:
            self.head.setheading(LEFT)
            self.input_locked = True

    def right(self):
        if self.current_direction != LEFT and not self.input_locked:
            self.head.setheading(RIGHT)
            self.input_locked = True
    
    def add_segments(self, position):
        snake_seg = Turtle("square")
        snake_seg.color("lime")
        snake_seg.penup()
        snake_seg.goto(position)
        self.segments.append(snake_seg)
    
    def extend(self):
        self.add_segments(self.segments[-1].position())

