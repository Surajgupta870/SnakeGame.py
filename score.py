from turtle import Turtle
ALIGNMENT = "CENTER"
FONT = ("Courier", 20 ,"normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 370)
        self.hideturtle()
        self.update_scoreboard()
        self.reset()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
            self.score += 1
            self.clear()
            self.update_scoreboard()

     def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
