from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.x_position = xcor
        self.y_position = ycor

    def create_paddle(self):
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=100 / 20, stretch_len=20 / 20)
        self.penup()
        self.goto(self.x_position, self.y_position)

    def up(self):
        self.goto(self.x_position, self.ycor() + 20)

    def down(self):
        self.goto(self.x_position, self.ycor() - 20)
