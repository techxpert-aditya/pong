import turtle

FIRST_PLAYER_PADDLE_COORDINATES = (-560, 0)
SECOND_PLAYER_PADDLE_COORDINATES = (560, 0)


class Paddle(turtle.Turtle):

    def __init__(self, player):
        """enter the str 'one' or 'two'"""
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape('square')
        self.set_size()
        if player == 'one':
            self.goto(FIRST_PLAYER_PADDLE_COORDINATES)
            self.color('cyan')
        elif player == 'two':
            self.goto(SECOND_PLAYER_PADDLE_COORDINATES)
            self.color('orange red')

    def set_size(self):
        super().resizemode('user')
        self.left(90)
        self.shapesize(stretch_wid=1.5, stretch_len=6)

    def move_up(self):
        if self.ycor() > 210:
            return
        else:
            self.forward(20)

    def move_down(self):
        if self.ycor() < -210:
            return
        else:
            self.backward(20)
