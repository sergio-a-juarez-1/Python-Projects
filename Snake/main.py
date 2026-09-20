import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

# Initialize screen environment
screen = Screen()
screen.setup(height=800, width=800)
screen.bgcolor("black")
screen.title('🐍 SNAKE 🐍')
screen.tracer(0)

# Speed control tracking variables
game_speed = 0.1 

# Instantiating entity classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Event listeners binding keyboard keys
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()
    
    # Hitbox distance check
    if snake.head.distance(food) < 15:
        food.refresh(snake.segments)
        snake.extend()
        scoreboard.increase_score()
        
        # Smoothly increase game acceleration speed
        if game_speed > 0.03:
            game_speed -= 0.002 
    
    # DYNAMIC BOUNDARY FIX: Calculate visual edges based on real window proportions
    half_width = screen.window_width() / 2 - 20
    half_height = screen.window_height() / 2 - 20
    
    # Boundary tracking conditional statement
    if abs(snake.head.xcor()) > half_width or abs(snake.head.ycor()) > half_height:
        game_on = False
        scoreboard.game_over()
        
    # Self-collision optimization loop
    if len(snake.segments) >= 5:
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 15:
                game_on = False
                scoreboard.game_over()
    
screen.exitonclick()

