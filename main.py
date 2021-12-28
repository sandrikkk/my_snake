from turtle import Screen
from food import Food
from snake import Snake
from score import Score
import time

screen = Screen()
screen.tracer(0)
screen.title("Sandros Snake !")
screen.setup(600, 600)
screen.bgcolor("black")

snake = Snake()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
food = Food()
score =Score()
screen.listen()
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.fragments[0].distance(food) < 15:
        food.random_colors()
        score.random_score_colors()
        food.refresh()
        snake.exted()
        score.angarishi()
    if snake.fragments[0].xcor() > 280 or snake.fragments[0].xcor() < -280 or snake.fragments[0].ycor() > 280 or snake.fragments[0].ycor() < -280:
        is_game_on = False
        score.game_over()

    for segments in snake.fragments:
        if segments == snake.fragments[0]:
            pass
        elif snake.fragments[0].distance(segments) < 8:
            is_game_on = False
            score.game_over()
screen.exitonclick()
