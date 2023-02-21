import turtle


class Board(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.color("yellow")
        self.draw_central_circle()

    def draw_central_circle(self):
        self.goto(0, -100)
        self.circle(100)
        self.draw_central_line()


    def draw_central_line(self):
        self.goto(0, 285)
        self.right(90)
        self.forward(570)
        self.left(90)
        self.draw_border()

    def draw_border(self):
        self.pensize(width=5)
        self.forward(600)
        self.left(90)
        self.forward(570)
        self.left(90)
        self.forward(1200)
        self.left(90)
        self.forward(570)
        self.left(90)
        self.forward(600)
