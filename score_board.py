import turtle

P1_COORDINATES = (-80, 230)
P2_COORDINATES = (80, 230)
ALIGN = 'center'
FONT = ('courier', 18, 'bold')

class ScoreBoard(turtle.Turtle):

    def __init__(self, player):
        """enter 1 or 2 inside the player number to declare their score"""
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        if player == 1:
            self.goto(P1_COORDINATES)
        elif player == 2:
            self.goto(P2_COORDINATES)

    def show_score(self):
        self.write(arg=f"{self.score}", move=False, align=ALIGN, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.show_score()
