from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score()

    def score(self):
        self.goto(-100, 200)
        self.write(self.l_score, False, font=("Courier", 60, "normal"), align="center")
        self.goto(100, 200)
        self.write(self.r_score, False, font=("Courier", 60, "normal"), align="center")

    def l_point(self):
        self.l_score += 1
        self.score()

    def r_point(self):
        self.r_score += 1
        self.score()

    def clear_score(self):
        self.clear()

    def game_over(self, winner_name):
        self.goto(-0, 0)
        self.write(f"GAME OVER! {winner_name} WINS", False, font=("Arial", 20, "normal"), align="center")
