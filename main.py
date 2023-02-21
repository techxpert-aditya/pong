import turtle
import paddle
import ball
import time
import score_board
import board
turtle.colormode(255)

# create a screen
screen = turtle.Screen()
screen.title('Pong')
screen.setup(width=1200, height=600)
screen.bgcolor((13, 9, 44))
screen.listen()
screen.tracer(0)

# drawing the board
board = board.Board()

# create a 1st paddle

paddle1 = paddle.Paddle('one')

# creating 2nd paddle
paddle2 = paddle.Paddle('two')
screen.update()

# creating the ball
ball = ball.Ball()

# creating score boards
score_board_p1 = score_board.ScoreBoard(1)
score_board_p2 = score_board.ScoreBoard(2)

score_board_p1.show_score()
score_board_p2.show_score()
game_is_on = True

# starting the game

while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    # making the ball move

    ball.start_moving()

    # listening to the keys
    screen.onkeypress(fun=paddle1.move_up, key='w')
    screen.onkeypress(fun=paddle2.move_up, key='Up')
    screen.onkeypress(fun=paddle1.move_down, key='s')
    screen.onkeypress(fun=paddle2.move_down, key='Down')
    screen.update()

    # detect collision with walls
    if ball.ycor() > 265:
        ball.bounce_back_from_upper_wall()
    elif ball.ycor() < -265:
        ball.bounce_back_from_lower_wall()

    # detect collision with bats
    if paddle1.distance(ball) < 60 and ball.xcor() < -530:
        ball.bounce_from_p1_bat()

    if paddle2.distance(ball) < 60 and ball.xcor() > 530:
        ball.bounce_from_p2_bat()

    # detecting if ball goes out of bound and restart the game
    if ball.xcor() < -700:
        ball.restart()
        score_board_p2.update_score()

    elif ball.xcor() > 700:
        ball.restart()
        score_board_p1.update_score()

screen.exitonclick()
