import turtle
import random


def get_angle():
    range = []
    range_1 = random.randint(135, 225)
    range.append(range_1)
    range2 = []
    r2_1 = random.randint(0, 45)
    range2 .append(r2_1)
    r2_2 = random.randint(325, 359)
    range2.append(r2_2)
    range_2 = random.choice(range2)
    range.append(range_2)

    answer = random.choice(range)
    return answer


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('azure')
        self.penup()
        self.speed(0)
        self.setheading(get_angle())
        self.ball_speed = 0.01

    def start_moving(self):
        self.forward(10)

    def bounce_back_from_upper_wall(self):
        incline_angle = 180 - self.heading()
        self.setheading(180+incline_angle)

    def bounce_back_from_lower_wall(self):
        compliment_of_incline = 360 - self.heading()
        incline_angle = 180 - compliment_of_incline
        self.setheading(180-incline_angle)

    def bounce_from_p1_bat(self):
        if self.heading() <= 180:
            bounce_angle = 180 - self.heading()
            self.setheading(bounce_angle)
        elif self.heading() > 180:
            theta = self.heading() - 180
            bounce_angle = 360 - theta
            self.setheading(bounce_angle)
        self.ball_speed *= 0.8

    def bounce_from_p2_bat(self):
        if self.heading() < 90:
            self.setheading(180 - self.heading())

        elif self.heading() > 270:
            bounce_angle = 360 - self.heading()
            self.setheading(180+bounce_angle)
        self.ball_speed *= 0.8

    def restart(self):
        self.goto(0, 0)
        self.ball_speed = 0.01

        angle = get_angle()
        self.setheading(angle)



