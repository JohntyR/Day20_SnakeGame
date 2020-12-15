from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


snake = []
for i in range(3):
    snake.append(Turtle("square"))
    snake[i].color("white")
    snake[i].penup()
    snake[i].goto(x=0 - (i * 20), y=0)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment_num in range(len(snake) - 1, 0, -1):
        new_x = snake[segment_num - 1].xcor()
        new_y = snake[segment_num - 1].ycor()

        snake[segment_num].goto(x=new_x, y=new_y)
    snake[0].forward(20)
    snake[0].left(20)


screen.exitonclick()