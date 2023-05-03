from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
game_is_on=True
user_score=0
segments = []
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)  # so that only movement of snake is shown and not the formation of snake
snake = Snake()
food=Food()
score=ScoreBoard(user_score)
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    x_end=snake.segments[0].xcor()
    y_end=snake.segments[0].ycor()
    if (x_end>280) or (x_end<-280) or (y_end>280) or (y_end<-280):
        game_is_on=False
        score.end_game()

    #Detect the collision of food with snake's head
    if snake.segments[0].distance(food)<15:
        user_score+=1
        score.refresh_score(user_score)
        food.refresh()
        snake.extend()

    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) <10:
            game_is_on=False
            score.end_game()

screen.exitonclick()