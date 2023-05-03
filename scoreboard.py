from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self,user_score):
        super().__init__()
        self.color("white")
        self.ht()
        self.goto(0,280)
        self.penup()
        self.refresh_score(user_score)

    def refresh_score(self,sc):
        self.clear()
        self.write(f"Score:{sc}",False,"center",("Courier",14,"normal"))

    def end_game(self):
        self.goto(0,0)
        self.write("Game Over!!",False,"center",("Courier",14,"normal"))