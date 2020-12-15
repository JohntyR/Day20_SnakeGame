from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_COORDS = {"x": 0, "y": 0}


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            self.segments.append(Turtle("square"))
            self.segments[i].color("white")
            self.segments[i].penup()
            self.segments[i].goto(
                x=STARTING_COORDS["x"] - (i * 20), y=STARTING_COORDS["y"]
            )

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()

            self.segments[segment_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)