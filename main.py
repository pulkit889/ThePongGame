# Prepare the screen
# slider -2
#   Move up and down
# Ball
#   collisions
#       with wall
#       with slider
#   movements
# Score

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

p1 = Paddle((350, 0))
p2 = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(p1.move_up, "Up")
screen.onkey(p1.move_down, "Down")

screen.onkey(p2.move_up, "w")
screen.onkey(p2.move_down, "s")
move_speed = 0.1
game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(move_speed)

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    if ball.xcor() >= 330 and ball.distance(p1) < 50:
        ball.bounce_x()
        move_speed = move_speed / 1.1
    if ball.xcor() <= -330 and ball.distance(p2) < 50:
        ball.bounce_x()
        move_speed = move_speed / 1.1

    # detect miss the paddle
    if ball.xcor() > 380:
        ball.reset()
        move_speed = 0.1
        scoreboard.l_score += 1
        scoreboard.update()

    if ball.xcor() < -380:
        ball.reset()
        move_speed = 0.1
        scoreboard.r_score += 1
        scoreboard.update()
screen.exitonclick()