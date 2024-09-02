from turtle import  Screen
from snake import Snake
from food import Food
from score import Score
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(1000,800)
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Score()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    #Detect collision with wall
    if snake.head.xcor() > 490 or  snake.head.xcor() < -490 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()











