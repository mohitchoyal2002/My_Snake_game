from turtle import Screen, Turtle
from food import Food
from scoreboard import ScoreBoard
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('Black')
screen.title('My Snake Game')
screen.tracer(0)
screen.listen()
snake = Snake()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

food = Food()#while creating object we called a constructor of Food class
score = ScoreBoard()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 299 or snake.head.ycor() < -280:
        score.reset()
        score.update_score()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            score.update_score()


screen.exitonclick()
