from turtle import Turtle

ALIGNMENT = "center"
FONT = "Tahoma"
FONT_SIZE = 16
FONT_WEIGHT = "normal"
FONT_COLOUR = "white"
X_POS = 0
Y_POS = 270


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(FONT_COLOUR)
        self.penup()
        self.goto(x=X_POS, y=Y_POS)
        self.hideturtle()
        self.refresh()

    def increment_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(
            f"Score: {self.score}", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_WEIGHT)
        )
